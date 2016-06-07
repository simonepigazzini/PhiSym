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
        
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_259862-434_259891-108.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/summed_272760-72_272775-138.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/summed_272775-139_272784-52.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/summed_272784-53_272786-15.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/summed_272786-16_272798-436.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/summed_272798-1309_272811-106.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/summed_272798-437_272798-854.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/summed_272798-855_272798-1308.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/summed_272811-107_272812-313.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/summed_272812-314_272818-362.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/summed_272818-363_272827-104.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/summed_272930-1_273013-254.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/summed_273013-255_273017-703.root"
        
    )
)
        

