import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.AlCa.GlobalTag import GlobalTag

process = cms.Process("PHISYMstep2")

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
                            fileNames = cms.untracked.vstring('file:phisym_numEvent1.root')
)

process.path = cms.Path(process.PhiSymCalibration)

process.schedule = cms.Schedule(process.path)
