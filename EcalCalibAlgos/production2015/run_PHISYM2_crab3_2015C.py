from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName     = 'PHISYM-CMSSW_7412-weights-74X_dataRun2_Prompt_v2-Run2015C-step2_v1'
config.General.transferLogs    = True
config.General.transferOutputs = True

config.section_('JobType')
config.JobType.pluginName      = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName        = 'PhiSymCalibration_cfg.py'
config.JobType.priority        = 20

config.section_('Data')
# This string determines the primary dataset of the newly-produced outputs.
config.Data.inputDataset       = '/AlCaPhiSym/spigazzi-crab_PHISYM-CMSSW_7412-weights-74X_dataRun2_Prompt_v2-Run2015C_v1-ad7dc4f8513717010b7a46f581acebfc/USER'

#config.Data.useParent = True
config.Data.inputDBS           = 'phys03'
config.Data.splitting          = 'LumiBased'
config.Data.lumiMask           = 'golden_25ns.json'
config.Data.unitsPerJob        = 100
config.Data.totalUnits         = -1
config.Data.publication        = False
config.Data.ignoreLocality     = True

# This string is used to construct the output dataset name
#config.Data.publishDataName = 'CRAB3-tutorial'
#config.Data.outLFNDirBase      =  '/store/group/dpg_ecal/alca_ecalcalib/phiSymmetry'
config.Data.outLFNDirBase      =  '/store/user/spigazzi/'

config.section_('Site')
# Where the output files will be transmitted to
config.Site.storageSite        = 'T3_IT_MIB'
config.Site.whitelist          = ['T1_IT_CNAF']
