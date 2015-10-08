import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.applyCorrections = cms.bool(False)
process.variables = cms.vstring("IC")
process.ioFilesOpt = cms.PSet(    
    inputFiles = cms.vstring(
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_191043_191062.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_191086_191226.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_191247_191277.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_191691_191810.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_193093_193334.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_193336_193575.root",

        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_193834_194050.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_194051_194120.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_194150_194210.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_194223_194428.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_194429_194479.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_194480_194644.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_194691_194897.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_194912_195115.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_195147_195390.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_195396_195552.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_195633_195868.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_195913_195950.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_195963_196239.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_196249_196438.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_196452_196531.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_198202_198249.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_198268_198522.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_198941_199008.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_199011_199336.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_199356_199436.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_199698_199754.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_199804_199877.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_199960_200091.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_200152_200466.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_200473_200601.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_200990_201115.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_201159_201176.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_201278_201625.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_201657_201824.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_202012_202075.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_202084_202209.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_202237_202477.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_202478_202478.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012ABCD_timeEvo/summed_202504_202504.root"        
    ),

    correctionsFiles = cms.vstring(
        #     #---Boff
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2012C_v1/geo_and_material_corr.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015A_v2/geo_and_material_corr.txt"

         #     #---Bon
         #  "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/newThr_2012D/geo_and_material_corr.txt",
         #  "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/geo_and_material_corr.txt"
    )
)
