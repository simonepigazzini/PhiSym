#ifndef _PHISYM_CALIBRATION_
#define _PHISYM_CALIBRATION_

/* ***************************************************************************************
 * kSides=2; 0->EB+, 1->EB-;
 *           0->EE+, 1->EE-;
 * **************************************************************************************/

#include "TGraphErrors.h"
#include "TF1.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Common/interface/Provenance.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "Calibration/Tools/interface/EcalRingCalibrationTools.h"

#include "DataFormats/Provenance/interface/ProductIDToBranchID.h"
#include "DataFormats/EcalDetId/interface/EBDetId.h"
#include "DataFormats/EcalDetId/interface/EEDetId.h"

#include "Geometry/CaloGeometry/interface/CaloSubdetectorGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"

#include "PhiSym/EcalCalibDataFormats/interface/PhiSymRecHit.h"
#include "PhiSym/EcalCalibDataFormats/interface/PhiSymInfo.h"
#include "PhiSym/EcalCalibAlgos/interface/CalibrationFile.h"
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

    //---utils
    void         GetICs();
    void         ComputeKfactors();
    float        GetKfactor(int& ring, int sub_det);
    
private:
    //---inputs
    edm::Handle<PhiSymInfoCollection> infoHandle_;
    edm::Handle<PhiSymRecHitCollection> recHitEBHandle_;
    edm::Handle<PhiSymRecHitCollection> recHitEEHandle_;
    edm::InputTag infoTag_;
    edm::InputTag recHitEBTag_;
    edm::InputTag recHitEETag_;
    int blocksToSum_;
    int nSummedLumis_;
    int nMisCalib_;
    int nEvents_;
    int nBlocks_;
    vector<double> misCalibValuesEB_;
    vector<double> misCalibValuesEE_;

    //---calibration---
    EcalRingCalibrationTools calibRing_;
    static const short kNRingsEB = EcalRingCalibrationTools::N_RING_BARREL;
    static const short kNRingsEE = EcalRingCalibrationTools::N_RING_ENDCAP;
    //---ring based
    //---EB
    uint64_t ebOccupancy_[kNRingsEB]={0};
    double ebRingsSumEt_[kNRingsEB][11];
    double ebRingsSumEt2_[kNRingsEB]={0};
    double kFactorsEB_[kNRingsEB]={0};
    double kFactorsErrEB_[kNRingsEB]={0};
    //---EE
    uint64_t eeOccupancy_[kNRingsEE]={0};
    double eeRingsSumEt_[kNRingsEE][11];
    double eeRingsSumEt2_[kNRingsEE]={0};
    double kFactorsEE_[kNRingsEE]={0};
    double kFactorsErrEE_[kNRingsEE]={0};
    //---cristall based
    PhiSymRecHit ebXstals_[EBDetId::kSizeForDenseIndexing];
    bool goodXstalsEB_[kNRingsEB][360][11];
    PhiSymRecHit eeXstals_[EEDetId::kSizeForDenseIndexing];
    bool goodXstalsEE_[kNRingsEE][EEDetId::IX_MAX][EEDetId::IY_MAX][11];
    bool kFactorComputed_;

    //---outputs
    auto_ptr<CalibrationFile> outFile_;
    edm::Service<TFileService> fs_;
};

PhiSymCalibration::PhiSymCalibration(const edm::ParameterSet& pSet):
    infoTag_(pSet.getUntrackedParameter<edm::InputTag>("infoTag")),
    recHitEBTag_(pSet.getUntrackedParameter<edm::InputTag>("recHitEBTag")),
    recHitEETag_(pSet.getUntrackedParameter<edm::InputTag>("recHitEETag")),
    blocksToSum_(pSet.getUntrackedParameter<int>("blocksToSum")),
    nSummedLumis_(1),
    nMisCalib_(-1),
    nEvents_(0),
    nBlocks_(0),
    kFactorComputed_(false)
{}

void PhiSymCalibration::beginJob()
{
    outFile_ = auto_ptr<CalibrationFile>(new CalibrationFile(&fs_->file()));
}

void PhiSymCalibration::endJob()
{
    //---collect spare lumis
    if(nBlocks_!=0)
        GetICs();

    //---finalize outputs
    outFile_->cd();
    outFile_->eb_rings.Write("eb_rings");
    outFile_->ee_rings.Write("ee_rings");
    outFile_->eb_xstals.Write("eb_xstals");
    outFile_->ee_xstals.Write("ee_xstals");
}

