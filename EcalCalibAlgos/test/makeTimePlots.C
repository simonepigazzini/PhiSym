{
    gSystem->Load("libFWCoreFWLite.so"); 
    AutoLibraryLoader::enable();
    gSystem->Load("libDataFormatsFWLite.so");
    gSystem->Load("libDataFormatsPatCandidates.so");
    gSystem->Load("libPhiSymEcalCalibDataFormats.so");

    vector<string> files={
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_191043_191062.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_191086_191226.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_191247_191277.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_191691_191810.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_193093_193334.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_193336_193575.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_193834_194050.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_194051_194120.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_194150_194210.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_194223_194428.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_194429_194479.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_194480_194644.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_194691_194897.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_194912_195115.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_195147_195390.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_195396_195552.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_195633_195868.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_195913_195950.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_195963_196239.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_196249_196438.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_196452_196531.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_198202_198249.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_198268_198522.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_198941_199008.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_199011_199336.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_199356_199436.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_199698_199754.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_199804_199877.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_199960_200091.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_200152_200466.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_200473_200601.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_200990_201115.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_201159_201176.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_201278_201625.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_201657_201824.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_202012_202075.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_202084_202209.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_202237_202477.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_202478_202478.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_203830_203912.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_203909_204101.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_204113_204555.root",
        // //"/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_204563_204601.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_204564_205085.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_205086_205310.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_205111_205217.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_205233_205311.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_205312_205617.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_205339_205627.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_205666_205718.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_205774_206066.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_206088_206210.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_206243_206331.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_206389_206448.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_206466_206513.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_206539_206605.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_206744_206869.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_206897_207100.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_207214_207233.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_207269_207398.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_207454_207518.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_207897_207924.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_208297_208357.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_208390_208487.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/oldThr_summed/summed_208538_208686.root"
        //"/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/2015B/summed_251027_251027.root",
        //"/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/2015B/summed_251028_251028.root",
        //"/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/2015B/summed_251244_251244.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/2015B/summed_251560_251560.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/2015B/summed_251561_251561.root",
        // "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/2015B/summed_251562_251562.root"
    };

    float ebICs[70][EBDetId::kSizeForDenseIndexing]={};
    float eeICs[70][EEDetId::kSizeForDenseIndexing]={};
    pair<int, int> ebMap[EBDetId::kSizeForDenseIndexing];
    int eeMap[EEDetId::kSizeForDenseIndexing];
    pair<int, int> eeMap2[EEDetId::kSizeForDenseIndexing];

    for(int iFile=0; iFile<files.size(); ++iFile)
    {
        TFile* file = TFile::Open(files[iFile].c_str(), "READ");
        if(!file)
            continue;
        CrystalsEBTree ebTree((TTree*)file->Get("eb_xstals"));
        CrystalsEETree eeTree((TTree*)file->Get("ee_xstals"));

        int index=-1;
        while(ebTree.NextEntry())
        {
            ++index;
            ebICs[iFile][index] = ebTree.ic_ch;
            if(iFile==0)
                ebMap[index] = make_pair(ebTree.ieta<0 ? ebTree.ieta+85 : ebTree.ieta+84, ebTree.iphi);
        }

        index=-1;
        while(eeTree.NextEntry())
        {
            ++index;
            eeICs[iFile][index] = eeTree.ic_ch;
            if(iFile==0)
            {
                eeMap[index] = eeTree.iring<0? eeTree.iring+39 : eeTree.iring+38;
                eeMap2[index] = make_pair(eeTree.iring<0 ? -eeTree.ix : eeTree.ix, eeTree.iy);
            }
        }

        file->Close();
    }
    TFile* outFile = new TFile("ic_ratios_vs_time.root", "RECREATE");
    outFile->cd();
    //---EB
    // TH2F* mapAbsEB[70];
    // TH2F* mapRelEB[70];
    TH1F* hAbsEB = new TH1F("hAbsEB", "Absolute #sigma_{ratio} spread --- barrel", 250, 0, 0.1);
    TH1F* hRelEB = new TH1F("hRelEB", "Relative #sigma_{ratio} spread --- barrel", 250, 0, 0.1);
    TH1F* prAbsEB[172];
    TH1F* prRelEB[172];
    TGraphErrors* grAbsRingEB[172];
    TGraphErrors* grRelRingEB[172];
    TGraphErrors* grAbsEB = new TGraphErrors();
    TGraphErrors* grRelEB = new TGraphErrors();
    TF1* fitFuncAbsEB = new TF1("fitFuncAbsEB", "gaus", 0.9, 1.1);
    TF1* fitFuncRelEB = new TF1("fitFuncRelEB", "gaus", 0.98, 1.02);
    //---EE
    // TH2F* mapAbsEE 
    // TH2F* mapRelEE 
    TH1F* hAbsEE = new TH1F("hAbsEE", "Absolute #sigma_{ratio} spread --- endcaps", 250, 0, 0.5);
    TH1F* hRelEE = new TH1F("hRelEE", "Relative #sigma_{ratio} spread --- endcaps", 250, 0, 0.5);
    TH1F* prAbsEE[80];
    TH1F* prRelEE[80];
    TGraphErrors* grAbsRingEE[80];
    TGraphErrors* grRelRingEE[80];
    TGraphErrors* grAbsEE = new TGraphErrors();
    TGraphErrors* grRelEE = new TGraphErrors();
    TF1* fitFuncAbsEE = new TF1("fitFuncAbsEE", "gaus", 0.8, 1.2);
    TF1* fitFuncRelEE = new TF1("fitFuncRelEE", "gaus", 0.8, 1.2);

    //---init eta histos
    for(int iRing=0; iRing<172; ++iRing)
    {
        prAbsEB[iRing] = new TH1F(to_string(iRing).c_str(), "", 1000, 0.8, 1.2);
        prRelEB[iRing] = new TH1F(to_string(iRing+200).c_str(), "", 1000, 0.9, 1.1);
        grAbsRingEB[iRing] = new TGraphErrors();
        grRelRingEB[iRing] = new TGraphErrors();
    }
    for(int iRing=0; iRing<80; ++iRing)
    {
        prAbsEE[iRing] = new TH1F(to_string(iRing+400).c_str(), "", 1000, 0.7, 1.3);
        prRelEE[iRing] = new TH1F(to_string(iRing+600).c_str(), "", 1000, 0.7, 1.3);
        grAbsRingEE[iRing] = new TGraphErrors();
        grRelRingEE[iRing] = new TGraphErrors();
    }
    //---fill histos
    for(int iFile=1; iFile<files.size(); ++iFile)
    {
        TH1F* tmpAbsEB = new TH1F("tmpAbsEB", "", 1000, 0.9, 1.1);
        TH1F* tmpRelEB = new TH1F("tmpRelEB", "", 1000, 0.99, 1.01);
        TH2F* mapAbsEB = new TH2F("mapAbsEB", "", 360, 0.5, 360.5, 171, -0.5, 170.5);
        TH2F* mapRelEB = new TH2F("mapRelEB", "", 360, 0.5, 360.5, 171, -0.5, 170.5);
        TH2F* mapAbsEE = new TH2F("mapAbsEE", "", 201, -100.5, 100.5, 101, 0.5, 100.5);
        TH2F* mapRelEE = new TH2F("mapRelEE", "", 201, -100.5, 100.5, 101, 0.5, 100.5);
        //---EB
        for(int index=0; index<EBDetId::kSizeForDenseIndexing; ++index)
        {
            if(ebICs[0][index] != 0 && ebICs[iFile][index] != 0)
            {
                tmpAbsEB->Fill(ebICs[0][index]/ebICs[iFile][index]);
                mapAbsEB->Fill(ebMap[index].second, ebMap[index].first, ebICs[0][index]/ebICs[iFile][index]);
                prAbsEB[ebMap[index].first]->Fill(ebICs[0][index]/ebICs[iFile][index]);
            }
            if(ebICs[iFile-1][index] != 0 && ebICs[iFile][index] != 0)
            {
                tmpRelEB->Fill(ebICs[iFile-1][index]/ebICs[iFile][index]);
                mapRelEB->Fill(ebMap[index].second, ebMap[index].first, ebICs[iFile-1][index]/ebICs[iFile][index]);
                prRelEB[ebMap[index].first]->Fill(ebICs[iFile-1][index]/ebICs[iFile][index]);
            }
        }
        //---EE
        TH1F* tmpAbsEE = new TH1F("tmpAbsEE", "", 1000, 0.5, 1.5);
        TH1F* tmpRelEE = new TH1F("tmpRelEE", "", 1000, 0.5, 1.5);
        for(int index=0; index<EEDetId::kSizeForDenseIndexing; ++index)
        {
            if(eeICs[0][index] != 0 && eeICs[iFile][index] != 0)
            {
                tmpAbsEE->Fill(eeICs[0][index]/eeICs[iFile][index]);
                mapAbsEE->Fill(eeMap2[index].first, eeMap2[index].second, eeICs[0][index]/eeICs[iFile][index]);
                prAbsEE[eeMap[index]]->Fill(eeICs[0][index]/eeICs[iFile][index]);
            }
            if(eeICs[iFile-1][index] != 0 && eeICs[iFile][index] != 0)
            {
                tmpRelEE->Fill(eeICs[iFile-1][index]/eeICs[iFile][index]);
                mapRelEE->Fill(eeMap2[index].first, eeMap2[index].second, eeICs[iFile-1][index]/eeICs[iFile][index]);
                prRelEE[eeMap[index]]->Fill(eeICs[iFile-1][index]/eeICs[iFile][index]);
            }       
        }
        //---EB
        // tmpAbsEB->Fit(fitFuncAbsEB, "OQ");
        // tmpRelEB->Fit(fitFuncRelEB, "OQ");
        hAbsEB->Fill(fitFuncAbsEB->GetParameter(2));
        grAbsEB->SetPoint(iFile-1, iFile, tmpAbsEB->GetRMS());
        grAbsEB->SetPointError(iFile-1, 0, tmpAbsEB->GetRMSError());
        hRelEB->Fill(fitFuncRelEB->GetParameter(2));
        grRelEB->SetPoint(iFile-1, iFile, tmpRelEB->GetRMS());
        grRelEB->SetPointError(iFile-1, 0, tmpRelEB->GetRMSError());
        tmpAbsEB->Write(string("AbsEB_"+to_string(iFile)).c_str());
        tmpRelEB->Write(string("RelEB_"+to_string(iFile)).c_str());
        mapAbsEB->SetAxisRange(0.98, 1.02, "Z");
        mapRelEB->SetAxisRange(0.98, 1.02, "Z");
        mapAbsEB->Write(string("mapAbsEB_"+to_string(iFile)).c_str());
        mapRelEB->Write(string("mapRelEB_"+to_string(iFile)).c_str());
        tmpAbsEB->Delete();
        tmpRelEB->Delete();
        mapAbsEB->Delete();
        mapRelEB->Delete();
        //---EE
        // tmpAbsEE->Fit(fitFuncAbsEE, "OQ");
        // tmpRelEE->Fit(fitFuncRelEE, "OQ");
        hAbsEE->Fill(fitFuncAbsEE->GetParameter(2));
        grAbsEE->SetPoint(iFile-1, iFile, tmpAbsEE->GetRMS());
        grAbsEE->SetPointError(iFile-1, 0, tmpAbsEE->GetRMSError());
        hRelEE->Fill(fitFuncRelEE->GetParameter(2));
        grRelEE->SetPoint(iFile-1, iFile, tmpRelEE->GetRMS());
        grRelEE->SetPointError(iFile-1, 0, tmpRelEE->GetRMSError());
        tmpAbsEE->Write(string("AbsEE_"+to_string(iFile)).c_str());
        tmpRelEE->Write(string("RelEE_"+to_string(iFile)).c_str());
        mapAbsEE->SetAxisRange(0.95, 1.05, "Z");
        mapRelEE->SetAxisRange(0.95, 1.05, "Z");
        mapAbsEE->Write(string("mapAbsEE_"+to_string(iFile)).c_str());
        mapRelEE->Write(string("mapRelEE_"+to_string(iFile)).c_str());
        tmpAbsEE->Delete();
        tmpRelEE->Delete();
        mapAbsEE->Delete();
        mapRelEE->Delete();
        //---reset
        for(int iRing=0; iRing<171; ++iRing)
        {
            // prAbsEB[iRing]->Fit(fitFuncAbsEB, "OQ");
            // prRelEB[iRing]->Fit(fitFuncRelEB, "OQ");
            // mapAbsEB->Fill(iFile, iRing<85 ? iRing-85 : iRing-84, prAbsEB[iRing]->GetRMS());
            // mapRelEB->Fill(iFile, iRing<85 ? iRing-85 : iRing-84, prRelEB[iRing]->GetRMS());
            grAbsRingEB[iRing]->SetPoint(iFile-1, iFile, prAbsEB[iRing]->GetRMS());
            grAbsRingEB[iRing]->SetPointError(iFile-1, 0, prAbsEB[iRing]->GetRMSError());
            grRelRingEB[iRing]->SetPoint(iFile-1, iFile, prRelEB[iRing]->GetRMS());
            grRelRingEB[iRing]->SetPointError(iFile-1, 0, prRelEB[iRing]->GetRMSError());
            prAbsEB[iRing]->Reset();
            prRelEB[iRing]->Reset();
        }
        for(int iRing=0; iRing<79; ++iRing)
        {
            // prAbsEE[iRing]->Fit(fitFuncAbsEE, "OQ");
            // prRelEE[iRing]->Fit(fitFuncRelEE, "OQ");
            // mapAbsEE->Fill(iFile, iRing<39 ? iRing-39 : -(iRing-38)+39, prAbsEE[iRing]->GetRMS());
            // mapRelEE->Fill(iFile, iRing<39 ? iRing-39 : -(iRing-38)+39, prRelEE[iRing]->GetRMS());
            grAbsRingEE[iRing]->SetPoint(iFile-1, iFile, prAbsEE[iRing]->GetRMS());
            grAbsRingEE[iRing]->SetPointError(iFile-1, 0, prAbsEE[iRing]->GetRMSError());
            grRelRingEE[iRing]->SetPoint(iFile-1, iFile, prRelEE[iRing]->GetRMS());
            grRelRingEE[iRing]->SetPointError(iFile-1, 0, prRelEE[iRing]->GetRMSError());
            prAbsEE[iRing]->Reset();
            prRelEE[iRing]->Reset();
        }
    }
    //---EB
    hAbsEB->SetFillColor(kBlue-4);
    hRelEB->SetFillColor(kRed-4);
    hAbsEB->Write("hAbsEB");
    hRelEB->Write("hRelEB");
    grAbsEB->SetMarkerColor(kBlue);
    grAbsEB->SetMarkerStyle(20);
    grAbsEB->SetMarkerSize(0.7);
    grRelEB->SetMarkerColor(kRed);
    grRelEB->SetMarkerStyle(20);
    grRelEB->SetMarkerSize(0.7);
    grAbsEB->Write("grAbsEB");
    grRelEB->Write("grRelEB");
    // mapAbsEB->Write("mapAbsEB");
    // mapRelEB->Write("mapRelEB");
    //---EE
    hAbsEE->SetFillColor(kBlue-4);
    hRelEE->SetFillColor(kRed-4);
    hAbsEE->Write("hAbsEE");
    hRelEE->Write("hRelEE");
    grAbsEE->SetMarkerColor(kBlue);
    grAbsEE->SetMarkerStyle(20);
    grAbsEE->SetMarkerSize(0.7);
    grRelEE->SetMarkerColor(kRed);
    grRelEE->SetMarkerStyle(20);
    grRelEE->SetMarkerSize(0.7);
    grAbsEE->Write("grAbsEE");
    grRelEE->Write("grRelEE");
    // mapAbsEE->Write("mapAbsEE");
    // mapRelEE->Write("mapRelEE");

    grAbsRingEB[5]->Write("grAbs_ieta_80");
    grAbsRingEB[80]->Write("grAbs_ieta_5");
    grAbsRingEB[5]->Write("grAbs_ieta_165");
    grAbsRingEB[80]->Write("grAbs_ieta_90");        
    grRelRingEB[5]->Write("grRel_ieta_80");
    grRelRingEB[80]->Write("grRel_ieta_5");
    grRelRingEB[5]->Write("grRel_ieta_165");
    grRelRingEB[80]->Write("grRel_ieta_90");

    grAbsRingEE[4]->Write("grAbs_iring_5m");
    grAbsRingEE[14]->Write("grAbs_iring_15m");
    grAbsRingEE[24]->Write("grAbs_iring_25m");
    grAbsRingEE[34]->Write("grAbs_iring_35m");        
    grAbsRingEE[4+39]->Write("grAbs_iring_5p");
    grAbsRingEE[14+39]->Write("grAbs_iring_15p");
    grAbsRingEE[24+38]->Write("grAbs_iring_25p");
    grAbsRingEE[34+39]->Write("grAbs_iring_35p");
    grRelRingEE[4]->Write("grRel_iring_5m");
    grRelRingEE[14]->Write("grRel_iring_15m");
    grRelRingEE[24]->Write("grRel_iring_25m");
    grRelRingEE[34]->Write("grRel_iring_35m");        
    grRelRingEE[4+39]->Write("grRel_iring_5p");
    grRelRingEE[14+39]->Write("grRel_iring_15p");
    grRelRingEE[24+38]->Write("grRel_iring_25p");
    grRelRingEE[34+39]->Write("grRel_iring_35p");
    
    outFile->Close();
}
