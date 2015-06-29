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
                                "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/phisym_weights_1lumis.root")
)

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