void PhiSymCalibration::beginLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& setup)
{}

void PhiSymCalibration::endLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& setup)
{    
    //---get the ecal ring geometry
    edm::ESHandle<CaloGeometry> geoHandle;
    setup.get<CaloGeometryRecord>().get(geoHandle);
    calibRing_.setCaloGeometry(&(*geoHandle));

    //---get PHISYM collections (skip void lumis)
    lumi.getByLabel(infoTag_, infoHandle_);
    lumi.getByLabel(recHitEBTag_, recHitEBHandle_);
    lumi.getByLabel(recHitEETag_, recHitEEHandle_);
    if(!infoHandle_.isValid())
        return;
    //---if good block count it
    nEvents_ += infoHandle_.product()->back().GetNEvents();
    ++nBlocks_;

    //---get mis calib values from metadata
    if(nMisCalib_ == -1)
    {
        nSummedLumis_ = edm::parameterSet(*recHitEBHandle_.provenance()).getParameter<int>("lumisToSum");
        nMisCalib_ = edm::parameterSet(*recHitEBHandle_.provenance()).getParameter<int>("nMisCalib");
        vector<double> misCalibRangeEB =
            edm::parameterSet(*recHitEBHandle_.provenance()).getParameter<vector<double> >("misCalibRangeEB");
        vector<double> misCalibRangeEE =
            edm::parameterSet(*recHitEEHandle_.provenance()).getParameter<vector<double> >("misCalibRangeEE");

        float misCalibStepEB = fabs(misCalibRangeEB[1]-misCalibRangeEB[0])/nMisCalib_;
        float misCalibStepEE = fabs(misCalibRangeEE[1]-misCalibRangeEE[0])/nMisCalib_;
        misCalibValuesEB_.resize(nMisCalib_+1);
        misCalibValuesEE_.resize(nMisCalib_+1);
        for(int iMis=-nMisCalib_/2; iMis<=nMisCalib_/2; ++iMis)
        {
            //--- 0 -> 0; -i -> [1...n/2]; +i -> [n/2+1...n]
            int index = iMis > 0 ? iMis+nMisCalib_/2 : iMis == 0 ? 0 : iMis+nMisCalib_/2+1;
            misCalibValuesEB_[index] = 1+misCalibStepEB*iMis;
            misCalibValuesEE_[index] = 1+misCalibStepEE*iMis;
        }
    }

    //---EB---
    //---fill the rings Et sum
    for(auto& recHit : *recHitEBHandle_.product())
    {
        EBDetId ebXstal(recHit.GetRawId());
        int currentRing=calibRing_.getRingIndex(ebXstal);
        ebXstals_[ebXstal.denseIndex()] += recHit;
        ebOccupancy_[currentRing] += recHit.GetNhits();
        ebRingsSumEt2_[currentRing] += recHit.GetSumEt2();            
        for(int iMis=0; iMis<=nMisCalib_; ++iMis)
        {
            if(recHit.GetSumEt(iMis) > 0)
            {
                ebRingsSumEt_[currentRing][iMis] += recHit.GetSumEt(iMis);
                goodXstalsEB_[currentRing][ebXstal.iphi()][iMis]=1;
            }
        }
    }
        
    //---EE---
    //---fill the rings Et sum
    for(auto& recHit : *recHitEEHandle_.product())
    {
        EEDetId eeXstal(recHit.GetRawId());
        int currentRing=calibRing_.getRingIndex(eeXstal)-kNRingsEB;
        eeXstals_[eeXstal.denseIndex()] += recHit;
        eeOccupancy_[currentRing] += recHit.GetNhits();
        eeRingsSumEt2_[currentRing] += recHit.GetSumEt2();            
        for(int iMis=0; iMis<=nMisCalib_; ++iMis)
        {
            if(recHit.GetSumEt(iMis) > 0)
            {
                eeRingsSumEt_[currentRing][iMis] += recHit.GetSumEt(iMis);
                goodXstalsEE_[currentRing][eeXstal.ix()][eeXstal.iy()][iMis]=1;
            }
        }
    }
    //---call the calibration computer 
    if(nBlocks_ == blocksToSum_)
        GetICs();
}

