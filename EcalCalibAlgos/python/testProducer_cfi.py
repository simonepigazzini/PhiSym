import FWCore.ParameterSet.Config as cms

testProducer = cms.EDProducer("testProducer",
            barrelHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB', 'PHISYM'),
            endcapHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEE', 'PHISYM'),
            eCut_barrel = cms.double(0.550),
)
