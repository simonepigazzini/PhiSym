#!/bin/bash

GOOD_N_BRANCHES=18

BAD_RUNS=[
PREV_RUN=0
DATASET=/AlCaPhiSym/Run2015A-v1/RAW
if [ ! -z "${2}" ]; then    
    DATASET=${2}
fi
INPUT_JSON=Run2015A.json
if [ ! -z "${1}" ]; then    
    INPUT_JSON=${1}
fi
OUTPUT_JSON=`echo $INPUT_JSON | sed 's:\.json:_filtered\.json:g'`

read -a FILES_LIST <<< `./das_client.py --query="file dataset=${DATASET} instance=prod/global" --limit=0 | sed 's:None: :g'`

for iLINE in ${FILES_LIST[@]}
do
    IFS='/' read -a PATH_FIELDS <<< $iLINE
    read -a PATH_FIELDS <<< $PATH_FIELDS
    CURR_RUN=`echo ${PATH_FIELDS[7]}${PATH_FIELDS[8]}`
    if [ $CURR_RUN != $PREV_RUN ]; then
        PREV_RUN=$CURR_RUN
        BRANCH_COUNT=`edmDumpEventContent $iLINE | wc -l`
        if [ $BRANCH_COUNT != $GOOD_N_BRANCHES ]; then
            BAD_RUNS="$BAD_RUNS'$CURR_RUN', "
        fi
    fi
done 

BAD_RUNS=`echo $BAD_RUNS | sed 's:,$:]:g'`
echo removing: $BAD_RUNS

#./filterJSON.py $INPUT_JSON --output="$OUTPUT_JSON" --runs="$BAD_RUNS"

unset IFS
