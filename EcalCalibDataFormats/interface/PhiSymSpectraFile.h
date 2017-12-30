#ifndef PHISYMFILE_H
#define PHISYMFILE_H

#include <string>
#include <vector>

#include "TFile.h"
#include "TTree.h"

#include "ExternalTools/DynamicTTree/interface/DynamicTTreeBase.h"

using namespace std;

//**********EB TREE***********************************************************************

#define DYNAMIC_TREE_NAME EBTree
//---create branches
#define DATA_TABLE                              \
    DATA(unsigned int, run)                     \
    DATA(unsigned int, lumi)                    \
    DATA(int, ieta)                             \
    DATA(int, iphi)                             \
    DATA(float, et)                                

#include "ExternalTools/DynamicTTree/interface/DynamicTTreeInterface.h"

//**********EE TREE***********************************************************************

#define DYNAMIC_TREE_NAME EETree
//---create branches
#define DATA_TABLE                             \
    DATA(unsigned int, run)                    \
    DATA(unsigned int, lumi)                   \
    DATA(int, iring)                           \
    DATA(int, ix)                              \
    DATA(int, iy)                              \
    DATA(float, et)                                

#include "ExternalTools/DynamicTTree/interface/DynamicTTreeInterface.h"
    
#endif 
