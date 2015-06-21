import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.AlCa.GlobalTag import GlobalTag

process = cms.Process("PHISYMstep2")

process.load('FWCore/MessageService/MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100000

process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')

# skip bad events
process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# Global tag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_P_V56')

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_1.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_10.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_11.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_12.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_13.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_14.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_15.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_16.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_17.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_18.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_19.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_2.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_20.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_21.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_22.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_23.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_24.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_25.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_26.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_27.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_28.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_29.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_3.root",
                                "/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_30.root"))

                                #"/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v3/150614_201220/0000/PHISYM_Run2015A_v1_1lumi_6.root"))

# PHISYM Calib
process.load('PhiSym.EcalCalibAlgos.PhiSymCalibration_cfi')
process.PhiSymCalibration.blocksToSum = 1000
process.PhiSymCalibration.oldCalibFile = "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2012D.dat"
process.PhiSymCalibration.absCalibFile = "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2015Abs.dat"

# Output TFile
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("phisym_intercalibs_1000lumis.root"))

process.path = cms.Path(process.PhiSymCalibration)

process.schedule = cms.Schedule(process.path)
