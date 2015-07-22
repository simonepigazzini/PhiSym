from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName     = 'PHISYM-CMSSW_741-multifit-GR_P_V56-Run2015A_all_v2'
config.General.transferLogs    = True
config.General.transferOutputs = True

config.section_('JobType')
config.JobType.pluginName      = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName        = 'PhiSymProducer_cfg.py'
config.JobType.priority        = 10

config.section_('Data')
# This string determines the primary dataset of the newly-produced outputs.
config.Data.inputDataset       = '/AlCaPhiSym/Run2015A-v1/RAW'
#config.Data.useParent = True
config.Data.inputDBS           = 'global'
config.Data.splitting          = 'LumiBased'
config.Data.lumiMask           = 'Run2015A.json'
config.Data.unitsPerJob        = 10
config.Data.totalUnits         = -1
config.Data.publication        = True
#config.Data.isbchecksum        = 'aa6d0f694fbde2c60e6338a92e82f36e'
#config.Data.ignoreLocality     = True

# This string is used to construct the output dataset name
#config.Data.publishDataName = 'CRAB3-tutorial'
config.Data.outLFNDirBase      =  '/store/user/spigazzi/'

config.section_('Site')
# Where the output files will be transmitted to
config.Site.storageSite        = 'T3_IT_MIB'

