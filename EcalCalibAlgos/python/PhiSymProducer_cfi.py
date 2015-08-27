import FWCore.ParameterSet.Config as cms

PhiSymProducer = cms.EDProducer(
    "PhiSymProducer",
    barrelHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB', 'PHISYM'),
    endcapHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEE', 'PHISYM'),
    eThreshold_barrel = cms.double(13*0.04),    
    etCut_barrel = cms.double(1), #this is actually summed to eCut in order to define the upper bound    
    etCut_endcap = cms.double(1), #this is actually summed to eCut in order to define the upper bound    
    A = cms.double(0.2442), # C + B*ring + A*ring*ring
    B = cms.double(-4.148),
    C = cms.double(79.29),
    ADCthrEE = cms.int32(20),
    nMisCalib = cms.int32(10), # <= 10; even; central value does not count
    misCalibRangeEB = cms.vdouble(0.95, 1.05),
    misCalibRangeEE = cms.vdouble(0.90, 1.10),
    lumisToSum = cms.int32(1),          
    statusThreshold = cms.int32(0),
    makeSpectraTreeEB = cms.untracked.bool(False),
    makeSpectraTreeEE = cms.untracked.bool(False)
)
