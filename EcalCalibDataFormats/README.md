PhiSymRecHit
============

+ the class has only one setter:
'''
PhiSymRecHit::AddHit(float* etValues, float lc)
'''

etValues must be an array of 5 elements. the 0-th element is considered as the central value, so
nHits_ (the number of times the channel has recorded a signal) is incremented if and only if etValues[0] > 0.


