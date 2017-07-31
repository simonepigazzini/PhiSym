#!/bin/bash

DATASET=/AlCaPhiSym/Run2016G-v1/RAW
INSTANCE=global
if [ ! -z "${1}" ]; then    
    DATASET=${1}
fi
if [ ! -z "${2}" ]; then    
    INSTANCE=${2}
fi
    
RUNLIST=`${CMSSW_BASE}/src/PhiSym/EcalCalibAlgos/scripts/das_client.py --query "lumi run dataset=${DATASET} instance=prod/${INSTANCE}" --limit 0 --secondary-key lumi.number`

echo -ne '{\n '$RUNLIST'\n}' | sed 's:]] :]],\n :g' | sed 's:\[\[:\: \[\[:g' | sed 's: \::" \::g' | sed 's:^[^{}]: ":g'

exit 0
