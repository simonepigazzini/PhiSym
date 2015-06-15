#ifndef CALIBRATIONFILE_H
#define CALIBRATIONFILE_H

#include <string>
#include <vector>

#include "TFile.h"
#include "TTree.h"
#include "TGraphErrors.h"

using namespace std;

// //**********RINGS TREE********************************************************************

// class RingsTree
// {
// public: 

//     //---ctors---
//     RingsTree();
//     RingsTree(TTree* tree);
//     //---dtor---
//     ~RingsTree() {};
//     //---wrappers
//     inline void Fill() {tree_->Fill();};
//     inline void SetMaxVirtualSize(uint64_t size) {tree_->SetMaxVirtualSize(size);};
//     inline void Write(const char* name) {tree_->Write(name);};
//     inline void Write(string name) {tree_->Write(name.c_str());};
//     bool        NextEntry(int64_t entry=-1);
    
//     //---branches variables---
//     int           block;
//     int           n_lumis;
//     uint64_t      n_events;
//     TGraphErrors* k_graph;
//     float         kfactors;
//     int           iring;
    
// private:

//     TTree* tree_;
//     int64_t currentEntry_;
// };

// RingsTree::RingsTree()
// {
//     tree_ = new TTree();
//     //---init
//     block=0;
//     n_lumis=0;
//     n_events=0;
//     k_graph = new TGraphErrors();
//     kfactors=0;
//     iring=0;
    
//     //---create branches
//     tree_->Branch("block", &block, "block/I");
//     tree_->Branch("n_lumis", &n_lumis, "n_lumis/I");
//     tree_->Branch("n_events", &n_events, "n_events/L");
//     tree_->Branch("k_graphs", &k_graph);
//     tree_->Branch("kfactors", &kfactors, "kfactors/F");
//     tree_->Branch("iring", &iring, "iring/I");
// }

// RingsTree::RingsTree(TTree* tree)
// {
//     tree_ = tree;
//     currentEntry_ = 0;
//     //---init
//     n_lumis=0;
//     n_events=0;    
//     k_graph = new TGraphErrors();
//     kfactors=0;
//     iring=0;
    
//     //---create branches
//     tree_->SetBranchAddress("block", &block);
//     tree_->SetBranchAddress("n_lumis", &n_lumis);
//     tree_->SetBranchAddress("n_events", &n_events);
//     tree_->SetBranchAddress("k_graphs", &k_graph);
//     tree_->SetBranchAddress("kfactors", &kfactors);
//     tree_->SetBranchAddress("iring", &iring);
// }

// bool RingsTree::NextEntry(int64_t entry)
// {
//     if(entry > -1)
//         currentEntry_ = entry;

//     if(currentEntry_ < tree_->GetEntriesFast())
//     {
//         tree_->GetEntry(currentEntry_);
//         return true;
//     }

//     return false;
// }

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
    bool        NextEntry(int64_t entry=-1);
    
    //---branches variables---
    int      block;
    int      n_lumis;
    uint64_t n_events;
    uint64_t n_hits;
    int      ieta;
    int      iphi;
    float    k_ring;
    float    k_ring_err;
    float    k_ch;
    float    k_ch_err;
    float    ic_ring;
    float    ic_ch;
    
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
    n_hits=0;
    ieta=0;
    iphi=0;
    k_ring=0;
    k_ring_err=0;
    k_ch=0;
    k_ch_err=0;
    ic_ring=0;
    ic_ch=0;
    
    //---create branches
    tree_->Branch("block", &block, "block/I");
    tree_->Branch("n_lumis", &n_lumis, "n_lumis/I");
    tree_->Branch("n_events", &n_events, "n_events/L");
    tree_->Branch("n_hits", &n_hits, "n_hits/L");
    tree_->Branch("ieta", &ieta, "ieta/I");
    tree_->Branch("iphi", &iphi, "iphi/I");
    tree_->Branch("k_ring", &k_ring, "k_ring/F");
    tree_->Branch("k_ring_err", &k_ring_err, "k_ring_err/F");
    tree_->Branch("k_ch", &k_ch, "k_ch/F");
    tree_->Branch("k_ch_err", &k_ch_err, "k_ch_err/F");
    tree_->Branch("ic_ring", &ic_ring, "ic_ring/F");
    tree_->Branch("ic_ch", &ic_ch, "ic_ch/F");
}


