#ifndef _PHISYM_CALIBRATION_
#define _PHISYM_CALIBRATION_

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/EcalDetId/interface/EBDetId.h"
#include "DataFormats/EcalDetId/interface/EEDetId.h"

#include "PhiSym/EcalCalibDataFormats/interface/PhiSymRecHit.h"
#include "PhiSym/EcalCalibDataFormats/interface/PhiSymInfo.h"
#include "PhiSym/EcalCalibAlgos/interface/EcalGeomPhiSymHelper.h"

using namespace std;

class PhiSymCalibration : public edm::EDAnalyzer
{
public:
    explicit PhiSymCalibration(const edm::ParameterSet& pSet);
    ~PhiSymCalibration() {};

    //---methods
    virtual void beginJob() override;
    virtual void beginLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& setup) override;
    virtual void endLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& setup) override;
    virtual void endJob() override;
    virtual void analyze(edm::Event const&, edm::EventSetup const&) override {};

private:
    //---inputs
    edm::Handle<PhiSymInfoCollection> infoHandle_;
    edm::Handle<PhiSymRecHitCollection> recHitEBHandle_;
    edm::Handle<PhiSymRecHitCollection> recHitEEHandle_;
    edm::InputTag infoTag_;
    edm::InputTag recHitEBTag_;
    edm::InputTag recHitEETag_;

    //---outputs
    double barrel_[kBarlRings][kBarlWedges][kSides];
    double endcaps_[kEndcWedgesX][kEndcWedgesY][kSides];
};

PhiSymCalibration::PhiSymCalibration(const edm::ParameterSet& pSet):
    infoTag_(pSet.getUntrackedParameter<edm::InputTag>("infoTag")),
    recHitEBTag_(pSet.getUntrackedParameter<edm::InputTag>("recHitEBTag")),
    recHitEETag_(pSet.getUntrackedParameter<edm::InputTag>("recHitEETag"))
{}

void PhiSymCalibration::beginJob()
{}

void PhiSymCalibration::endJob()
{}

void PhiSymCalibration::beginLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& setup)
{    
    lumi.getByLabel(infoTag_, infoHandle_);
    lumi.getByLabel(recHitEBTag_, recHitEBHandle_);
    lumi.getByLabel(recHitEETag_, recHitEEHandle_);

    if(!infoHandle_.isValid())
        return;

    for(auto& recHit : *recHitEBHandle_.product())
    {}
}

void PhiSymCalibration::endLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& setup)
{
    for(int iRing=0; iRing<kBarlRings; ++iRing)
    {
        for(int iWed=0; iWed<kBarlWedges; ++iWed)
        {
            barrel_[iRing][iWed][0]=0;
            barrel_[iRing][iWed][1]=0;
        }
    }
    for(int iWedX=0; iWedX<kEndcWedgesX; ++iWedX)
    {
        for(int iWedY=0; iWedY<kEndcWedgesY; ++iWedY)
        {
            endcaps_[iWedX][iWedY][0]=0;
            endcaps_[iWedX][iWedY][1]=0;
        }
    }
}

DEFINE_FWK_MODULE(PhiSymCalibration);

#endif
