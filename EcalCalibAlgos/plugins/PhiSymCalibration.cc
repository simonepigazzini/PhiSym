#ifndef _PHISYM_CALIBRATION_
#define _PHISYM_CALIBRATION_

/* ***************************************************************************************
 * kSides=2; 0->EB+, 1->EB-;
 *           0->EE+, 1->EE-;
 * **************************************************************************************/

#include <fstream>

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
#include "PhiSym/EcalCalibDataFormats/interface/CalibrationFile.h"

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
    void               Read2012ICs(string name);
    void               ReadAbsICs(string name);
    void               ComputeICs();
    void               ComputeKfactors();
    void               FillOutput();
    pair<float, float> GetRingKfactor(int& ring, int sub_det);
    pair<float, float> GetChannelKfactor(uint32_t& index, int sub_det);
    
private:
    //---inputs
    edm::Handle<PhiSymInfoCollection> infoHandle_;
    edm::Handle<PhiSymRecHitCollection> recHitEBHandle_;
    edm::Handle<PhiSymRecHitCollection> recHitEEHandle_;
    edm::InputTag infoTag_;
    edm::InputTag recHitEBTag_;
    edm::InputTag recHitEETag_;
    string oldICsFile_;
    string absICsFile_;
    int    blocksToSum_;
    bool   computeICs_;
    int    nSummedLumis_;
    int    nMisCalib_;
    int    nEvents_;
    int    nBlocks_;
    vector<float> misCalibValuesEB_;
    vector<float> misCalibValuesEE_;

    //---calibration---
    EcalRingCalibrationTools calibRing_;
    static const short kNRingsEB = EcalRingCalibrationTools::N_RING_BARREL;
    static const short kNRingsEE = EcalRingCalibrationTools::N_RING_ENDCAP;
    float ebOldICs_[kNRingsEB][360];
    float eeOldICs_[100][100][2];
    float ebAbsICs_[kNRingsEB][360];
    float eeAbsICs_[100][100][2];
    //---ring based
    //---EB
    double ebRingsSumEt_[kNRingsEB][11];
    double ebRingsSumEt2_[kNRingsEB]={0};
    double kFactorsEB_[kNRingsEB]={0};
    double kFactorsErrEB_[kNRingsEB]={0};
    //---EE
    double eeRingsSumEt_[kNRingsEE][11];
    double eeRingsSumEt2_[kNRingsEE]={0};
    double kFactorsEE_[kNRingsEE]={0};
    double kFactorsErrEE_[kNRingsEE]={0};
    //---cristall based
    //---EB
    PhiSymRecHit ebXstals_[EBDetId::kSizeForDenseIndexing];
    bool goodXstalsEB_[kNRingsEB][360][11];
    double kFactorsChEB_[EBDetId::kSizeForDenseIndexing]={0};
    double kFactorsChErrEB_[EBDetId::kSizeForDenseIndexing]={0};
    float ebICErr_[EBDetId::kSizeForDenseIndexing]={0};
    //---EE
    PhiSymRecHit eeXstals_[EEDetId::kSizeForDenseIndexing];
    bool goodXstalsEE_[kNRingsEE][EEDetId::IX_MAX][EEDetId::IY_MAX][11];
    double kFactorsChEE_[EEDetId::kSizeForDenseIndexing]={0};
    double kFactorsChErrEE_[EEDetId::kSizeForDenseIndexing]={0};
    float eeICErr_[EEDetId::kSizeForDenseIndexing]={0};
    bool kFactorComputed_;

    //---outputs
    auto_ptr<CalibrationFile> outFile_;
    edm::Service<TFileService> fs_;
};

PhiSymCalibration::PhiSymCalibration(const edm::ParameterSet& pSet):    
    infoTag_(pSet.getUntrackedParameter<edm::InputTag>("infoTag")),
    recHitEBTag_(pSet.getUntrackedParameter<edm::InputTag>("recHitEBTag")),
    recHitEETag_(pSet.getUntrackedParameter<edm::InputTag>("recHitEETag")),
    oldICsFile_(pSet.getUntrackedParameter<string>("oldCalibFile")),
    absICsFile_(pSet.getUntrackedParameter<string>("absCalibFile")),
    blocksToSum_(pSet.getUntrackedParameter<int>("blocksToSum")),
    computeICs_(pSet.getUntrackedParameter<bool>("computeICs")),
    nSummedLumis_(1),
    nMisCalib_(-1),
    nEvents_(0),
    nBlocks_(0),
    kFactorComputed_(false)
{}

