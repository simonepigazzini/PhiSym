# import ROOT in batch mode
from __future__ import division
import sys
import re
import argparse
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

from PhiSym.EcalCalibAlgos.EcalCalibAnalysis import *

parser = argparse.ArgumentParser (description = 'Dump PhiSym IC correction from a ROOT file')
parser.add_argument('inputfile' , default="phisym_intercalibs.root", help='analyze this file')
parser.add_argument('-b', '--block' , default=-1, type=int, help='analyze this block')
parser.add_argument('-f', '--outputFile' , default=-1, type=int, help='store the ICs in this file')
parser.add_argument('-k', '--kType' , default="ch", help='k-Factor computation type: ch / ring')
parser.add_argument('--rel' , action="store_true", default=False, help='dump phisym ICs correction only')

opts = parser.parse_args ()

# Load the CalibrationFile format
ROOT.gSystem.Load("libPhiSymEcalCalibDataFormats.so");
ROOT.AutoLibraryLoader.enable()

# Get the crystals trees
inFile = ROOT.TFile(opts.inputfile)
bareTree = inFile.Get("eb_xstals")
ebTree = ROOT.CrystalsEBTree(bareTree)
bareTree = inFile.Get("ee_xstals")
eeTree = ROOT.CrystalsEETree(bareTree)

#EB
while ebTree.NextEntry():
    if opts.block != -1 and ebTree.block != opts.block:
        continue;
    if opts.kType == "ch":
        ic = 1/ebTree.ic_ch        
        ic_err = ebTree.ic_ch_err*ic
    else:
        ic = 1/ebTree.ic_ring
        ic_err = ebTree.ic_ring_err*ic
    if not opts.rel:
        ic = ebTree.ic_abs*ic
    if ic == 0:        
        ic_err = 999    

    print repr(ebTree.ieta), repr(ebTree.iphi), repr(0), "%.5f" % ic, "%.7f" % ic_err

#EE
while eeTree.NextEntry():
    if opts.block != -1 and eeTree.block != opts.block:
        continue;
    if opts.kType == "ch":
        ic = 1/eeTree.ic_ch
        ic_err = eeTree.ic_ch_err*ic
    else:
        ic = 1/eeTree.ic_ring
        ic_err = eeTree.ic_ring_err*ic
    if not opts.rel:
        ic = eeTree.ic_abs*ic
    if ic == 0:
        ic_err = 999
    if eeTree.iring > 0:
        side = 1
    else:
        side = -1
        
    print repr(eeTree.ix), repr(eeTree.iy), repr(side), "%.5f" % ic, "%.7f" % ic_err
