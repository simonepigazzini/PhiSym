import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.AlCa.GlobalTag import GlobalTag

# parse commad line options
options = VarParsing('analysis')
options.maxEvents = -1
options.outputFile = 'phisym_multifit_1lumis.root'
options.parseArguments()

process=cms.Process("PHISYM")

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('RecoLuminosity.LumiProducer.bunchSpacingProducer_cfi')
process.load('RecoLocalCalo.EcalRecProducers.ecalMultiFitUncalibRecHit_cfi')
process.load('RecoLocalCalo.EcalRecProducers.ecalUncalibRecHit_cfi')
process.load('RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi')
process.load('RecoVertex.BeamSpotProducer.BeamSpot_cff')

process.load('FWCore/MessageService/MessageLogger_cfi')

process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.cerr.default = cms.untracked.PSet(
    limit = cms.untracked.int32(10000000),
    reportEvery = cms.untracked.int32(5000)
)

# import of standard configurations
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

# skip bad events
process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound'),
)

# Input source
process.source = cms.Source("PoolSource",
#                             inputCommands = cms.untracked.vstring(
#                                 'keep *',
#                                 'drop *_hltEcalDigis_*_*',
#                                 'drop *_hltTriggerSummaryAOD_*_*'
#                             ),
                            fileNames = cms.untracked.vstring(
                                "/store/data/Commissioning2016/AlCaPhiSym/RAW/v1/000/268/930/00000/D624B590-A2FD-E511-B7AD-02163E011AEE.root"
))

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('step_PHISYM nevts:'+str(options.maxEvents)),
    name = cms.untracked.string('PhiSymProducer')
)

#ecalMultiFitUncalibRecHit
process.ecalMultiFitUncalibRecHit.EBdigiCollection = cms.InputTag("hltEcalPhiSymFilter","phiSymEcalDigisEB")
process.ecalMultiFitUncalibRecHit.EEdigiCollection = cms.InputTag("hltEcalPhiSymFilter","phiSymEcalDigisEE")

#ecalRecHit (no ricovery)
process.ecalRecHit.killDeadChannels = cms.bool( False )
process.ecalRecHit.recoverEBVFE = cms.bool( False )
process.ecalRecHit.recoverEEVFE = cms.bool( False )
process.ecalRecHit.recoverEBFE = cms.bool( False )
process.ecalRecHit.recoverEEFE = cms.bool( False )
process.ecalRecHit.recoverEEIsolatedChannels = cms.bool( False )
process.ecalRecHit.recoverEBIsolatedChannels = cms.bool( False )

# PHISYM producer
process.load('PhiSym.EcalCalibAlgos.PhiSymProducer_cfi')
#process.PhiSymProducer.makeSpectraTreeEB = True
#process.PhiSymProducer.makeSpectraTreeEE = True
process.PhiSymProducer.eThreshold_barrel = 0.9
process.PhiSymProducer.thrEEmod = 14.

# Output definition
PHISYM_output_commands = cms.untracked.vstring(
    "drop *",
    "keep *_PhiSymProducer_*_*")

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
                                         splitLevel = cms.untracked.int32(0),
                                         outputCommands = PHISYM_output_commands,
                                         fileName = cms.untracked.string(options.outputFile)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("phisym_spectra.root"))

# GLOBAL-TAG
from CondCore.DBCommon.CondDBSetup_cfi import *
process.GlobalTag = cms.ESSource("PoolDBESSource",
                                 CondDBSetup,
                                 connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                                 globaltag = cms.string('80X_dataRun2_2016LegacyRepro_Candidate_v2'),
                                 toGet = cms.VPSet(
                                     cms.PSet(record = cms.string("EcalPedestalsRcd"),
                                              tag = cms.string("EcalPedestals_timestamp_2016"),
                                              connect = cms.string("frontier://FrontierPrep/CMS_CONDITIONS"),
                                          ),
                                     cms.PSet(
                                         record = cms.string('EcalLaserAlphasRcd'),
                                         tag = cms.string('EcalLaserAlphas_EB_1.52Russian_1.5Chinese'),
                                         connect = cms.string('frontier://FrontierPrep/CMS_CONDITIONS')
                                     ),
                                     cms.PSet(record = cms.string("ESIntercalibConstantsRcd"),
                                              tag = cms.string("ESIntercalibConstants_Run1_Run2_V07_offline"),
                                              connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
                                          ),
                                     cms.PSet(record = cms.string("ESEEIntercalibConstantsRcd"),
                                              tag = cms.string("ESEEIntercalibConstants_Legacy2016_v3"),
                                              connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
                                          ),
                                     cms.PSet(record = cms.string("EcalIntercalibConstantsRcd"),
                                              tag = cms.string("EcalIntercalibConstants_Cal_Mar2017_PNcorrection_eop_v2"),
                                              connect = cms.string('frontier://FrontierPrep/CMS_CONDITIONS')
                                          ),
                                     cms.PSet(record = cms.string("EcalLinearCorrectionsRcd"),
                                              tag = cms.string("EcalLinearCorrections_from2011_offline"),
                                              connect = cms.string("frontier://FrontierPrep/CMS_CONDITIONS"),
                                          ),
                                 )
)

# SCHEDULE
process.reconstruction_step = cms.Sequence( process.bunchSpacingProducer * (process.ecalMultiFitUncalibRecHit + process.ecalRecHit) )

process.p = cms.Path(process.reconstruction_step)
process.p *= process.offlineBeamSpot
process.p *= process.PhiSymProducer

process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.schedule = cms.Schedule(process.p, process.RECOSIMoutput_step)
