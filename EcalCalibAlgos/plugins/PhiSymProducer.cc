#ifndef _PHISYM_PRODUCER_
#define _PHISYM_PRODUCER_

#include <iostream>
#include <memory>

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

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

#include "PhiSym/EcalCalibDataFormats/interface/PhiSymRecHit.h"
#include "PhiSym/EcalCalibDataFormats/interface/PhiSymInfo.h"
#include "PhiSym/EcalCalibAlgos/interface/PhiSymFile.h"
#include "PhiSym/EcalCalibAlgos/interface/EcalGeomPhiSymHelper.h"

using namespace std;

//****************************************************************************************

class PhiSymProducer : public edm::one::EDProducer<edm::EndLuminosityBlockProducer,
                                                 edm::one::WatchLuminosityBlocks>
{
public:
    explicit PhiSymProducer(const edm::ParameterSet& pSet);
    ~PhiSymProducer();

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
    float          eThresholdEB_;
    float          AP_;
    float          B_;
    int            nMisCalib_;
    vector<double> misCalibRangeEB_;
    vector<double> misCalibRangeEE_;
    int            lumisToSum_;
    int            statusThreshold_;
    int            nLumis_;
    bool           applyEtThreshold_;
    //---geometry
    EcalGeomPhiSymHelper* ecalGeoAndStatus_;

    //---output edm
    auto_ptr<PhiSymInfoCollection> lumiInfo_;
    auto_ptr<PhiSymRecHitCollection> recHitCollEB_;
    auto_ptr<PhiSymRecHitCollection> recHitCollEE_;
    vector<float> detIdKeyEB_;
    vector<float> detIdKeyEE_;
    //---output plain tree
    bool makeSpectraTreeEB_;
    bool makeSpectraTreeEE_;
    auto_ptr<PhiSymFile> outFile_;
    edm::Service<TFileService> fs_;
};

//----------IMPLEMENTATION----------------------------------------------------------------

PhiSymProducer::PhiSymProducer(const edm::ParameterSet& pSet):
    ebTag_(pSet.getParameter<edm::InputTag>("barrelHitCollection")),
    eeTag_(pSet.getParameter<edm::InputTag>("endcapHitCollection")),
    eCutEB_(pSet.getParameter<double>("eCut_barrel")),
    eThresholdEB_(pSet.getParameter<double>("eThreshold_barrel")),
    AP_(pSet.getParameter<double>("AP")),
    B_(pSet.getParameter<double>("B")),
    nMisCalib_(pSet.getParameter<int>("nMisCalib")),
    misCalibRangeEB_(pSet.getParameter<vector<double> >("misCalibRangeEB")),
    misCalibRangeEE_(pSet.getParameter<vector<double> >("misCalibRangeEE")),
    lumisToSum_(pSet.getParameter<int>("lumisToSum")),
    statusThreshold_(pSet.getParameter<int>("statusThreshold")),
    nLumis_(0),
    applyEtThreshold_(pSet.getParameter<bool>("applyEtThreshold")),
    ecalGeoAndStatus_(NULL),
    makeSpectraTreeEB_(pSet.getUntrackedParameter<bool>("makeSpectraTreeEB")),
    makeSpectraTreeEE_(pSet.getUntrackedParameter<bool>("makeSpectraTreeEE"))
{    
    //---register the product
    produces<PhiSymInfoCollection, edm::InLumi>();
    produces<PhiSymRecHitCollection, edm::InLumi>("EB");
    produces<PhiSymRecHitCollection, edm::InLumi>("EE");
}

PhiSymProducer::~PhiSymProducer()
{}

void PhiSymProducer::beginJob()
{
    if(makeSpectraTreeEB_ || makeSpectraTreeEE_)
        outFile_ = auto_ptr<PhiSymFile>(new PhiSymFile(&fs_->file()));
}

void PhiSymProducer::endJob()
{
    outFile_->cd();
    if(makeSpectraTreeEB_)
        outFile_->ebTree.Write("eb_xstals");
    if(makeSpectraTreeEE_)
        outFile_->eeTree.Write("ee_xstals");
}

