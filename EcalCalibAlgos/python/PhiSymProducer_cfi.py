import FWCore.ParameterSet.Config as cms

PhiSymProducer = cms.EDProducer(
    "PhiSymProducer",
    barrelHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB', 'PHISYM'),
    endcapHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEE', 'PHISYM'),
    eCut_barrel = cms.double(13*0.04),
    eThreshold_barrel = cms.double(1), #this is actually summed to eCut in order to define the upper bound    
    Aplus = cms.double(0.2262), # C + B*ring + A*ring*ring
    Bplus = cms.double(-3.096),
    Cplus = cms.double(69.6),
    Aminus = cms.double(0.2442), # C + B*ring + A*ring*ring
    Bminus = cms.double(-4.148),
    Cminus = cms.double(79.29),
    ADCcutEE = cms.int32(20),
    nMisCalib = cms.int32(10), # <= 10; even; central value does not count 
    misCalibRangeEB = cms.vdouble(0.95, 1.05),
    misCalibRangeEE = cms.vdouble(0.90, 1.10),
    lumisToSum = cms.int32(1),          
    statusThreshold = cms.int32(0),
    applyEtThreshold = cms.bool(True),
    makeSpectraTreeEB = cms.untracked.bool(False),
    makeSpectraTreeEE = cms.untracked.bool(False)
)
