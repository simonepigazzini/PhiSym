#include "PhiSym/EcalCalibDataFormat/interface/PhiSymRecHit.h"

//**********constructors******************************************************************
PhiSymRecHit::PhiSymRecHit():
    id_(0), nHits_(0), et2Sum_(0)
{}

PhiSymRecHit::PhiSymRecHit(float& id):
    id_(id), nHits_(0), et2Sum_(0)
{}

//**********utils*************************************************************************

void PhiSymRecHit::AddHit(float* etValues)
{
    if(etValues[0] != 0)
    {
        ++nHits_;
        etSum_[0] += etValues[0];
        et2Sum_ += etValues[0]*etValues[0];
    }
    for(int i=1; i<5; ++i)
        etSum_[i] += etValues[i];
}

void PhiSymRecHit::Reset()
{
    nHits_ = 0;
    et2Sum_ = 0;
    for(int i=0; i<5; ++i)
        etSum_[i] = 0;
}
