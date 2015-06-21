import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.AlCa.GlobalTag import GlobalTag

# parse commad line options
options = VarParsing('analysis')
options.maxEvents = -1
options.outputFile = 'phisym.root'
options.parseArguments()

process=cms.Process("PHISYM")

#process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('RecoLocalCalo.EcalRecProducers.ecalMultiFitUncalibRecHit_cfi')
process.load('RecoLocalCalo.EcalRecProducers.ecalUncalibRecHit_cfi')
process.load('RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi')
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")

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
                            inputCommands = cms.untracked.vstring(
                                'keep *',
                                'drop *_hltEcalDigis_*_*',
                                'drop *_hltTriggerSummaryAOD_*_*'
                            ),
                            fileNames = cms.untracked.vstring(
                                "/store/data/Run2012D/AlCaPhiSym/RAW/v1/000/203/774/B492587E-FF08-E211-953F-BCAEC53296FB.root")
                                # "root://cmsxrootd-site.fnal.gov//store/data/Run2015A/AlCaPhiSym/RAW/v1/000/247/720/00000/4C0AF78B-4810-E511-8C09-02163E0143CB.root",
                                # "root://cmsxrootd-site.fnal.gov//store/data/Run2015A/AlCaPhiSym/RAW/v1/000/247/795/00000/E001FA5B-D510-E511-A5B8-02163E0135FD.root")
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('step_PHISYM nevts:'+str(options.maxEvents)),
    name = cms.untracked.string('PhiSymProducer')
)

isStream=True
runMultiFit=False
isBX50ns=True

if (runMultiFit):
    if (isBX50ns):
        process.ecalMultiFitUncalibRecHit.algoPSet = cms.PSet(
            useLumiInfoRunHeader = cms.bool(False),
            activeBXs = cms.vint32(-4,-2,0,2,4)
        )
    else:
        process.ecalMultiFitUncalibRecHit.algoPSet = cms.PSet(
            useLumiInfoRunHeader = cms.bool(False),
            activeBXs = cms.vint32(-5,-4,-3,-2,-1,0,1,2,3,4)
        ) 

#ecalUncalibRecHit
if (isStream):
    process.ecalUncalibRecHit.EBdigiCollection = cms.InputTag("hltEcalPhiSymFilter","phiSymEcalDigisEB")
    process.ecalUncalibRecHit.EEdigiCollection = cms.InputTag("hltEcalPhiSymFilter","phiSymEcalDigisEE")

#ecalMultiFitUncalibRecHit
if (isStream):
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
if (not runMultiFit):
    process.ecalRecHit.EBuncalibRecHitCollection = cms.InputTag("hltAlCaPhiSymUncalibrator","phiSymEcalRecHitsEB")
    process.ecalRecHit.EEuncalibRecHitCollection = cms.InputTag("hltAlCaPhiSymUncalibrator","phiSymEcalRecHitsEE")

# PHISYM producer
process.load('PhiSym.EcalCalibAlgos.PhiSymProducer_cfi')
# process.PhiSymProducer.applyEtThreshold=cms.bool(False)
process.PhiSymProducer.makeSpectraTreeEB = False
process.PhiSymProducer.makeSpectraTreeEE = False
process.PhiSymProducer.barrelHitCollection = cms.InputTag('hltAlCaPhiSymUncalibrator', 'phiSymEcalRecHitsEB', 'HLT')
process.PhiSymProducer.endcapHitCollection = cms.InputTag('hltAlCaPhiSymUncalibrator', 'phiSymEcalRecHitsEE', 'HLT')

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
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_R_74_V12A')

# SCHEDULE
if (not runMultiFit):
    process.reconstruction_step = cms.Sequence( process.ecalUncalibRecHit + process.ecalRecHit )
else:
    process.reconstruction_step = cms.Sequence( process.ecalMultiFitUncalibRecHit + process.ecalRecHit )

if (isStream):
    process.p = cms.Path(process.reconstruction_step)
    process.p *= process.offlineBeamSpot
    process.p *= process.PhiSymProducer
else:
    process.p = cms.Path(process.RawToDigi) 
    process.p *= process.L1Reco
    process.p *= process.reconstruction_step
    process.p *= process.offlineBeamSpot
    process.p *= process.PhiSymProducer

process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.path = cms.Path(process.offlineBeamSpot)
process.path *= process.PhiSymProducer
process.schedule = cms.Schedule(process.path, process.RECOSIMoutput_step)
