# import ROOT in batch mode
import sys
import re
import argparse
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

# Read command line options
parser = argparse.ArgumentParser (description = 'options')
parser.add_argument('-b', '--block' , default=-1, type=int, help='analyze this block')
parser.add_argument('--plots' , action="store_true", default=False, help='produce .png and .pdf plots')
parser.add_argument('-d', '--outdir' , default="./", help='store path for .png, .pdf and .root')

opts = parser.parse_args ()

# Load the CalibrationFile format
ROOT.gSystem.Load("libPhiSymEcalCalibDataFormats.so");
ROOT.AutoLibraryLoader.enable()

# Setup the style
ROOT.gErrorIgnoreLevel=ROOT.kInfo + 1
ROOT.gStyle.SetOptStat("")
ROOT.gStyle.SetLabelSize(0.05, "XY");
ROOT.gStyle.SetTickLength(0.03, "XYZ");
ROOT.gStyle.SetNdivisions(510, "XYZ");
ROOT.gStyle.SetTitleColor(1, "XYZ");
ROOT.gStyle.SetTitleSize(0.07, "XYZ");
ROOT.gStyle.SetTitleXOffset(0.8);
ROOT.gStyle.SetTitleYOffset(0.7);
ROOT.gStyle.SetPadTopMargin(0.12);
ROOT.gStyle.SetPadBottomMargin(0.13);
ROOT.gStyle.SetPadLeftMargin(0.1);
ROOT.gStyle.SetPadRightMargin(0.1);

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
histos["EB_k_ring"]=ROOT.TH2F("EB_k_ring", "EB ring-based k-factors", 171, -85.5, 85.5, 360, 0.5, 360.5)
histos["EB_k_ch"]=ROOT.TH2F("EB_k_ch", "EB channel-based k-factors", 171, -85.5, 85.5, 360, 0.5, 360.5)
histos["EB_k_diff"]=ROOT.TH2F("EB_k_diff", "EB k-factors relative difference (ch-ring)/ring", 171, -85.5, 85.5, 360, 0.5, 360.5)
# EE plus
histos["EEp_ic_ring"]=ROOT.TH2F("EEp_ic_ring", "EE plus ICs with ring-based k-factors", 100, 0.5, 100.5, 100, 0.5, 100.5)
histos["EEp_ic_ch"]=ROOT.TH2F("EEp_ic_ch", "EE plus ICs with channel-based k-factors", 100, 0.5, 100.5, 100, 0.5, 100.5)
histos["EEp_ic_diff"]=ROOT.TH2F("EEp_ic_diff", "EE plus ICs relative difference (ch-ring)/ring", 100, 0.5, 100.5, 100, 0.5, 100.5)
histos["EEp_k_ring"]=ROOT.TH2F("EEp_k_ring", "EE plus ring-based k-factors", 100, 0.5, 100.5, 100, 0.5, 100.5)
histos["EEp_k_ch"]=ROOT.TH2F("EEp_k_ch", "EE plus channel-based k-factors", 100, 0.5, 100.5, 100, 0.5, 100.5)
histos["EEp_k_diff"]=ROOT.TH2F("EEp_k_diff", "EE plus k-factors relative difference (ch-ring)/ring",
                               100, 0.5, 100.5, 100, 0.5, 100.5)
# EE minus
histos["EEm_ic_ring"]=ROOT.TH2F("EEm_ic_ring", "EE minus ICs with channel-based k-factors", 100, 0.5, 100.5, 100, 0.5, 100.5)
histos["EEm_ic_ch"]=ROOT.TH2F("EEm_ic_ch", "EE minus ICs with channel-based k-factors", 100, 0.5, 100.5, 100, 0.5, 100.5)
histos["EEm_ic_diff"]=ROOT.TH2F("EEm_ic_diff", "EE minus ICs relative difference (ch-ring)/ring", 100, 0.5, 100.5, 100, 0.5, 100.5)
histos["EEm_k_ring"]=ROOT.TH2F("EEm_k_ring", "EE minus ring-based k-factors", 100, 0.5, 100.5, 100, 0.5, 100.5)
histos["EEm_k_ch"]=ROOT.TH2F("EEm_k_ch", "EE minus channel-based k-factors", 100, 0.5, 100.5, 100, 0.5, 100.5)
histos["EEm_k_diff"]=ROOT.TH2F("EEm_k_diff", "EE minus k-factors relative difference (ch-ring)/ring",
                               100, 0.5, 100.5, 100, 0.5, 100.5)

