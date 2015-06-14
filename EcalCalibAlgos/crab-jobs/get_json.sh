#!/bin/bash

if [ -z "${2}" ]; then    
    DATASET=/AlCaPhiSym/Run2015A-v1/RAW
else
    DATASET=${2}
fi
    
RUNLIST=`./das_client.py --query "lumi run dataset=${DATASET} instance=prod/global" --limit 0 --secondary-key lumi.number`

echo -ne '{\n '$RUNLIST'\n}' | sed 's:]] :]],\n :g' | sed 's:\[\[:\: \[\[:g' | sed 's: \::" \::g' | sed 's:^[^{}]: ":g' > ${1}

exit 0
