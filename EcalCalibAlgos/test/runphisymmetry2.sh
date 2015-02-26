#! /bin/bash 
#
# yet another glue script to run phisymmetry calibration
# 
# This one will: 
#    1. Call  makephisym to setup the area
#    2. Use crab to run the calibration step 1
#    3. Run step 2
#
# See usage for instructions
#

crabcfg=phisym-cfg.crab.cfg
crab3cfg=phisym-cfg_crab.py
datadir=$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/data
step2out="CalibHistos.root ehistos.root etsumMean_barl.dat etsumMean_endc.dat PhiSymmetryCalibration_miscal_resid.root PhiSymmetryCalibration.root etsummary_barl.dat etsummary_endc.dat" 

usage(){
    echo "$0 mode dataset group firstrun lastrun globaltag"
    exit
}

if [ $# -ne 6 ] 
then
    usage
fi


if [ ! $CRABDIR ] ; then
   echo "Please set CRAB environment"
   exit
fi

mode=$1
dataset=$2
group=$3
firstrun=$4
lastrun=$5
globaltag=$6

. phisym-functions.sh

# setup job
echo "$0: Setting up job"
echo "./makephisym.py --mode=$mode --dataset=$dataset --runrange=$firstrun-$lastrun --globaltag=$globaltag --group=$group" 


./makephisym2.py --mode=$mode --dataset=$dataset --runrange=$firstrun-$lastrun --globaltag="$globaltag" --group="$group"

if [ $? -eq 1 ] ; then
   echo "$0 : Got an error from makephisym , exiting" 
   exit 1
fi


#cd into last made dir .. ok think of something smarter
rundir="$dataset"_"$firstrun"_"$lastrun"
rundir=`echo $rundir | sed s-/-_-g | sed 's/.\(.*\)/\1/'`
echo "$0 : Running dir is $rundir"
cd  $rundir


# create and submit jobs
echo "$0: Invoking  crab"
if [ "$mode" == "caf" ] || [ "$mode" == "remoteGlidein" ]
then
   source /cvmfs/cms.cern.ch/crab/crab.sh
   crab -cfg $crabcfg -create 
   exit 0   
   crab -submit

   findcrabdir

   #keep checking if crab is done
   crabstatus=0  
   while [  $crabstatus -eq 0 ]; do

     sleep 120
     crabdone
   
   done

   crab -getoutput 
elif [ "$mode" == "crab3" ]
then
   source /cvmfs/cms.cern.ch/crab3/crab.sh
   crab submit $crab3cfg

   findcrabdir

   #keep checking if crab is done
   crabstatus=0  
   while [  $crabstatus -eq 0 ]; do

     sleep 120
     crab3done
   
   done

   crab getoutput 
fi

echo "$0: jobs done,  process step 2"
#crab is done, run step 2

#this is what function dostep2 calls the output dir
i="res"
if [ "$mode" == "crab3" ]
then
  i="results"
fi

dostep2

echo "$0 Done at `date`. Results in $rundir/$i"