//---calibration loop method
void PhiSymCalibration::GetICs()
{
    //---increment block output trees counters
    outFile_->eb_rings.block++;
    outFile_->eb_rings.n_lumis = nBlocks_*nSummedLumis_;
    outFile_->ee_rings.block++;
    outFile_->ee_rings.n_lumis = nBlocks_*nSummedLumis_;
    outFile_->eb_xstals.block++;
    outFile_->ee_xstals.block++;
    
    //---get channels IC
    int nGoodThisRing=0;
    //---compute EB rings averages
    for(int iRing=0; iRing<kNRingsEB; ++iRing)
    {
        for(int iMis=0; iMis<=nMisCalib_; ++iMis)
        {
            for(int iPhi=0; iPhi<360; ++iPhi)
                nGoodThisRing += goodXstalsEB_[iRing][iPhi][iMis];
            if(nGoodThisRing > 0)
            {
                if(iMis==0)
                    ebRingsSumEt2_[iRing] = ebRingsSumEt2_[iRing] / nGoodThisRing;
                ebRingsSumEt_[iRing][iMis] = ebRingsSumEt_[iRing][iMis] / nGoodThisRing;
                nGoodThisRing=0;
            }
        }
    }
    //---compute EE rings averages
    for(int iRing=0; iRing<kNRingsEE; ++iRing)
    {
        for(int iMis=0; iMis<=nMisCalib_; ++iMis)
        {
            for(int iX=0; iX<EEDetId::IX_MAX; ++iX)                
                for(int iY=0; iY<EEDetId::IY_MAX; ++iY)
                    nGoodThisRing += goodXstalsEE_[iRing][iX][iY][iMis];
            if(nGoodThisRing > 0)
            {
                if(iMis==0)
                    eeRingsSumEt2_[iRing] = eeRingsSumEt2_[iRing] / nGoodThisRing;
                eeRingsSumEt_[iRing][iMis] = eeRingsSumEt_[iRing][iMis] / nGoodThisRing;
                nGoodThisRing=0;
            }
        }
    }
    ComputeKfactors();
    
    //---loop over the EB channels and compute the IC
    for(uint32_t index=0; index<EBDetId::kSizeForDenseIndexing; ++index)
    {
        EBDetId ebXstal = EBDetId::detIdFromDenseIndex(index);
        int currentRing=calibRing_.getRingIndex(ebXstal);            
        if(goodXstalsEB_[currentRing][ebXstal.iphi()][0])
        {
            //---fill the output tree
            outFile_->eb_xstals.n_events = nEvents_;
            outFile_->eb_xstals.n_hits = ebXstals_[index].GetNhits();
            outFile_->eb_xstals.ieta = ebXstal.ieta();
            outFile_->eb_xstals.iphi = ebXstal.iphi();
            outFile_->eb_xstals.ic = (ebXstals_[index].GetSumEt(0)/ebRingsSumEt_[currentRing][0]-1)/GetKfactor(currentRing, 0)+1;
            outFile_->eb_xstals.Fill();

            //---reset channel status and sum
            ebXstals_[index].Reset();
            for(int iMis=0; iMis<=nMisCalib_; ++iMis)
                goodXstalsEB_[currentRing][ebXstal.iphi()][iMis]=0;
        }
    }
    //---loop over the EE channels and compute the IC
    for(uint32_t index=0; index<EEDetId::kSizeForDenseIndexing; ++index)
    {
        EEDetId eeXstal = EEDetId::detIdFromDenseIndex(index);
        int currentRing=calibRing_.getRingIndex(eeXstal)-kNRingsEB;            
        if(goodXstalsEE_[currentRing][eeXstal.ix()][eeXstal.iy()][0])
        {
            //---fill the output tree
            outFile_->ee_xstals.n_events = nEvents_;
            outFile_->ee_xstals.n_hits = eeXstals_[index].GetNhits();
            outFile_->ee_xstals.zside = eeXstal.zside();
            outFile_->ee_xstals.ix = eeXstal.ix();
            outFile_->ee_xstals.iy = eeXstal.iy();
            outFile_->ee_xstals.ic = (eeXstals_[index].GetSumEt(0)/eeRingsSumEt_[currentRing][0]-1)/GetKfactor(currentRing, 1)+1;
            outFile_->ee_xstals.Fill();            

            //---reset channel status and sum
            eeXstals_[index].Reset();
            for(int iMis=0; iMis<=nMisCalib_; ++iMis)
                goodXstalsEE_[currentRing][eeXstal.ix()][eeXstal.iy()][iMis]=0;
        }
    }
    
    //---reset EB rings
    for(int iRing=0; iRing<kNRingsEB; ++iRing)
    {
        ebOccupancy_[iRing]=0;
        for(int iMis=0; iMis<=nMisCalib_; ++iMis)
            ebRingsSumEt_[iRing][iMis]=0;
    }
    //---reset EE
    for(int iRing=0; iRing<kNRingsEE; ++iRing)
    {
        eeOccupancy_[iRing]=0;
        for(int iMis=0; iMis<=nMisCalib_; ++iMis)
            eeRingsSumEt_[iRing][iMis]=0;
    }
    //---reset counters and kFactor flag
    nEvents_=0;
    nBlocks_=0;
    kFactorComputed_=false;
}