void PhiSymProducer::beginLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& setup)
{
    //---reset the RecHit and DetId vectors
    if(nLumis_ == 0)
    {
        lumiInfo_ = auto_ptr<PhiSymInfoCollection>(new PhiSymInfoCollection);
        lumiInfo_->push_back(PhiSymInfo());
        lumiInfo_->back().setStartLumi(lumi);
        recHitCollEB_ = auto_ptr<PhiSymRecHitCollection>(new PhiSymRecHitCollection);
        recHitCollEE_ = auto_ptr<PhiSymRecHitCollection>(new PhiSymRecHitCollection);
	//---get the ecal geometry
	edm::ESHandle<CaloGeometry> geoHandle;
	setup.get<CaloGeometryRecord>().get(geoHandle);
	const CaloSubdetectorGeometry* barrelGeometry = 
	  geoHandle->getSubdetectorGeometry(DetId::Ecal, EcalBarrel);
	const CaloSubdetectorGeometry* endcapGeometry = 
	  geoHandle->getSubdetectorGeometry(DetId::Ecal, EcalEndcap);
	
	std::vector<DetId> barrelDetIds=barrelGeometry->getValidDetIds(DetId::Ecal, EcalBarrel);
	std::vector<DetId> endcapDetIds=endcapGeometry->getValidDetIds(DetId::Ecal, EcalEndcap);
	recHitCollEB_->resize(barrelDetIds.size());
	recHitCollEE_->resize(endcapDetIds.size());
	for(auto& ebDetId : barrelDetIds)
        {
	    EBDetId myId(ebDetId);
	    recHitCollEB_->at(myId.denseIndex())=PhiSymRecHit(ebDetId.rawId(), 0);
        }
	for(auto& eeDetId : endcapDetIds)
        {
	    EEDetId myId(eeDetId);
	    recHitCollEE_->at(myId.denseIndex())=PhiSymRecHit(eeDetId.rawId(), 0);
        }
    }
    
    ++nLumis_;
}

void PhiSymProducer::endLuminosityBlockProduce(edm::LuminosityBlock& lumi, edm::EventSetup const& setup)
{
    //---put the collection in the LuminosityBlocks tree
    if(nLumis_ == lumisToSum_)
    {
      lumiInfo_->back().setEndLumi(lumi);
      lumi.put(lumiInfo_);
      lumi.put(recHitCollEB_, "EB");
      lumi.put(recHitCollEE_, "EE");
      nLumis_ = 0;
    }       
}

