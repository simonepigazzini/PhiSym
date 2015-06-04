#ifndef DATAFORMAT_PHISYMINFO_H
#define DATAFORMAT_PHISYMINFO_H

#include <vector>

#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/Provenance/interface/LuminosityBlockID.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"


//****************************************************************************************

class PhiSymInfo
{
public:
    //---ctors---
    PhiSymInfo();
    
    //---dtor---
    ~PhiSymInfo();

    //---set------
    void            setStartLumi(edm::LuminosityBlock const& lumi);
    void            setEndLumi(edm::LuminosityBlock const& lumi);

    //---getters---
    inline uint64_t GetTotHitsEB()  const {return totHitsEB_;};
    inline uint64_t GetTotHitsEE()  const {return totHitsEE_;};
    inline uint32_t GetNEvents()    const {return nEvents_;};
    float           GetMean(char k)      const;
    float           GetMeanSigma(char k) const;
    inline edm::LuminosityBlockID getStartLumi() const { return startLumi_; };
    inline edm::LuminosityBlockID getEndLumi() const { return endLumi_; };

    //---utils---
    void            Update(const reco::BeamSpot* bs, uint64_t& nEB, uint64_t& nEE);


    //---operators---
    friend std::ostream& operator<<(std::ostream& out, const PhiSymInfo& obj);

private:
    edm::LuminosityBlockID startLumi_;
    edm::LuminosityBlockID endLumi_;

    uint64_t totHitsEB_;
    uint64_t totHitsEE_;
    uint32_t nEvents_;
    
    float    meanX_;
    float    meanSigmaX_;
    float    meanY_;
    float    meanSigmaY_;
    float    meanZ_;
    float    meanSigmaZ_;
};

typedef std::vector<PhiSymInfo> PhiSymInfoCollection;

#endif
