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

#include "PhiSym/EcalCalibDataFormat/interface/PhiSymRecHit.h"

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
    virtual void beginLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& es) override;
    virtual void endLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& es) override {};
    virtual void endLuminosityBlockProduce(edm::LuminosityBlock& lumi, edm::EventSetup const& es) override;
    virtual void produce(edm::Event& event, const edm::EventSetup& es);
    virtual void endJob();

    //---input 
    edm::Handle<EBRecHitCollection> barrelRecHitsHandle_;
    edm::Handle<EERecHitCollection> endcapRecHitsHandle_;
    edm::InputTag ebTag_;
    edm::InputTag eeTag_;
    float  eCutEB_;
    int    statusThreshold_;
    int    nLumis_;

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
    statusThreshold_(pSet.getUntrackedParameter<int>("statusThreshold",3)),
    nLumis_(0)
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

void testProducer::beginLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& es)
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

void testProducer::endLuminosityBlockProduce(edm::LuminosityBlock& lumi, edm::EventSetup const& es)
{
    //---put the collection in the LuminosityBlocks tree
    if(nLumis_ == 1)
    {
        lumi.put(recHitCollEB_, "EB");
        lumi.put(recHitCollEE_, "EE");
    
        nLumis_ = 0;
    }       
}

void testProducer::produce(edm::Event& event, const edm::EventSetup& es)
{
    event.getByLabel(ebTag_, barrelRecHitsHandle_);
    if(!barrelRecHitsHandle_.isValid())
        edm::LogError("") << "[PhiSymmetryCalibration] Error! Can't get EB RecHits!" << endl;
  
    event.getByLabel(eeTag_, endcapRecHitsHandle_);
    if(!endcapRecHitsHandle_.isValid())
        edm::LogError("") << "[PhiSymmetryCalibration] Error! Can't get EE RecHits!" << endl;

    //---EB---
    for(auto& recHit : *barrelRecHitsHandle_.product())
    {
        float currentId(recHit.id().rawId());
        float etValues[5]={1,1,1,1,1};
        bool found=false;
        if(detIdKeyEB_.size() != recHitCollEB_->size())
            edm::LogError("") << "[PhiSymmetryCalibration] Error! PhiSymRecHitCollection and DetIdKeys have different size" << endl;
        for(unsigned int iId=0; iId<detIdKeyEB_.size(); ++iId)
        {
            //---if found add update the rechit
            if(detIdKeyEB_.at(iId) == currentId)
            {
                recHitCollEB_->at(iId).AddHit(etValues);
                found=true;
                break;
            }
        }
        //---if first hit initialize the cristall
        if(!found)
        {
            recHitCollEB_->push_back(PhiSymRecHit(currentId));
            detIdKeyEB_.push_back(currentId);
        }
    }

    //---EE---
    for(auto& recHit : *endcapRecHitsHandle_.product())
    {
        float currentId(recHit.id().rawId());
        float etValues[5]={1,1,1,1,1};
        bool found=false;
        if(detIdKeyEE_.size() != recHitCollEE_->size())
            edm::LogError("") << "[PhiSymmetryCalibration] Error! PhiSymRecHitCollection and DetIdKeys have different size" << endl;
        for(unsigned int iId=0; iId<detIdKeyEE_.size(); ++iId)
        {
            //---if found add update the rechit
            if(detIdKeyEE_.at(iId) == currentId)
            {
                recHitCollEE_->at(iId).AddHit(etValues);
                found=true;
                break;
            }
        }
        //---if first hit initialize the cristall
        if(!found)
        {
            recHitCollEE_->push_back(PhiSymRecHit(currentId));
            detIdKeyEE_.push_back(currentId);
        }
    }
}

DEFINE_FWK_MODULE(testProducer);

#endif
