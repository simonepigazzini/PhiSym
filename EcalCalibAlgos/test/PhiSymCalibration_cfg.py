import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.AlCa.GlobalTag import GlobalTag

process = cms.Process("PHISYMstep2")

process.load('FWCore/MessageService/MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100000

process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')

process.load('PhiSym.EcalCalibAlgos.PhiSymCalibration_cfi')

# skip bad events
process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# Global tag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_E_V48')

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                               "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_1.root",
                               "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_10.root",
                                "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_11.root",
                                "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_12.root",
                                "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_13.root",
                                "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_14.root",
                                "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_15.root"))
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_16.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_17.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_18.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_19.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_2.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_20.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_21.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_22.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_23.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_24.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_25.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_26.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_27.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_28.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_29.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_3.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_30.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_31.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_32.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_33.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_34.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_35.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_36.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_37.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_38.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_39.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_4.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_40.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_41.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_42.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_43.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_44.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_45.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_46.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_47.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_48.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_49.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_5.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_50.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_51.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_52.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_53.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_54.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_55.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_56.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_57.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_58.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_6.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_7.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_8.root",
#                                 "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/samples/PHISYM_Run2015A_v0_test_9.root")
# )

# Output TFile
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("phisym_kfactors.root"))

process.path = cms.Path(process.PhiSymCalibration)

process.schedule = cms.Schedule(process.path)
