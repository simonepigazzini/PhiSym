#include "DataFormats/Common/interface/Wrapper.h"

#include "PhiSym/EcalCalibDataFormat/interface/PhiSymRecHit.h"

namespace
{
    struct dictionary
    {
        PhiSymRecHit dummy11;
        std::vector<PhiSymRecHit> dummy12;
        edm::Wrapper<edm::PhiSymRecHitCollection> dummy13;
    };
}
