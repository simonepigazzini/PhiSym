from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName     = 'PHISYM-CMSSW_741-weights-GR_P_v56-Run2015A-step2_v1'
#config.General.requestName     = 'PHISYM-CMSSW_741_oldTHR-GR_P_v56-Run2012D-step2_v4'
config.General.transferLogs    = True
config.General.transferOutputs = True

config.section_('JobType')
config.JobType.pluginName      = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName        = 'PhiSymCalibration_cfg.py'
config.JobType.priority        = 20

config.section_('Data')
# This string determines the primary dataset of the newly-produced outputs.
config.Data.inputDataset       = '/AlCaPhiSym/spigazzi-crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1-d1d8759b5763650129fcdb1ec58b4e6a/USER'
#config.Data.inputDataset       = '/AlCaPhiSym/spigazzi-crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012D_v2-f7938e3696e7187e48e8e9d9a5f4207d/USER'


#config.Data.useParent = True
config.Data.inputDBS           = 'phys03'
config.Data.splitting          = 'LumiBased'
#config.Data.lumiMask           = 'Run2015A_v0.json'
config.Data.unitsPerJob        = 100
config.Data.totalUnits         = -1
config.Data.publication        = False
config.Data.ignoreLocality     = True

# This string is used to construct the output dataset name
#config.Data.publishDataName = 'CRAB3-tutorial'
config.Data.outLFNDirBase      =  '/store/user/spigazzi/'

config.section_('Site')
# Where the output files will be transmitted to
config.Site.storageSite        = 'T3_IT_MIB'
config.Site.whitelist          = ['T1_IT_CNAF']
