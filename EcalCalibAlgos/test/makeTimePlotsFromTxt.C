{
    gSystem->Load("libFWCoreFWLite.so"); 
    AutoLibraryLoader::enable();
    gSystem->Load("libDataFormatsFWLite.so");
    gSystem->Load("libDataFormatsPatCandidates.so");
    gSystem->Load("libPhiSymEcalCalibDataFormats.so");

    vector<string> files={
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_1_193621.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_203830_203912.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_203909_204101.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_204113_204555.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_204563_204601.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_204563_205085.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_205086_205310.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_205111_205217.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_205233_205311.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_205312_205617.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_205339_205627.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_205666_205718.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_205774_206066.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_206088_206210.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_206243_206331.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_206389_206448.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_206466_206513.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_206539_206605.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_206744_206869.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_206897_207100.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_207214_207233.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_207269_207398.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_207454_207518.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_207897_207924.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_208297_208357.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_208390_208487.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/ntuples/summed_208538_208686.root"};

    float ebICs[30][EBDetId::kSizeForDenseIndexing]={};
    float eeICs[30][EEDetId::kSizeForDenseIndexing]={};
    int ebMap[EBDetId::kSizeForDenseIndexing];
    int eeMap[EEDetId::kSizeForDenseIndexing];
    
    for(int iFile=0; iFile<files.size(); ++iFile)
    {
        TFile* file = TFile::Open(files[iFile].c_str(), "READ");
        CrystalsEBTree ebTree((TTree*)file->Get("eb_xstals"));
        CrystalsEETree eeTree((TTree*)file->Get("ee_xstals"));

        int index=0;
        while(ebTree.NextEntry())
        {
            ++index;
            ebICs[iFile][index] = ebTree.ic_ch;
            if(iFile==0)
                ebMap[index] = ebTree.ieta<0 ? ebTree.ieta+85 : ebTree.ieta+84;
        }

        index=0;
        while(eeTree.NextEntry())
        {
            ++index;
            eeICs[iFile][index] = eeTree.ic_ch;
            if(iFile==0)
                eeMap[index] = eeTree.iring<0? eeTree.iring+39 : eeTree.iring+38;
        }

        file->Close();
    }

    TFile* outFile = new TFile("ic_ratios_vs_time.root", "RECREATE");
    //---EB
    TH2F* mapAbsEB = new TH2F("mapAbsEB", "", 30, 0, 30, 171, -85.5, 85.5);
    TH2F* mapRelEB = new TH2F("mapRelEB", "", 30, 0, 30, 171, -85.5, 85.5);
    TH1F* hAbsEB = new TH1F("hAbsEB", "Absolute #sigma_{ratio} spread --- barrel", 250, 0, 0.01);
    TH1F* hRelEB = new TH1F("hRelEB", "Relative #sigma_{ratio} spread --- barrel", 250, 0, 0.01);
    TH1F* prAbsEB[172];
    TH1F* prRelEB[172];
    TGraphErrors* grAbsEB = new TGraphErrors();
    TGraphErrors* grRelEB = new TGraphErrors();
    TF1* fitFuncAbsEB = new TF1("fitFuncAbsEB", "gaus", 0.9, 1.1);
    TF1* fitFuncRelEB = new TF1("fitFuncRelEB", "gaus", 0.98, 1.02);
    //---EE
    TH2F* mapAbsEE = new TH2F("mapAbsEE", "", 30, 0, 30, 77, -38.5, 38.5);
    TH2F* mapRelEE = new TH2F("mapRelEE", "", 30, 0, 30, 77, -38.5, 38.5);
    TH1F* hAbsEE = new TH1F("hAbsEE", "Absolute #sigma_{ratio} spread --- endcaps", 250, 0, 0.1);
    TH1F* hRelEE = new TH1F("hRelEE", "Relative #sigma_{ratio} spread --- endcaps", 250, 0, 0.1);
    TH1F* prAbsEE[80];
    TH1F* prRelEE[80];
    TGraphErrors* grAbsEE = new TGraphErrors();
    TGraphErrors* grRelEE = new TGraphErrors();
    TF1* fitFuncAbsEE = new TF1("fitFuncAbsEE", "gaus", 0.8, 1.2);
    TF1* fitFuncRelEE = new TF1("fitFuncRelEE", "gaus", 0.8, 1.2);

    //---init eta histos
    for(int iRing=0; iRing<172; ++iRing)
    {
        prAbsEB[iRing] = new TH1F(to_string(iRing).c_str(), "", 1000, 0.8, 1.2);
        prRelEB[iRing] = new TH1F(to_string(iRing+200).c_str(), "", 1000, 0.9, 1.1);
    }
    for(int iRing=0; iRing<80; ++iRing)
    {
        prAbsEE[iRing] = new TH1F(to_string(iRing+400).c_str(), "", 1000, 0.7, 1.3);
        prRelEE[iRing] = new TH1F(to_string(iRing+600).c_str(), "", 1000, 0.7, 1.3);
    }
    //---fill histos
    for(int iFile=1; iFile<files.size(); ++iFile)
    {
        TH1F* tmpAbsEB = new TH1F("tmpAbsEB", "", 1000, 0.9, 1.1);
        TH1F* tmpRelEB = new TH1F("tmpRelEB", "", 1000, 0.98, 1.02);
         //---EB
        for(int index=0; index<EBDetId::kSizeForDenseIndexing; ++index)
        {
            if(ebICs[0][index] != 0 && ebICs[iFile][index] != 0)
            {
                tmpAbsEB->Fill(ebICs[0][index]/ebICs[iFile][index]);
                prAbsEB[ebMap[index]]->Fill(ebICs[0][index]/ebICs[iFile][index]);
            }
            if(ebICs[iFile-1][index] != 0 && ebICs[iFile][index] != 0)
            {
                tmpRelEB->Fill(ebICs[iFile-1][index]/ebICs[iFile][index]);
                prRelEB[ebMap[index]]->Fill(ebICs[iFile-1][index]/ebICs[iFile][index]);
            }
        }
        //---EE
        TH1F* tmpAbsEE = new TH1F("tmpAbsEE", "", 1000, 0.8, 1.2);
        TH1F* tmpRelEE = new TH1F("tmpRelEE", "", 1000, 0.8, 1.2);
        for(int index=0; index<EEDetId::kSizeForDenseIndexing; ++index)
        {
            if(eeICs[0][index] != 0 && eeICs[iFile][index] != 0)
            {
                tmpAbsEE->Fill(eeICs[0][index]/eeICs[iFile][index]);
                prAbsEE[eeMap[index]]->Fill(eeICs[0][index]/eeICs[iFile][index]);
            }
            if(eeICs[iFile-1][index] != 0 && eeICs[iFile][index] != 0)
            {
                tmpRelEE->Fill(eeICs[iFile-1][index]/eeICs[iFile][index]);
                prRelEE[eeMap[index]]->Fill(eeICs[iFile-1][index]/eeICs[iFile][index]);
            }       
        }
        //---EB
        tmpAbsEB->Fit(fitFuncAbsEB, "OQ");
        tmpRelEB->Fit(fitFuncRelEB, "OQ");
        hAbsEB->Fill(fitFuncAbsEB->GetParameter(2));
        grAbsEB->SetPoint(iFile-1, iFile, fitFuncAbsEB->GetParameter(2));
        grAbsEB->SetPointError(iFile-1, 0, fitFuncAbsEB->GetParError(2));
        hRelEB->Fill(fitFuncRelEB->GetParameter(2));
        grRelEB->SetPoint(iFile-1, iFile, fitFuncRelEB->GetParameter(2));
        grRelEB->SetPointError(iFile-1, 0, fitFuncRelEB->GetParError(2));
        tmpAbsEB->Write(string("AbsEB_"+to_string(iFile)).c_str());
        tmpRelEB->Write(string("RelEB_"+to_string(iFile)).c_str());
        tmpAbsEB->Delete();
        tmpRelEB->Delete();
        //---EE
        tmpAbsEE->Fit(fitFuncAbsEE, "OQ");
        tmpRelEE->Fit(fitFuncRelEE, "OQ");
        hAbsEE->Fill(fitFuncAbsEE->GetParameter(2));
        grAbsEE->SetPoint(iFile-1, iFile, fitFuncAbsEE->GetParameter(2));
        grAbsEE->SetPointError(iFile-1, 0, fitFuncAbsEE->GetParError(2));
        hRelEE->Fill(fitFuncRelEE->GetParameter(2));
        grRelEE->SetPoint(iFile-1, iFile, fitFuncRelEE->GetParameter(2));
        grRelEE->SetPointError(iFile-1, 0, fitFuncRelEE->GetParError(2));
        tmpAbsEE->Write(string("AbsEE_"+to_string(iFile)).c_str());
        tmpRelEE->Write(string("RelEE_"+to_string(iFile)).c_str());
        tmpAbsEE->Delete();
        tmpRelEE->Delete();
        //---reset
        for(int iRing=0; iRing<171; ++iRing)
        {
            // prAbsEB[iRing]->Fit(fitFuncAbsEB, "OQ");
            // prRelEB[iRing]->Fit(fitFuncRelEB, "OQ");
            mapAbsEB->Fill(iFile, iRing<85 ? iRing-85 : iRing-84, prAbsEB[iRing]->GetRMS());
            mapRelEB->Fill(iFile, iRing<85 ? iRing-85 : iRing-84, prRelEB[iRing]->GetRMS());
            prAbsEB[iRing]->Reset();
            prRelEB[iRing]->Reset();
        }
        for(int iRing=0; iRing<79; ++iRing)
        {
            // prAbsEE[iRing]->Fit(fitFuncAbsEE, "OQ");
            // prRelEE[iRing]->Fit(fitFuncRelEE, "OQ");
            mapAbsEE->Fill(iFile, iRing<39 ? iRing-39 : -(iRing-38)+39, prAbsEE[iRing]->GetRMS());
            mapRelEE->Fill(iFile, iRing<39 ? iRing-39 : -(iRing-38)+39, prRelEE[iRing]->GetRMS());
            if(iFile==20)
                cout << iRing << "  " << (iRing<39 ? iRing-39 : -(iRing-38)+39) << "  " << prAbsEE[iRing]->GetRMS() << endl;
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
    mapAbsEB->Write("mapAbsEB");
    mapRelEB->Write("mapRelEB");
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
    mapAbsEE->Write("mapAbsEE");
    mapRelEE->Write("mapRelEE");
    
    outFile->Close();
}
