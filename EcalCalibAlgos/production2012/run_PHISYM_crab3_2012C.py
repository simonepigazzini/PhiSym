from WMCore.Configuration import Configuration

config = Configuration()
config.section_('General')
config.General.requestName = 'PHISYM-CMSSW_746-74X_dataRun2_Prompt_v0-Run2012C_TimeEvo_v1'
config.General.transferLogs = True
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.pluginName = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName = 'PhiSymProducer2012D_cfg.py'
config.JobType.priority = 20
config.JobType.maxJobRuntimeMin= 3000
config.section_('Data')

# This string determines the primary dataset of the newly-produced outputs.
config.Data.inputDataset = '/AlCaPhiSym/Run2012C-v1/RAW'
#config.Data.useParent = True
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
#config.Data.lumiMask = 'Run2012C_0T.json'
config.Data.lumiMask = 'json_Golden.txt'
config.Data.unitsPerJob = 100
config.Data.totalUnits = -1
config.Data.publication = True
#config.Data.isbchecksum = 'aa6d0f694fbde2c60e6338a92e82f36e'
#config.Data.ignoreLocality = True

# This string is used to construct the output dataset name
#config.Data.publishDataName = 'CRAB3-tutorial'
config.Data.outLFNDirBase = '/store/user/spigazzi/'
config.section_('Site')

# Where the output files will be transmitted to
config.Site.storageSite = 'T3_IT_MIB'
