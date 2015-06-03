#include "DataFormats/Common/interface/Wrapper.h"

#include "PhiSym/EcalCalibDataFormats/interface/PhiSymRecHit.h"
#include "PhiSym/EcalCalibDataFormats/interface/PhiSymInfo.h"

namespace
{
    struct dictionary
    {
        PhiSymRecHit dummy11;
        std::vector<PhiSymRecHit> dummy12;
        edm::Wrapper<PhiSymRecHitCollection> dummy13;

        PhiSymInfo dummy21;
        std::vector<PhiSymInfo> dummy22;
        edm::Wrapper<PhiSymInfoCollection> dummy23;
    };

}
