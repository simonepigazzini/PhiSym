from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName     = 'PHISYM_test_calibration_1000lumis_v0'
config.General.transferLogs    = True
config.General.transferOutputs = True

config.section_('JobType')
config.JobType.pluginName      = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName        = 'PhiSymCalibration_cfg.py'
config.JobType.priority        = 20

config.section_('Data')
# This string determines the primary dataset of the newly-produced outputs.
config.Data.inputDataset       = '/AlCaPhiSym/spigazzi-crab_PHISYM_test_production_Run2015A_v1-b3a63a3628794e07f253ccb3bf8017ab/USER'
#config.Data.useParent = True
config.Data.inputDBS           = 'phys03'
config.Data.splitting          = 'LumiBased'
#config.Data.lumiMask           = 'Run2015A_v0.json'
config.Data.unitsPerJob        = 1000
config.Data.totalUnits         = -1
config.Data.publication        = False
#config.Data.isbchecksum        = 'b3a63a3628794e07f253ccb3bf8017ab'
#config.Data.ignoreLocality     = True

# This string is used to construct the output dataset name
#config.Data.publishDataName = 'CRAB3-tutorial'
config.Data.outLFNDirBase      =  '/store/user/spigazzi/'

config.section_('Site')
# Where the output files will be transmitted to
config.Site.storageSite        = 'T3_IT_MIB'