//---compute the ring-dependent k-factors for both EB and EE
void PhiSymCalibration::ComputeKfactors()
{
    TF1* kFactFitFunc = new TF1("kFFF", "[0]*x", -0.5, 0.5);
    kFactFitFunc->SetParameter(0, 1);
    TGraphErrors* kFactorGraph = new TGraphErrors();    

    //---EB
    for(int iRing=0; iRing<kNRingsEB; ++iRing)
    {
        if(ebRingsSumEt_[iRing][0] == 0)
            continue;
        float variance = sqrt(ebRingsSumEt2_[iRing]-pow(ebRingsSumEt_[iRing][0], 2))/ebRingsSumEt_[iRing][0];
        for(int iMis=0; iMis<=nMisCalib_; ++iMis)
        {
            float point = ebRingsSumEt_[iRing][iMis]/ebRingsSumEt_[iRing][0]-1;
            float error = variance*sqrt(pow(point, 2)+1);
            kFactorGraph->SetPoint(iMis, misCalibValuesEB_[iMis]-1, point);
            kFactorGraph->SetPointError(iMis, 0, error);
        }
        kFactorGraph->Fit(kFactFitFunc, "Q");
        kFactorsEB_[iRing]=kFactorGraph->GetFunction("kFFF")->GetParameter(0);
        kFactorsErrEB_[iRing]=kFactorGraph->GetFunction("kFFF")->GetParError(0);

        //---fill the output tree
        outFile_->eb_rings.n_events = nEvents_;
        outFile_->eb_rings.k_graph = kFactorGraph;
        outFile_->eb_rings.kfactors = kFactorsEB_[iRing];
        outFile_->eb_rings.iring = iRing<85 ? iRing-85 : iRing-84;
        outFile_->eb_rings.Fill();
    }

    //---EE
    for(int iRing=0; iRing<kNRingsEE; ++iRing)
    {
        if(eeRingsSumEt_[iRing][0] == 0)
            continue;
        float variance = sqrt(eeRingsSumEt2_[iRing]-pow(eeRingsSumEt_[iRing][0], 2))/eeRingsSumEt_[iRing][0];
        for(int iMis=0; iMis<=nMisCalib_; ++iMis)
        {
            float point = eeRingsSumEt_[iRing][iMis]/eeRingsSumEt_[iRing][0]-1;
            float error = variance*sqrt(pow(point, 2)+1);
            kFactorGraph->SetPoint(iMis, misCalibValuesEE_[iMis]-1, point);
            kFactorGraph->SetPointError(iMis, 0, error);
        }
        kFactorGraph->Fit(kFactFitFunc, "Q");
        kFactorsEE_[iRing]=kFactorGraph->GetFunction("kFFF")->GetParameter(0);
        kFactorsErrEE_[iRing]=kFactorGraph->GetFunction("kFFF")->GetParError(0);

        //---fill the output tree
        outFile_->ee_rings.n_events = nEvents_;
        outFile_->ee_rings.k_graph = kFactorGraph;
        outFile_->ee_rings.kfactors = kFactorsEE_[iRing];
        outFile_->ee_rings.iring = iRing<39 ? iRing-39 : iRing-38;
        outFile_->ee_rings.Fill();
    }

    kFactFitFunc->Delete();
    kFactorGraph->Delete();
    kFactorComputed_=true;
}

//---return the ring-dependent k-factor --- 0->EB, 1->EE
float PhiSymCalibration::GetKfactor(int& ring, int sub_det)
{
    if(!kFactorComputed_)
        ComputeKfactors();

    if(sub_det == 0)
        return kFactorsEB_[ring];
    else
        return kFactorsEE_[ring];
}

DEFINE_FWK_MODULE(PhiSymCalibration);

#endif
