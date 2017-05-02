import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.IOVBounds = cms.PSet(
    startingIOV     = cms.int32(0),
    nIOVs           = cms.int32(-1),
    manualSplitting = cms.bool(False),
    beginRuns       = cms.vint32(),
    endRuns         = cms.vint32(),
    IOVMaps         = cms.vstring(
        #"$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/IOVmap.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/IOVmap.root",
    )
)

process.ioFilesOpt = cms.PSet(    
    outputFile = cms.string('summed_'),
    
    oldConstantsFiles = cms.vstring('/afs/cern.ch/work/s/spigazzi/ECAL/CMSSW_8_0_3/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2015Boff.dat'),
    
    recoConstantsFile = cms.string('/afs/cern.ch/work/s/spigazzi/ECAL/CMSSW_8_0_3/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_Prompt2016.dat'),
    
    inputFiles = cms.vstring([
        #Comm2016 weights
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_1.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_10.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_11.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_12.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_13.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_14.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_15.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_16.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_17.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_19.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_2.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_3.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_4.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_6.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_7.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_8.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/phisym_merged_9.root"

        #Comm2016 multifit
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/phisym_merged_1.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/phisym_merged_10.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/phisym_merged_11.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/phisym_merged_12.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/phisym_merged_13.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/phisym_merged_14.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/phisym_merged_15.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/phisym_merged_2.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/phisym_merged_3.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/phisym_merged_4.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/phisym_merged_5.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/phisym_merged_6.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/phisym_merged_7.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/phisym_merged_8.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/phisym_merged_9.root"
    ])
)

