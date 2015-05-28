#ifndef DATAFORMAT_PHISYMRECHIT_H
#define DATAFORMAT_PHISYMRECHIT_H

/** \class PhiSymRecHit
 * 
 * Dataformat dedicated to Phi Symmetry ecal calibration
 * 
 * Note: SumEt array ordering:
 *       0 - central value
 *       1 - mis-calib -5%
 *       2 - mis-calib -2.5%
 *       3 - mis-calib +2.5%
 *       4 - mis-calib +5%
 */

#include <vector>

#include "DataFormats/DetId/interface/DetId.h"

//---define the number of allowed mis-calibrated values for etSum_ (+ the central value)
#define N_VALUES 5

class PhiSymRecHit
{
public:
    //---ctors---
    PhiSymRecHit();
    PhiSymRecHit(uint32_t& id, float* etValues=NULL);
    
    //---dtor---
    ~PhiSymRecHit();

    //---getters---
    inline float GetRawId()           const {return id_;};
    inline float GetSumEt(int iMis=0) const {return etSum_[iMis];};
    inline float GetSumEt2()          const {return et2Sum_;};
    inline float GetNhits()           const {return nHits_;};

    //---utils---
    void         AddHit(float* etValues, float laserCorr=0);
    void         Reset();

private:

    uint32_t id_;
    uint32_t nHits_;
    float    etSum_[N_VALUES];
    float    et2Sum_;
    float    lcSum_;
    float    lc2Sum_;
};

namespace edm
{
    typedef std::vector<PhiSymRecHit> PhiSymRecHitCollection;
}

#endif