while ebTree.NextEntry():
    if opts.block != -1 and ebTree.block != opts.block:
        continue
    histos["EB_ic_ring"].Fill(ebTree.ieta, ebTree.iphi, ebTree.ic_ring)
    histos["EB_ic_ch"].Fill(ebTree.ieta, ebTree.iphi, ebTree.ic_ch)
    histos["EB_ic_diff"].Fill(ebTree.ieta, ebTree.iphi, (ebTree.ic_ch-ebTree.ic_ring)/ebTree.ic_ring)
    histos["EB_k_ring"].Fill(ebTree.ieta, ebTree.iphi, ebTree.k_ring)
    histos["EB_k_ch"].Fill(ebTree.ieta, ebTree.iphi, ebTree.k_ch)
    histos["EB_k_diff"].Fill(ebTree.ieta, ebTree.iphi, (ebTree.k_ch-ebTree.k_ring)/ebTree.k_ring)

while eeTree.NextEntry():
    if opts.block != -1 and eeTree.block != opts.block:
        continue
    if eeTree.iring > 0:
        subdet = "EEp_"
    else:
        subdet = "EEm_"
    histos[subdet+"ic_ring"].Fill(eeTree.ix, eeTree.iy, eeTree.ic_ring)
    histos[subdet+"ic_ch"].Fill(eeTree.ix, eeTree.iy, eeTree.ic_ch)
    histos[subdet+"ic_diff"].Fill(eeTree.ix, eeTree.iy, (eeTree.ic_ch-eeTree.ic_ring)/eeTree.ic_ring)
    histos[subdet+"k_ring"].Fill(eeTree.ix, eeTree.iy, eeTree.k_ring)
    histos[subdet+"k_ch"].Fill(eeTree.ix, eeTree.iy, eeTree.k_ch)
    histos[subdet+"k_diff"].Fill(eeTree.ix, eeTree.iy, (eeTree.k_ch-eeTree.k_ring)/eeTree.k_ring)

# Define z-axis ranges: with regexp matching ;)
ranges={}
ranges[re.compile("^EB_ic_((?!diff).)*$")]=[0.8, 1.2]
ranges[re.compile("^EB_ic_diff$")]=[-0.01, 0.01]
ranges[re.compile("^EB_k_((?!diff).)*$")]=[1.5, 2.6]
ranges[re.compile("^EB_k_diff$")]=[-0.5, 0.6]
ranges[re.compile("^EE.*_ic_((?!diff).)*$")]=[0.5, 1.5]
ranges[re.compile("^EE.*_ic_diff$")]=[-0.15, 0.15]
ranges[re.compile("^EE.*_k_((?!diff).)*$")]=[1, 2]
ranges[re.compile("^EE.*_k_diff$")]=[-0.5, 0.7]

axisTitles={}
axisTitles[re.compile("^EB.*")]=["#eta", "#phi"]
axisTitles[re.compile("^EE.*")]=["ix", "iy"]

outFile=ROOT.TFile(opts.outdir+"phiSymCalibCheck.root", "RECREATE")
for key in histos.keys():
    for title in axisTitles:
        if title.match(key):
            histos[key].GetXaxis().SetTitle(axisTitles[title][0])
            histos[key].GetYaxis().SetTitle(axisTitles[title][1])
    for cat in ranges.keys():
        if cat.match(key):
            histos[key].SetAxisRange(ranges[cat][0], ranges[cat][1], "Z")
    histos[key].Write()
    if opts.plots:
        canvas=ROOT.TCanvas()
        histos[key].Draw("COLZ")
        canvas.Print(opts.outdir+key+".png", "png")
        canvas.Print(opts.outdir+key+".pdf", "pdf")
outFile.Close()
