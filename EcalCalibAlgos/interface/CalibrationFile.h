#ifndef CALIBRATIONFILE_H
#define CALIBRATIONFILE_H

#include <string>
#include <vector>

#include "TFile.h"
#include "TTree.h"
#include "TGraphErrors.h"

using namespace std;

//**********RINGS TREE********************************************************************

class RingsTree
{
public: 

    //---ctors---
    RingsTree();
    RingsTree(TTree* tree);
    //---dtor---
    ~RingsTree() {};
    //---wrappers
    inline void Fill() {tree_->Fill();};
    inline void SetMaxVirtualSize(uint64_t size) {tree_->SetMaxVirtualSize(size);};
    inline void Write(const char* name) {tree_->Write(name);};
    inline void Write(string name) {tree_->Write(name.c_str());};
    bool        NextEntry(int64_t entry=-1);
    
    //---branches variables---
    int           block;
    int           n_lumis;
    uint64_t      n_events;
    TGraphErrors* k_graph;
    float         kfactors;
    int           iring;
    
private:

    TTree* tree_;
    int64_t currentEntry_;
};

RingsTree::RingsTree()
{
    tree_ = new TTree();
    //---init
    block=0;
    n_lumis=0;
    n_events=0;
    k_graph = new TGraphErrors();
    kfactors=0;
    iring=0;
    
    //---create branches
    tree_->Branch("block", &block, "block/I");
    tree_->Branch("n_lumis", &n_lumis, "n_lumis/I");
    tree_->Branch("n_events", &n_events, "n_events/l");
    tree_->Branch("k_graphs", &k_graph);
    tree_->Branch("kfactors", &kfactors, "kfactors/F");
    tree_->Branch("iring", &iring, "iring/I");
}

RingsTree::RingsTree(TTree* tree)
{
    tree_ = tree;
    currentEntry_ = 0;
    //---init
    n_lumis=0;
    n_events=0;    
    k_graph = new TGraphErrors();
    kfactors=0;
    iring=0;
    
    //---create branches
    tree_->SetBranchAddress("block", &block);
    tree_->SetBranchAddress("n_lumis", &n_lumis);
    tree_->SetBranchAddress("n_events", &n_events);
    tree_->SetBranchAddress("k_graphs", &k_graph);
    tree_->SetBranchAddress("kfactors", &kfactors);
    tree_->SetBranchAddress("iring", &iring);
}

bool RingsTree::NextEntry(int64_t entry)
{
    if(entry > -1)
        currentEntry_ = entry;

    if(currentEntry_ < tree_->GetEntriesFast())
    {
        tree_->GetEntry(currentEntry_);
        return true;
    }

    return false;
}

//**********IC EB TREE********************************************************************

class CristalsEBTree
{
public: 

    //---ctors---
    CristalsEBTree();
    CristalsEBTree(TTree* tree);
    //---dtor---
    ~CristalsEBTree() {};
    //---wrappers
    inline void Fill() {tree_->Fill();};
    inline void SetMaxVirtualSize(uint64_t size) {tree_->SetMaxVirtualSize(size);};
    inline void Write(const char* name) {tree_->Write(name);};
    inline void Write(string name) {tree_->Write(name.c_str());};
    bool        NextEntry(int64_t entry=-1);
    
    //---branches variables---
    int      block;
    uint64_t n_events;
    uint64_t n_hits;
    int      ieta;
    int      iphi;
    float    ic;
    
private:
    
    TTree* tree_;
    int64_t currentEntry_;
};

CristalsEBTree::CristalsEBTree()
{
    tree_ = new TTree();
    //---init
    block=0;
    n_events=0;
    n_hits=0;
    ieta=0;
    iphi=0;
    ic=0;
    
    //---create branches
    tree_->Branch("block", &block, "block/I");
    tree_->Branch("n_events", &n_events, "n_events/l");
    tree_->Branch("n_hits", &n_hits, "n_hits/l");
    tree_->Branch("ieta", &ieta, "ieta/I");
    tree_->Branch("iphi", &iphi, "iphi/I");
    tree_->Branch("ic", &ic, "ic/F");
}


