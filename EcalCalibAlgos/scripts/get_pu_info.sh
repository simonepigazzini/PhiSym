#!/bin/bash

dump=""
for run in `echo ${1} | tr ',' ' '`
do
    dump+=`brilcalc lumi --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -r ${run} --byls -u /nb | cut -d '|' -f 2,3,8,9 | sed -r '1,4 d; s:\|::g; s/:[0-9]+//g; /\+-----/d; s:^ ::g; s: {2,}: :g' | awk '(NF>3){print $0}'`
done

echo "{"
current_run=-1
while read line;
do
    read -a tokens <<< "$line"
    if [ $current_run -eq -1 ]
    then
        current_run=${tokens[0]}
        echo \"${tokens[0]}\" ": {"
        echo -n \"${tokens[1]}\" ":" \"${tokens[3]}\"
    elif [ ${tokens[0]} -ne $current_run ]
    then
        current_run=${tokens[0]}
        echo "},"
        echo \"${tokens[0]}\" ": {"
        echo -n \"${tokens[1]}\" ":" \"${tokens[3]}\"
    else
        echo ","
        echo -n \"${tokens[1]}\" ":" \"${tokens[3]}\"
    fi
done <<< "$dump"

echo -e "\\n} \\n}"

exit 0
