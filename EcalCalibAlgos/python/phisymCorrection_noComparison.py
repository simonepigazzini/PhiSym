#! /usr/bin/env python
#
#apply EB corrections and dump XML with corrected constants
#

#
# To run the script (e.g.)
# python phisymCorrection_noComparison.py --c1=EcalIntercalibConstants_res.xml --xmlout1=EcalIntercalibConstants_2015MC_PU40bx25_Multifit_noise10.xml  --applycorrections --bd1=/afs/cern.ch/work/g/gnegro/work/CMSSW_7_4_0_pre9/src/PhiSym/EcalCalibAlgos/test/Neutrino_Pt-2to20_gun_Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1_GEN-SIM-RAW_MultiFit_noise10/res/
#

import optparse
import sys

from ROOT import gStyle 


options= optparse.OptionParser(description='Phisym analysis script')


#get absolute path 
options.add_option('--bd1',action='store',dest='basedir1',help='absolute path to Etsummary and constant files - required')

#get calibration constants 
options.add_option('--ac1',action='store',dest='absconst1',help='name of first absolute constants xml')

#xml calibration constants 
options.add_option('--c1',action='store',dest='xml1',help='name of first constants xml - required')

#dataset names
options.add_option('--n1',action='store',dest='c1name',default='Set1',help='Name to be shown for first set')


options.add_option('--applycorrections',action='store_true',dest='docorr',default=False,
                     help='apply systematics corrections')

options.add_option('--rootout',action='store',dest='rootoutfile',default='phisymstdanalysisEB.root',
                     help='name of ROOT output file')

options.add_option('--xmlout1',action='store',dest='xmlout1', default=None,
                     help='name of xml file with corrected constants for raw constants specified with -c1')

options.add_option('--absoluteconstants',action='store_true',dest='absconst', default=False,
                     help='use absolute constants rather than corrections. To be used with --gt')

options.add_option('--gt',action='store',dest='gt', default=None,
                     help='Global tag to retrieve starting constants ')


(optargs,args)=options.parse_args()

c1name=optargs.c1name
basedir1=optargs.basedir1
absconst1=optargs.absconst1
xml1=optargs.xml1
docorr=optargs.docorr
rootoutfile=optargs.rootoutfile
xmlout1=optargs.xmlout1
absconst=optargs.absconst
gt=optargs.gt

if xml1 is None or basedir1 is None:
    options.print_help()
    sys.exit(1)

from EcalCalibAnalysis import *
from EcalPyUtils import *
from ROOT import TGraph,TGraphErrors,TCanvas,TH1F,TH2D,TFile,TPad,gROOT
from pluginCondDBPyInterface import *
from pluginEcalPyUtils import *

gROOT.SetBatch()

#read old IC
if absconst:
     ac1b,ac1e = fromXML(absconst1)

# read phisym IC
print 'XML1'
c1bps,c1eps = fromXML(basedir1+xml1)

ones = [1 for i in range (61200)]

#calculate absolute IC if required
if absconst:
	c1b = [ ac1b[i] * c1bps[i] for i in range(len(ac1b)) ]
	c1e = [ ac1e[i] * c1eps[i] for i in range(len(ac1e)) ]

else:
	c1b = [c1bps[i] for i in range(len(c1bps)) ]
	c1e = [c1eps[i] for i in range(len(c1eps)) ]

	
#apply correction for SM boundaries and Tk rail 	
if docorr :
    
    #calculate average differences from precalib, in each module
    diffp,rmsp,diffm,rmsm= calculatedifferences(c1b,ones)
    #apply correction for SM boundaries and Tk rail 
    c1b_corr = applycorrections(c1b,diffp,diffm)

    
else :
    c1b_corr = c1b 


# dump to XML
c1bp= VFloat() #python-> C++ type issue... ugly workaround...
c1ep= VFloat()

for x in c1b_corr:
    c1bp.append(x)
    
for x in c1e:
    c1ep.append(x)
    

if xmlout1 is not None :

    if docorr:
        out1 = open("xmltotext_tools/XML_2015/"+xmlout1,'w')
    else:
        out1 = open("xmltotext_tools/XML_2015_noCorr/"+xmlout1,'w')    

    xmldump=arraystoXML(c1bp,c1ep)
    print >> out1, xmldump
    print 'Saved xml file : ', xmlout1
    