void PhiSymCalibration::beginJob()
{    
    Read2012ICs(oldICsFile_);
    ReadAbsICs(absICsFile_);
    
    //---output file
    outFile_ = auto_ptr<CalibrationFile>(new CalibrationFile(&fs_->file()));    
}

void PhiSymCalibration::endJob()
{
    //---collect spare lumis
    if(nBlocks_!=0)
    {
        //---increment block output trees counters
        outFile_->eb_xstals.block++;
        outFile_->eb_xstals.n_lumis = nBlocks_*nSummedLumis_;
        outFile_->ee_xstals.block++;
        outFile_->ee_xstals.n_lumis = nBlocks_*nSummedLumis_;

        if(computeICs_)
            ComputeICs();
        else
            FillOutput();
    }

    //---finalize outputs
    outFile_->cd();
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
        outFile_->StoreMisCalibs(misCalibValuesEB_, misCalibValuesEE_);
    }

    const map<uint32_t, short>* badChMap = infoHandle_.product()->back().GetBadChannels();
    //---EB---
    //---fill the rings Et sum
    for(auto& recHit : *recHitEBHandle_.product())
    {
        if(badChMap->find(recHit.GetRawId()) != badChMap->end())
            continue;
        EBDetId ebXstal(recHit.GetRawId());
        int currentRing=calibRing_.getRingIndex(ebXstal);
        ebXstals_[ebXstal.denseIndex()] += recHit;
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
        if(badChMap->find(recHit.GetRawId()) != badChMap->end())
            continue;
        EEDetId eeXstal(recHit.GetRawId());
        int currentRing=calibRing_.getRingIndex(eeXstal)-kNRingsEB;
        eeXstals_[eeXstal.denseIndex()] += recHit;
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
    {
        //---increment block output trees counters
        outFile_->eb_xstals.block++;
        outFile_->eb_xstals.n_lumis = nBlocks_*nSummedLumis_;
        outFile_->ee_xstals.block++;
        outFile_->ee_xstals.n_lumis = nBlocks_*nSummedLumis_;

        if(computeICs_)
            ComputeICs();
        else
            FillOutput();
    }
}

//---calibration loop method
void PhiSymCalibration::ComputeICs()
{    
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
            outFile_->eb_xstals.rec_hit = &ebXstals_[index];
            outFile_->eb_xstals.ieta = ebXstal.ieta();
            outFile_->eb_xstals.iphi = ebXstal.iphi();
            outFile_->eb_xstals.k_ring = GetRingKfactor(currentRing, 0).first;
            outFile_->eb_xstals.k_ring_err = GetRingKfactor(currentRing, 0).second;
            outFile_->eb_xstals.k_ch = GetChannelKfactor(index, 0).first;
            outFile_->eb_xstals.k_ch_err = GetChannelKfactor(index, 0).second;
            outFile_->eb_xstals.ic_ring = (ebXstals_[index].GetSumEt(0)/ebRingsSumEt_[currentRing][0]-1)
                /outFile_->eb_xstals.k_ring+1;
            outFile_->eb_xstals.ic_ch = (ebXstals_[index].GetSumEt(0)/ebRingsSumEt_[currentRing][0]-1)
                /outFile_->eb_xstals.k_ch+1;
            outFile_->eb_xstals.ic_old = ebOldICs_[currentRing][ebXstal.iphi()];
            outFile_->eb_xstals.ic_abs = ebAbsICs_[currentRing][ebXstal.iphi()];
            outFile_->eb_xstals.ic_err = ebICErr_[index]/(ebRingsSumEt_[currentRing][0]*outFile_->eb_xstals.k_ch);
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
            outFile_->ee_xstals.rec_hit = &eeXstals_[index];
            outFile_->ee_xstals.iring = currentRing<kNRingsEE/2 ? currentRing-kNRingsEE/2 : currentRing-kNRingsEE/2 + 1;
            outFile_->ee_xstals.ix = eeXstal.ix();
            outFile_->ee_xstals.iy = eeXstal.iy();
            outFile_->ee_xstals.k_ring = GetRingKfactor(currentRing, 1).first;
            outFile_->ee_xstals.k_ring_err = GetRingKfactor(currentRing, 1).second;
            outFile_->ee_xstals.k_ch = GetChannelKfactor(index, 1).first;
            outFile_->ee_xstals.k_ch_err = GetChannelKfactor(index, 1).second;
            outFile_->ee_xstals.ic_ring = (eeXstals_[index].GetSumEt(0)/eeRingsSumEt_[currentRing][0]-1)
                /outFile_->ee_xstals.k_ring+1;
            outFile_->ee_xstals.ic_ch = (eeXstals_[index].GetSumEt(0)/eeRingsSumEt_[currentRing][0]-1)
                /outFile_->ee_xstals.k_ch+1;
            outFile_->ee_xstals.ic_old = eeOldICs_[eeXstal.ix()][eeXstal.iy()][eeXstal.zside()<0 ? 0 : 1];
            outFile_->ee_xstals.ic_abs = eeAbsICs_[eeXstal.ix()][eeXstal.iy()][eeXstal.zside()<0 ? 0 : 1];            
            outFile_->ee_xstals.ic_err = eeICErr_[index]/(eeRingsSumEt_[currentRing][0]*outFile_->ee_xstals.k_ch);
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
        ebRingsSumEt2_[iRing]=0;
        for(int iMis=0; iMis<=nMisCalib_; ++iMis)
            ebRingsSumEt_[iRing][iMis]=0;
    }
    //---reset EE
    for(int iRing=0; iRing<kNRingsEE; ++iRing)
    {
        eeRingsSumEt2_[iRing]=0;
        for(int iMis=0; iMis<=nMisCalib_; ++iMis)
            eeRingsSumEt_[iRing][iMis]=0;
    }
    //---reset counters and kFactor flag
    nEvents_=0;
    nBlocks_=0;
    kFactorComputed_=false;
}

