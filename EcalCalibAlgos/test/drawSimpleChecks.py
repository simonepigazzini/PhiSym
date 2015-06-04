# import ROOT in batch mode
import sys
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.gSystem.Load("libDataFormatsEcalDetId.so");
ROOT.AutoLibraryLoader.enable()

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events, Lumis

# open file (you can use 'edmFileUtil -d /store/whatever.root' to get the physical file name)
lumis = Lumis("file:phisym.root")

handlePhiSymInfo  = Handle ("std::vector<PhiSymInfo>")
handlePhiSymRecHitsEB  = Handle ("std::vector<PhiSymRecHit>")
handlePhiSymRecHitsEE  = Handle ("std::vector<PhiSymRecHit>")
labelPhiSymInfo = ("PhiSymProducer")
labelPhiSymRecHitsEB = ("PhiSymProducer","EB")
labelPhiSymRecHitsEE = ("PhiSymProducer","EE")

histos={}
histos["EB_OccupancyMap"]=ROOT.TH2F("EB_OccupancyMap","EB_OccupancyMap",360,0.5,360.5,171,-85.5,85.5)
histos["EB_EtMap"]=ROOT.TH2F("EB_EtMap","EB_EtMap",360,0.5,360.5,171,-85.5,85.5)
for i,lumi in enumerate(lumis):
    print "====>"
    lumi.getByLabel (labelPhiSymInfo,handlePhiSymInfo)
    lumi.getByLabel (labelPhiSymRecHitsEB,handlePhiSymRecHitsEB)
    lumi.getByLabel (labelPhiSymRecHitsEE,handlePhiSymRecHitsEE)
    phiSymInfo = handlePhiSymInfo.product()
    phiSymRecHitsEB = handlePhiSymRecHitsEB.product()
    phiSymRecHitsEE = handlePhiSymRecHitsEE.product()
    print "Run "+str(phiSymInfo.back().getStartLumi().run())+" Lumi "+str(phiSymInfo.back().getStartLumi().luminosityBlock())
    print "NEvents in this LS "+str(phiSymInfo.back().GetNEvents())
    print "EB PhiSymRecHits "+str(phiSymRecHitsEB.size())
    print "EE PhiSymRecHits "+str(phiSymRecHitsEE.size())
    for hit in phiSymRecHitsEB:
        myId=ROOT.EBDetId(hit.GetRawId())
        histos["EB_EtMap"].Fill(myId.iphi(),myId.ieta(),hit.GetSumEt(0))
        histos["EB_OccupancyMap"].Fill(myId.iphi(),myId.ieta(),hit.GetNhits())


outFile=ROOT.TFile("phiSymStreamCheck.root","RECREATE")
for histo in histos.keys():
    histos[histo].Write()
outFile.Write()
outFile.Close()

