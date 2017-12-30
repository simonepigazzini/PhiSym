#ifndef DATAFORMAT_PHISYM_RECHIT_H
#define DATAFORMAT_PHISYM_RECHIT_H

/** \class PhiSymRecHit
 * 
 * Dataformat dedicated to Phi Symmetry ecal calibration
 * 
 * Note: SumEt array ordering:
 *       0         - central value
 *       1<->N/2   - misCalib<1
 *       N/2+1<->N - misCalib>1
 */

#include <iostream>
#include <iomanip>
#include <vector>

#include "DataFormats/DetId/interface/DetId.h"

//---define the number of allowed mis-calibrated values for etSum_ (+ the central value)
#define N_MISCALIB_VALUES 11

class PhiSymRecHit
{
public:
    //---ctors---
    PhiSymRecHit();
    PhiSymRecHit(uint32_t id, float* etValues=NULL);
    
    //---dtor---
    ~PhiSymRecHit();

    //---getters---
    inline uint32_t GetRawId()           const {return id_;};
    inline uint32_t GetNhits()           const {return nHits_;};
    inline float    GetSumEt(int iMis=0) const {return etSum_[iMis];};
    inline float    GetSumEt2()          const {return et2Sum_;};
    inline float    GetLCSum()           const {return lcSum_;};
    inline float    GetLC2Sum()          const {return lc2Sum_;};

    //---utils---
    void         AddHit(float* etValues, float laserCorr=0);
    void         Reset();

    //---operators---
    PhiSymRecHit&        operator+=(const PhiSymRecHit& rhs);
    friend std::ostream& operator<<(std::ostream& out, const PhiSymRecHit& obj);

private:

    uint32_t id_;
    uint32_t nHits_;
    float    etSum_[N_MISCALIB_VALUES];
    float    et2Sum_;
    float    lcSum_;
    float    lc2Sum_;
};

typedef std::vector<PhiSymRecHit> PhiSymRecHitCollection;

#endif