//---compute the ring-dependent k-factors for both EB and EE
// + errors for different iMis are assumed to be ugual to the error on the nominal <sumEt>
// + for the averages the error is the RMS of the channels sumEt distribution inside a ring
//   (sum over N blocks)
// + for the single channel k-factor otherwise the error is the RMS of the sumEt distribution
//   (sum over 1 block)
// + this implies that the error on the single channel k-factor is larger.
void PhiSymCalibration::ComputeKfactors()
{
    TF1* kFactFitFunc = new TF1("kFFF", "[0]*x", -0.5, 0.5);
    kFactFitFunc->SetParameter(0, 1);
    TGraphErrors* kFactorGraph = new TGraphErrors();    

    //---EB---
    //---ring-averaged k-factors
    for(int iRing=0; iRing<kNRingsEB; ++iRing)
    {
        if(ebRingsSumEt_[iRing][0] == 0)
            continue;
        float error = sqrt(ebRingsSumEt2_[iRing]-pow(ebRingsSumEt_[iRing][0], 2))/ebRingsSumEt_[iRing][0];
        for(int iMis=0; iMis<=nMisCalib_; ++iMis)
        {
            float point = ebRingsSumEt_[iRing][iMis]/ebRingsSumEt_[iRing][0]-1;
            float p_error = error*sqrt(pow(point, 2)+1);
            kFactorGraph->SetPoint(iMis, misCalibValuesEB_[iMis]-1, point);
            kFactorGraph->SetPointError(iMis, 0, p_error);
        }
        kFactorGraph->Fit(kFactFitFunc, "Q");
        kFactorsEB_[iRing]=kFactorGraph->GetFunction("kFFF")->GetParameter(0);
        kFactorsErrEB_[iRing]=kFactorGraph->GetFunction("kFFF")->GetParError(0);
    }
    //---channel-based k-factors
    for(uint32_t index=0; index<EBDetId::kSizeForDenseIndexing; ++index)
    {
        if(ebXstals_[index].GetNhits() == 0)
            continue;
        ebICErr_[index]=sqrt(ebXstals_[index].GetSumEt2()/ebXstals_[index].GetNhits()-
                             pow(ebXstals_[index].GetSumEt()/ebXstals_[index].GetNhits(), 2));
        float error = ebICErr_[index]/ebXstals_[index].GetSumEt(0);        
        for(int iMis=0; iMis<=nMisCalib_; ++iMis)
        {
            float point = ebXstals_[index].GetSumEt(iMis)/ebXstals_[index].GetSumEt(0) - 1;
            float p_error = error*sqrt(pow(point, 2)+1);
            kFactorGraph->SetPoint(iMis, misCalibValuesEB_[iMis]-1, point);
            kFactorGraph->SetPointError(iMis, 0, p_error);
        }
        kFactorGraph->Fit(kFactFitFunc, "Q");
        kFactorsChEB_[index]=kFactorGraph->GetFunction("kFFF")->GetParameter(0);
        kFactorsChErrEB_[index]=kFactorGraph->GetFunction("kFFF")->GetParError(0);
    }

    //---EE---
    for(int iRing=0; iRing<kNRingsEE; ++iRing)
    {
        if(eeRingsSumEt_[iRing][0] == 0)
            continue;
        float error = sqrt(eeRingsSumEt2_[iRing]-pow(eeRingsSumEt_[iRing][0], 2))/eeRingsSumEt_[iRing][0];        
        for(int iMis=0; iMis<=nMisCalib_; ++iMis)
        {
            float point = eeRingsSumEt_[iRing][iMis]/eeRingsSumEt_[iRing][0]-1;
            float p_error = error*sqrt(pow(point, 2)+1);
            kFactorGraph->SetPoint(iMis, misCalibValuesEE_[iMis]-1, point);
            kFactorGraph->SetPointError(iMis, 0, p_error);
        }
        kFactorGraph->Fit(kFactFitFunc, "Q");
        kFactorsEE_[iRing]=kFactorGraph->GetFunction("kFFF")->GetParameter(0);
        kFactorsErrEE_[iRing]=kFactorGraph->GetFunction("kFFF")->GetParError(0);
    }
    //---channel-based k-factors
    for(uint32_t index=0; index<EEDetId::kSizeForDenseIndexing; ++index)
    {
        if(eeXstals_[index].GetNhits() == 0)
            continue;
        eeICErr_[index]=sqrt(eeXstals_[index].GetSumEt2()/eeXstals_[index].GetNhits()-
                             pow(eeXstals_[index].GetSumEt()/eeXstals_[index].GetNhits(), 2));
        float error = eeICErr_[index]/eeXstals_[index].GetSumEt(0);        
        for(int iMis=0; iMis<=nMisCalib_; ++iMis)
        {
            float point = eeXstals_[index].GetSumEt(iMis)/eeXstals_[index].GetSumEt(0) - 1;
            float p_error = error*sqrt(pow(point, 2)+1);
            kFactorGraph->SetPoint(iMis, misCalibValuesEE_[iMis]-1, point);
            kFactorGraph->SetPointError(iMis, 0, p_error);
        }
        kFactorGraph->Fit(kFactFitFunc, "Q");
        kFactorsChEE_[index]=kFactorGraph->GetFunction("kFFF")->GetParameter(0);
        kFactorsChErrEE_[index]=kFactorGraph->GetFunction("kFFF")->GetParError(0);
    }
    
    kFactFitFunc->Delete();
    kFactorGraph->Delete();
    kFactorComputed_=true;
}

