import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.applyCorrections = cms.bool(True)
process.variables = cms.vstring("IC", "LC", "Nhits")
process.ioFilesOpt = cms.PSet(    
    inputFiles = cms.vstring(
        ## weights vs multifit
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251562_251562.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415_m/summed_251562_251562.root"

        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015C_7415/summed_254790_254790.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015C_7415_m/summed_254790_254790.root"

        ## TRANSPORT
        
        # # 2012C Boff
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012C_v1/summed_200781_200798.root",
        
        # # 2015A Boff
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015A_v2/summed_250896_250896.root",
        
        # # 2012D Bon
        #"$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012D_newThr/summed_208538_208686.root",
        
        # # 2015B Bon
        #"$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251562_251562.root",
        #"$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_256843_256843.root"

        # 2015D Boff
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Run2015D_Boff_v1/summed_259971-1_260043-410.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Run2015D_Boff_v1/summed_260043-411_260108-355.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Run2015D_Boff_v1/summed_260132-1_260235-25.root",
        
        # Comm2016
        # weights
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/summed_268930-1_269000-30.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/summed_269012-1_269073-68.root"

        # multifit
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/summed_268930-1_269000-30.root"

        # Run2016B
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_259862-434_259891-108.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/summed_272760-72_272776-22.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/summed_272776-23_272784-193.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/summed_272784-194_272798-255.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/summed_272798-256_272798-730.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/summed_272798-731_272798-1194.root"
        
    ),

    correctionsFiles = cms.vstring(
        # #---Boff
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2012C_v1/corrections_200781_200798.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015A_v2/corrections_250896_250896.txt"

        #---Bon
        #"/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_15/src/PhiSym/EcalCalibAlgos/ntuples/2012D_newThr/corrections_208538_208686.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_15/src/PhiSym/EcalCalibAlgos/corrections_208538_208686.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_15/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/corrections_251562_251562.txt"
        #"/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_15/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/corrections_256843_256843.txt"
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_15/src/PhiSym/EcalCalibAlgos/corrections_256843_256843.txt"

        # Run2016B
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_8_0_7/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/corrections_259862-434_259891-108.txt",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_8_0_7/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/corrections_272760-72_272776-22.txt",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_8_0_7/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/corrections_272776-23_272784-193.txt",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_8_0_7/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/corrections_272784-194_272798-255.txt",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_8_0_7/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/corrections_272798-256_272798-730.txt",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_8_0_7/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/corrections_272798-731_272798-1194.txt"

    )
)

