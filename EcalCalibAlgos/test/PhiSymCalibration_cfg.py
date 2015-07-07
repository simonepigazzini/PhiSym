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
                                #                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_FAST-GR_P_V56-Run2012D_v1/150626_221215/0000/phisym_weights_1lumis_1.root"
                                #                                "file:/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/phisym_weights_1lumis.root")
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_1.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_10.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_100.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_101.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_102.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_103.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_104.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_105.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_106.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_107.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_108.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_109.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_110.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_111.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_112.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_113.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_114.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_115.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_116.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_117.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_118.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_119.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_12.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_120.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_121.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_122.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_123.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_124.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_125.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_126.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_127.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_128.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_13.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_130.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_131.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_132.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_133.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_134.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_135.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_136.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_137.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_138.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_139.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_14.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_140.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_141.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_142.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_143.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_144.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_145.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_147.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_148.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_149.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_15.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_150.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_151.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_152.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_153.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_154.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_155.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_156.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_157.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_158.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_159.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_16.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_160.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_161.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_162.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_163.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_164.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_17.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_18.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_19.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_2.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_20.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_22.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_23.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_24.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_25.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_26.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_27.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_28.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_3.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_30.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_31.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_35.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_37.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_38.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_39.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_4.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_40.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_41.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_43.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_46.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_47.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_48.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_49.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_5.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_50.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_51.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_52.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_53.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_54.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_55.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_56.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_57.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_58.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_59.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_6.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_60.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_61.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_62.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_63.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_64.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_65.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_66.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_67.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_68.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_69.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_7.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_70.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_71.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_72.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_73.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_74.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_75.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_76.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_77.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_78.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_79.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_8.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_80.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_81.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_82.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_83.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_84.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_85.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_86.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_87.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_88.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_89.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_9.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_90.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_91.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_92.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_93.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_94.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_95.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_96.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_97.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_98.root",
                                "root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741_oldTHR-GR_P_V56-Run2012A_v1/150706_031725/0000/phisym_weights_1lumis_99.root")
)

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
