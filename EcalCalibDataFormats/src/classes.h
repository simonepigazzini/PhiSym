#include "DataFormats/Common/interface/Wrapper.h"

#include "PhiSym/EcalCalibDataFormats/interface/PhiSymRecHit.h"
#include "PhiSym/EcalCalibDataFormats/interface/PhiSymInfo.h"
#include "PhiSym/EcalCalibDataFormats/interface/CalibrationFile.h"
#include "PhiSym/EcalCalibDataFormats/interface/PhiSymFile.h"

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

        EBTree dummy31;
        EETree dummy32;

        // RingsTree dummy41;
        CrystalsEBTree dummy42;
        CrystalsEETree dummy43;
        CalibrationFile dummy44;
    };

}
