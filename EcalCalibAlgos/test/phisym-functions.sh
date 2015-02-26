#
# helper functions used in some phisym scripts
#
# Author: Stefano Argiro
#

debug=0

#function that returns the last crab dir name in $crabdir
findcrabdir(){
    crabdir=`ls -t |grep crab_ | head -n1`
    #return crabdir
}

#function to check if crab finished, set $crabstatus to 1 if done
crabdone(){
    tmpfile=`mktemp`
    if [ $debug -eq 0 ]; then	
      crab -status  >& $tmpfile
    else
      cp crab.status.output $tmpfile
    fi

    njobs=`grep "Total Jobs" $tmpfile | awk '{print $2}'`
    ndone=`grep -i "DONE" $tmpfile |wc| awk '{print $1}'`
    # number of jobs with exit status zero
    nzero=`cat $tmpfile | awk '{print $6}'| grep -i "0"| wc | awk '{print $1}'`

#    if [ $debug -eq 1 ]; then
      echo "Total number of jobs $njobs of which $ndone completed"
#    fi

    if [ "$njobs" == "$ndone" ] ; then
     rm $tmpfile
     crabstatus=1
    else
     rm $tmpfile
     crabstatus=0
    fi    
    
    #return crabstatus   
}

crab3done(){
    tmpfile=`mktemp`
    #tmpfile=tmp.xOU9IcTWnb
    if [ $debug -eq 0 ]; then	
      crab status  >& $tmpfile
    else
      cp crab.status.output $tmpfile
    fi
    
    status=0
    njobs=0
    ndone=0

    while read line; do
       if [[ $line == *"finished"* ]]
       then
          status=2
       fi
       if [[ $line == *"idle"* || $line == *"unsubmitted"* || $line == *"running"* ]]
       then
          status=1
       fi
    done <$tmpfile
     
    while read line; do
       if [ $status -eq 1 ]
       then
          if [[ $line == *"idle"* ]]
          then
             ndone=`cat $tmpfile  | grep idle | sed 's|.*(\([0-9]*\)/\([0-9]*\))|\1\n\2|' | head -1`
             njobs=`cat $tmpfile  | grep idle | sed 's|.*(\([0-9]*\)/\([0-9]*\))|\1\n\2|' | tail -1`
             nchar=`grep -o "s" <<<"$njobs" | wc -l` 
             if [ $nchar -gt 5 ]
             then
                njobs=0   
             fi
             ndone=0
          elif [[ $line == *"unsubmitted"* ]]
          then
             ndone=`cat $tmpfile  | grep unsubmitted | sed 's|.*(\([0-9]*\)/\([0-9]*\))|\1\n\2|' | head -1`
             njobs=`cat $tmpfile  | grep unsubmitted | sed 's|.*(\([0-9]*\)/\([0-9]*\))|\1\n\2|' | tail -1`
             nchar=`grep -o "s" <<<"$njobs" | wc -l` 
             if [ $nchar -gt 5 ]
             then
                njobs=0   
             fi
             ndone=0
          elif [[ $line == *"running"* ]]
          then
             ndone=`cat $tmpfile  | grep running | sed 's|.*(\([0-9]*\)/\([0-9]*\))|\1\n\2|' | head -1`
             njobs=`cat $tmpfile  | grep running | sed 's|.*(\([0-9]*\)/\([0-9]*\))|\1\n\2|' | tail -1`
             nchar=`grep -o "s" <<<"$njobs" | wc -l` 
             if [ $nchar -gt 5 ]
             then
                njobs=0   
             fi
             ndone=0
          fi
       elif [ $status -eq 2 ]
       then
          if [[ $line == *"finished"* ]]
          then
             ndone=`cat $tmpfile  | grep finished | sed 's|.*(\([0-9]*\)/\([0-9]*\))|\1\n\2|' | head -1`
             njobs=`cat $tmpfile  | grep finished | sed 's|.*(\([0-9]*\)/\([0-9]*\))|\1\n\2|' | tail -1`
             nchar=`grep -o "s" <<<"$njobs" | wc -l` 
             if [ $nchar -gt 5 ]
             then
                njobs=0   
             fi
          fi
       fi 
    done <$tmpfile

#    if [ $debug -eq 1 ]; then
      echo "Total number of jobs $njobs of which $ndone completed"
#    fi

    if [ "$njobs" == "$ndone" ] && [ $njobs -gt 0 ] && [ $ndone -gt 0 ] ; then
     rm $tmpfile
     crabstatus=1
    else
     rm $tmpfile
     crabstatus=0
    fi    
}



