#ifndef __PHISYM_CALIBRATION_LITE__
#define __PHISYM_CALIBRATION_LITE__

#include <map>
#include <vector>
#include <string>

#include "TSystem.h"
#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"
#include "TF1.h"
#include "TGraphErrors.h"

#include "FWCore/FWLite/interface/AutoLibraryLoader.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h"

#include "DataFormats/EcalDetId/interface/EBDetId.h"
#include "DataFormats/EcalDetId/interface/EEDetId.h"

#include "Calibration/Tools/interface/EcalRingCalibrationTools.h"

#include "PhiSym/EcalCalibDataFormats/interface/PhiSymRecHit.h"
#include "PhiSym/EcalCalibDataFormats/interface/CalibrationFile.h"

//****************************************************************************************
//-----gloabal variables definition------
int nLumis_;
int nEvents_;
int nMisCalib_;
vector<double> misCalibValuesEB_;
vector<double> misCalibValuesEE_;

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
//---crystal based
//---EB
map<int, int> ebRingsMap_;
PhiSymRecHit ebXstals_[EBDetId::kSizeForDenseIndexing];
bool goodXstalsEB_[kNRingsEB][360][11];
double kFactorsChEB_[EBDetId::kSizeForDenseIndexing]={0};
double kFactorsChErrEB_[EBDetId::kSizeForDenseIndexing]={0};
float ebICErr_[EBDetId::kSizeForDenseIndexing]={0};
//---EE
map<int, int> eeRingsMap_;
PhiSymRecHit eeXstals_[EEDetId::kSizeForDenseIndexing];
bool goodXstalsEE_[kNRingsEE][EEDetId::IX_MAX][EEDetId::IY_MAX][11];
double kFactorsChEE_[EEDetId::kSizeForDenseIndexing]={0};
double kFactorsChErrEE_[EEDetId::kSizeForDenseIndexing]={0};
float eeICErr_[EEDetId::kSizeForDenseIndexing]={0};
bool kFactorsComputed_;

//---outputs
auto_ptr<CalibrationFile> outFile_;

//----------------------------------------------------------------------------------------
//---compute the ring-dependent k-factors for both EB and EE
// + errors for different iMis are assumed to be ugual to the error on the nominal <sumEt>
// + for the averages the error is the RMS of the channels sumEt distribution inside a ring
// (sum over N blocks)
// + for the single channel k-factor otherwise the error is the RMS of the sumEt distribution
// (sum over 1 block)
// + this implies that the error on the single channel k-factor is larger.
void ComputeKfactors()
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
    kFactorsComputed_=true;
}

//---return the ring-based k-factor --- sub_det: 0->EB, 1->EE
pair<float, float> GetRingKfactor(int& ring, int sub_det)
{
    if(!kFactorsComputed_)
        ComputeKfactors();
    if(sub_det == 0)
        return make_pair(kFactorsEB_[ring], kFactorsErrEB_[ring]);
    else
        return make_pair(kFactorsEE_[ring], kFactorsErrEE_[ring]);
}

//---return the channel-based k-factor --- sub_det: 0->EB, 1->EE
pair<float, float> GetChannelKfactor(uint32_t& index, int sub_det)
{
    if(!kFactorsComputed_)
        ComputeKfactors();
    if(sub_det == 0)
        return make_pair(kFactorsChEB_[index], kFactorsChErrEB_[index]);
    else
        return make_pair(kFactorsChEE_[index], kFactorsChErrEE_[index]);
}

//---cumpute phisym ICs for both EB and EE and fill the output tree
void ComputeICs()
{
    //---increment block output trees counters
    outFile_->eb_xstals.block++;
    outFile_->eb_xstals.n_lumis = nLumis_;
    outFile_->ee_xstals.block++;
    outFile_->ee_xstals.n_lumis = nLumis_;

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
        int currentRing = ebRingsMap_[index];
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
            outFile_->eb_xstals.ic_err = ebICErr_[index]/(ebRingsSumEt_[currentRing][0]*outFile_->eb_xstals.k_ch);
            outFile_->eb_xstals.Fill();
        }
    }
    //---loop over the EE channels and compute the IC
    for(uint32_t index=0; index<EEDetId::kSizeForDenseIndexing; ++index)
    {
        EEDetId eeXstal = EEDetId::detIdFromDenseIndex(index);
        int currentRing = eeRingsMap_[index];
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
            outFile_->ee_xstals.ic_err = eeICErr_[index]/(eeRingsSumEt_[currentRing][0]*outFile_->ee_xstals.k_ch);
            outFile_->ee_xstals.Fill();
        }
    }
}

