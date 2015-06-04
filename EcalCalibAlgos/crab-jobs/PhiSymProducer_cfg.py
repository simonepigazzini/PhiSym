import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.AlCa.GlobalTag import GlobalTag

# parse commad line options
options = VarParsing('analysis')
options.maxEvents = -1
options.outputFile = 'PHISYM_Run2015A_v0_test.root'
options.parseArguments()

process=cms.Process("PHISYM")

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
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                '/store/data/Run2015A/AlCaPhiSym/RAW/v1/000/246/919/00000/04281A56-F509-E511-8C9A-02163E0143C5.root',
                                '/store/data/Run2015A/AlCaPhiSym/RAW/v1/000/246/919/00000/0657B565-EC09-E511-825B-02163E011DC2.root',
                                '/store/data/Run2015A/AlCaPhiSym/RAW/v1/000/246/919/00000/18766157-F509-E511-93A8-02163E011DE4.root',
                                '/store/data/Run2015A/AlCaPhiSym/RAW/v1/000/246/919/00000/1A16BC83-F909-E511-B17C-02163E011B6D.root',
                                '/store/data/Run2015A/AlCaPhiSym/RAW/v1/000/246/919/00000/2235CE58-F509-E511-804E-02163E013826.root',
                                '/store/data/Run2015A/AlCaPhiSym/RAW/v1/000/246/919/00000/368DD35A-F509-E511-BAD4-02163E011891.root',
                                '/store/data/Run2015A/AlCaPhiSym/RAW/v1/000/246/919/00000/3ECCF956-F509-E511-8E13-02163E011DE4.root',
                                '/store/data/Run2015A/AlCaPhiSym/RAW/v1/000/246/919/00000/66007B5B-F509-E511-A910-02163E014349.root',
                                '/store/data/Run2015A/AlCaPhiSym/RAW/v1/000/246/919/00000/6ABBFC56-F509-E511-8AF7-02163E01396D.root',
                                '/store/data/Run2015A/AlCaPhiSym/RAW/v1/000/246/919/00000/AE98FA5A-F509-E511-A205-02163E0142B3.root',
                                '/store/data/Run2015A/AlCaPhiSym/RAW/v1/000/246/919/00000/F098F257-F509-E511-9270-02163E012124.root',
                                '/store/data/Run2015A/AlCaPhiSym/RAW/v1/000/246/919/00000/FA57815A-F509-E511-86CD-02163E011B82.root')
                                #'/store/data/Run2015A/AlCaPhiSym/RAW/v1/000/246/920/00000/F082B567-DE09-E511-B94D-02163E011D50.root')
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('step_PHISYM nevts:'+str(options.maxEvents)),
    name = cms.untracked.string('PhiSymProducer')
)

isStream=True
runMultiFit=True
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
    process.ecalRecHit.EBuncalibRecHitCollection = cms.InputTag("ecalUncalibRecHit","EcalUncalibRecHitsEB")
    process.ecalRecHit.EEuncalibRecHitCollection = cms.InputTag("ecalUncalibRecHit","EcalUncalibRecHitsEE")

# PHISYM producer
process.load('PhiSym.EcalCalibAlgos.PhiSymProducer_cfi')
# process.PhiSymProducer.applyEtThreshold=cms.bool(False)
process.PhiSymProducer.makeSpectraTreeEB = False
process.PhiSymProducer.makeSpectraTreeEE = False

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
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_E_V48')
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string("EcalChannelStatusRcd"),
             tag = cms.string("EcalChannelStatus_v1_hlt"),
             connect = cms.untracked.string("frontier://PromptProd/CMS_COND_31X_ECAL")
         ),
    cms.PSet(record = cms.string("EcalIntercalibConstantsRcd"),
             tag = cms.string("EcalIntercalibConstants_V1_express"),
             connect = cms.untracked.string("frontier://PromptProd/CMS_COND_31X_ECAL")
         )
)

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
process.schedule = cms.Schedule(process.p, process.RECOSIMoutput_step)
