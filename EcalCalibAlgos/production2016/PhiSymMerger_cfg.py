import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.AlCa.GlobalTag import GlobalTag

process = cms.Process("PHISYMstep2")

process.load('FWCore/MessageService/MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100000

process.load('Configuration.Geometry.GeometryExtended2017Reco_cff')

# skip bad events
process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# Global tag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_2016LegacyRepro_Candidate_v2')

# Input source
process.source = cms.Source("PoolSource",
                            processingMode = cms.untracked.string("RunsAndLumis"),
                            fileNames = cms.untracked.vstring(
                                "/store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_9_0_3-weights-90X_dataRun2_Prompt_v3-Comm2017_v1/170515_113632/0000/phisym_weights_1lumis_100.root"
                            )
)                                
process.source.skipBadFiles = cms.untracked.bool(True)

# PHISYM Calib
process.load('PhiSym.EcalCalibAlgos.PhiSymMerger_cfi')
process.PhiSymMerger.blocksToSum = 1000
process.PhiSymMerger.IOVfile = cms.untracked.string("IOVmap.root")

# Output TFile
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("phisym_merged.root"))

process.path = cms.Path(process.PhiSymMerger)

process.schedule = cms.Schedule(process.path)
