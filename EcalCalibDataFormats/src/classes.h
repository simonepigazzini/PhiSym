#include "DataFormats/Common/interface/Wrapper.h"

#include "PhiSym/EcalCalibDataFormats/interface/PhiSymRecHit.h"
#include "PhiSym/EcalCalibDataFormats/interface/PhiSymInfo.h"
#include "PhiSym/EcalCalibDataFormats/interface/PhiSymCalibrationFile.h"
#include "PhiSym/EcalCalibDataFormats/interface/PhiSymSpectraFile.h"

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

        EBSpectraTree dummy31;
        EESpectraTree dummy32;

        // RingsTree dummy41;
        PhiSymCrystalsEBTree dummy42;
        PhiSymCrystalsEETree dummy43;
        PhiSymCalibrationFile dummy44;
    };

}
