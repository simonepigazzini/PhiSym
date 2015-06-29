#include "PhiSym/EcalCalibDataFormats/interface/PhiSymRecHit.h"

//**********constructors******************************************************************
PhiSymRecHit::PhiSymRecHit():
    id_(0), nHits_(0), et2Sum_(0)
{
    for(int i=0; i<N_MISCALIB_VALUES; ++i)
        etSum_[i] = 0;
}
            
PhiSymRecHit::PhiSymRecHit(uint32_t id, float* etValues):
    id_(id), nHits_(0), et2Sum_(0)
{
    for(int i=0; i<N_MISCALIB_VALUES; ++i)
        etSum_[i] = 0;

    if(etValues)
        AddHit(etValues);
}

//**********destructor********************************************************************
PhiSymRecHit::~PhiSymRecHit()
{}

//**********utils*************************************************************************

void PhiSymRecHit::AddHit(float* etValues, float laserCorr)
{
    if(etValues[0] > 0)
    {
        ++nHits_;
        etSum_[0] += etValues[0];
        et2Sum_ += etValues[0]*etValues[0];
        lcSum_ += laserCorr;
        lc2Sum_ += laserCorr*laserCorr;
    }
    for(short i=1; i<N_MISCALIB_VALUES; ++i)        
        etSum_[i] += etValues[i];
}

void PhiSymRecHit::Reset()
{
    nHits_ = 0;
    et2Sum_ = 0;
    lcSum_ = 0;
    lc2Sum_ = 0;
    for(short i=0; i<N_MISCALIB_VALUES; ++i)
        etSum_[i] = 0;
}

//**********operators*********************************************************************

PhiSymRecHit& PhiSymRecHit::operator+=(const PhiSymRecHit& rhs)
{
    if(id_ == 0)
        id_ = rhs.GetRawId();
    nHits_ += rhs.GetNhits();
    et2Sum_ += rhs.GetSumEt2();
    lcSum_ += rhs.GetLCSum();
    lc2Sum_ += rhs.GetLC2Sum();
    for(short i=0; i<N_MISCALIB_VALUES; ++i)
        etSum_[i] += rhs.GetSumEt(i);

    return *this;
}

std::ostream& operator<<(std::ostream& out, const PhiSymRecHit& obj)
{
    //---dump all the informations
    out << std::endl;
    out << std::setw(20) << "raw-id:" << obj.GetRawId() << std::endl;
    out << std::setw(20) << "number of hits:" << obj.GetNhits() << std::endl;
    for(short i=1; i<N_MISCALIB_VALUES; ++i)        
        out << std::setw(20) << "sumEt: " << i << obj.GetSumEt(i) << std::endl;
    out << std::setw(20) << "sumEt2: " << obj.GetSumEt2() << std::endl;
    out << std::setw(20) << "laser-corr sum: " << obj.GetLCSum() << std::endl;
    out << std::setw(20) << "laser-corr^2 sum: " << obj.GetLC2Sum() << std::endl;
    out << std::endl;
    
    return out;
}
