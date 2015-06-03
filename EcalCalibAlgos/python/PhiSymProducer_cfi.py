import FWCore.ParameterSet.Config as cms

PhiSymProducer = cms.EDProducer(
    "PhiSymProducer",
    barrelHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB', 'PHISYM'),
    endcapHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEE', 'PHISYM'),
    eCut_barrel = cms.double(0.0),
    eThreshold_barrel = cms.double(1000.0), #this is actually summed to eCut in order to define the upper bound
    AP = cms.double(-0.15),
    B = cms.double(0.6),
    nMisCalib = cms.int32(10), # <= 10; even; central value does not count 
    misCalibRangeEB = cms.vdouble(0.95, 1.05),
    misCalibRangeEE = cms.vdouble(0.90, 1.10),
    lumisToSum = cms.int32(1),          
    statusThreshold = cms.untracked.int32(0)
)
