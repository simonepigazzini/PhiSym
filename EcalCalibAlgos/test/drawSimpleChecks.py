# import ROOT in batch mode
import sys
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

# load FWLite C++ librarie
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.gSystem.Load("libDataFormatsEcalDetId.so");
ROOT.gSystem.Load("libPhiSymEcalCalibDataFormats.so");
ROOT.AutoLibraryLoader.enable()

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events, Lumis

# open file (you can use 'edmFileUtil -d /store/whatever.root' to get the physical file name)
#lumis = Lumis("file:phisym.root")
lumis = Lumis("file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/phisym.root")

handlePhiSymInfo  = Handle ("std::vector<PhiSymInfo>")
handlePhiSymRecHitsEB  = Handle ("std::vector<PhiSymRecHit>")
handlePhiSymRecHitsEE  = Handle ("std::vector<PhiSymRecHit>")
labelPhiSymInfo = ("PhiSymProducer")
labelPhiSymRecHitsEB = ("PhiSymProducer","EB")
labelPhiSymRecHitsEE = ("PhiSymProducer","EE")

histos={}

histos["EB_OccupancyMap"]=ROOT.TH2F("EB_OccupancyMap","EB_OccupancyMap",360,0.5,360.5,171,-85.5,85.5)
histos["EB_EtMap"]=ROOT.TH2F("EB_EtMap","EB_EtMap",360,0.5,360.5,171,-85.5,85.5)

histos["EEM_OccupancyMap"]=ROOT.TH2F("EEM_OccupancyMap","EEM_OccupancyMap",100,0.5,100.5,100,0.5,100.5)
histos["EEM_EtMap"]=ROOT.TH2F("EEM_EtMap","EEM_EtMap",100,0.5,100.5,100,0.5,100.5)

histos["EEP_OccupancyMap"]=ROOT.TH2F("EEP_OccupancyMap","EEP_OccupancyMap",100,0.5,100.5,100,0.5,100.5)
histos["EEP_EtMap"]=ROOT.TH2F("EEP_EtMap","EEP_EtMap",100,0.5,100.5,100,0.5,100.5)

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
    print "TotHits EB "+str(phiSymInfo.back().GetTotHitsEB())+" Avg occ EB "+str(float(phiSymInfo.back().GetTotHitsEB())/phiSymInfo.back().GetNEvents()) 
    print "TotHits EE "+str(phiSymInfo.back().GetTotHitsEE())+" Avg occ EE "+str(float(phiSymInfo.back().GetTotHitsEE())/phiSymInfo.back().GetNEvents()) 

    print "EB PhiSymRecHits "+str(phiSymRecHitsEB.size())
    print "EE PhiSymRecHits "+str(phiSymRecHitsEE.size())

    for hit in phiSymRecHitsEB:
        myId=ROOT.EBDetId(hit.GetRawId())
        histos["EB_EtMap"].Fill(myId.iphi(),myId.ieta(),hit.GetSumEt(0))
        histos["EB_OccupancyMap"].Fill(myId.iphi(),myId.ieta(),hit.GetNhits())
    for hit in phiSymRecHitsEE:
        myId=ROOT.EEDetId(hit.GetRawId())
        if (myId.zside()<0):
            histos["EEM_EtMap"].Fill(myId.ix(),myId.iy(),hit.GetSumEt(0))
            histos["EEM_OccupancyMap"].Fill(myId.ix(),myId.iy(),hit.GetNhits())
        else:
            histos["EEP_EtMap"].Fill(myId.ix(),myId.iy(),hit.GetSumEt(0))
            histos["EEP_OccupancyMap"].Fill(myId.ix(),myId.iy(),hit.GetNhits())

outFile=ROOT.TFile("phiSymStreamCheck.root","RECREATE")
for histo in histos.keys():
    histos[histo].Write()
outFile.Write()
outFile.Close()

