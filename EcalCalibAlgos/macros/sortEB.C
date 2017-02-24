void sortEB()
{
    auto f = TFile::Open("alpha_values_EB_TT_eflow2012.root", "READ");
    auto inputEB = (TTree*)f->Get("alphas");

    int ieta=0;
    int iphi=0;
    float alpha=0;

    int ieta2=0;
    int iphi2=0;
    float alpha2=0;
    
    inputEB->SetBranchAddress("ieta", &ieta);
    inputEB->SetBranchAddress("iphi", &iphi);
    inputEB->SetBranchAddress("alpha", &alpha);

    auto ff = TFile::Open("sorted.root", "RECREATE");
    auto EB = (TTree*)inputEB->Clone();
    EB->SetName("alphas");

    EB->SetBranchAddress("ieta", &ieta2);
    EB->SetBranchAddress("iphi", &iphi2);
    EB->SetBranchAddress("alpha", &alpha2);
    
    EB->Reset();
    EB->Print(); 
    inputEB->BuildIndex("ieta", "iphi"); 
    for(int iEta=-85; iEta<=85; ++iEta)
    { 
        if(iEta==0)
            continue; 
        for(int iPhi=1; iPhi<=360; ++iPhi)
        { 
            //cout << iEta << "  " << iPhi << endl; 
            inputEB->GetEntryWithIndex(iEta, iPhi);
            ieta2 = ieta; 
            iphi2 = iphi; 
            alpha2 = alpha; 
            EB->Fill();
        }        
    }
    EB->Write();
    ff->Close();
}

