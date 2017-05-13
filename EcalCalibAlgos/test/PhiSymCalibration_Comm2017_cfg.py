import FWCore.ParameterSet.Config as cms

process = cms.Process("Calibration")

process.IOVBounds = cms.PSet(
    startingIOV     = cms.int32(0),
    nIOVs           = cms.int32(-1),
    manualSplitting = cms.bool(True),
    beginRuns       = cms.vint32(1),
    endRuns         = cms.vint32(300000),
    IOVMaps         = cms.vstring("")
)

process.ioFilesOpt = cms.PSet(    
    outputFile = cms.string('summed_'),
    
    oldConstantsFiles = cms.vstring('/afs/cern.ch/work/s/spigazzi/ECAL/CMSSW_8_0_3/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2015Boff.dat'),
    
    recoConstantsFile = cms.string('/afs/cern.ch/work/s/spigazzi/ECAL/CMSSW_8_0_3/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_Prompt2016.dat'),
    
    inputFiles = cms.vstring([
        "file:phisym_merged.root"
    ])
)