#
# do the step 2 in current dir assuming we have crab output 
#
dostep2(){
   
   if [ "$mode" == "crab3" ] 
   then
     results='results'
   else
     results='res'
   fi

   #take the first k file 
   kbarlfile=`ls $crabdir/$results/k_barl_* |head -n1`
   kendcfile=`ls $crabdir/$results/k_endc_* |head -n1`

   cp $kbarlfile $crabdir/$results/k_barl.dat
   cp $kendcfile $crabdir/$results/k_endc.dat
   cat $crabdir/$results/etsum_barl_*.dat > $crabdir/$results/etsum_barl.dat
   cat $crabdir/$results/etsum_endc_*.dat > $crabdir/$results/etsum_endc.dat

   ln -sf $crabdir/$results/k_barl.dat
   ln -sf $crabdir/$results/k_endc.dat
   ln -sf $crabdir/$results/etsum_barl.dat
   ln -sf $crabdir/$results/etsum_endc.dat

   mkdir -p $i

   cmsRun phisym_step2.py >& $i/cmsrun.step2.$i.log

   if [ $? -ne 0 ] ; then
     echo "Possible problems with step2, please check $i/cmsrun.step2.$i.log"
   fi  

   rm k_barl.dat
   rm k_endc.dat
   rm etsum_barl.dat
   rm etsum_endc.dat

       
   mv $step2out $i

   if [ -f  $datadir/EcalIntercalibConstants.xml ] ; then
      mv $datadir/EcalIntercalibConstants.xml $datadir/EcalIntercalibConstants_$i.xml 
   fi

   cp EcalIntercalibConstants_new.xml $i/EcalIntercalibConstants_$i.xml
   mv EcalIntercalibConstants_new.xml $datadir/EcalIntercalibConstants.xml
 
}



#
# do the step 2 in current dir assuming we have crab output 
#
dostep2loop(){
     #take the first k file 
   kbarlfile=`ls $crabdir/res/k_barl_* |head -n1`
   kendcfile=`ls $crabdir/res/k_endc_* |head -n1`

   cp $kbarlfile $crabdir/res/k_barl.dat
   cp $kendcfile $crabdir/res/k_endc.dat
   cat $crabdir/res/etsum_barl_*.dat > $crabdir/res/etsum_barl.dat
   cat $crabdir/res/etsum_endc_*.dat > $crabdir/res/etsum_endc.dat

   ln -sf $crabdir/res/k_barl.dat
   ln -sf $crabdir/res/k_endc.dat
   ln -sf $crabdir/res/etsum_barl.dat
   ln -sf $crabdir/res/etsum_endc.dat

   mkdir -p $i


   cp $datadir/EcalIntercalibConstants.xml .

   cmsRun phisym_step2_loop.py >& $i/cmsrun.step2.$i.log

   if [ $? -ne 0 ] ; then
     echo "Possible problems with step2, please check $i/cmsrun.step2.$i.log"
   fi  

   rm k_barl.dat
   rm k_endc.dat
   rm etsum_barl.dat
   rm etsum_endc.dat

       
   mv $step2out $i

   if [ -f  $datadir/EcalIntercalibConstants.xml ] ; then
      mv $datadir/EcalIntercalibConstants.xml $datadir/EcalIntercalibConstants_$i.xml 
   fi

   cp EcalIntercalibConstants_new.xml $i/EcalIntercalibConstants_$i.xml
   mv EcalIntercalibConstants_new.xml $datadir/EcalIntercalibConstants.xml
 
}
