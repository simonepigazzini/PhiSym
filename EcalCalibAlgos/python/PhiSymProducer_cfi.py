import FWCore.ParameterSet.Config as cms

PhiSymProducer = cms.EDProducer(
    "PhiSymProducer",
    barrelHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB', 'PHISYM'),
    endcapHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEE', 'PHISYM'),
    etCut_barrel = cms.double(1), #this is actually summed to eThr in order to define the upper bound
    eThreshold_barrel = cms.double(0.550), 
    etCut_endcap = cms.double(1), #this is actually summed to eThr in order to define the upper bound
    A = cms.double( -0.150),
    B = cms.double( 0.600),
    nMisCalib = cms.int32(10), # <= 10; even; central value does not count 
    misCalibRangeEB = cms.vdouble(0.95, 1.05),
    misCalibRangeEE = cms.vdouble(0.90, 1.10),
    lumisToSum = cms.int32(1),          
    statusThreshold = cms.int32(0),
    applyEtThreshold = cms.bool(True),
    makeSpectraTreeEB = cms.untracked.bool(False),
    makeSpectraTreeEE = cms.untracked.bool(False)
)
