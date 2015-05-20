import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

process = cms.Process('testProducer')

# parse commad line options
options = VarParsing('analysis')
options.maxEvents = -1
options.outputFile = 'phisym.root'
options.parseArguments()

# import of standard configurations
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('/store/data/Run2012A/AlCaPhiSym/RAW/v1/000/190/482/D08E58E5-4B7F-E111-8BBD-003048D2C0F4.root')
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('step_PHISYM nevts:'+str(options.maxEvents)),
    name = cms.untracked.string('testProducer')
)

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


# Path and EndPath definitions
process.PHISYM = cms.Path(process.testProducer)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.PHISYM, process.RECOSIMoutput_step)
