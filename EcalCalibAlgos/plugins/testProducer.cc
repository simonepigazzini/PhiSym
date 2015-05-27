#ifndef TEST_PRODUCER_H
#define TEST_PRODUCER_H

#include <iostream>
#include <memory>

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/EcalDetId/interface/EBDetId.h"
#include "DataFormats/EcalDetId/interface/EEDetId.h"

#include "CalibCalorimetry/EcalLaserCorrection/interface/EcalLaserDbService.h"
#include "CalibCalorimetry/EcalLaserCorrection/interface/EcalLaserDbRecord.h"

#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "Geometry/CaloGeometry/interface/CaloSubdetectorGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloCellGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"

#include "CondFormats/EcalObjects/interface/EcalChannelStatus.h"
#include "CondFormats/DataRecord/interface/EcalChannelStatusRcd.h"
#include "CondFormats/EcalObjects/interface/EcalChannelStatusCode.h"

#include "PhiSym/EcalCalibDataFormat/interface/PhiSymRecHit.h"
#include "PhiSym/EcalCalibAlgos/interface/EcalGeomPhiSymHelper.h"

using namespace std;

//****************************************************************************************

class testProducer : public edm::one::EDProducer<edm::EndLuminosityBlockProducer,
                                                 edm::one::WatchLuminosityBlocks>
{
public:
    explicit testProducer(const edm::ParameterSet& pSet);
    ~testProducer();

private:

    //---methods
    virtual void beginJob();
    virtual void beginLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& setup) override;
    virtual void endLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& setup) override {};
    virtual void endLuminosityBlockProduce(edm::LuminosityBlock& lumi, edm::EventSetup const& setup) override;
    virtual void produce(edm::Event& event, const edm::EventSetup& setup);
    virtual void endJob();

    //---input 
    edm::Handle<EBRecHitCollection> barrelRecHitsHandle_;
    edm::Handle<EERecHitCollection> endcapRecHitsHandle_;
    edm::InputTag ebTag_;
    edm::InputTag eeTag_;
    float          eCutEB_;
    float          AP_;
    float          B_;
    int            nMisCalib_;
    vector<double> misCalibValues_;
    int            lumisToSum_;
    int            statusThreshold_;
    int            nLumis_;

    //---geometry
    EcalGeomPhiSymHelper* ecalGeoAndStatus_;

    //---output
    auto_ptr<edm::PhiSymRecHitCollection> recHitCollEB_;
    auto_ptr<edm::PhiSymRecHitCollection> recHitCollEE_;
    vector<float> detIdKeyEB_;
    vector<float> detIdKeyEE_;
};

//----------IMPLEMENTATION----------------------------------------------------------------

testProducer::testProducer(const edm::ParameterSet& pSet):
    ebTag_(pSet.getParameter<edm::InputTag>("barrelHitCollection")),
    eeTag_(pSet.getParameter<edm::InputTag>("endcapHitCollection")),
    eCutEB_(pSet.getParameter<double>("eCut_barrel")),
    AP_(pSet.getParameter<double>("AP")),
    B_(pSet.getParameter<double>("B")),
    nMisCalib_(pSet.getParameter<int>("nMisCalib")),
    misCalibValues_(pSet.getParameter<vector<double> >("misCalibValues")),
    lumisToSum_(pSet.getParameter<int>("lumisToSum")),
    statusThreshold_(pSet.getUntrackedParameter<int>("statusThreshold",3)),
    nLumis_(0),
    ecalGeoAndStatus_(NULL)
{    
    //---register the product
    produces<edm::PhiSymRecHitCollection, edm::InLumi>("EB");
    produces<edm::PhiSymRecHitCollection, edm::InLumi>("EE");
}

testProducer::~testProducer()
{}

void testProducer::beginJob()
{}

void testProducer::endJob()
{}

void testProducer::beginLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& setup)
{
    //---reset the RecHit and DetId vectors
    if(nLumis_ == 0)
    {
        recHitCollEB_ = auto_ptr<edm::PhiSymRecHitCollection>(new edm::PhiSymRecHitCollection);
        recHitCollEE_ = auto_ptr<edm::PhiSymRecHitCollection>(new edm::PhiSymRecHitCollection);
        detIdKeyEB_.clear();
        detIdKeyEE_.clear();
    }
    
    ++nLumis_;
}

void testProducer::endLuminosityBlockProduce(edm::LuminosityBlock& lumi, edm::EventSetup const& setup)
{
    //---put the collection in the LuminosityBlocks tree
    if(nLumis_ == lumisToSum_)
    {
        lumi.put(recHitCollEB_, "EB");
        lumi.put(recHitCollEE_, "EE");
    
        nLumis_ = 0;
    }       
}

