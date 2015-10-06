import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.ioFilesOpt = cms.PSet(    
    outputFileBase = cms.string('corrections_'),
    inputFile = cms.string(        
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/newThr_2012D/summed_208538_208686.root"
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015A_v2/summed_250866_250866.root"
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015A_thr600_v1/summed_250866_250866.root"
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/summed_251562_251562.root"
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015C_Boff_v1/summed_254349_254349.root"
    )
)
        

