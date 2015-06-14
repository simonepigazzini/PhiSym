#include "PhiSym/EcalCalibDataFormats/interface/PhiSymInfo.h"

//**********constructors******************************************************************
PhiSymInfo::PhiSymInfo():
    totHitsEB_(0), totHitsEE_(0), nEvents_(0),
    meanX_(0), meanSigmaX_(0), meanY_(0), meanSigmaY_(0), meanZ_(0), meanSigmaZ_(0)
{}

//**********destructor********************************************************************
PhiSymInfo::~PhiSymInfo()
{}

//**********getters***********************************************************************
float PhiSymInfo::GetMean(char k) const
{
    if(k == 'X')
        return meanX_;
    if(k == 'Y')
        return meanY_;
    if(k == 'Z')
        return meanZ_;

    return -999;
}

float PhiSymInfo::GetMeanSigma(char k) const
{
    if(k == 'X')
        return meanSigmaX_;
    if(k == 'Y')
        return meanSigmaY_;
    if(k == 'Z')
        return meanSigmaZ_;

    return -999;
}

void PhiSymInfo::SetStartLumi(edm::LuminosityBlock const& lumi)
{
  startLumi_=lumi.luminosityBlockAuxiliary().id();
}

void PhiSymInfo::SetEndLumi(edm::LuminosityBlock const& lumi)
{
  endLumi_=lumi.luminosityBlockAuxiliary().id();
}
//**********utils*************************************************************************
void PhiSymInfo::Update(const reco::BeamSpot* bs, uint64_t& nEB, uint64_t& nEE)
{
    meanX_ = (meanX_*nEvents_ + bs->x0())/(nEvents_+1);
    meanY_ = (meanY_*nEvents_ + bs->y0())/(nEvents_+1);
    meanZ_ = (meanZ_*nEvents_ + bs->z0())/(nEvents_+1);

    meanSigmaX_ = (meanSigmaX_*nEvents_ + bs->BeamWidthX())/(nEvents_+1);
    meanSigmaY_ = (meanSigmaY_*nEvents_ + bs->BeamWidthY())/(nEvents_+1);
    meanSigmaZ_ = (meanSigmaZ_*nEvents_ + bs->sigmaZ())/(nEvents_+1);

    totHitsEB_ += nEB;
    totHitsEE_ += nEE;

    nEvents_++;
}

//**********operators*********************************************************************

std::ostream& operator<<(std::ostream& out, const PhiSymInfo& obj)
{
    //---dump all the informations
    out << std::endl;
    out << std::setw(20) << "# event: " << obj.GetNEvents() << std::endl;
    out << std::setw(20) << "hits EB: " << obj.GetTotHitsEB() << std::endl;
    out << std::setw(20) << "hits EE: " << obj.GetTotHitsEE() << std::endl;
    out << std::setw(20) << "X: mean | meanSigma: " << obj.GetMean('X') << " | " << obj.GetMeanSigma('X') <<std::endl;
    out << std::setw(20) << "Y: mean | meanSigma: " << obj.GetMean('Y') << " | " << obj.GetMeanSigma('Y') <<std::endl;
    out << std::setw(20) << "Z: mean | meanSigma: " << obj.GetMean('Z') << " | " << obj.GetMeanSigma('Z') <<std::endl;
    out << std::endl;
    
    return out;
}

    


