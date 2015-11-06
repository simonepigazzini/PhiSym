import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.ioFilesOpt = cms.PSet(    
    outputFileBase = cms.string('corrections_'),
    inputFiles = cms.vstring(
        # # 2012C Boff
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012C_v1/summed_200781_200798.root",
        
        # # 2015A Boff
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015A_v2/summed_250896_250896.root"

        # 2012D Bon
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012D_newThr/summed_208538_208686.root",

        # # 2015B Bon
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/summed_251562_251562.root"

        # 2015CD
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015CD_v1/summed_254232_254232.root",
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
        
    )
)
        

