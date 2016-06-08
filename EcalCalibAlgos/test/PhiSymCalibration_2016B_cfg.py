import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.IOVBounds = cms.PSet(
    startingIOV     = cms.int32(0),
    nIOVs           = cms.int32(-1),
    manualSplitting = cms.bool(False),
    beginRuns       = cms.vint32(),
    endRuns         = cms.vint32(),
    IOVMaps         = cms.vstring(
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/IOVmap.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/IOVmap.root",
    )
)

process.ioFilesOpt = cms.PSet(    
    outputFile = cms.string('summed_'),
    
    oldConstantsFiles = cms.vstring(''),
    
    recoConstantsFile = cms.string('/afs/cern.ch/work/s/spigazzi/ECAL/CMSSW_8_0_7/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2016B_prompt.dat'),
    
    inputFiles = cms.vstring([
        # 2016B_v1 weights
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_1.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_10.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_11.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_12.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_13.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_14.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_15.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_16.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_17.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_19.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_2.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_3.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_4.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_6.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_7.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_8.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/phisym_merged_9.root"

        # 2016B_v2 weights
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_11.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_12.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_13.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_14.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_15.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_16.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_17.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_18.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_19.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_1.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_20.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_21.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_22.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_23.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_24.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_25.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_26.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_27.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_28.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_29.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_2.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_30.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_31.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_32.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_33.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_34.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_35.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_36.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_37.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_38.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_39.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_3.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_40.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_41.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_42.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_43.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_44.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_45.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_46.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_47.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_48.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_49.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_4.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_50.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_51.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_52.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_53.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_54.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_55.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_56.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_57.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_5.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_9.root"
        
    ])
)

