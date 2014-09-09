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

cd EcalCalibAlgos/test/

eg: ./SubmitPhisym_2012.sh 206539 206542 2012D FT_R_70_V1::All caf
eg: ./RunPhisymStep2_2012.sh 206539 206542 2012D FT_R_70_V1::All caf // run only the step2
