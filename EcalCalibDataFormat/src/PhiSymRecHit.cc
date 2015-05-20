#include "PhiSym/EcalCalibDataFormat/interface/PhiSymRecHit.h"

PhiSymRecHit::PhiSymRecHit():
    id_(0), e_sum_(0)
{}

PhiSymRecHit::PhiSymRecHit(DetId id, float energy):
    id_(id), e_sum_(energy)
{}

