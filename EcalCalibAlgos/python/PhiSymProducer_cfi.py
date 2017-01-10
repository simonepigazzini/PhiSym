import FWCore.ParameterSet.Config as cms

# - thrEEmod is the value in ADC count that rappresent the "5 sigma noise" threshold 
# - A*ring + B is a ad-hoc parametrization of the equivalent noise level, in this way the thr is set in MeV

PhiSymProducer = cms.EDProducer(
    "PhiSymProducer",
    barrelHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB', 'PHISYM'),
    endcapHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEE', 'PHISYM'),
    beamspot = cms.InputTag('offlineBeamSpot'),
    eThreshold_barrel = cms.double(10*1.75*0.04),    
    etCut_barrel = cms.double(1), #this is actually summed to eThr in order to define the upper bound    
    etCut_endcap = cms.double(1), #this is actually summed to eThr in order to define the upper bound    
    A = cms.vdouble(10, 112.5), # B + A*ring 2016 thr are defined as two linear cut (one for iring<30 and one above)
    B = cms.vdouble(150, -2925),
    thrEEmod = cms.double(10.),
    nMisCalib = cms.int32(10), # <= 10; even; central value does not count
    misCalibRangeEB = cms.vdouble(0.95, 1.05),
    misCalibRangeEE = cms.vdouble(0.90, 1.10),
    lumisToSum = cms.int32(1),          
    statusThreshold = cms.int32(0),
    makeSpectraTreeEB = cms.untracked.bool(False),
    makeSpectraTreeEE = cms.untracked.bool(False)
)
