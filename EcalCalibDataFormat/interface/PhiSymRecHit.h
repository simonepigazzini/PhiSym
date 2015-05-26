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

class PhiSymRecHit
{
public:
    //---ctors---
    PhiSymRecHit();
    PhiSymRecHit(float& id);
    
    //---dtor---
    ~PhiSymRecHit();

    //---getters---
    inline float GetRawId()           const {return id_;};
    inline float GetSumEt(int iMis=0) const {return etSum_[iMis];};
    inline float GetSumEt2()          const {return et2Sum_;};
    inline float GetNhits()           const {return nHits_;};

    //---utils---
    void         AddHit(float* etValues);
    void         Reset();

private:

    float  id_;
    int    nHits_;
    float  etSum_[5]={0,0,0,0,0};
    float  et2Sum_;
};

namespace edm
{
    typedef std::vector<PhiSymRecHit> PhiSymRecHitCollection;
}

#endif
