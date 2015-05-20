#ifndef TEST_PRODUCER_H
#define TEST_PRODUCER_H

#include <iostream>

#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "PhiSym/EcalCalibDataFormat/interface/PhiSymRecHit.h"

class testProducer : public edm::one::EDProducer<edm::EndLuminosityBlockProducer,
                                                 edm::one::WatchLuminosityBlocks>
{
public:
    explicit testProducer(const edm::ParameterSet& ps);
    ~testProducer();

private:

    virtual void beginJob();
    virtual void beginLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& es) override {};
    virtual void endLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& es) override {};
    virtual void endLuminosityBlockProduce(edm::LuminosityBlock& lumi, edm::EventSetup const& es) override;
    virtual void produce(edm::Event& evt, const edm::EventSetup& es);
    virtual void endJob();
    
    edm::PhiSymRecHitCollection recHitColl_;
};

//----------IMPLEMENTATION----------------------------------------------------------------

testProducer::testProducer(const edm::ParameterSet& pSet)
{
    produces<std::vector<PhiSymRecHit>, edm::InLumi>();
}

testProducer::~testProducer()
{
    recHitColl_.clear();
}

void testProducer::beginJob()
{
    recHitColl_.push_back(PhiSymRecHit());
}

void testProducer::endJob()
{}

void testProducer::endLuminosityBlockProduce(edm::LuminosityBlock& lumi, edm::EventSetup const& es)
{
    std::auto_ptr<edm::PhiSymRecHitCollection> recHitProduct(new edm::PhiSymRecHitCollection);
    recHitColl_.at(0).AddEnergy(1);
    *recHitProduct = recHitColl_;

    lumi.put(recHitProduct);
}

void testProducer::produce(edm::Event& evt, const edm::EventSetup& es)
{
    recHitColl_.at(0).AddEnergy(1);
}

DEFINE_FWK_MODULE(testProducer);

#endif
