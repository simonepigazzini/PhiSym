import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.AlCa.GlobalTag import GlobalTag

# parse commad line options
options = VarParsing('analysis')
options.maxEvents = -1
options.outputFile = 'phisym_weights_1lumis.root'
options.parseArguments()

process=cms.Process("PHISYM")

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('RecoLocalCalo.EcalRecProducers.ecalRecalibRecHit_cfi')
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")

process.load('FWCore/MessageService/MessageLogger_cfi')

process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.cerr.default = cms.untracked.PSet(
    limit = cms.untracked.int32(10000000),
    reportEvery = cms.untracked.int32(5000)
)

# import of standard configurations
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(300000)
)

# skip bad events
process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound'),
)

# Input source
process.source = cms.Source("PoolSource",
                            inputCommands = cms.untracked.vstring(
                                'keep *',
                                'drop *_hltEcalDigis_*_*',
                                'drop *_hltTriggerSummaryAOD_*_*'
                            ),
                            fileNames = cms.untracked.vstring(
                                #"/store/data/Run2012D/AlCaPhiSym/RAW/v1/000/208/538/185B7750-433E-E211-8FA0-E0CB4E55365D.root"
                                #"/store/data/Run2012D/AlCaPhiSym/RAW/v1/000/208/538/185B7750-433E-E211-8FA0-E0CB4E55365D.root",
                                "/store/data/Run2012D/AlCaPhiSym/RAW/v1/000/208/538/7ABC81F3-543E-E211-A801-003048678098.root",
                                "/store/data/Run2012D/AlCaPhiSym/RAW/v1/000/208/538/8C50E001-423E-E211-BEDA-BCAEC5329716.root",
                                "/store/data/Run2012D/AlCaPhiSym/RAW/v1/000/208/538/B0BE6B16-423E-E211-B0CD-002481E0D90C.root",
                                "/store/data/Run2012D/AlCaPhiSym/RAW/v1/000/208/538/C628AB90-3F3E-E211-BC83-5404A63886A2.root"
                            )
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('step_PHISYM nevts:'+str(options.maxEvents)),
    name = cms.untracked.string('PhiSymProducer')
)

#ecalRecHit (no ricovery)
process.ecalRecHit.doEnergyScale = cms.bool(True)
process.ecalRecHit.doIntercalib = cms.bool(True)
process.ecalRecHit.doLaserCorrections = cms.bool(True)
process.ecalRecHit.EBRecalibRecHitCollection = cms.string('recalibEcalRecHitsEB')
process.ecalRecHit.EERecalibRecHitCollection = cms.string('recalibEcalRecHitsEE')
process.ecalRecHit.EBRecHitCollection = cms.InputTag('hltAlCaPhiSymUncalibrator', 'phiSymEcalRecHitsEB', 'HLT')
process.ecalRecHit.EERecHitCollection = cms.InputTag('hltAlCaPhiSymUncalibrator', 'phiSymEcalRecHitsEE', 'HLT')

# PHISYM producer
process.load('PhiSym.EcalCalibAlgos.PhiSymProducer_cfi')
# process.PhiSymProducer.applyEtThreshold=cms.bool(False)
process.PhiSymProducer.makeSpectraTreeEB = True
process.PhiSymProducer.makeSpectraTreeEE = True
process.PhiSymProducer.barrelHitCollection = cms.InputTag('ecalRecHit', 'recalibEcalRecHitsEB', 'PHISYM')
process.PhiSymProducer.endcapHitCollection = cms.InputTag('ecalRecHit', 'recalibEcalRecHitsEE', 'PHISYM')


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
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_P_V56')
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string("EcalLaserAPDPNRatiosRcd"),
             tag = cms.string("EcalLaserAPDPNRatios_20130130_447_p1_v2"),
             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_42X_ECAL_LAS")
         ),
    cms.PSet(record = cms.string("EcalIntercalibConstantsRcd"),
             # tag = cms.string("EcalIntercalibConstants_V20120620_piZPhiSEtaScale2012_IOV2_AlphaStudies"),
             # connect = cms.untracked.string("frontier://FrontierInt/CMS_COND_ECAL")
             tag = cms.string("EcalIntercalibConstants_2012ABCD_offline"),
             connect = cms.untracked.string("frontier://PromptProd/CMS_COND_31X_ECAL")
         ),
    cms.PSet(record = cms.string("EcalChannelStatusRcd"),
             tag = cms.string("EcalChannelStatus_v1_prompt"),
             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_ECAL")
         )
)

# SCHEDULE
process.reconstruction_step = cms.Sequence(process.ecalRecHit)

process.p = cms.Path(process.reconstruction_step)
process.p *= process.offlineBeamSpot
process.p *= process.PhiSymProducer

process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.schedule = cms.Schedule(process.p, process.RECOSIMoutput_step)
