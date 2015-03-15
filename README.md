PhiSym
===========

cmsrel CMSSW_X_Y_Z
cd CMSSW_X_Y_Z/src/
cmsenv
git clone https://github.com/ECALELFS/PhiSym
scramv1 b distclean
scramv1 b -j 8

How to run
===========

Data2012:
eg: ./SubmitPhisym_2012.sh 206539 206542 2012D FT_R_70_V1::All caf
eg: ./RunPhisymStep2_2012.sh 206539 206542 2012D FT_R_70_V1::All caf // run only the step2

MC:
eg: ./SubmitPhisym_MC.sh /Neutrino_Pt-2to20_gun/Fall13dr-tsg_PU40bx50_POSTLS162_V1-v1/GEN-SIM-RAW POSTLS162_V1 crab3
eg: ./RunPhisymStep2_MC.sh /Neutrino_Pt-2to20_gun/Fall13dr-tsg_PU40bx50_POSTLS162_V1-v1/GEN-SIM-RAW POSTLS162_V1 crab3 // run only the step2
