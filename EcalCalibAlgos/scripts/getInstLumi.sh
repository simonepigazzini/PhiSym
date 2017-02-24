#!/bin/bash

brilcalc lumi -r 276811 --byls -u /nb | cut -d '|' -f 2,3,8,9 | sed -r '1,4 d; s:\|::g; s/:[0-9]+//g;/\+-----/d' | awk '(NF>3){print $0}' > ${1}
