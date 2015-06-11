import FWCore.ParameterSet.Config as cms

process = cms.Process("PHISYM")

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('/store/user/spigazzi/AlCaPhiSym/crab_PHISYM_test_production/150527_083742/0000/phisym_1.root'))

# Output definition
process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
                                         splitLevel = cms.untracked.int32(0),
                                         outputCommands = cms.untracked.vstring("keep *"),
                                         fileName = cms.untracked.string("PHISYM_test_userInputFiles.root")
)

process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.schedule = cms.Schedule(process.RECOSIMoutput_step)


