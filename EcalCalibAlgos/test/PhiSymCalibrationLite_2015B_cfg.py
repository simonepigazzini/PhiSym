import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.IOVBounds = cms.PSet(
    startingIOV = cms.int32(0),
    nIOVs       = cms.int32(18),    
    beginRuns   = cms.vint32(251022, 251023, 251024, 251025, 251026, 251027, 251028,
                             251244, 251251, 251252, 251521, 251522, 251523, 251548,
                             251559, 251560, 251561, 251562),
    beginLumis  = cms.vint32(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
                             -1, -1),
    endRuns     = cms.vint32(251022, 251023, 251024, 251025, 251026, 251027, 251028,
                             251244, 251251, 251252, 251521, 251522, 251523, 251548,
                             251559, 251560, 251561, 251562),
    endLumis    = cms.vint32(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
                             -1, -1)
)

process.ioFilesOpt = cms.PSet(    
    outputFile = cms.string('summed_'),
    
    oldConstantsFiles = cms.vstring('/afs/cern.ch/work/s/spigazzi/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2012D_newThr.dat'),
    #oldConstantsFiles = cms.vstring('/afs/cern.ch/work/s/spigazzi/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/data/giulia_ic.dat'),
    
    recoConstantsFile = cms.string('/afs/cern.ch/work/s/spigazzi/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2012ABCD_25iov.dat'),
    #recoConstantsFile = cms.string('/afs/cern.ch/work/s/spigazzi/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2015B_Abs.dat'),
    
    inputFiles = cms.vstring([        
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_1.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_16.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_4.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_10.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_17.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_5.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_11.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_18.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_6.root",        
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_12.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_19.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_7.root",        
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_13.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_2.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_8.root",        
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_14.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_20.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_9.root",        
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_15.root",
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/phisym_intercalibs_1000blocks_3.root"
        
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_1.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_10.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_11.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_12.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_13.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_14.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_15.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_16.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_17.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_18.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_19.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_2.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_20.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_3.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_4.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_5.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_6.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_7.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_8.root",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v4/phisym_intercalibs_1000blocks_9.root"
        ])
)