//**********MAIN**************************************************************************
int main( int argc, char *argv[] )
{
    gSystem->Load("libFWCoreFWLite");
    AutoLibraryLoader::enable();

    if(argc < 2)
    {
        cout << "Usage : " << argv[0] << " [parameters.py]" << endl;
        return 0;
    }
    if(!edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process"))
    {
        cout << " ERROR: ParametersSet 'process' is missing in your configuration file"
             << endl;
        return 0;
    }

    //---inputs    
    vector<string> inputFiles;
    kFactorsComputed_=false;
    nLumis_=0;
    nEvents_=0;
    
    //-----get the python configuration-----
    const edm::ParameterSet &process = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");
    const edm::ParameterSet &filesOpt = process.getParameter<edm::ParameterSet>("ioFilesOpt");
    
    //---get input files
    inputFiles=filesOpt.getParameter<vector<string> >("inputFiles");

    //---output file
    TFile* out = TFile::Open(filesOpt.getParameter<string>("outputFile").c_str(), "RECREATE");
    outFile_ = auto_ptr<CalibrationFile>(new CalibrationFile(out));
    for(int ch=0; ch<EBDetId::kSizeForDenseIndexing; ++ch)
        ebXstals_[ch] = PhiSymRecHit();
    for(int ch=0; ch<EEDetId::kSizeForDenseIndexing; ++ch)
        eeXstals_[ch] = PhiSymRecHit();
    
    for(auto& fileName : inputFiles)
    {
        cout << "Reading file: " << fileName.c_str() << "..." << endl;
        TFile* file = TFile::Open(fileName.c_str());
        CrystalsEBTree ebTree((TTree*)file->Get("eb_xstals"));
        CrystalsEETree eeTree((TTree*)file->Get("ee_xstals"));

        //---get miscalib values
        if(misCalibValuesEB_.size() == 0)
        {
            TH1F* eb = (TH1F*)file->Get("eb_miscalib");
            TH1F* ee = (TH1F*)file->Get("ee_miscalib");
            nMisCalib_=eb->GetNbinsX();
            for(int i=1; i<=nMisCalib_; ++i)
            {
                misCalibValuesEB_.push_back(eb->GetBinContent(i));
                misCalibValuesEE_.push_back(ee->GetBinContent(i));
            }
        }

        int currentBlock=-1;
        //---EB
        while(ebTree.NextEntry())
        {
            //---counts summed lumis
            if(currentBlock != ebTree.block)
            {
                nLumis_ += ebTree.n_lumis;
                nEvents_ += ebTree.n_events;
                currentBlock = ebTree.block;
            }
            
            int index = EBDetId(ebTree.ieta, ebTree.iphi).denseIndex();
            int currentRing = ebTree.ieta<0 ? ebTree.ieta + 85 : ebTree.ieta + 84;
            ebXstals_[index] += *ebTree.rec_hit;
            ebRingsSumEt2_[currentRing] += ebTree.rec_hit->GetSumEt2(); 
            for(int iMis=0; iMis<=nMisCalib_; ++iMis)
            {
                if(ebTree.rec_hit->GetSumEt(iMis) > 0)
                {
                    ebRingsSumEt_[currentRing][iMis] += ebTree.rec_hit->GetSumEt(iMis);
                    goodXstalsEB_[currentRing][ebTree.iphi][iMis]=1;
                }
            }
            //---no geometry available, thus fill a hashedIndex->ring map
            if(ebRingsMap_.find(index) == ebRingsMap_.end())
                ebRingsMap_[index]=currentRing;
        }

        //---EE
        while(eeTree.NextEntry())
        {
            int currentRing = eeTree.iring;
            currentRing = currentRing<0 ? currentRing+kNRingsEE/2 : currentRing-1+kNRingsEE;
            int index = EEDetId(eeTree.ix, eeTree.iy, eeTree.iring>0?1:-1).denseIndex();
            eeXstals_[index] += *eeTree.rec_hit;
            eeRingsSumEt2_[currentRing] += eeTree.rec_hit->GetSumEt2();
            for(int iMis=0; iMis<=nMisCalib_; ++iMis)
            {
                if(eeTree.rec_hit->GetSumEt(iMis) > 0)
                {
                    eeRingsSumEt_[currentRing][iMis] += eeTree.rec_hit->GetSumEt(iMis);
                    goodXstalsEE_[currentRing][eeTree.ix][eeTree.iy][iMis]=1;
                }
            }
            //---no geometry available, thus fill a hashedIndex->ring map
            if(eeRingsMap_.find(index) == eeRingsMap_.end())
                eeRingsMap_[index]=currentRing;
        }
    }
    ComputeICs();

    //---finalize outputs
    outFile_->cd();
    outFile_->eb_xstals.Write("eb_xstals");
    outFile_->ee_xstals.Write("ee_xstals");
    out->Close();
}

#endif