//---return the ring-based k-factor --- sub_det: 0->EB, 1->EE
pair<float, float> PhiSymCalibration::GetRingKfactor(int& ring, int sub_det)
{
    if(!kFactorComputed_)
        ComputeKfactors();

    if(sub_det == 0)
        return make_pair(kFactorsEB_[ring], kFactorsErrEB_[ring]);
    else
        return make_pair(kFactorsEE_[ring], kFactorsErrEE_[ring]);
}

//---return the channel-based k-factor --- sub_det: 0->EB, 1->EE
pair<float, float> PhiSymCalibration::GetChannelKfactor(uint32_t& index, int sub_det)
{
    if(!kFactorComputed_)
        ComputeKfactors();

    if(sub_det == 0)
        return make_pair(kFactorsChEB_[index], kFactorsChErrEB_[index]);
    else
        return make_pair(kFactorsChEE_[index], kFactorsChErrEE_[index]);
}

//---do not compute k-factors and IC, just add up lumis
void PhiSymCalibration::FillOutput()
{
    //---loop over the EB channels and store summed rechits
    for(uint32_t index=0; index<EBDetId::kSizeForDenseIndexing; ++index)
    {
        EBDetId ebXstal = EBDetId::detIdFromDenseIndex(index);
        int currentRing=calibRing_.getRingIndex(ebXstal);            
        if(goodXstalsEB_[currentRing][ebXstal.iphi()][0])
        {
            //---fill the output tree
            outFile_->eb_xstals.n_events = nEvents_;
            outFile_->eb_xstals.rec_hit = &ebXstals_[index];
            outFile_->eb_xstals.ieta = ebXstal.ieta();
            outFile_->eb_xstals.iphi = ebXstal.iphi();
            outFile_->eb_xstals.Fill();

            //---reset channel status and sum
            ebXstals_[index].Reset();
            for(int iMis=0; iMis<=nMisCalib_; ++iMis)
                goodXstalsEB_[currentRing][ebXstal.iphi()][iMis]=0;
        }
    }
    //---loop over the EE channels and store summed rechits
    for(uint32_t index=0; index<EEDetId::kSizeForDenseIndexing; ++index)
    {
        EEDetId eeXstal = EEDetId::detIdFromDenseIndex(index);
        int currentRing=calibRing_.getRingIndex(eeXstal)-kNRingsEB;            
        if(goodXstalsEE_[currentRing][eeXstal.ix()][eeXstal.iy()][0])
        {
            //---fill the output tree
            outFile_->ee_xstals.n_events = nEvents_;
            outFile_->ee_xstals.rec_hit = &eeXstals_[index];
            outFile_->ee_xstals.iring = currentRing<kNRingsEE/2 ? currentRing-kNRingsEE/2 : currentRing-kNRingsEE/2 + 1;
            outFile_->ee_xstals.ix = eeXstal.ix();
            outFile_->ee_xstals.iy = eeXstal.iy();
            outFile_->ee_xstals.Fill();            

            //---reset channel status and sum
            eeXstals_[index].Reset();
            for(int iMis=0; iMis<=nMisCalib_; ++iMis)
                goodXstalsEE_[currentRing][eeXstal.ix()][eeXstal.iy()][iMis]=0;
        }
    }
    
    //---reset counters and kFactor flag
    nEvents_=0;
    nBlocks_=0;
}