void testProducer::produce(edm::Event& event, const edm::EventSetup& setup)
{
    //---get recHits collections - check for errors
    event.getByLabel(ebTag_, barrelRecHitsHandle_);
    if(!barrelRecHitsHandle_.isValid())
        edm::LogError("") << "[PhiSymmetryCalibration] Error! Can't get EB RecHits!" << endl;
  
    event.getByLabel(eeTag_, endcapRecHitsHandle_);
    if(!endcapRecHitsHandle_.isValid())
        edm::LogError("") << "[PhiSymmetryCalibration] Error! Can't get EE RecHits!" << endl;

    //---get the laser corrections
    edm::Timestamp evtTimeStamp(event.time().value());
    edm::ESHandle<EcalLaserDbService> laser;
    setup.get<EcalLaserDbRecord>().get(laser);
    if(!laser.isValid())
        edm::LogError("") << "[PhiSymmetryCalibration] Error! Can't get the laser corrections!" << endl;
    
    //---get the ecal geometry
    edm::ESHandle<CaloGeometry> geoHandle;
    setup.get<CaloGeometryRecord>().get(geoHandle);
    const CaloSubdetectorGeometry* barrelGeometry = 
        geoHandle->getSubdetectorGeometry(DetId::Ecal, EcalBarrel);
    const CaloSubdetectorGeometry* endcapGeometry = 
        geoHandle->getSubdetectorGeometry(DetId::Ecal, EcalEndcap);
    
    //---get the channel status only once
    if(!ecalGeoAndStatus_)
    {
        edm::ESHandle<EcalChannelStatus> chStatus;
        setup.get<EcalChannelStatusRcd>().get(chStatus);
        edm::ESHandle<CaloGeometry> geoHandle;
        setup.get<CaloGeometryRecord>().get(geoHandle);
        
        ecalGeoAndStatus_ = new EcalGeomPhiSymHelper();
        ecalGeoAndStatus_->setup(&(*geoHandle), &(*chStatus), statusThreshold_);
    }

    //---EB---
    for(auto& recHit : *barrelRecHitsHandle_.product())
    {
        cout << laser.product()->getLaserCorrection(recHit.id(), edm::Timestamp(event.time().value())) << endl;
        //---check channel status
        EBDetId ebHit = EBDetId(recHit.id());
        float eta=barrelGeometry->getGeometry(ebHit)->getPosition().eta();
        if(!ecalGeoAndStatus_->goodCell_barl[abs(ebHit.ieta())-1][ebHit.iphi()-1][ebHit.ieta()>0 ? 1 : 0])
            continue;

        //---compute et + miscalibration
        uint32_t currentId(recHit.id().rawId());                
        float* etValues = new float[nMisCalib_];        
        for(int iMis=0; iMis<nMisCalib_; ++iMis)
        {
            etValues[iMis] = recHit.energy()/cosh(eta)*misCalibValues_[iMis];
            //---set et to zero if out of range [e_thr, et_thr+1]
            if(etValues[iMis]*cosh(eta) < eCutEB_ || etValues[iMis] > eCutEB_/cosh(eta)+1)                
                etValues[iMis] = 0;
        }

        //---loop over the known rechits
        bool found=false;
        if(detIdKeyEB_.size() != recHitCollEB_->size())
            edm::LogError("") << "[PhiSymmetryCalibration] Error! PhiSymRecHitCollection and DetIdKeys have different size" << endl;        
        for(unsigned int iId=0; iId<detIdKeyEB_.size(); ++iId)
        {
            //---if found update the rechit
            if(detIdKeyEB_.at(iId) == currentId)
            {
                recHitCollEB_->at(iId).AddHit(etValues,
                                              laser.product()->getLaserCorrection(recHit.id(), evtTimeStamp));
                found=true;
                break;
            }
        }
        //---if first hit initialize the cristall
        if(!found)
        {
            recHitCollEB_->push_back(PhiSymRecHit(currentId, etValues));
            detIdKeyEB_.push_back(currentId);
        }
    }

    //---EE---
    for(auto& recHit : *endcapRecHitsHandle_.product())
    {
        //---check channel status
        EEDetId eeHit = EEDetId(recHit.id());
        float eta=endcapGeometry->getGeometry(eeHit)->getPosition().eta();
        if(!ecalGeoAndStatus_->goodCell_endc[eeHit.ix()-1][eeHit.iy()-1][eeHit.zside()>0 ? 1 : 0])
            continue;

        //---compute et + miscalibration
        uint32_t currentId(recHit.id().rawId());                
        float* etValues = new float[nMisCalib_];
        float eCutEE=0;
        for (int ring=0; ring<kEndcEtaRings; ring++)
        {
            if(eta>ecalGeoAndStatus_->etaBoundary_[ring] && eta<ecalGeoAndStatus_->etaBoundary_[ring+1])
                eCutEE = AP_ + abs(ecalGeoAndStatus_->cellPos_[ring][50].eta())*B_;
        }

        for(int iMis=0; iMis<nMisCalib_; ++iMis)
        {
            etValues[iMis] = recHit.energy()/cosh(eta)*misCalibValues_[iMis];
            //---set et to zero if out of range [e_thr, et_thr+1]
            if(etValues[iMis]*cosh(eta) < eCutEE || etValues[iMis] > eCutEE/cosh(eta)+1)
                etValues[iMis] = 0;
        }

        //---loop over the known rechits
        bool found=false;
        if(detIdKeyEE_.size() != recHitCollEE_->size())
            edm::LogError("") << "[PhiSymmetryCalibration] Error! PhiSymRecHitCollection and DetIdKeys have different size" << endl;        
        for(unsigned int iId=0; iId<detIdKeyEE_.size(); ++iId)
        {
            //---if found update the rechit
            if(detIdKeyEE_.at(iId) == currentId)
            {
                recHitCollEE_->at(iId).AddHit(etValues,
                                              laser.product()->getLaserCorrection(recHit.id(), evtTimeStamp));
                found=true;
                break;
            }
        }
        //---if first hit initialize the cristall
        if(!found)
        {
            recHitCollEE_->push_back(PhiSymRecHit(currentId, etValues));
            detIdKeyEE_.push_back(currentId);
        }
    }    
}

DEFINE_FWK_MODULE(testProducer);

#endif
