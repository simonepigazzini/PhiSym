#include "DataFormats/Common/interface/Wrapper.h"

#include "PhiSym/EcalCalibDataFormats/interface/PhiSymRecHit.h"
#include "PhiSym/EcalCalibDataFormats/interface/PhiSymLumiInfo.h"

namespace
{
    struct dictionary
    {
        PhiSymRecHit dummy11;
        std::vector<PhiSymRecHit> dummy12;
        edm::Wrapper<PhiSymRecHitCollection> dummy13;

        PhiSymLumiInfo dummy21;
        std::vector<PhiSymLumiInfo> dummy22;
        edm::Wrapper<PhiSymLumiInfoCollection> dummy23;
    };

}
