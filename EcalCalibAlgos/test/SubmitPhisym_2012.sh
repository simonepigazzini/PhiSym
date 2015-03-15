#!/bin/sh

#$1 = run_min
#$2 = run_max
#$3 = run_period
#$4 = GT
#$5 = scheduler

python ./filterJSON.py json_Golden.txt --min $1 --max $2 --output jsonls-alcaphisym.txt
#cp json_$1_$2.txt jsonls-alcaphisym.txt  
./runphisymmetry2.sh $5 /AlCaPhiSym/Run$3-v1/RAW Collisions12 $1 $2 $4
