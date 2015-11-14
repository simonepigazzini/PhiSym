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
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251244_251244.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251251_251251.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251252_251252.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251521_251521.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251522_251522.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251523_251523.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251548_251548.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251559_251559.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251560_251560.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251561_251561.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251562_251562.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_254232_254232.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_254790_254790.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_254852_254879.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_254906_254914.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_256630_256677.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_256801_256842.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_256843_256843.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_256866_256867.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_256868_256868.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_256869_256926.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_256941_256941.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_257461_257461.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_257531_257531.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_257599_257599.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_257613_257613.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_257614_257645.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_257682_257735.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_257751_257751.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_257805_257805.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_257816_257816.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_257819_257819.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_257968_257968.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_257969_257969.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258129_258157.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258158_258158.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258159_258159.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258177_258177.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258211_258211.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258213_258213.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258214_258214.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258215_258215.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258287_258287.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258403_258403.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258425_258425.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258426_258426.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258427_258427.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258428_258428.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258432_258432.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258434_258434.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258440_258440.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258443_258443.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258444_258444.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258445_258445.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258446_258446.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258448_258448.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258655_258655.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258656_258656.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258694_258694.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258702_258702.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258703_258703.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258705_258705.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258706_258706.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258712_258712.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258713_258713.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258714_258714.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258741_258741.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258742_258742.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258745_258745.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258749_258749.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_258750_258750.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259626_259626.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259637_259637.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259681_259681.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259683_259683.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259685_259685.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259686_259686.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259721_259721.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259809_259809.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259810_259810.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259811_259811.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259813_259813.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259817_259817.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259818_259818.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259820_259820.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259821_259821.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259822_259822.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259861_259861.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259862_259862.root"
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259884_259884.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259890_259890.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_259891_259891.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_260373_260373.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_260425_260425.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_260426_260426.root"
        
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
