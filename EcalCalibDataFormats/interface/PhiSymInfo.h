#ifndef DATAFORMAT_PHISYMINFO_H
#define DATAFORMAT_PHISYMINFO_H

#include <vector>

#include "DataFormats/BeamSpot/interface/BeamSpot.h"

//****************************************************************************************

class PhiSymInfo
{
public:
    //---ctors---
    PhiSymInfo();
    
    //---dtor---
    ~PhiSymInfo();

    //---getters---
    inline uint64_t GetTotHitsEB()  const {return totHitsEB_;};
    inline uint64_t GetTotHitsEE()  const {return totHitsEE_;};
    inline uint32_t GetNEvents()    const {return nEvents_;};
    float           GetMean(char k)      const;
    float           GetMeanSigma(char k) const;

    //---utils---
    void            Update(const reco::BeamSpot* bs, uint64_t& nEB, uint64_t& nEE);

    //---operators---
    friend std::ostream& operator<<(std::ostream& out, const PhiSymInfo& obj);

private:

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
