import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.AlCa.GlobalTag import GlobalTag

process = cms.Process("PHISYMstep2")

process.load('FWCore/MessageService/MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100000

process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')

# skip bad events
process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# Global tag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_P_V56')

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                # "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-GR_P_V56-Run2012D_v2/150624_101618/0000/phisym_weights_1lumis_331.root",
                                # "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-GR_P_V56-Run2012D_v2/150624_101618/0000/phisym_weights_1lumis_339.root",                                
                                # "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-GR_P_V56-Run2012D_v2/150624_101618/0000/phisym_weights_1lumis_331.root",
                                # "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-GR_P_V56-Run2012D_v2/150624_101618/0000/phisym_weights_1lumis_343.root",
                                # "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-GR_P_V56-Run2012D_v2/150624_101618/0000/phisym_weights_1lumis_345.root",
                                # "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-GR_P_V56-Run2012D_v2/150624_101618/0000/phisym_weights_1lumis_346.root",
                                # "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-GR_P_V56-Run2012D_v2/150624_101618/0000/phisym_weights_1lumis_348.root",
                                # "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-GR_P_V56-Run2012D_v2/150624_101618/0000/phisym_weights_1lumis_355.root",
                                # "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-GR_P_V56-Run2012D_v2/150624_101618/0000/phisym_weights_1lumis_356.root",
                                # "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-GR_P_V56-Run2012D_v2/150624_101618/0000/phisym_weights_1lumis_362.root"))

                                #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_100.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_103.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_105.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_107.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_110.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_112.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_113.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_114.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_115.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_117.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_86.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_87.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_88.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_90.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_91.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_92.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_93.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_94.root",
                            #     "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-multifit-_GR_P_V56-Run2015A_v1/150623_102846/0000/phisym_weights_1lumis_96.root"
                            # ))

                                #"root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis__1.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_10.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_11.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_12.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_13.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_14.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_15.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_16.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_17.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_18.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_19.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis__2.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_20.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_21.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_22.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_23.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_24.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_25.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_26.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_27.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_28.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_29.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis__3.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-_GR_P_V56-Run2015A_v1/150621_200143/0000/phisym_weights_1lumis_30.root"))
                                

# PHISYM Calib
process.load('PhiSym.EcalCalibAlgos.PhiSymCalibration_cfi')
process.PhiSymCalibration.blocksToSum = 1000
process.PhiSymCalibration.computeICs = False
process.PhiSymCalibration.oldCalibFile = "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2012D_newThr.dat"
process.PhiSymCalibration.absCalibFile = "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2015Abs.dat"

# Output TFile
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("phisym_intercalibs_1000lumis.root"))

process.path = cms.Path(process.PhiSymCalibration)

process.schedule = cms.Schedule(process.path)
