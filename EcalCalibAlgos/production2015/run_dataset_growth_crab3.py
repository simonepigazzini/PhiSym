from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName     = 'PHISYM_test_userInputFiles'
config.General.transferLogs    = True
config.General.transferOutputs = True

config.section_('JobType')
config.JobType.pluginName      = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName        = 'PhiSymDummy_cfg.py'
config.JobType.priority        = 20

config.section_('Data')
# This string determines the primary dataset of the newly-produced outputs.
config.Data.primaryDataset     = 'AlCaPhiSym'
#config.Data.inputDBS           = 'global'
config.Data.splitting          = 'FileBased'
config.Data.unitsPerJob        = 1
config.Data.totalUnits         = 1
config.Data.publication        = True
config.Data.ignoreLocality     = True
#config.Data.userInputFiles     = ['/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_Run2015A_v1/150608_072558/0000/PHISYM_Run2015A_v0_test_10.root']
config.Data.userInputFiles     = ['/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production_USERtest/150605_185019/0000/phisym_1.root']

# This string is used to construct the output dataset name
#config.Data.publishDataName = 'CRAB3-tutorial'
config.Data.outLFNDirBase      =  '/store/user/spigazzi/'

config.section_('Site')
# Where the output files will be transmitted to
config.Site.storageSite        = 'T3_IT_MIB'
config.Site.whitelist          = ['T2_IT_Rome', 'T2_CH_CERN']

