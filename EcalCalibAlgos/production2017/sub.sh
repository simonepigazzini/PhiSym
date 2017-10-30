#!/bin/bash

# ./submit.sh -d /AlCaPhiSym/Run2017A-v1/RAW -g 92X_dataRun2_Prompt_v9 -m Run2017A_prompt_v3 -j json_DCSONLY.txt -l multifit --storage T2_CH_CERN

# for era in B C D;
# do

#     ./submit.sh -d /AlCaPhiSym/Run2017${era}-v1/RAW -g 92X_dataRun2_Prompt_v9 -m Run2017${era}_SepRepro_v3 -j Cert_294927-302663_13TeV_PromptReco_Collisions17_JSON.txt -l multifit --storage T2_CH_CERN

# done

for era in B C D;
do
    ./submit.sh -d /AlCaPhiSym/dpg_ecal-crab_PHISYM-CMSSW_9_2_12-multifit-92X_dataRun2_Prompt_v9-Run2017${era}_SepRepro_v3-c970aa7cdede0a44be80c4e98950503e/USER -g 92X_dataRun2_Prompt_v9 --template run_MERGER_template.py --merger --storage T2_CH_CERN -m Run2017${era}_SepRepro_v3-merged_v1 --iovmap=../ntuples/Run2017${era}_SepRepro_v1/IOVMap2017${era}.root -l multifit

done

