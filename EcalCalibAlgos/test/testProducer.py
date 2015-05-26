import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.AlCa.GlobalTag import GlobalTag

# parse commad line options
options = VarParsing('analysis')
options.maxEvents = -1
options.outputFile = 'phisym.root'
options.parseArguments()

process=cms.Process("PHISYM")

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')#condDBv2_cff')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('RecoLocalCalo.EcalRecProducers.ecalMultiFitUncalibRecHit_cfi')
process.load('RecoLocalCalo.EcalRecProducers.ecalUncalibRecHit_cfi')
process.load('RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi')

process.load('FWCore/MessageService/MessageLogger_cfi')

process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.cerr.default = cms.untracked.PSet(
    limit = cms.untracked.int32(10000000),
    reportEvery = cms.untracked.int32(5000)
)

# import of standard configurations
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('/store/data/Commissioning2015/AlCaPhiSym/RAW/v1/000/240/226/00000/9087B70C-A2E1-E411-A01E-02163E013902.root')
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('step_PHISYM nevts:'+str(options.maxEvents)),
    name = cms.untracked.string('testProducer')
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
    process.ecalUncalibRecHit.EBdigiCollection = cms.InputTag("HLTEcalPhiSymFilter","phiSymEcalDigisEB")
    process.ecalUncalibRecHit.EEdigiCollection = cms.InputTag("HLTEcalPhiSymFilter","phiSymEcalDigisEE")

#ecalMultiFitUncalibRecHit
if (isStream):
    process.ecalMultiFitUncalibRecHit.EBdigiCollection = cms.InputTag("HLTEcalPhiSymFilter","phiSymEcalDigisEB")
    process.ecalMultiFitUncalibRecHit.EEdigiCollection = cms.InputTag("HLTEcalPhiSymFilter","phiSymEcalDigisEE")

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

process.load('PhiSym.EcalCalibAlgos.testProducer_cfi')

# Output definition
PHISYM_output_commands = cms.untracked.vstring(
    "drop *",
    "keep *_testProducer_*_*")

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
                                         splitLevel = cms.untracked.int32(0),
                                         outputCommands = PHISYM_output_commands,
                                         fileName = cms.untracked.string(options.outputFile)
)

process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_R_74_V8A::All')
# process.GlobalTag.globaltag = 'FT_R_70_V1::All'
# process.GlobalTag.toGet = cms.VPSet(
#     cms.PSet(record = cms.string("EcalIntercalibConstantsRcd"),
#              tag = cms.string("EcalIntercalibConstantsMC_mc"),
#              connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_ECAL")
#              )
#     )


if (not runMultiFit):
    process.reconstruction_step = cms.Sequence( process.ecalUncalibRecHit + process.ecalRecHit )
else:
    process.reconstruction_step = cms.Sequence( process.ecalMultiFitUncalibRecHit + process.ecalRecHit )

if (isStream):
    process.p = cms.Path(process.reconstruction_step)
    process.p *= process.testProducer
else:
    process.p = cms.Path(process.RawToDigi) 
    process.p *= process.L1Reco
    process.p *= process.reconstruction_step
    process.p *= process.testProducer

#process.path = cms.Path(process.testProducer)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.schedule = cms.Schedule(process.p, process.RECOSIMoutput_step)
