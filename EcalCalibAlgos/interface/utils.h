#ifndef _UTILS_H_
#define _UTILS_H_

namespace PhiSym
{   
//----------compute std::vector averages in a selected range------------------------------
    pair<float, float> VectorMeanRMS(vector<float>& data, int low, int high)
    {
        float sum=0;
        float sum2=0;
        int n=0;
        for(int i=low; i<high; ++i)
        {
            sum += data[i];
            sum2 += data[i]*data[i];
            ++n;
        }

        return make_pair(sum/n, sqrt((sum2/n - sum*sum/(n*n))/n));
    }

//----------compute std::vector outliers iterative removal--------------------------------
    pair<float, float> IterativeCut(vector<float>& data, int low, int high, double eps)
    {
        if(low >= high)
            return make_pair(-1, -1);
    
        pair<float, float> current = VectorMeanRMS(data, low, high);
        if(fabs(current.first - VectorMeanRMS(data, low+1, high-1).first) < eps)
            return current;
        else 
            return IterativeCut(data, low+1, high-1, eps);
    }
}
    
#endif
