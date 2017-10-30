#include <vector>
#include "TTree.h"

template<class INT, class OUTT>
void MakeHistoryTrees(std::vector<INT> eb_iovs, std::vector<INT> eb_even_iovs, std::vector<INT> eb_odd_iovs,
                      OUTT eb_ratio)
{
    vector<double> etSumEB(eb_iovs.size(), 0); 
    map<int, vector<double> > etSumPN; 
    for(int iV=0; iV<eb_iovs.size(); ++iV)
    { 
        while(eb_iovs[iV]->NextEntry())
        { 
            if(etSumPN.find(WhichPN(eb_iovs[iV]->ieta, eb_iovs[iV]->iphi)) == etSumPN.end())
                etSumPN[WhichPN(eb_iovs[iV]->ieta, eb_iovs[iV]->iphi)] = vector<double>(eb_iovs.size(), 0);
            etSumPN[WhichPN(eb_iovs[iV]->ieta, eb_iovs[iV]->iphi)][iV] += eb_iovs[iV]->rec_hit->GetSumEt(); 
            etSumEB[iV] += eb_iovs[iV]->rec_hit->GetSumEt();
        }
    } 
    for(int i=0; i<61200; ++i)
    { 
        for(int iV=0; iV<eb_iovs.size(); ++iV)
        { 
            eb_iovs[iV]->NextEntry(); 
            eb_even_iovs[iV]->NextEntry(); 
            eb_odd_iovs[iV]->NextEntry();
        } 
        int ref=1; 
        for(int iV=ref; iV<eb_iovs.size(); ++iV)
        { 
            if(iV==ref) eb_ratio->status = eb_iovs[iV]->rec_hit->GetSumEt() == 0 ? 0 : 1; 
            eb_ratio->n_events[iV-ref] = eb_iovs[iV]->n_events; 
            eb_ratio->iov[iV-ref] = iV; 
            eb_ratio->avg_time[iV-ref] = eb_iovs[iV]->avg_time; 
            eb_ratio->hashId = i; 
            eb_ratio->ieta = eb_iovs[ref]->ieta; 
            eb_ratio->iphi = eb_iovs[ref]->iphi; 
            eb_ratio->pn = WhichPN(eb_ratio->ieta, eb_ratio->iphi); 
            eb_ratio->sm = eb_ratio->ieta>0 ? (eb_ratio->iphi-1)/20+1 : -(eb_ratio->iphi-1)/20-1; 
            eb_ratio->mean_bs_x[iV-ref] = eb_iovs[iV]->mean_bs_x; 
            eb_ratio->mean_bs_sigmax[iV-ref] = eb_iovs[iV]->mean_bs_sigmax; 
            eb_ratio->mean_bs_y[iV-ref] = eb_iovs[iV]->mean_bs_y; 
            eb_ratio->mean_bs_sigmay[iV-ref] = eb_iovs[iV]->mean_bs_sigmay; 
            eb_ratio->mean_bs_z[iV-ref] = eb_iovs[iV]->mean_bs_z; 
            eb_ratio->mean_bs_sigmaz[iV-ref] = eb_iovs[iV]->mean_bs_sigmaz; 
            eb_ratio->ic_ratio_abs[iV-ref] = eb_iovs[iV]->ic_ch/eb_iovs[ref]->ic_ch; 
            eb_ratio->ic_ratio_rel[iV-ref] = eb_iovs[iV]->ic_ch/eb_iovs[iV-1]->ic_ch; 
            eb_ratio->ic_precision[iV-ref] = eb_even_iovs[iV]->ic_ch/eb_odd_iovs[iV]->ic_ch; 
            eb_ratio->k_ratio_abs[iV-ref] = eb_iovs[iV]->k_ch/eb_iovs[ref]->k_ch; 
            eb_ratio->k_ratio_rel[iV-ref] = eb_iovs[iV]->k_ch/eb_iovs[iV-1]->k_ch; 
            eb_ratio->mean_et_ratio[iV-ref] = (eb_iovs[iV]->rec_hit->GetSumEt()/eb_iovs[iV]->rec_hit->GetNhits())/(eb_iovs[ref]->rec_hit->GetSumEt()/eb_iovs[ref]->rec_hit->GetNhits()); 
            eb_ratio->eflow_pn_abs[iV-ref] = 1+((eb_iovs[iV]->rec_hit->GetSumEt()/etSumPN[eb_ratio->pn][iV])/(eb_iovs[ref]->rec_hit->GetSumEt()/etSumPN[eb_ratio->pn][ref])-1)/eb_iovs[iV]->k_ch; 
            eb_ratio->eflow_abs[iV-ref] = 1+((eb_iovs[iV]->rec_hit->GetSumEt()/etSumEB[iV])/(eb_iovs[ref]->rec_hit->GetSumEt()/etSumEB[ref])-1)/eb_iovs[iV]->k_ch; 
            eb_ratio->eflow_norm[iV-ref] = 1+((eb_iovs[iV]->rec_hit->GetSumEt()/eb_iovs[iV]->eflow_norm)/(eb_iovs[ref]->rec_hit->GetSumEt()/eb_iovs[ref]->eflow_norm)-1)/eb_iovs[iV]->k_ch; 
            eb_ratio->lc[iV-ref] = eb_iovs[iV]->rec_hit->GetNhits()>0 ? eb_iovs[iV]->rec_hit->GetLCSum()/eb_iovs[iV]->rec_hit->GetNhits() : 0;
        } 
        eb_ratio->n_iovs = eb_iovs.size()-ref; 
        eb_ratio->GetTTreePtr()->Fill();}
    eb_ratio->GetTTreePtr()->BuildIndex("hashId"); 
    eb_ratio->GetTTreePtr()->AddFriend("EB", "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/data/sorted_crystals_info_EB.root"); 
}
