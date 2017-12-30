#!/bin/bash
# an extra zero is added before the bx delivered lumis to match the ordering of the ls_info.json from CMSSW RECO step

# --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json

# bx columns (more than needed, just to be sure}
bx_columns=""
for i in {17..16000..3}
do
    bx_columns+=","$i
done

current_run=-1
for run in `echo ${1} | tr ',' ' '`
do
    dump=`brilcalc lumi -r ${run} -b 'STABLE BEAMS' --xing -u hz/ub --output-style csv | grep -e '^[0-9]' | sed -e 's/[: ]/,/g' | sed 's:]::g' | cut -d ',' -f 1,2,3,12,14,15${bx_columns}`

    while read line;
    do
        lumi_info=`echo ${line} | cut -d ',' -f 1-6 | sed 's:,: :g'`
        bx_info=`echo ${line} | cut -d ',' -f 7-`

        read -a tokens <<< "$lumi_info"
        
        if [ $current_run -eq -1 ]
        then
            current_run=${tokens[0]}
            echo "{" > ${2}            
            echo \"${tokens[0]}\" ": {" >> ${2}
            echo -n \"${tokens[2]}\" ": [" ${tokens[1]} "," ${tokens[3]} "," ${tokens[4]} ", \""${tokens[5]}"\" , 0, " >> ${2}
            echo $bx_info >> ${2}
            echo -n " ]" >> ${2}
        elif [ ${tokens[0]} -ne $current_run ]
        then
            current_run=${tokens[0]}
            echo "}," >> ${2}
            echo \"${tokens[0]}\" ": {" >> ${2}
            echo -n \"${tokens[2]}\" ": [" ${tokens[1]} "," ${tokens[3]} "," ${tokens[4]} ", \""${tokens[5]}"\" , 0, " >> ${2}
            echo $bx_info >> ${2}
            echo -n " ]" >> ${2}
        else
            echo "," >> ${2}
            echo -n \"${tokens[2]}\" ": [" ${tokens[1]} "," ${tokens[3]} "," ${tokens[4]} ", \""${tokens[5]}"\" , 0, " >> ${2}
            echo $bx_info >> ${2}
            echo -n " ]" >> ${2}
        fi
    done <<< "$dump"

done

echo -e "\\n} \\n}" >> ${2}

exit 0




exit 0

    while read line;
    do
        echo $lumi_info
    done <<< "$dump"


