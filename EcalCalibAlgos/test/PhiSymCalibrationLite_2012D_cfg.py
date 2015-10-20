import FWCore.ParameterSet.Config as cms

process = cms.PSet()

nIOVs=1

process.IOVBounds = cms.PSet(
    startingIOV = cms.int32(65),
    nIOVs       = cms.int32(nIOVs),    
    beginRuns   = cms.vint32(191043, 191086, 191247, 191691, 193093, 193336, 193834, 194051, 194150, 194223,
                             194429, 194480, 194691, 194912, 195147, 195396, 195633, 195913, 195963, 196249,
                             196452, 198202, 198268, 198941, 199011, 199356, 199698, 199804, 199960, 200152,
                             200473, 200990, 201159, 201278, 201657, 202012, 202084, 202237, 202478, 202504,
                             203830, 203909, 204113, 204563, 204564, 205086, 205111, 205233, 205312, 205339,
                             205666, 205774, 206088, 206243, 206389, 206466, 206539, 206744, 206897, 207214,
                             207269, 207454, 207897, 208297, 208390, 208538),
    beginLumis  = cms.vint32(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
                             -1, -1),
    endRuns     = cms.vint32(191062, 191226, 191277, 191810, 193334, 193575, 194050, 194120, 194210,
                             194428, 194479, 194644, 194897, 195115, 195390, 195552, 195868, 195950,
                             196239, 196438, 196531, 198249, 198522, 199008, 199336, 199436, 199754,
                             199877, 200091, 200466, 200601, 201115, 201176, 201625, 201824, 202075,
                             202209, 202477, 202478, 202504, 203912, 204101, 204555, 204601, 205085,
                             205310, 205217, 205311, 205617, 205627, 205718, 206066, 206210, 206331,
                             206448, 206513, 206605, 206869, 207100, 207233, 207398, 207518, 207924,
                             208357, 208487, 208686),
    endLumis    = cms.vint32(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
                             -1, -1)
)

process.ioFilesOpt = cms.PSet(    
    outputFile = cms.string('summed_'),
    
    oldConstantsFiles = cms.vstring('/afs/cern.ch/work/s/spigazzi/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2012D_newThr.dat'),
        
    recoConstantsFile = cms.string('/afs/cern.ch/work/s/spigazzi/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2012ABCD_25iov.dat'),
        
    inputFiles = cms.vstring([        
        "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2012D_newThr/phisym_intercalibs_1000lumis.root"
        ])
)

# for iov in range(65, 66):
#     process.ioFilesOpt.oldConstantsFiles.append('/afs/cern.ch/cms/CAF/CMSALCA/ALCA_ECALCALIB/energy-calibration-repository/phiSymmetry/2012D_LTCorrJan13/EcalIntercalibConstants_Oct13Jump_Corr_2012D_'+str(process.IOVBounds.beginRuns[iov])+'_'+str(process.IOVBounds.endRuns[iov])+'_Absolute.txt')
    #print process.ioFilesOpt.oldConstantsFiles[iov]
    #process.ioFilesOpt.oldConstantsFiles.append('/afs/cern.ch/cms/CAF/CMSALCA/ALCA_ECALCALIB/energy-calibration-repository/phiSymmetry/2012D_NewLaserTag/EcalIntercalibConstants_NLT_2012D_'+str(process.IOVBounds.beginRuns[iov])+'_'+str(process.IOVBounds.endRuns[iov])+'_NewCodeChecked_Absolute.txt')

