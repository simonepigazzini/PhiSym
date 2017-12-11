#!/bin/bash

### MAIN ###
# very simple script to generate list of iov files from a directory.
# The generated file will be written into directory/iovs_list.cfg (direcory is specified by the -d option.
# Note that directory/iovs_list.cfg is overwritten by this script without notice
# The file can than be passed as input to the make_hisotry_trees routine.

TEMP=`getopt -o d:o:p:h --long directory:,output:,patter:,help -n 'generate_iov_list.sh' -- "$@"`

if [ $? != 0 ] ; then echo "Options are wrong..." >&2 ; exit 1 ; fi

# Note the quotes around `$TEMP': they are essential!
eval set -- "$TEMP"

pattern="summed*.root"
output=""

while true; do
    case "$1" in
        -d | --directory) directory="$2"; shift 2;;
        -o | --output) output="$2"; shift 2;;
        -g | --patter) pattern="$2"; shift 2;;        
        -h | --help ) help=1; shift;;
        -- ) shift; break ;;
        * ) break ;;
    esac
done

if [[ $output == "" ]]; then
    output=$directory/iovs_list.cfg
fi

directory=`readlink -f $directory`
last_char="${directory: -1}"
if [[ $last_char != "/" ]]; then
    directory="$directory/"
fi
pattern="$directory$pattern"
files=`ls $pattern`

echo -n "iovs_files+=" > $output
for file in $files; do
    echo -ne " \\ \n $file" >> $output
done
echo "" >> $output