CristalsEBTree::CristalsEBTree(TTree* tree)
{
    tree_ = tree;
    currentEntry_ = 0;
    //---init
    block=0;
    n_events=0;
    n_hits=0;
    ieta=0;
    iphi=0;
    ic=0;
    
    //---create branches
    tree_->SetBranchAddress("block", &block);
    tree_->SetBranchAddress("n_events", &n_events);
    tree_->SetBranchAddress("n_hits", &n_hits);
    tree_->SetBranchAddress("ieta", &ieta);
    tree_->SetBranchAddress("iphi", &iphi);
    tree_->SetBranchAddress("ic", &ic);
}

bool CristalsEBTree::NextEntry(int64_t entry)
{
    if(entry > -1)
        currentEntry_ = entry;

    if(currentEntry_ < tree_->GetEntriesFast())
    {
        tree_->GetEntry(currentEntry_);
        return true;
    }

    return false;
}

//**********IC EE TREE********************************************************************

class CristalsEETree
{
public: 

    //---ctors---
    CristalsEETree();
    CristalsEETree(TTree* tree);
    //---dtor---
    ~CristalsEETree() {};
    //---wrappers
    inline void Fill() {tree_->Fill();};
    inline void SetMaxVirtualSize(uint64_t size) {tree_->SetMaxVirtualSize(size);};
    inline void Write(const char* name) {tree_->Write(name);};
    inline void Write(string name) {tree_->Write(name.c_str());};
    bool        NextEntry(int64_t entry=-1);
    
    //---branches variables---
    int      block;
    uint64_t n_events;
    uint64_t n_hits;
    int      zside;
    int      ix;
    int      iy;
    float    ic;
    
private:

    TTree* tree_;
    int64_t currentEntry_;
};

CristalsEETree::CristalsEETree()
{
    tree_ = new TTree();    
    //---init
    block=0;
    n_events=0;
    n_hits=0;
    zside=0;
    ix=0;
    iy=0;
    ic=0;
    
    //---create branches
    tree_->Branch("block", &block, "block/I");
    tree_->Branch("n_events", &n_events, "n_events/l");
    tree_->Branch("n_hits", &n_hits, "n_hits/l");
    tree_->Branch("zside", &zside, "zside/I");
    tree_->Branch("ix", &ix, "ix/I");
    tree_->Branch("iy", &iy, "iy/I");
    tree_->Branch("ic", &ic, "ic/F");
}

CristalsEETree::CristalsEETree(TTree* tree)
{
    tree_ = tree;
    currentEntry_ = 0;
    //---init
    block=0;
    n_events=0;
    n_hits=0;
    zside=0;
    ix=0;
    iy=0;
    ic=0;
    
    //---create branches
    tree_->SetBranchAddress("block", &block);
    tree_->SetBranchAddress("n_events", &n_events);
    tree_->SetBranchAddress("n_hits", &n_hits);
    tree_->SetBranchAddress("zside", &zside);
    tree_->SetBranchAddress("ix", &ix);
    tree_->SetBranchAddress("iy", &iy);
    tree_->SetBranchAddress("ic", &ic);
}

bool CristalsEETree::NextEntry(int64_t entry)
{
    if(entry > -1)
        currentEntry_ = entry;

    if(currentEntry_ < tree_->GetEntriesFast())
    {
        tree_->GetEntry(currentEntry_);
        return true;
    }

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

    RingsTree      eb_rings;
    RingsTree      ee_rings;
    CristalsEBTree eb_xstals;
    CristalsEETree ee_xstals;
    
private:
    
    TFile* file_;
};

CalibrationFile::CalibrationFile()
{}

CalibrationFile::CalibrationFile(TFile* file)
{
    file_ = file;
    file_->cd();
    eb_rings.SetMaxVirtualSize(50);
    ee_rings.SetMaxVirtualSize(50);
    eb_xstals.SetMaxVirtualSize(50);
    ee_xstals.SetMaxVirtualSize(50);
}

#endif 
