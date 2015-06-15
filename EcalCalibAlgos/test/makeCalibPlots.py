# import ROOT in batch mode
import sys
import argparse
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

# Read command line options
parser = argparse.ArgumentParser (description = 'options')
parser.add_argument('-b', '--block' , default=-1, type=int, help='analyze this block')

opts = parser.parse_args ()

# Load the CalibrationFile format
ROOT.gSystem.Load("libPhiSymEcalCalibDataFormats.so");
ROOT.AutoLibraryLoader.enable()

# Setup the style
ROOT.gStyle.SetOptStat("e")

# Get the crystals trees
inFile = ROOT.TFile("../phisym_intercalibs_150lumis.root")
bareTree = inFile.Get("eb_xstals")
ebTree = ROOT.CrystalsEBTree(bareTree)
bareTree = inFile.Get("ee_xstals")
eeTree = ROOT.CrystalsEETree(bareTree)

## Book the histos ##
histos={}
# EB
histos["EB_ic_ring"]=ROOT.TH2F("EB_ic_ring", "EB ICs with ring-based k-factors", 171, -85.5, 85.5, 360, 0.5, 360.5)
histos["EB_ic_ch"]=ROOT.TH2F("EB_ic_ch", "EB ICs with channel-based k-factors", 171, -85.5, 85.5, 360, 0.5, 360.5)
histos["EB_ic_diff"]=ROOT.TH2F("EB_ic_diff", "EB ICs relative difference (ch-ring)/ring", 171, -85.5, 85.5, 360, 0.5, 360.5)
# EE
histos["EEp_ic_ring"]=ROOT.TH2F("EEp_ic_ring", "EE plus ICs with ring-based k-factors", 100, 0.5, 100.5, 100, 0.5, 100.5)
histos["EEp_ic_ch"]=ROOT.TH2F("EEp_ic_ch", "EE plus ICs with channel-based k-factors", 100, 0.5, 100.5, 100, 0.5, 100.5)
histos["EEp_ic_diff"]=ROOT.TH2F("EEp_ic_diff", "EE plus ICs relative difference (ch-ring)/ring", 100, 0.5, 100.5, 100, 0.5, 100.5)
histos["EEm_ic_ring"]=ROOT.TH2F("EEm_ic_ring", "EE minus ICs with channel-based k-factors", 100, 0.5, 100.5, 100, 0.5, 100.5)
histos["EEm_ic_ch"]=ROOT.TH2F("EEm_ic_ch", "EE minus ICs with channel-based k-factors", 100, 0.5, 100.5, 100, 0.5, 100.5)
histos["EEm_ic_diff"]=ROOT.TH2F("EEm_ic_diff", "EE minus ICs relative difference (ch-ring)/ring", 100, 0.5, 100.5, 100, 0.5, 100.5)

while ebTree.NextEntry():
    if opts.block != -1 and ebTree.block != opts.block:
        continue
    histos["EB_ic_ring"].Fill(ebTree.ieta, ebTree.iphi, ebTree.ic_ring)
    histos["EB_ic_ch"].Fill(ebTree.ieta, ebTree.iphi, ebTree.ic_ch)
    histos["EB_ic_diff"].Fill(ebTree.ieta, ebTree.iphi, ebTree.ic_ch>0 if (ebTree.ic_ch-ebTree.ic_ring)/ebTree.ic_ring else -10)

while eeTree.NextEntry():
    if opts.block != -1 and eeTree.block != opts.block:
        continue
    if eeTree.iring > 0:
        subdet = "EEp_"
    else:
        subdet = "EEm_"
    histos[subdet+"ic_ring"].Fill(eeTree.ix, eeTree.iy, eeTree.ic_ring)
    histos[subdet+"ic_ch"].Fill(eeTree.ix, eeTree.iy, eeTree.ic_ch)
    histos[subdet+"ic_diff"].Fill(eeTree.ix, eeTree.iy, eeTree.ic_ch>0 if (eeTree.ic_ch-eeTree.ic_ring)/eeTree.ic_ring else -10)
    
outFile=ROOT.TFile("phiSymCalibCheck.root","RECREATE")
for key in histos.keys():
    if "_ic_" in key:
        if "EB" in key:
            histos[key].SetAxisRange(0.8, 1.2, "Z")
        else:
            histos[key].SetAxisRange(0.5, 1.5, "Z")
    if "_diff" in key:
        if "EB" in key:
            histos[key].SetAxisRange(-0.9, 1.1, "Z")
        else:
            histos[key].SetAxisRange(-0.7, 1.3, "Z")
    histos[key].Write()
outFile.Close()