CrystalsEBTree::CrystalsEBTree(TTree* tree)
{
    tree_ = tree;
    currentEntry_ = -1;
    //---init
    block=0;
    n_lumis=0;
    n_events=0;
    n_hits=0;
    ieta=0;
    iphi=0;
    k_ring=0;
    k_ring_err=0;
    k_ch=0;
    k_ch_err=0;
    ic_ring=0;
    ic_ch=0;
    
    //---create branches
    tree_->SetBranchAddress("block", &block);
    tree_->SetBranchAddress("n_lumis", &n_lumis);
    tree_->SetBranchAddress("n_events", &n_events);
    tree_->SetBranchAddress("n_hits", &n_hits);
    tree_->SetBranchAddress("ieta", &ieta);
    tree_->SetBranchAddress("iphi", &iphi);
    tree_->SetBranchAddress("k_ring", &k_ring);
    tree_->SetBranchAddress("k_ring_err", &k_ring_err);
    tree_->SetBranchAddress("k_ch", &k_ch);
    tree_->SetBranchAddress("k_ch_err", &k_ch_err);
    tree_->SetBranchAddress("ic_ring", &ic_ring);
    tree_->SetBranchAddress("ic_ch", &ic_ch);
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
    bool        NextEntry(int64_t entry=-1);
    
    //---branches variables---
    int      block;
    int      n_lumis;
    uint64_t n_events;
    uint64_t n_hits;
    int      iring;
    int      ix;
    int      iy;
    float    k_ring;
    float    k_ring_err;
    float    k_ch;
    float    k_ch_err;
    float    ic_ring;
    float    ic_ch;
    
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
    n_hits=0;
    iring=0;
    ix=0;
    iy=0;
    k_ring=0;
    k_ring_err=0;
    k_ch=0;
    k_ch_err=0;
    ic_ring=0;
    ic_ch=0;
    
    //---create branches
    tree_->Branch("block", &block, "block/I");
    tree_->Branch("n_lumis", &n_lumis, "n_lumis/I");
    tree_->Branch("n_events", &n_events, "n_events/L");
    tree_->Branch("n_hits", &n_hits, "n_hits/L");
    tree_->Branch("iring", &iring, "iring/I");
    tree_->Branch("ix", &ix, "ix/I");
    tree_->Branch("iy", &iy, "iy/I");
    tree_->Branch("k_ring", &k_ring, "k_ring/F");
    tree_->Branch("k_ring_err", &k_ring_err, "k_ring_err/F");
    tree_->Branch("k_ch", &k_ch, "k_ch/F");
    tree_->Branch("k_ch_err", &k_ch_err, "k_ch_err/F");
    tree_->Branch("ic_ring", &ic_ring, "ic_ring/F");
    tree_->Branch("ic_ch", &ic_ch, "ic_ch/F");
}

CrystalsEETree::CrystalsEETree(TTree* tree)
{
    tree_ = tree;
    currentEntry_ = -1;
    //---init
    block=0;
    n_lumis=0;
    n_events=0;
    n_hits=0;
    iring=0;
    ix=0;
    iy=0;
    k_ring=0;
    k_ring_err=0;
    k_ch=0;
    k_ch_err=0;
    ic_ring=0;
    ic_ch=0;
    
    //---create branches
    tree_->SetBranchAddress("block", &block);
    tree_->SetBranchAddress("n_lumis", &n_lumis);
    tree_->SetBranchAddress("n_events", &n_events);
    tree_->SetBranchAddress("n_hits", &n_hits);
    tree_->SetBranchAddress("iring", &iring);
    tree_->SetBranchAddress("ix", &ix);
    tree_->SetBranchAddress("iy", &iy);
    tree_->SetBranchAddress("k_ring", &k_ring);
    tree_->SetBranchAddress("k_ring_err", &k_ring_err);
    tree_->SetBranchAddress("k_ch", &k_ch);
    tree_->SetBranchAddress("k_ch_err", &k_ch_err);
    tree_->SetBranchAddress("ic_ring", &ic_ring);
    tree_->SetBranchAddress("ic_ch", &ic_ch);
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

    // RingsTree      eb_rings;
    // RingsTree      ee_rings;
    CrystalsEBTree eb_xstals;
    CrystalsEETree ee_xstals;
    
private:
    
    TFile* file_;
};

CalibrationFile::CalibrationFile()
{}

CalibrationFile::CalibrationFile(TFile* file)
{
    file_ = file;
    file_->cd();
    // eb_rings.SetMaxVirtualSize(50);
    // ee_rings.SetMaxVirtualSize(50);
    eb_xstals.SetMaxVirtualSize(50);
    ee_xstals.SetMaxVirtualSize(50);
}

#endif 
