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
ROOT.AutoLibraryLoader.enable()

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events, Lumis

# open file (you can use 'edmFileUtil -d /store/whatever.root' to get the physical file name)
lumis = Lumis("file:phisym.root")

handlePhiSymInfo  = Handle ("std::vector<PhiSymInfo>")
labelPhiSymInfo = ("PhiSymProducer")

for i,lumi in enumerate(lumis):
    print "Lumi", i
    lumi.getByLabel (labelPhiSymInfo,handlePhiSymInfo)
    phiSymInfo = handlePhiSymInfo.product()
    print "NEvents in this LS "+str(phiSymInfo.back().GetNEvents())
