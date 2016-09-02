#ifndef CALIBRATIONFILE_H
#define CALIBRATIONFILE_H

#include <string>
#include <vector>

#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"

#include "ExternalTools/DynamicTTree/interface/DynamicTTreeBase.h"

using namespace std;

//**********IC EB TREE********************************************************************

#define DYNAMIC_TREE_NAME CrystalsEBTree
//---create branches
#define DATA_TABLE                              \
    DATA(double, avg_time)                      \
    DATA(char, iov_flag)                        \
    DATA(int, block)                            \
    DATA(int, n_lumis)                          \
    DATA(Long64_t, n_events)                    \
    DATA(float, mean_bs_x)                      \
    DATA(float, mean_bs_sigmax)                 \
    DATA(float, mean_bs_y)                      \
    DATA(float, mean_bs_sigmay)                 \
    DATA(float, mean_bs_z)                      \
    DATA(float, mean_bs_sigmaz)                 \
    DATA(int, ieta)                             \
    DATA(int, iphi)                             \
    DATA(float, k_ring)                         \
    DATA(float, k_ring_err)                     \
    DATA(float, k_ch)                           \
    DATA(float, k_ch_err)                       \
    DATA(float, ic_ring)                        \
    DATA(float, ic_ch)                          \
    DATA(float, ic_old)                         \
    DATA(float, ic_abs)                         \
    DATA(double, ic_ring_err)                   \
    DATA(double, ic_ch_err)                     \
    DATA(double, ic_err_sys)                    

#define DATA_VECT_TABLE                         \
    DATA(int, begin, 2)                         \
    DATA(int, end, 2)                           \
    DATA(float, bounds, 2) 

#define DATA_CLASS_TABLE                        \
    DATA(PhiSymRecHit, rec_hit) 

#include "ExternalTools/DynamicTTree/interface/DynamicTTreeInterface.h"

//**********IC EE TREE********************************************************************

#define DYNAMIC_TREE_NAME CrystalsEETree
//---create branches
#define DATA_TABLE                              \
    DATA(double, avg_time)                      \
    DATA(char, iov_flag)                        \
    DATA(int, block)                            \
    DATA(int, n_lumis)                          \
    DATA(Long64_t, n_events)                    \
    DATA(float, mean_bs_x)                      \
    DATA(float, mean_bs_sigmax)                 \
    DATA(float, mean_bs_y)                      \
    DATA(float, mean_bs_sigmay)                 \
    DATA(float, mean_bs_z)                      \
    DATA(float, mean_bs_sigmaz)                 \
    DATA(int, iring)                            \
    DATA(int, ix)                               \
    DATA(int, iy)                               \
    DATA(float, k_ring)                         \
    DATA(float, k_ring_err)                     \
    DATA(float, k_ch)                           \
    DATA(float, k_ch_err)                       \
    DATA(float, ic_ring)                        \
    DATA(float, ic_ch)                          \
    DATA(float, ic_old)                         \
    DATA(float, ic_abs)                         \
    DATA(double, ic_ring_err)                   \
    DATA(double, ic_ch_err)                     \
    DATA(double, ic_err_sys) 

#define DATA_VECT_TABLE                         \
    DATA(int, begin, 2)                         \
    DATA(int, end, 2)

#define DATA_CLASS_TABLE                        \
    DATA(PhiSymRecHit, rec_hit) 

#include "ExternalTools/DynamicTTree/interface/DynamicTTreeInterface.h"

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
    eb_xstals.GetTTreePtr()->SetMaxVirtualSize(50);
    ee_xstals.GetTTreePtr()->SetMaxVirtualSize(50);
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
