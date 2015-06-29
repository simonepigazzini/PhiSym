#ifndef CALIBRATIONFILE_H
#define CALIBRATIONFILE_H

#include <string>
#include <vector>

#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"

using namespace std;

//**********IC EB TREE********************************************************************

class CrystalsEBTree
{
public: 

    //---ctors---
    CrystalsEBTree();
    CrystalsEBTree(TTree* tree);
    //---dtor---
    ~CrystalsEBTree() {};
    //---wrappers
    inline void Fill() {tree_->Fill();};
    inline void SetMaxVirtualSize(uint64_t size) {tree_->SetMaxVirtualSize(size);};
    inline void Write(const char* name) {tree_->Write(name);};
    inline void Write(string name) {tree_->Write(name.c_str());};
    inline void Draw(const char* var, const char* cut, Option_t* opt="") {tree_->Draw(var, cut, opt);};
    bool        NextEntry(int64_t entry=-1);
    
    //---branches variables---
    int           block;
    int           n_lumis;
    Long64_t      n_events;
    PhiSymRecHit* rec_hit;
    int           ieta;
    int           iphi;
    float         k_ring;
    float         k_ring_err;
    float         k_ch;
    float         k_ch_err;
    float         ic_ring;
    float         ic_ch;
    float         ic_old;
    float         ic_abs; 
    float         ic_err;
    
private:
    
    TTree* tree_;
    int64_t currentEntry_;
};

CrystalsEBTree::CrystalsEBTree()
{
    tree_ = new TTree();
    //---init
    block=0;
    n_lumis=0;
    n_events=0;
    rec_hit=new PhiSymRecHit();
    ieta=0;
    iphi=0;
    k_ring=0;
    k_ring_err=0;
    k_ch=0;
    k_ch_err=0;
    ic_ring=0;
    ic_ch=0;
    ic_old=0;
    ic_abs=0;
    ic_err=0;
    
    //---create branches
    tree_->Branch("block", &block, "block/I");
    tree_->Branch("n_lumis", &n_lumis, "n_lumis/I");
    tree_->Branch("n_events", &n_events, "n_events/L");
    tree_->Branch("rec_hit", &rec_hit);
    tree_->Branch("ieta", &ieta, "ieta/I");
    tree_->Branch("iphi", &iphi, "iphi/I");
    tree_->Branch("k_ring", &k_ring, "k_ring/F");
    tree_->Branch("k_ring_err", &k_ring_err, "k_ring_err/F");
    tree_->Branch("k_ch", &k_ch, "k_ch/F");
    tree_->Branch("k_ch_err", &k_ch_err, "k_ch_err/F");
    tree_->Branch("ic_ring", &ic_ring, "ic_ring/F");
    tree_->Branch("ic_ch", &ic_ch, "ic_ch/F");
    tree_->Branch("ic_old", &ic_old, "ic_old/F");
    tree_->Branch("ic_abs", &ic_abs, "ic_abs/F");
    tree_->Branch("ic_err", &ic_err, "ic_err/F");
}


CrystalsEBTree::CrystalsEBTree(TTree* tree)
{
    tree_ = tree;
    currentEntry_ = -1;
    //---init
    block=0;
    n_lumis=0;
    n_events=0;
    rec_hit=new PhiSymRecHit();
    ieta=0;
    iphi=0;
    k_ring=0;
    k_ring_err=0;
    k_ch=0;
    k_ch_err=0;
    ic_ring=0;
    ic_ch=0;
    ic_old=0;
    ic_abs=0;
    ic_err=0;
    
    //---create branches
    tree_->SetBranchAddress("block", &block);
    tree_->SetBranchAddress("n_lumis", &n_lumis);
    tree_->SetBranchAddress("n_events", &n_events);
    tree_->SetBranchAddress("rec_hit", &rec_hit);
    tree_->SetBranchAddress("ieta", &ieta);
    tree_->SetBranchAddress("iphi", &iphi);
    tree_->SetBranchAddress("k_ring", &k_ring);
    tree_->SetBranchAddress("k_ring_err", &k_ring_err);
    tree_->SetBranchAddress("k_ch", &k_ch);
    tree_->SetBranchAddress("k_ch_err", &k_ch_err);
    tree_->SetBranchAddress("ic_ring", &ic_ring);
    tree_->SetBranchAddress("ic_ch", &ic_ch);
    tree_->SetBranchAddress("ic_old", &ic_old);
    tree_->SetBranchAddress("ic_abs", &ic_abs);
    tree_->SetBranchAddress("ic_err", &ic_err);
}

bool CrystalsEBTree::NextEntry(int64_t entry)
{
    if(entry > -1)
        currentEntry_ = entry;

    ++currentEntry_;
    if(currentEntry_ < tree_->GetEntriesFast())
    {
        tree_->GetEntry(currentEntry_);
        return true;
    }
    
    currentEntry_=-1;
    return false;
}

//**********IC EE TREE********************************************************************

class CrystalsEETree
{
public: 

    //---ctors---
    CrystalsEETree();
    CrystalsEETree(TTree* tree);
    //---dtor---
    ~CrystalsEETree() {};
    //---wrappers
    inline void Fill() {tree_->Fill();};
    inline void SetMaxVirtualSize(uint64_t size) {tree_->SetMaxVirtualSize(size);};
    inline void Write(const char* name) {tree_->Write(name);};
    inline void Write(string name) {tree_->Write(name.c_str());};
    inline void Draw(const char* var, const char* cut, Option_t* opt="") {tree_->Draw(var, cut, opt);};
    bool        NextEntry(int64_t entry=-1);
    
