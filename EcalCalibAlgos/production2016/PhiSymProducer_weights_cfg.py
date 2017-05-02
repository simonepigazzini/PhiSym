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
                            fileNames = cms.untracked.vstring(
                                "root://cms-xrd-global.cern.ch//store/data/Run2016H/AlCaPhiSym/RAW/v1/000/281/110/00000/02780885-647E-E611-AE36-02163E0140F5.root"
                                #"root://cms-xrd-global.cern.ch//store/data/Run2016G/AlCaPhiSym/RAW/v1/000/278/815/00000/0A63C6B5-0D62-E611-88E8-02163E011FA4.root"
                                #"/store/data/Commissioning2016/AlCaPhiSym/RAW/v1/000/268/930/00000/D624B590-A2FD-E511-B7AD-02163E011AEE.root"
                                #"/store/data/Run2015A/AlCaPhiSym/RAW/v1/000/247/720/00000/4C0AF78B-4810-E511-8C09-02163E0143CB.root"
                                #"root://cmsxrootd-site.fnal.gov//store/data/Run2015B/AlCaPhiSym/RAW/v1/000/251/562/00000/0014158C-7728-E511-8847-02163E0122C2.root",
))

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('step_PHISYM nevts:'+str(options.maxEvents)),
    name = cms.untracked.string('PhiSymProducer')
)

#ecalUncalibRecHit
process.ecalUncalibRecHit.EBdigiCollection = cms.InputTag("hltEcalPhiSymFilter","phiSymEcalDigisEB")
process.ecalUncalibRecHit.EEdigiCollection = cms.InputTag("hltEcalPhiSymFilter","phiSymEcalDigisEE")

#ecalRecHit (no ricovery)
process.ecalRecHit.killDeadChannels = cms.bool( False )
process.ecalRecHit.recoverEBVFE = cms.bool( False )
process.ecalRecHit.recoverEEVFE = cms.bool( False )
process.ecalRecHit.recoverEBFE = cms.bool( False )
process.ecalRecHit.recoverEEFE = cms.bool( False )
process.ecalRecHit.recoverEEIsolatedChannels = cms.bool( False )
process.ecalRecHit.recoverEBIsolatedChannels = cms.bool( False )
process.ecalRecHit.EBuncalibRecHitCollection = cms.InputTag("ecalUncalibRecHit","EcalUncalibRecHitsEB")
process.ecalRecHit.EEuncalibRecHitCollection = cms.InputTag("ecalUncalibRecHit","EcalUncalibRecHitsEE")

# PHISYM producer
process.load('PhiSym.EcalCalibAlgos.PhiSymProducer_cfi')
# process.PhiSymProducer.makeSpectraTreeEB = True
# process.PhiSymProducer.makeSpectraTreeEE = True
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
                                 globaltag = cms.string('80X_dataRun2_2016LegacyRepro_Candidate_v2')
)

### APD gain loss due to dark current corrections (for 2016 legacy ReReco)
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string("EcalLinearCorrectionsRcd"),
             tag = cms.string("EcalLinearCorrections_from2011_offline"),
             connect = cms.string("frontier://FrontierPrep/CMS_CONDITIONS"),
         )
)       

### Test E/p PN corrections for 2016 legac
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string("EcalIntercalibConstantsRcd"),
             tag = cms.string("EcalIntercalibConstants_Cal_Mar2017_PNcorrection_eop_v2"),
             connect = cms.string('frontier://FrontierPrep/CMS_CONDITIONS')
         )
)

### New alpha tag from 2016 B and C
# process.GlobalTag.toGet = cms.VPSet(
#     cms.PSet(record = cms.string("EcalLaserAlphasRcd"),
#              tag = cms.string("EcalLaserAlphas_EFlow_3sigma"),
#              connect = cms.string("frontier://FrontierPrep/CMS_CONDITIONS")
#          )
#      )

### Custum alpha tag from 2012
# process.GlobalTag.toGet = cms.VPSet(
#     cms.PSet(record = cms.string("EcalLaserAlphasRcd"),
#              tag = cms.string("alphaTest"),
#              connect = cms.string("sqlite_file:alphas_eflow2012.db")
#          )
#     )

### Force tags: examples
# process.GlobalTag.toGet = cms.VPSet(
#     cms.PSet(record = cms.string("EcalADCToGeVConstantRcd"),
#              tag = cms.string("EcalADCToGeVConstant_2016_Bon"),
#              connect = cms.string("sqlite_file:EcalADCToGeVConstant_2016_Bon.db")
#          ),
#     # cms.PSet(record = cms.string("EcalLaserAPDPNRatiosRcd"),
#     #          tag = cms.string("EcalLaserAPDPNRatios_offline_2016"),
#     #          connect = cms.string("frontier://FrontierPrep/CMS_CONDITIONS")
#     #      )
# )

# SCHEDULE
process.reconstruction_step = cms.Sequence( process.ecalUncalibRecHit + process.ecalRecHit )

process.p = cms.Path(process.reconstruction_step)
process.p *= process.offlineBeamSpot
process.p *= process.PhiSymProducer

process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.schedule = cms.Schedule(process.p, process.RECOSIMoutput_step)
