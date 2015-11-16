import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.applyCorrections = cms.bool(False)
process.variables = cms.vstring("IC")
process.ioFilesOpt = cms.PSet(    
    inputFiles = cms.vstring(

        # 2012 ABCD
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_193834_194050.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_194051_194120.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_194150_194210.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_194223_194428.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_194429_194479.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_194480_194644.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_194691_194897.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_194912_195115.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_195147_195390.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_195396_195552.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_195633_195868.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_195913_195950.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_195963_196239.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_196249_196438.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_196452_196531.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_198202_198249.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_198268_198522.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_198941_199008.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_199011_199336.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_199356_199436.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_199698_199754.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_199804_199877.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_199960_200091.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_200152_200466.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_200473_200601.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_200990_201115.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_201159_201176.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_201278_201625.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_201657_201824.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_202012_202075.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_202084_202209.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_202237_202477.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_202478_202478.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_202504_202504.root"

        #---2015BCD 25ns
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415_merged/summed_251244-332_251252-1.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415_merged/summed_251244-85_251244-331.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415_merged/summed_251252-2_251252-301.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415_merged/summed_251252-302_251252-554.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415_merged/summed_251521-39_251562-93.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415_merged/summed_251562-293_251562-511.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415_merged/summed_251562-94_251562-292.root"
        
        ## TRANSPORT
        
        # # 2012C Boff
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012C_v1/summed_200781_200798.root",
        
        # # 2015A Boff
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015A_v2/summed_250896_250896.root",
        
        # # 2012D Bon
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012D_newThr/summed_208538_208686.root",
        
        # # 2015B Bon
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/summed_251561_251561.root"
    ),

    correctionsFiles = cms.vstring(
        # #---Boff
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2012C_v1/corrections_200781_200798.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015A_v2/corrections_250896_250896.txt"

        #---Bon
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2012D_newThr/corrections_208538_208686.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/corrections_251562_251562.txt"        
    )
)