void PhiSymProducer::produce(edm::Event& event, const edm::EventSetup& setup)
{
    //---get recHits collections - check for errors
    event.getByLabel(ebTag_, barrelRecHitsHandle_);
    if(!barrelRecHitsHandle_.isValid())
        edm::LogError("") << "[PhiSymmetryCalibration] Error! Can't get EB RecHits!" << endl;
  
    event.getByLabel(eeTag_, endcapRecHitsHandle_);
    if(!endcapRecHitsHandle_.isValid())
        edm::LogError("") << "[PhiSymmetryCalibration] Error! Can't get EE RecHits!" << endl;

    //---get the beamspot
    uint64_t totHitsEB=0;
    uint64_t totHitsEE=0;
    edm::Handle<reco::BeamSpot> recoBeamSpotHandle;
    event.getByLabel("offlineBeamSpot", recoBeamSpotHandle);
    
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
    
    //---get the channel status 
    edm::ESHandle<EcalChannelStatus> chStatus;
    setup.get<EcalChannelStatusRcd>().get(chStatus);

    if(!ecalGeoAndStatus_)
    {
        ecalGeoAndStatus_ = new EcalGeomPhiSymHelper();
        ecalGeoAndStatus_->setup(&(*geoHandle), &(*chStatus), statusThreshold_, false);
    }

    //---EB---
    for(auto& recHit : *barrelRecHitsHandle_.product())
    {
        //---check channel status
        EBDetId ebHit = EBDetId(recHit.id());
        float eta=barrelGeometry->getGeometry(ebHit)->getPosition().eta();
        if(!ecalGeoAndStatus_->goodCell_barl[abs(ebHit.ieta())-1][ebHit.iphi()-1][ebHit.ieta()>0 ? 1 : 0])
            continue;
        
        //---compute et + miscalibration
        float* etValues = new float[nMisCalib_+1];
        float  misCalibStep = fabs(misCalibRangeEB_[1]-misCalibRangeEB_[0])/nMisCalib_;
        for(int iMis=-nMisCalib_/2; iMis<=nMisCalib_/2; ++iMis)
        {
            //--- 0 -> 0; -i -> [1...n/2]; +i -> [n/2+1...n]
            int index = iMis > 0 ? iMis+nMisCalib_/2 : iMis == 0 ? 0 : iMis+nMisCalib_/2+1; 
            etValues[index] = recHit.energy()/cosh(eta)*(1+misCalibStep*iMis);
            //---set et to zero if out of range [e_thr, et_thr+1]
            if(etValues[index]*cosh(eta) < eCutEB_ || etValues[index] > eCutEB_/cosh(eta)+eThresholdEB_)                
                etValues[index] = 0;
        }

        if(etValues[0] > 0)
            ++totHitsEB;   

	recHitCollEB_->at(ebHit.denseIndex()).AddHit(etValues,
						     laser.product()->getLaserCorrection(recHit.id(), evtTimeStamp));
     
        //---fill the plain tree
        if(makeSpectraTreeEB_)
        {
            outFile_->ebTree.ieta = ebHit.ieta();
            outFile_->ebTree.iphi = ebHit.iphi();
            outFile_->ebTree.et = recHit.energy()/cosh(eta);
            outFile_->ebTree.Fill();
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
        float* etValues = new float[nMisCalib_+1];
        float  misCalibStep = fabs(misCalibRangeEB_[1]-misCalibRangeEB_[0])/nMisCalib_;
        float eCutEE=0;
        int iring=0;
        for(int ring=0; ring<kEndcEtaRings; ring++)
        {
            if(fabs(eta)>ecalGeoAndStatus_->etaBoundary_[ring] && fabs(eta)<ecalGeoAndStatus_->etaBoundary_[ring+1])
            {
                iring = ring;
                //eCutEE = 20*(C_ + B_*ring
                eCutEE = AP_ + abs(ecalGeoAndStatus_->cellPos_[ring][50].eta())*B_;
            }
        }
        for(int iMis=-nMisCalib_/2; iMis<=nMisCalib_/2; ++iMis)
        {
            //--- 0 -> 0; -i -> [1...n/2]; +i -> [n/2+1...n]
            int index = iMis > 0 ? iMis+nMisCalib_/2 : iMis == 0 ? 0 : iMis+nMisCalib_/2+1; 
            etValues[index] = recHit.energy()/cosh(eta)*(1+misCalibStep*iMis);
            //---set et to zero if out of range [e_thr, et_thr+1]
            if(applyEtThreshold_ && (etValues[index]*cosh(eta) < eCutEE || etValues[index] > eCutEE/cosh(eta)+1))                
                etValues[index] = 0;
        }
        if(etValues[0] > 0)
            ++totHitsEE;

	recHitCollEE_->at(eeHit.denseIndex()).AddHit(etValues,
						     laser.product()->getLaserCorrection(recHit.id(), evtTimeStamp));

        //---fill the plain tree
        if(makeSpectraTreeEE_)
        {
            outFile_->eeTree.iring = iring;
            outFile_->eeTree.ix = eeHit.ix();
            outFile_->eeTree.iy = eeHit.iy();
            outFile_->eeTree.et = recHit.energy()/cosh(eta);
            outFile_->eeTree.Fill();
        }        
        
    }

    //---update the beamspot
    lumiInfo_->at(0).Update(recoBeamSpotHandle.product(), totHitsEB, totHitsEE);
}

DEFINE_FWK_MODULE(PhiSymProducer);

#endif
