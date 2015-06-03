import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.AlCa.GlobalTag import GlobalTag

process = cms.Process("PHISYMstep2")

process.load('PhiSym.EcalCalibAlgos.PhiSymCalibration_cfi')

# skip bad events
process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_0/src/PhiSym/EcalCalibAlgos/phisym.root')
)

process.path = cms.Path(process.PhiSymCalibration)

process.schedule = cms.Schedule(process.path)
