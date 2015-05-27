from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName     = 'PHISYM_test_production'
config.General.transferLogs    = True
config.General.transferOutputs = True

config.section_('JobType')
config.JobType.pluginName      = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName        = 'testProducer.py'
#config.JobType.outputFiles     = ['GEN-SIM_H125GG-VBF_SLHC25_patch3.root']

config.section_('Data')
# This string determines the primary dataset of the newly-produced outputs.
# For instance, this dataset will be named /CrabTestSingleMu/something/USER
config.Data.inputDataset       = '/AlCaPhiSym/Commissioning2015-v1/RAW'
#config.Data.useParent = True
config.Data.inputDBS           = 'global'
config.Data.splitting          = 'LumiBased'
config.Data.lumiMask           = 'testSample.json'
config.Data.unitsPerJob        = 1000
config.Data.totalUnits         = 1000
config.Data.publication        = True
#config.Data.ignoreLocality     = True

# This string is used to construct the output dataset name
#config.Data.publishDataName = 'CRAB3-tutorial'
config.Data.outLFNDirBase      =  '/store/user/spigazzi/'

config.section_('Site')
# Where the output files will be transmitted to
config.Site.storageSite        = 'T3_IT_MIB'

