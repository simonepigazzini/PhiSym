#ifndef _PHISYM_CALIBRATION_
#define _PHISYM_CALIBRATION_

/* ***************************************************************************************
 * kSides=2; 0->EB+, 1->EB-;
 *           0->EE+, 1->EE-;
 * **************************************************************************************/

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Common/interface/Provenance.h"

#include "Calibration/Tools/interface/EcalRingCalibrationTools.h"

#include "DataFormats/Provenance/interface/ProductIDToBranchID.h"
#include "DataFormats/EcalDetId/interface/EBDetId.h"
#include "DataFormats/EcalDetId/interface/EEDetId.h"

#include "Geometry/CaloGeometry/interface/CaloSubdetectorGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"

#include "PhiSym/EcalCalibDataFormats/interface/PhiSymRecHit.h"
#include "PhiSym/EcalCalibDataFormats/interface/PhiSymInfo.h"
#include "PhiSym/EcalCalibAlgos/interface/EcalGeomPhiSymHelper.h"

using namespace std;

class PhiSymCalibration : public edm::EDAnalyzer
{
public:
    explicit PhiSymCalibration(const edm::ParameterSet& pSet);
    ~PhiSymCalibration() {};

d    //---methods
    virtual void beginJob() override;
    virtual void beginLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& setup) override;
    virtual void endLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& setup) override;
    virtual void endJob() override;
    virtual void analyze(edm::Event const&, edm::EventSetup const&) override {};

    //---utils
    float        GetKfactor(const PhiSymRecHit& recHit);
    
private:
    //---inputs
    edm::Handle<PhiSymInfoCollection> infoHandle_;
    edm::Handle<PhiSymRecHitCollection> recHitEBHandle_;
    edm::Handle<PhiSymRecHitCollection> recHitEEHandle_;
    edm::InputTag infoTag_;
    edm::InputTag recHitEBTag_;
    edm::InputTag recHitEETag_;
    int nMisCalib_;
    vector<double> misCalibRangeEB_;
    vector<double> misCalibRangeEE_;

    //---outputs
    //EcalRingCalibrationTools calibRing_;
    static const short kNRingsEB = EcalRingCalibrationTools::N_RING_BARREL;
    static const short kNRingsEE = EcalRingCalibrationTools::N_RING_ENDCAP;
    double ebRingsSumEt_[kNRingsEB];
    double eeRingsSumEt_[kNRingsEE];
};

PhiSymCalibration::PhiSymCalibration(const edm::ParameterSet& pSet):
    infoTag_(pSet.getUntrackedParameter<edm::InputTag>("infoTag")),
    recHitEBTag_(pSet.getUntrackedParameter<edm::InputTag>("recHitEBTag")),
    recHitEETag_(pSet.getUntrackedParameter<edm::InputTag>("recHitEETag")),
    nMisCalib_(-1)
{}

void PhiSymCalibration::beginJob()
{}

void PhiSymCalibration::endJob()
{}

void PhiSymCalibration::beginLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& setup)
{
    //---get the ecal ring geometry
    // edm::ESHandle<CaloGeometry> geoHandle;
    // setup.get<CaloGeometryRecord>().get(geoHandle);
    // calibRing_.setCaloGeometry(&(*geoHandle));

    //---get PHISYM collections (skip void lumis)
    lumi.getByLabel(infoTag_, infoHandle_);
    lumi.getByLabel(recHitEBTag_, recHitEBHandle_);
    lumi.getByLabel(recHitEETag_, recHitEEHandle_);
    if(!infoHandle_.isValid())
        return;
    //---get mis calib values from metadata
    if(nMisCalib_ == -1)
    {
        nMisCalib_ = edm::parameterSet(*recHitEBHandle_.provenance()).getParameter<int>("nMisCalib");
        misCalibRangeEB_ =
            edm::parameterSet(*recHitEBHandle_.provenance()).getParameter<vector<double> >("misCalibRangeEB");
        misCalibRangeEE_ =
            edm::parameterSet(*recHitEBHandle_.provenance()).getParameter<vector<double> >("misCalibRangeEE");
    }
    
    // //---EB---
    // //---fill the rings Et sum
    // for(auto& recHit : *recHitEBHandle_.product())
    // {
    //     EBDetId ebXstal(recHit.GetRawId());
    //     ebRingsSumEt_[calibRing_.getRingIndex(ebXstal)] += recHit.GetSumEt(0);
    // }

    // //---EE---
    // //---fill the rings Et sum
    // for(auto& recHit : *recHitEEHandle_.product())
    // {
    //     EEDetId eeXstal(recHit.GetRawId());
    //     eeRingsSumEt_[calibRing_.getRingIndex(eeXstal)-kNRingsEE] += recHit.GetSumEt(0);
    // }
}

void PhiSymCalibration::endLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& setup)
{
    //---reset rings sumEt
    for(int iRing=0; iRing<kNRingsEB; ++iRing)
            ebRingsSumEt_[iRing]=0;
    for(int iRing=0; iRing<kNRingsEE; ++iRing)
            eeRingsSumEt_[iRing]=0;
}

float PhiSymCalibration::GetKfactor(const PhiSymRecHit& recHit)
{
    return 0;
}

DEFINE_FWK_MODULE(PhiSymCalibration);

#endif
