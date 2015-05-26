import FWCore.ParameterSet.Config as cms

testProducer = cms.EDProducer("testProducer",
            barrelHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB', 'PHISYM'),
            endcapHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEE', 'PHISYM'),
            eCut_barrel = cms.double(0.550),
            nMisCalib = cms.int32(5), # fixed
            misCalibValues = cms.vdouble(1, 0.975, 0.95, 1.025, 1.05),
            lumisToSum = cms.int32(2)
)
