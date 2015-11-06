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

        # 2015CD 25ns
        # # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_254232_254232.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_254790_254790.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_254852_254879.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_254906_254914.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_256630_256677.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_256801_256842.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_256843_256843.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_256866_256867.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_256868_256868.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_256869_256926.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_256941_256941.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_257461_257461.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_257531_257531.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_257599_257599.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_257613_257613.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_257614_257645.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_257682_257735.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_257751_257751.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_257805_257805.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_257816_257816.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_257819_257819.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_257968_257968.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_257969_257969.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_258129_258157.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_258158_258158.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_258159_258159.root"
        
        ## TRANSPORT
        
        # # 2012C Boff
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012C_v1/summed_200781_200798.root",
        
        # # 2015A Boff
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015A_v2/summed_250896_250896.root",
        
        # 2012D Bon
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012D_newThr/summed_208538_208686.root",
        
        # 2015B Bon
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/summed_251561_251561.root"
    ),

    correctionsFiles = cms.vstring(
        # #---Boff
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2012C_v1/corrections_200781_200798.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015A_v2/corrections_250896_250896.txt"

        #---Bon
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2012D_newThr/corrections_208538_208686.txt",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/corrections_251562_251562.txt"

        #---2015CD 25ns
        # # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_254232_254232.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_254790_254790.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_254852_254879.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_254906_254914.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_256630_256677.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_256801_256842.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_256843_256843.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_256866_256867.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_256868_256868.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_256869_256926.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_256941_256941.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_257461_257461.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_257531_257531.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_257599_257599.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_257613_257613.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_257614_257645.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_257682_257735.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_257751_257751.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_257805_257805.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_257816_257816.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_257819_257819.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_257968_257968.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_257969_257969.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_258129_258157.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_258158_258158.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/corrections_258159_258159.txt"

    )
)
