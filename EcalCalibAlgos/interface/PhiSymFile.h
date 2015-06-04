#ifndef PHISYMFILE_H
#define PHISYMFILE_H

#include <string>
#include <vector>

#include "TFile.h"
#include "TTree.h"

using namespace std;

//**********EB TREE***********************************************************************

class EBsTree
{
public: 

    //---ctors---
    EBsTree();
    //---dtor---
    ~EBsTree() {};
    //---wrappers
    inline void Fill() {tree_->Fill();};
    inline void Write(const char* name) {tree_->Write(name);};
    inline void Write(string name) {tree_->Write(name.c_str());};
    
    //---branches variables---
    int ieta;
    int iphi;
    float et;
    
private:

    TTree* tree_;    
};

EBsTree::EBsTree()
{
    tree_ = new TTree();
    //---init
    ieta=0;
    iphi=0;
    et=0;
    
    //---create branches
    tree_->Branch("ieta", &ieta, "ieta/I");
    tree_->Branch("iphi", &iphi, "iphi/I");
    tree_->Branch("et", &et, "et/F");
}

//**********EE TREE***********************************************************************

class EEsTree
{
public: 

    //---ctors---
    EEsTree();
    //---dtor---
    ~EEsTree() {};
    //---wrappers
    inline void Fill() {tree_->Fill();};
    inline void Write(const char* name) {tree_->Write(name);};
    inline void Write(string name) {tree_->Write(name.c_str());};
    
    //---branches variables---
    int iring;
    int ix;
    int iy;
    float et;
    
private:

    TTree* tree_;    
};

EEsTree::EEsTree()
{
    tree_ = new TTree();
    //---init
    iring=0;
    ix=0;
    iy=0;
    et=0;
    
    //---create branches
    tree_->Branch("iring", &iring, "iring/I");
    tree_->Branch("ix", &ix, "ix/I");
    tree_->Branch("iy", &iy, "iy/I");
    tree_->Branch("et", &et, "et/F");
}

//**********FILE**************************************************************************

class PhiSymFile
{
public:    
    
    PhiSymFile();
    PhiSymFile(TFile* file);

    inline void Close() {file_->Close();};
    inline void cd() {file_->cd();};

    EBTree ebTree;
    EETree ebTree;
    
private:
    
    TFile* file_;
};

PhiSymFile::PhiSymFile()
{}

PhiSymFile::PhiSymFile(TFile* file)
{
    file_ = file;
    file_->cd();
}

#endif 
