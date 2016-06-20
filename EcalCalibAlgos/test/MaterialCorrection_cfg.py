import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.absoluteICs = cms.bool(True)
process.ioFilesOpt = cms.PSet(
    getRunsFromFileName = cms.bool(True),
    userOutputName = cms.bool(False),
    outputFiles = cms.vstring(""),
    outputFileBase = cms.string('corrections_'),
    inputFiles = cms.vstring(
        # # 2012C Boff
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012C_v1/summed_200781_200798.root",
        
        # # 2015A Boff
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015A_v2/summed_250896_250896.root"

        # 2012D Bon
        #"$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012D_newThr/summed_208538_208686.root",

        # 2015B Bon
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251562_251562.root"

        # 2015D
        #"$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_256843_256843.root"

        # Comm2016
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/summed_268930-1_269000-30.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/summed_269012-1_269073-68.root"

        # Run2016B
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_259862-434_259891-108.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272760-72_272775-150.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272775-151_272784-75.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272784-76_272786-51.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272786-52_272798-481.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272798-1385_272811-172.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272798-482_272798-924.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272798-925_272798-1384.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272811-173_272818-7.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272818-8_272827-104.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272930-1_273013-214.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_273013-215_273017-646.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273158-1_273158-744.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273158-745_273158-1279.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273302-1_273402-162.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273402-163_273425-203.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273425-204_273450-647.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273492-71_273503-598.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273554-77_273555-173.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273725-83_273730-321.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273730-322_273730-2126.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_274094-105_274146-67.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_274159-1_274172-95.root"
        
    )
)
        

