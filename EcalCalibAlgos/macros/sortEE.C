void sortEE()
{
    auto f = TFile::Open("ana_rad_ecal_v3.root", "READ");
    auto inputEE = (TTree*)f->Get("EE");

    int ix=0;
    int iy=0;
    int iz=0;
    double sc_barcode=0;
    int producer=0; 
    int rawId=0; 

    int ix2=0;
    int iy2=0;
    int iz2=0;
    double sc_barcode2=0;
    int producer2=0; 
    int rawId2=0; 
    
    inputEE->SetBranchAddress("ix", &ix);
    inputEE->SetBranchAddress("iy", &iy);
    inputEE->SetBranchAddress("iz", &iz);
    inputEE->SetBranchAddress("producer", &producer);
    inputEE->SetBranchAddress("sc_barcode", &sc_barcode);
    inputEE->SetBranchAddress("rawId", &rawId);

    auto ff = TFile::Open("sorted_crystals_info_EE.root", "RECREATE");
    auto EE = (TTree*)inputEE->Clone();
    EE->SetName("EE");

    EE->SetBranchAddress("ix", &ix2);
    EE->SetBranchAddress("iy", &iy2);
    EE->SetBranchAddress("iz", &iz2);
    EE->SetBranchAddress("producer", &producer2);
    EE->SetBranchAddress("sc_barcode", &sc_barcode2);
    EE->SetBranchAddress("rawId", &rawId2);
    
    EE->Reset();
    EE->Print(); 
    inputEE->BuildIndex("iy", "iz*ix"); 
    for(int iY=1; iY<=100; ++iY)
    { 
        for(int iX=1; iX<=100; ++iX)
        {
            vector<int> sides={-1,1};
            for(auto& iZ : sides)
            {
                if(inputEE->GetEntryWithIndex(iY, iZ*iX) == -1)
                    continue;
                ix2 = ix; 
                iy2 = iy;
                iz2 = iz; 
                producer2 = producer; 
                sc_barcode2 = sc_barcode; 
                rawId2 = rawId; 
                EE->Fill();
            }        
        }
    }
    EE->BuildIndex("rawId");
    EE->Write();
    ff->Close();
}