    //---branches variables---
    int           block;
    int           n_lumis;
    Long64_t      n_events;
    PhiSymRecHit* rec_hit;
    int           iring;
    int           ix;
    int           iy;
    float         k_ring;
    float         k_ring_err;
    float         k_ch;
    float         k_ch_err;
    float         ic_ring;
    float         ic_ch;
    float         ic_old;
    float         ic_abs;
    float         ic_err;
    
private:

    TTree* tree_;
    int64_t currentEntry_;
};

CrystalsEETree::CrystalsEETree()
{
    tree_ = new TTree();    
    //---init
    block=0;
    n_lumis=0;
    n_events=0;
    rec_hit=new PhiSymRecHit();
    iring=0;
    ix=0;
    iy=0;
    k_ring=0;
    k_ring_err=0;
    k_ch=0;
    k_ch_err=0;
    ic_ring=0;
    ic_ch=0;
    ic_old=0;
    ic_abs=0;
    ic_err=0;
    
    //---create branches
    tree_->Branch("block", &block, "block/I");
    tree_->Branch("n_lumis", &n_lumis, "n_lumis/I");
    tree_->Branch("n_events", &n_events, "n_events/L");
    tree_->Branch("rec_hit", &rec_hit);
    tree_->Branch("iring", &iring, "iring/I");
    tree_->Branch("ix", &ix, "ix/I");
    tree_->Branch("iy", &iy, "iy/I");
    tree_->Branch("k_ring", &k_ring, "k_ring/F");
    tree_->Branch("k_ring_err", &k_ring_err, "k_ring_err/F");
    tree_->Branch("k_ch", &k_ch, "k_ch/F");
    tree_->Branch("k_ch_err", &k_ch_err, "k_ch_err/F");
    tree_->Branch("ic_ring", &ic_ring, "ic_ring/F");
    tree_->Branch("ic_ch", &ic_ch, "ic_ch/F");
    tree_->Branch("ic_old", &ic_old, "ic_old/F");
    tree_->Branch("ic_abs", &ic_abs, "ic_abs/F");
    tree_->Branch("ic_err", &ic_err, "ic_err/F");
}

CrystalsEETree::CrystalsEETree(TTree* tree)
{
    tree_ = tree;
    currentEntry_ = -1;
    //---init
    block=0;
    n_lumis=0;
    n_events=0;
    rec_hit=new PhiSymRecHit();
    iring=0;
    ix=0;
    iy=0;
    k_ring=0;
    k_ring_err=0;
    k_ch=0;
    k_ch_err=0;
    ic_ring=0;
    ic_ch=0;
    ic_old=0;
    ic_abs=0;
    ic_err=0;
    
    //---create branches
    tree_->SetBranchAddress("block", &block);
    tree_->SetBranchAddress("n_lumis", &n_lumis);
    tree_->SetBranchAddress("n_events", &n_events);
    tree_->SetBranchAddress("rec_hit", &rec_hit);
    tree_->SetBranchAddress("iring", &iring);
    tree_->SetBranchAddress("ix", &ix);
    tree_->SetBranchAddress("iy", &iy);
    tree_->SetBranchAddress("k_ring", &k_ring);
    tree_->SetBranchAddress("k_ring_err", &k_ring_err);
    tree_->SetBranchAddress("k_ch", &k_ch);
    tree_->SetBranchAddress("k_ch_err", &k_ch_err);
    tree_->SetBranchAddress("ic_ring", &ic_ring);
    tree_->SetBranchAddress("ic_ch", &ic_ch);
    tree_->SetBranchAddress("ic_old", &ic_old);
    tree_->SetBranchAddress("ic_abs", &ic_abs);
    tree_->SetBranchAddress("ic_err", &ic_err);
}

bool CrystalsEETree::NextEntry(int64_t entry)
{
    if(entry > -1)
        currentEntry_ = entry;

    ++currentEntry_;
    if(currentEntry_ < tree_->GetEntriesFast())
    {
        tree_->GetEntry(currentEntry_);
        return true;
    }
    
    currentEntry_=-1;
    return false;
}

//**********FILE**************************************************************************

class CalibrationFile
{
public:    
    
    CalibrationFile();
    CalibrationFile(TFile* file);
    
    inline void Close() {file_->Close();};
    inline void cd() {file_->cd();};
    bool        StoreMisCalibs(vector<float>& eb, vector<float>& ee);
    
    CrystalsEBTree eb_xstals;
    CrystalsEETree ee_xstals;
    TH1F*          eb_miscalib;
    TH1F*          ee_miscalib;
    
private:
    
    TFile* file_;
};

CalibrationFile::CalibrationFile()
{}

CalibrationFile::CalibrationFile(TFile* file)
{
    file_ = file;
    file_->cd();
    eb_xstals.SetMaxVirtualSize(50);
    ee_xstals.SetMaxVirtualSize(50);
}

bool CalibrationFile::StoreMisCalibs(vector<float>& eb, vector<float>& ee)
{
    if(!file_)
        return false;
    
    file_->cd();
    int n=eb.size();
    eb_miscalib = new TH1F("eb_miscalib", "", n, -0.5, n-0.5);
    ee_miscalib = new TH1F("eb_miscalib", "", n, -0.5, n-0.5);
    for(int i=0; i<n; ++i)
    {
        eb_miscalib->SetBinContent(i+1, eb[i]);
        ee_miscalib->SetBinContent(i+1, ee[i]);
    }
    eb_miscalib->Write("eb_miscalib");
    ee_miscalib->Write("ee_miscalib");

    eb_miscalib->Delete();
    ee_miscalib->Delete();
    
    return true;
}

#endif 