//---if a file is specified read the old ICs, otherwise set them to -1
void PhiSymCalibration::Read2012ICs(string name)
{
    //---no file specified
    if(name == "")
    {
        //---EB
        for(int ieta=0; ieta<kNRingsEB; ++ieta)
            for(int iphi=0; iphi<360; ++iphi)
                ebOldICs_[ieta][iphi]=-1;
        //---EE
        for(int ix=0; ix<100; ++ix)
        {
            for(int iy=0; iy<100; ++iy)
            {
                eeOldICs_[ix][iy][0]=-1;
                eeOldICs_[ix][iy][1]=-1;
            }
        }
    }
    
    //---help variables
    int x,y,subdet;
    float ic, fake;
        
    ifstream oldICs(name.c_str(), ios::in);
    while(oldICs.good())
    {
        oldICs >> x >> y >> subdet >> ic >> fake;
        if(subdet==0)
            ebOldICs_[x<0 ? x+85 : x+84][y]=ic;        
        else
            eeOldICs_[x][y][subdet<0 ? 0 : 1]=ic;
    }
    oldICs.close();

    return;
}

//---if a file is specified read the abs ICs, otherwise set them to -1
void PhiSymCalibration::ReadAbsICs(string name)
{
    //---no file specified
    if(name == "")
    {
        //---EB
        for(int ieta=0; ieta<kNRingsEB; ++ieta)
            for(int iphi=0; iphi<360; ++iphi)
                ebAbsICs_[ieta][iphi]=-1;
        //---EE
        for(int ix=0; ix<100; ++ix)
        {
            for(int iy=0; iy<100; ++iy)
            {
                eeAbsICs_[ix][iy][0]=-1;
                eeAbsICs_[ix][iy][1]=-1;
            }
        }
    }
    
    //---help variables
    int x,y,subdet;
    float ic;
        
    ifstream absICs(name.c_str(), ios::in);
    while(absICs.good())
    {
        absICs >> x >> y >> subdet >> ic;
        if(subdet==0)
            ebAbsICs_[x<0 ? x+85 : x+84][y]=ic;        
        else
            eeAbsICs_[x][y][subdet<0 ? 0 : 1]=ic;
    }
    absICs.close();

    return;
}

DEFINE_FWK_MODULE(PhiSymCalibration);

#endif
