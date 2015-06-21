#! /usr/bin/env python


#
# Collection of functions for ic analysis
# Stefano Argiro', 2010
#
# $Id$


from EcalPyUtils import *
from array import array
from math import *
from ROOT import TGraph,TGraphErrors,TCanvas,TH1F,TH2D,TFile,TDirectory,TF1
from pluginCondDBPyInterface import *
from pluginEcalPyUtils import *

initialized=0
initializedTB=0
endcapringmap= {}
crystalphi = {}
eeareacorrection = {}

tbcrystals_EE= []

pi= acos(-1)
hashsizeEE=2*7324 +1

def excludedchannels():
    '''channels in bad TT or to be investigated '''

    bads=[]

    # a bad TT
    for phi in range(326,331):
       for eta in range (-85,-80) :
           bads.append((eta,phi))    

    # another bad TT
    for phi in range(61,66):
       for eta in range (-5,0) :
           bads.append((eta,phi))    
 
    return bads          

def im(ieta):
    '''Given ieta return module number'''
    kModuleBoundaries=[ 25, 45, 65, 85]
    for i,c in enumerate(kModuleBoundaries):
       if abs(ieta)<= c: return i;



def calculateBoundaryCorrectionEBP(differences) :
    """Calculate average correction factor for sm boundaries"""

    correction=[0. for i in range(4)]

    for m in range(4):
      for iphi,c in enumerate(differences[m]):
        if iphi==0 : continue
        if not iphi%20 :
            correction[m]= correction[m] + c

      correction[m] = correction[m]/18  
      

    return  correction

def calculateBoundaryCorrectionEBM(differences) :
    """Calculate average correction factor for sm boundaries"""

    correction=[0. for i in range(4)]

    for m in range(4):
      for iphi,c in enumerate(differences[m]):
        if iphi==0 : continue
        if  iphi%20 ==1 :
            correction[m]= correction[m] + c
      correction[m] = correction[m]/18   
      

    return  correction



def calculate10degCorrection(differences):
    """Calculate correction for SM rail at 10 degrees"""
    
    correction= [[0 for iphi in range(20)] for row in range(4) ]
    for m in range(4):
        correction[m]= differences[m][1:21]
    return correction


def calculate190degCorrection(differences):
    """Calculate correction for SM rail at 190 degrees"""
    
    correction= [[0 for iphi in range(20)] for row in range(4) ]
    for m in range(4):
        correction[m]= differences[m][181:201]
    return correction

def applycorrections(coefficients, differencesp, differencesm):

    c_i_prime = array("f",[ i for i in coefficients])
       
    boundarycorrp= calculateBoundaryCorrectionEBP(differencesp)
    boundarycorrm= calculateBoundaryCorrectionEBM(differencesm)
    corr10p     = calculate10degCorrection(differencesp)
    corr10m     = calculate10degCorrection(differencesm)
    corr190p     = calculate190degCorrection(differencesp)
    corr190m     = calculate190degCorrection(differencesm)


    print "boundary correction +", boundarycorrp
    print "boundary correction -", boundarycorrm

    print "10p",corr10p   
    print "10m",corr10m    
    print "190p",corr190p    
    print "190m",corr190m    

    #now apply correction
    for i,c_i in enumerate(coefficients):
          ieta,iphi= unhashEBIndex(i)
          m=im(ieta)
          if ieta>0 :
             if not iphi%20 :
                c_i_prime[i]= c_i - boundarycorrp[m]
             if iphi>0 and iphi < 21:
                 c_i_prime[i] = c_i - corr10p[m][iphi-1] 
             if iphi>180 and iphi < 201:
                 c_i_prime[i] = c_i - corr190p[m][iphi-181]
                
          else:
             if  iphi%20 ==1 :
                c_i_prime[i]= c_i - boundarycorrm[m] 
             if iphi>0 and iphi < 21:
                c_i_prime[i] = c_i - corr10m[m][iphi-1] 
             if iphi>180 and iphi < 201:
            
                 c_i_prime[i] = c_i - corr190m[m][iphi-181]
                 
          #if we could not derive a constant, dont bother correcting
          if c_i ==1.0 : c_i_prime[i] =1.0
          #if we could not derive a constant, dont bother correcting ---- MO metto -1
          #if c_i ==1.0 : c_i_prime[i] =-1.0
       
    return c_i_prime            




def calculatedifferences(c_i,c_i_p):
    '''calculate the average differences between  two sets, per module
       separately for plus and minus side'''

    differencesp = [[0.0 for col in range(361)] for row in range (4) ]
    differencesm = [[0.0 for col in range(361)] for row in range (4) ]


    rmssp        = [[0.0 for col in range(361)] for row in range (4) ]
    rmssm        = [[0.0 for col in range(361)] for row in range (4) ] 

 
    nm=20
    n1=25


    for i,c in enumerate(c_i):
        if c==0.0 : c=1.0
  
        diff = c*c_i_p[i]  - c_i_p[i]
        ieta,iphi= unhashEBIndex(i)
        
        n=nm
        if  not im(ieta)  : n=n1
        if ieta>0 :
            differencesp[im(ieta)][iphi] += diff/n
        else:
            differencesm[im(ieta)][iphi] += diff/n

         
    #we got differences, now rmss
    for i,c in enumerate(c_i):
        if c==0.0 : c=1.0
        diff = c*c_i_p[i]  - c_i_p[i]
        ieta,iphi= unhashEBIndex(i)
        #there's one high value there...
        #if  ieta==1 and iphi==160 :continue
        if ieta>0 :
            rmssp[im(ieta)][iphi] += pow(diff- differencesp[im(ieta)][iphi],2) 
  
        else:
            rmssm[im(ieta)][iphi] += pow(diff- differencesm[im(ieta)][iphi],2) 


    for m in range(4):
       for phi in range(361):
         n=nm
         if  m == 0 : n=n1        
         rmssp[m][phi] = sqrt(rmssp[m][phi]/n/(n-1))
         rmssm[m][phi] = sqrt(rmssm[m][phi]/n/(n-1))

         #iphi starts from 1, let's put [0] out of range   
         differencesp[m][0]=-100
         differencesm[m][0]=-100
         rmssp[m][0]=0
         rmssm[m][0]=0   


    return differencesp,rmssp,differencesm,rmssm


def precalibprecision(ieta):
    '''Precision of precalib c_i vs eta '''
    if ieta<50 :return 1.5 /100
    else :  return (1.5+ (ieta -50)* 0.02)/100


def istbsm(ieta,iphi):
    ''' Tells if we are in a TB SM or not'''
    #test beam modules #includes the 2004 tb
    # tbsm =[1,2,3,10,11,15,19,20,21,24] #includes the 2004 tb
    #test beam modules
    tbsm =[1,2,10,11,15,19,20,21,24]
    #bad cosmic test modules
    #tbsm =[5,8,9,12,13,14,16,17,22,29,31,32,33] 

    for i in tbsm:
       if ism(ieta,iphi) == i : return 1
    return 0

def istbsmnumber(sm):
      #test beam modules
    #tbsm =[1,2,3,10,11,15,19,20,21,24]
    tbsm =[1,2,10,11,15,19,20,21,24]
    
    for i in tbsm:
       if sm == i : return 1
    return 0


def plotspread(c_i,c_1,c_2,rfile,prefix,minbin,maxbin,nbin):
    '''Make an histo of coefficients in each ring and fit  '''

    dir=rfile.mkdir("spread"+prefix)    
    dir.cd()
    
    #array of precision vs eta
    precision      =[]
    precision_err  =[]

    meanIC1      =[]
    meanIC1_err  =[]

    meanIC2      =[]
    meanIC2_err  =[]

    meanICr      =[]
    meanICr_err  =[]

    # estimates from rms instead of gaussian fit
    precisionrms   =[]
    precisionrms_e =[]

    h1_all=TH1F(prefix+"IC1","IC1",120,0.8,1.4)
    h2_all=TH1F(prefix+"IC2","IC2",120,0.8,1.4)
    hr_all=TH1F(prefix+"ICRatio","ICRatio",100,0.9,1.1)

    for ieta in range(85):

        # histo of ic in that ring
        h=TH1F(prefix+"ieta"+repr(ieta),"ieta"+repr(ieta),nbin,minbin,maxbin)
        h1=TH1F(prefix+"IC1"+repr(ieta),"IC1"+repr(ieta),50,0.5,1.5)
        h2=TH1F(prefix+"IC2"+repr(ieta),"IC2"+repr(ieta),50,0.5,1.5)
        hr=TH1F(prefix+"ICratio"+repr(ieta),"ICratio"+repr(ieta),30,0.7,1.3)

        for iphi in range(360):

            hash= hashedIndex(ieta+1,iphi+1)
            c = c_i[hash]
            c1 = c_1[hash]
            c2 = c_2[hash]
	    h.Fill(c)
            h1.Fill(c1)
            h2.Fill(c2)
            hr.Fill(c2/c1)
            h1_all.Fill(c1)
            h2_all.Fill(c2)
            if c1!=1 and c2!=1: 
	       hr_all.Fill(c2/c1)
            
	    hash= hashedIndex(-1*(ieta+1),iphi+1)
            c = c_i[hash]
            c1 = c_1[hash]
            c2 = c_2[hash]
            h.Fill(c)
            h1.Fill(c1)
            h2.Fill(c2)
	    hr.Fill(c2/c1)
            h1_all.Fill(c1)
            h2_all.Fill(c2)
            if c1!=1 and c2!=1: 
               hr_all.Fill(c2/c1)

        h.Fit("gaus","Q")
        h.Write()
        h1.Fit("gaus","Q")
        h1.Write()
        h2.Fit("gaus","Q")
        h2.Write()
        hr.Fit("gaus","Q")
        hr.Write()


        sigma =h.GetFunction("gaus").GetParameter(2)
        sigmaerr= h.GetFunction("gaus").GetParError(2)
         
	mean1 = h1.GetFunction("gaus").GetParameter(1)
        meanerr1= h1.GetFunction("gaus").GetParError(1) 

	mean2 = h2.GetFunction("gaus").GetParameter(1)
        meanerr2= h2.GetFunction("gaus").GetParError(1) 
        
	mean_r = hr.GetFunction("gaus").GetParameter(1)
        meanerr_r= hr.GetFunction("gaus").GetParError(1) 

	rms     = h.GetRMS()
        rmserr  = rms/sqrt(2*h.GetEntries())

        precision.append(sigma*100)
        precision_err.append(sigmaerr*100)

        meanIC1.append(mean1)
        meanIC1_err.append(meanerr1)

        meanIC2.append(mean1)
        meanIC2_err.append(meanerr1)

        meanICr.append(mean_r)
        meanICr_err.append(meanerr_r)

        precisionrms.append(rms*100)
        precisionrms_e.append(rmserr*100)
                
        
 
    x = array('f',[i+1 for i in range(len(precision))])
    xe= array('f',[0 for i in range(len(precision))])
    y=  array('f',[i for i in precision])
    ye= array('f',[i for i in precision_err])

    rfile.cd()

    g= TGraphErrors (len(precision),x,y,xe,ye)
 
    g.SetName(prefix+"spreadvsring")
    g.SetTitle("spread vs ring")
    g.SetMarkerStyle(8)
    g.SetMarkerColor(2)
    g.Write()

    xm1 = array('f',[i+1 for i in range(len(meanIC1))])
    xme1= array('f',[0 for i in range(len(meanIC1))])
    ym1=  array('f',[i for i in meanIC1])
    yme1= array('f',[i for i in meanIC1_err])

    rfile.cd()

    mIC1= TGraphErrors (len(meanIC1),xm1,ym1,xme1,yme1)
 
    mIC1.SetName(prefix+"mean1vsring")
    mIC1.SetTitle("mean1 vs ring")
    mIC1.SetMarkerStyle(8)
    mIC1.SetMarkerColor(2)
    mIC1.Write()

    xm2 = array('f',[i+1 for i in range(len(meanIC2))])
    xme2= array('f',[0 for i in range(len(meanIC2))])
    ym2=  array('f',[i for i in meanIC2])
    yme2= array('f',[i for i in meanIC2_err])

    rfile.cd()

    mIC2= TGraphErrors (len(meanIC2),xm2,ym2,xme2,yme2)
 
    mIC2.SetName(prefix+"mean2vsring")
    mIC2.SetTitle("mean2 vs ring")
    mIC2.SetMarkerStyle(8)
    mIC2.SetMarkerColor(2)
    mIC2.Write()

    xmr = array('f',[i+1 for i in range(len(meanICr))])
    xmer= array('f',[0 for i in range(len(meanICr))])
    ymr=  array('f',[i for i in meanICr])
    ymer= array('f',[i for i in meanICr_err])

    rfile.cd()

    mICr= TGraphErrors (len(meanICr),xmr,ymr,xmer,ymer)
 
    mICr.SetName(prefix+"ratiovsring")
    mICr.SetTitle("ratio vs ring")
    mICr.SetMarkerStyle(8)
    mICr.SetMarkerColor(2)
    mICr.Write()


    yr =  array('f',[i for i in precisionrms])
    yre=  array('f',[i for i in precisionrms_e])

    grms = TGraphErrors (len(precision),x,yr,xe,yre)
    grms.SetName(prefix+"spreadrms")
    grms.SetTitle("")
    grms.SetMarkerStyle(8)
    grms.Write()    

    hr_all.Fit("gaus","Q")
    hr_all.Write()
    print "Ratio RMS  ",hr_all.GetRMS()," +/- ",hr_all.GetRMS()/sqrt(2*h.GetEntries())  
    print "Ratio sigma  ",hr_all.GetFunction("gaus").GetParameter(2)," +/- ",hr_all.GetFunction("gaus").GetParError(2)  

    #return graph of spread vs eta
    return g,mIC1,mIC2,mICr,h1_all,h2_all,hr_all 

def plotspreadEE(c_i,c_1,c_2,rfile,prefix,minbin,maxbin,nbin):
    '''Make an histo of coefficients in each ring and fit  '''

    dir=rfile.mkdir("spread"+prefix)    
    dir.cd()
    
    #array of precision vs eta
    precision      =[]
    precision_err  =[]

    meanIC1      =[]
    meanIC1_err  =[]

    meanIC2      =[]
    meanIC2_err  =[]

    meanICr      =[]
    meanICr_err  =[]

    # estimates from rms instead of gaussian fit
    precisionrms   =[]
    precisionrms_e =[]

    h1_all=TH1F(prefix+"EE_IC1","EE_IC1",120,0.8,1.4)
    h2_all=TH1F(prefix+"EE_IC2","EE_IC2",120,0.8,1.4)
    hr_all=TH1F(prefix+"EE_ICRatio","EE_ICRatio",100,0.9,1.1)

    for ring in range(39):
        # histo of ic in that ring
        h=TH1F(prefix+"ring"+repr(ring),"ring"+repr(ring),nbin,minbin,maxbin)
        h1=TH1F(prefix+"IC1"+repr(ring),"IC1"+repr(ring),100,0,2)
        h2=TH1F(prefix+"IC2"+repr(ring),"IC2"+repr(ring),100,0,2)
        hr=TH1F(prefix+"ICratio"+repr(ring),"ICratio"+repr(ring),30,0.7,1.3)

        for ix in range(100):
            for iy in range(100):
                for iz in [-1,1]:

                    if ring==endcapring(ix+1,iy+1,iz) :
                        idx = hashedIndexEE(ix+1,iy+1,iz)
                        c = c_i[idx]
                        c1= c_1[idx]
			c2= c_2[idx]
			h.Fill(c)
			h1.Fill(c1)
			h2.Fill(c2)
			hr.Fill(c2/c1)
                        h1_all.Fill(c1)
                        h2_all.Fill(c2)
                        if c1!=1 and c2!=1 and c1<1.2 and c1<1.2:
                              hr_all.Fill(c2/c1)
			      if c2/c1>1.19 and c2/c1<1.24: 
			          print "ratio 1.2 ", ix,iy,iz,c1,c2
                        else:
			    print  ix,iy,iz,c1,c2
        h.Fit("gaus","Q")
        h.Write()
        h1.Fit("gaus","Q")
	h1.Write()
	h2.Fit("gaus","Q")
	h2.Write()
	hr.Fit("gaus","Q")
	hr.Write()
	
	if ring > -1:
	#if ring <17 or ring>20:
	  sigma   = h.GetFunction("gaus").GetParameter(2)
          sigmaerr= h.GetFunction("gaus").GetParError(2)
        else:
	  sigma   = h.GetRMS()
          sigmaerr= sigma/sqrt(2*h.GetEntries())
	#if ring == 11:
	#  sigma   = h.GetRMS()
        #  sigmaerr= sigma/sqrt(2*h.GetEntries())

	mean1 = h1.GetFunction("gaus").GetParameter(1)
        meanerr1= h1.GetFunction("gaus").GetParError(1) 

	mean2 = h2.GetFunction("gaus").GetParameter(1)
        meanerr2= h2.GetFunction("gaus").GetParError(1) 
        
	mean_r = hr.GetFunction("gaus").GetParameter(1)
        meanerr_r= hr.GetFunction("gaus").GetParError(1) 
	
        rms     = h.GetRMS()
        rmserr  = rms/sqrt(2*h.GetEntries())

        precision.append(sigma*100)
        precision_err.append(sigmaerr*100)

        meanIC1.append(mean1)
        meanIC1_err.append(meanerr1)

        meanIC2.append(mean1)
        meanIC2_err.append(meanerr1)

        meanICr.append(mean_r)
        meanICr_err.append(meanerr_r)

        precisionrms.append(rms*100)
        precisionrms_e.append(rmserr*100)
                
        
 
    x = array('f',[i+1 for i in range(len(precision))])
    xe= array('f',[0 for i in range(len(precision))])
    y=  array('f',[i for i in precision])
    ye= array('f',[i for i in precision_err])

    rfile.cd()

    g= TGraphErrors (len(precision),x,y,xe,ye)
 
    g.SetName(prefix+"spreadvsring")
    g.SetTitle("spread vs ring")
    g.SetMarkerStyle(8)
    g.SetMarkerColor(2)
    g.Write()

    xm1 = array('f',[i+1 for i in range(len(meanIC1))])
    xme1= array('f',[0 for i in range(len(meanIC1))])
    ym1=  array('f',[i for i in meanIC1])
    yme1= array('f',[i for i in meanIC1_err])

    rfile.cd()

    mIC1= TGraphErrors (len(meanIC1),xm1,ym1,xme1,yme1)
 
    mIC1.SetName(prefix+"mean1vsring")
    mIC1.SetTitle("mean1 vs ring")
    mIC1.SetMarkerStyle(8)
    mIC1.SetMarkerColor(2)
    mIC1.Write()

    xm2 = array('f',[i+1 for i in range(len(meanIC2))])
    xme2= array('f',[0 for i in range(len(meanIC2))])
    ym2=  array('f',[i for i in meanIC2])
    yme2= array('f',[i for i in meanIC2_err])

    rfile.cd()

    mIC2= TGraphErrors (len(meanIC2),xm2,ym2,xme2,yme2)
 
    mIC2.SetName(prefix+"mean2vsring")
    mIC2.SetTitle("mean2 vs ring")
    mIC2.SetMarkerStyle(8)
    mIC2.SetMarkerColor(2)
    mIC2.Write()

    xmr = array('f',[i+1 for i in range(len(meanICr))])
    xmer= array('f',[0 for i in range(len(meanICr))])
    ymr=  array('f',[i for i in meanICr])
    ymer= array('f',[i for i in meanICr_err])

    rfile.cd()

    mICr= TGraphErrors (len(meanICr),xmr,ymr,xmer,ymer)
 
    mICr.SetName(prefix+"ratiovsring")
    mICr.SetTitle("ratio vs ring")
    mICr.SetMarkerStyle(8)
    mICr.SetMarkerColor(2)
    mICr.Write()


    yr =  array('f',[i for i in precisionrms])
    yre=  array('f',[i for i in precisionrms_e])

    grms = TGraphErrors (len(precision),x,yr,xe,yre)
    grms.SetName(prefix+"spreadrms")
    grms.SetTitle("")
    grms.SetMarkerStyle(8)
    grms.Write()    

    hr_all.Fit("gaus","Q")
    hr_all.Write()
    print "Ratio EE RMS  ",hr_all.GetRMS()," +/- ",hr_all.GetRMS()/sqrt(2*h.GetEntries())  
    print "Ratio EE sigma  ",hr_all.GetFunction("gaus").GetParameter(2)," +/- ",hr_all.GetFunction("gaus").GetParError(2)  

    #return graph of spread vs eta
    return g,mIC1,mIC2,mICr,h1_all,h2_all,hr_all 

def plotprecision(c_i, rfile,prefix):
    '''Make an histo of coefficients in each ring and fit, differentiating test beam SM from non testbeam SM '''

    dir=rfile.mkdir("precision"+prefix)    
    dir.cd()
    
    #array of precision vs eta
    precision      =[]
    precision_err  =[]

    precisiontb    =[]
    precisiontb_err=[]

    # estimates from rms instead of gaussian fit
    precisionrms   =[]
    precisionrms_e =[]

    precisionrmstb   =[]
    precisionrmstb_e =[]

    for ieta in range(85):

        # histo of ic in that ring
        h=TH1F(prefix+"ieta"+repr(ieta),"ieta"+repr(ieta),60,0.7,1.3)
        #same but only tb sm
        htb=TH1F(prefix+"tbieta"+repr(ieta),"tbieta"+repr(ieta),60,0.7,1.3)

        for iphi in range(360):


            hash= hashedIndex(ieta+1,iphi+1)
            c = c_i[hash]

            if istbsm(ieta+1,iphi+1):htb.Fill(c)
            #else: h.Fill(c)
            h.Fill(c)
            hash= hashedIndex(-1*(ieta+1),iphi+1)
            c = c_i[hash]

            if istbsm(-1*(ieta+1),iphi+1):htb.Fill(c)
            #else : h.Fill(c)
            h.Fill(c)
	    
        h.Fit("gaus","Q")
        h.Write()
        sigma   = h.GetFunction("gaus").GetParameter(2)
        sigmaerr= h.GetFunction("gaus").GetParError(2)

        rms     = h.GetRMS()
        rmserr  = rms/sqrt(2*h.GetEntries())

        precision.append(sigma*100)
        precision_err.append(sigmaerr*100)
        #print "**********ICp all xtal ",ieta,sigma,sigmaerr
        precisionrms.append(rms*100)
        precisionrms_e.append(rmserr*100)
                
 #       print "eta", ieta+1, " sigma " , sigma, sigmaerr

        htb.Fit("gaus","Q")
        htb.Write()
        sigma   = htb.GetFunction("gaus").GetParameter(2)
        sigmaerr= htb.GetFunction("gaus").GetParError(2)
        rms     = htb.GetRMS()
        rmserr  = rms/sqrt(2*htb.GetEntries())
        
        precisiontb.append(sigma*100)
        precisiontb_err.append(sigmaerr*100)
        #print "**********ICp tb xtal ",ieta,sigma,sigmaerr

        precisionrmstb.append(rms*100)
        precisionrmstb_e.append(rmserr*100)


    x = array('f',[i+1 for i in range(len(precision))])
    xe= array('f',[0 for i in range(len(precision))])
    y=  array('f',[i for i in precision])
    ye= array('f',[i for i in precision_err])

    rfile.cd()

    g= TGraphErrors (len(precision),x,y,xe,ye)
 
    g.SetName(prefix+"precvsring")
    g.SetTitle("precision vs ring")
    g.SetMarkerStyle(8)
    g.SetMarkerColor(2)
    g.Write()


    yy=  array('f',[i for i in precisiontb])
    yye= array('f',[i for i in precisiontb_err])


    gtb= TGraphErrors (len(precision),x,yy,xe,yye)

    gtb.SetName(prefix+"prectb")
    gtb.SetTitle("precisionvs ring (tb sm )")
    gtb.SetMarkerStyle(8)
    gtb.Write()    


    yr =  array('f',[i for i in precisionrms])
    yre=  array('f',[i for i in precisionrms_e])

    grms = TGraphErrors (len(precision),x,yr,xe,yre)
    grms.SetName(prefix+"precrms")
    grms.SetTitle("")
    grms.SetMarkerStyle(8)
    grms.Write()    


    yrtb =  array('f',[i for i in precisionrmstb])
    yrtbe=  array('f',[i for i in precisionrmstb_e])

    grmstb = TGraphErrors (len(precision),x,yrtb,xe,yrtbe)
    grmstb.SetName(prefix+"precrmstb")
    grmstb.SetTitle("")
    grmstb.SetMarkerStyle(8)
    grmstb.Write()    

    

    return  y,ye,yy,yye


def plotsmprecision(sm,c_i, rfile,prefix):
    '''Distribution of calibration constants for a particular SM '''

    dir=rfile.mkdir("SM"+repr(sm))
    dir.cd()

    h= TH1F(prefix+"SM"+repr(sm),prefix+"SM"+repr(sm),50,0.8,1.2)
    
    for i,c in enumerate(c_i):
       ieta,iphi=unhashEBIndex(i)

#use only eta < 45 !!       
       if ieta >45 : continue
       if ism(ieta,iphi) == sm : h.Fill(c)

    h.Fit("gaus","q")
    print "sm",sm," sigma", h.GetFunction("gaus").GetParameter(2), \
          "rms", h.GetRMS() 
    
    h.Write()
    return  h.GetFunction("gaus").GetParameter(2), \
            h.GetRMS() 


def smscale(c_i,rfile,prefix):

    smfile=open("smscale"+prefix+".txt","w")

    dir=rfile.mkdir("smscale"+prefix)  
    dir.cd()

    sm_c    =[]
    sm_cerr =[]
    smh =[]

    htb= TH1F(prefix+"tbsm",prefix+"tbsm",40,0.9,1.1 )
    htc= TH1F(prefix+"tbcos",prefix+"tbcos",40,0.9,1.1 )
    
    for i in range(36):
        smh.append(TH1F(prefix+"sm"+repr(i+1),prefix+"sm"+repr(i+1),40,0.6,1.4) )
    
    for i,c in enumerate(c_i):
        ieta,iphi=unhashEBIndex(i)
        sm=ism(ieta,iphi)
        smh[sm-1].Fill(c)

    for i in range(36):
        smh[i].Fit("gaus","q")
        smh[i].Write()
        mean=smh[i].GetFunction("gaus").GetParameter(1)
        sm_c.append(mean)
        sm_cerr.append(smh[i].GetFunction("gaus").GetParError(1))
        if istbsmnumber(i+1) : htb.Fill(mean)
        else :htc.Fill(mean)
   
    htb.Write()
    htc.Write()


     #sm scale distro for tb sm
    tbdistr= TH1F(prefix+"_smscaletb",prefix+"_smscaletb",20,0.95,1.05)
    for i in range(36):
        if istbsmnumber(i+1): tbdistr.Fill(sm_c[i])
    tbdistr.Write()

    rfile.cd()
        
    x  =array('f',[i+1 for i in range(len(sm_c)+1)])
    xe =array('f',[0 for i in range(len(sm_c)+1)])

    y = array('f',[i for i in sm_c])
    ye= array('f',[0.005 for i in range(len(x))])

#    print prefix,y
    
    g=TGraphErrors(len(x),x,y,xe,ye)
    g.SetMaximum(1.1)
    g.SetMinimum(0.9)
    g.SetTitle(prefix+"smsscale")
    g.SetName(prefix+"smsscale")
    g.Write()

   

    print >> smfile ,"SM  scale  stat  sys"
    for i in range(36):
       print >>smfile,"%2d %6.4f %6.4f %6.4f"% (i+1,sm_c[i], sm_cerr[i],0.005)
    
    return sm_c, sm_cerr

def calculatedifferencesfromfit(c_i,c_i_p):
    '''calculate the average differences between  two sets, per module
       separately for plus and minus side'''

   
    hhp=[]
    hhm=[]
    for m in range(4):
        hhhp=[]
        hhhm=[]
        for phi in range(360) :
            hip=TH1F("diffm_p"+repr(m)+"_"+repr(phi),
                     "diffm_p"+repr(m)+"_"+repr(phi),50,-.15,.15)
            him=TH1F("diffm_m"+repr(m)+"_"+repr(phi),
                     "diffm_m"+repr(m)+"_"+repr(phi),50,-.15,.15)
            
            hhhp.append(hip)
            hhhm.append(him)
            
        hhp.append(hhhp)    
        hhm.append(hhhm)
        
    for i,c in enumerate(c_i):
        if c==0.0 : c=1.0
  
        diff = c*c_i_p[i]  - c_i_p[i]
        ieta,iphi= unhashEBIndex(i)
        
        
        n=nm
        if  im(ieta) == 1 : n=n1
        if ieta>0 :
            hhp[im(ieta)][iphi-1].Fill(diff)
        else:
            hhm[im(ieta)][iphi-1].Fill(diff)
         
    #gaussian mean and difference     
    diffgp=[]
    diffgm=[]
    sigmap=[]
    sigmam=[]


    for m in range(4):
       for phi in range(361):
          
         #fit distributions
         if phi==0 :continue

         hhp[m][phi-1].Fit("gaus","Q") 
         hhm[m][phi-1].Fit("gaus","Q")
         
         
         hhp[m][phi-1].Write()
         hhm[m][phi-1].Write()
         
         mup= hhp[m][phi-1].GetFunction("gaus").GetParameter(1)
         mum= hhm[m][phi-1].GetFunction("gaus").GetParameter(1)
         sp= hhp[m][phi-1].GetFunction("gaus").GetParError(1)
         sm= hhm[m][phi-1].GetFunction("gaus").GetParError(1) 
         
         diffgp.append(mup)
         diffgm.append(mum)
         sigmap.append(sp)
         sigmam.append(sm)

    return diffgp,diffgm,sigmap,sigmam

def plotdifferences(diffp, diffm,rmsp,rmsm,diffpmc,diffmmc,prefix,rfile):
    """ Plot systematic effects"""
    
    dir=rfile.mkdir("differences"+prefix)  
    dir.cd()

    for m in range(4):

        x    = array('f',[i for i in range(len(diffp[m]))])
        xerr = array('f',[0 for i in range(len(x))])


        yp    = array('f',[i for i in diffp[m]])
        yperr = array('f',[i for i in rmsp[m]])

        ym    = array('f',[i for i in diffm[m]])
        ymerr = array('f',[i for i in rmsm[m]])


        g=TGraphErrors(361,x,yp,xerr,yperr)
        g.SetName("systematcs-EBP-m"+repr(m))
        g.SetTitle("")
        g.SetMinimum(-0.15)
        g.SetMaximum(0.15)
        g.Write()


        g=TGraphErrors(361,x,ym,xerr,yperr)
        g.SetName("systematcs-EBM-m"+repr(m))
        g.SetTitle("")
        g.SetMinimum(-0.15)
        g.SetMaximum(0.15)
        g.Write()


        #as a histo

        hgp= TH1F("system_mc_h-EBP-m"+repr(m),"system_mc_h-m"+repr(m),360,0.5,360.5)
        hgm= TH1F("system_mc_h-EBM-m"+repr(m),"system_mc_h-m"+repr(m),360,0.5,360.5)

        hgp.SetMinimum(-0.15)
        hgp.SetMaximum(0.15)

        hgm.SetMinimum(-0.15)
        hgm.SetMaximum(0.15)

        for i,x in enumerate(diffpmc[m]):
            if i==0:continue
            hgp.Fill(i,x)
            hgm.Fill(i,diffmmc[m][i])

        hgp.Write()
        hgm.Write()

    
def systbysm(diffp,diffm,prefix,rfile):
    """ Average syst differences over SMs"""

    dir =rfile.mkdir("smsyst-"+prefix)
    dir.cd()

    h=TH1F("smdiff","smdiff",20,-0.05,0.05)
    
    #systematic effects by SM
    smsyst  =[0. for i in range(36)]

    for i in range(18):
       x=0
       y=0

       for j in range(20):
          for m in range(4):  
             iphi=i*20+j+1
             x+= diffp[m][iphi]
             y+= diffm[m][iphi]
             
       h.Fill(x/20/4)
       h.Fill(y/20/4)

       smsyst[i]    =x/20/4
       smsyst[i+18] =y/20/4

    h.Write()

    x = array('f',[i+1 for i in range(36)])
    y = array('f',[i for i in smsyst])
    g= TGraph(36,x,y)
    g.SetName("smsyst-g")
    g.Write()


def isbadsm(sm):
   """true if believed to be badly precalibrated """

   badsm=[5,8,9,12,13,14,16,17,22,29,31,32,33]
   
   for i in badsm:
       if sm == i : return 1
   return 0


def endcapring(ix,iy,iz):
    """return ring to which the crystal belongs """
    
    global initialized
#    global endcapringmap
    
    if not initialized:
        f = open('endcaprings.dat')

        for line in f:
            id = int(line.split() [0])
            rn = int(line.split() [1])
            phi= float(line.split() [2])
            area = float(line.split() [3])
            endcapringmap[id]=rn
            crystalphi[id] = phi
            eeareacorrection[id]=area
         
#            print   unhashEEIndex(id), rn
            
        initialized=1

    hash=  hashedIndexEE(ix,iy,iz)

    if hash: return endcapringmap[hash]
    return 0


def areacorrection(ix,iy,iz):
    """Return area correction for EE crystals"""
    if not initialized: dummy = endcapring(1,1,1)

    hash=  hashedIndexEE(ix,iy,iz)
    if hash: return eeareacorrection[hash]
    
    return 999
    
def eecrystalphi(ix,iy,iz):
    """phi of crystal in rad """
    if not initialized: dummy = endcapring(1,1,1)

    hash=  hashedIndexEE(ix,iy,iz)
    if hash : return crystalphi[hash]
    return 999

def istbcrystalEE(ix,iy,iz):
    """ return true if the crystal was tested at TB"""
    
    global initializedTB
    
    if not initializedTB:
        file=open('TBcoeff.txt')
        for line in file:
            ix = int( line.split()[0])
            iy = int(line.split() [1])
            iz=-1
            tbcrystals_EE.append((ix,iy))
        initializedTB=1
        
    if iz== 1: return 0        
    if (ix,iy) in tbcrystals_EE : return 1

    return 0
            
def eeprecalibprecision(ring):


    if ring >=10 and ring <=25 : return 0.046
    return 0.049

def sector(ix,iy,iz):
    """Divide EE in 72 sectors of 5 deg and tell in which one we are [0,71]"""

    if eecrystalphi(ix,iy,iz) ==999  : return 999
    
    deg = ( eecrystalphi(ix,iy,iz)+ pi ) * 180/pi
    return int(deg/5)

def plotprecisionEE(c_i,rfile,prefix):
    '''same as plotprecision for EE '''
        
    dir=rfile.mkdir("precisionEE"+prefix)    
    dir.cd()
    h=[]
    a=[]
    
    precision=[]
    precision_err=[]
    areac=[]
    
    for ring in range(39):
        h.append(TH1F(prefix+"r"+repr(ring),prefix+"r"+repr(ring),\
                      50,0.5,1.5))
        a.append(TH1F("area_r"+repr(ring),"area_r"+repr(ring),\
                      50,0.8,1.2))
    
    for ix in range(100)  :
       for iy in range(100):
          for iz in [-1,1]:
	             
	     idx = hashedIndexEE(ix+1,iy+1,iz)
	     if idx>0: 
		ring= endcapring(ix+1,iy+1,iz)
                h[ring].Fill(c_i[idx])
                ix,iy,iz= unhashEEIndex(idx)
                a[ring].Fill(areacorrection(ix,iy,iz))
                #print "Ring ",ring," ",ix," ",iy," ",iz," ",c_i[idx]
    for ring in range(39):
#Le prossime 3 righe erano commentate
#        f=TF1("mygaus","gaus",0,2)
#        f.SetParLimits(1,1,1)
#        h[ring].Fit("mygaus","wq")        
        h[ring].Write()
#        a[ring].Fit("mygaus","q")
        a[ring].Write()
#        if ring > 0 and ring < 37  :
#        sigma    = h[ring].GetFunction("mygaus").GetParameter(2#)
#        sigmaerr=  h[ring].GetFunction("mygaus").GetParError(2)
#	   print "Ring ",ring," Sigma  ",sigma
#        sigma   = sqrt( pow(h[ring].GetRMS(),2) -.05*.05)

#        pprec= eeprecalibprecision(ring)
#        sigma   = sqrt (pow(h[ring].GetRMS(),2) - pprec*pprec)
#        else:
#mo21/3        sigma   = h[ring].GetRMS()
#mo21/3        sigmaerr= h[ring].GetRMS()/sqrt(2*h[ring].GetEntries())
#	   print "Ring ",ring," RMS  ",sigma
#mo21/3        print ring," ", sigma," ",sigmaerr
        sigma   = h[ring].GetRMS()
       # if ring<2: 
       #    sigma   = sqrt( pow(h[ring].GetRMS(),2) -.035*.035)
       # else: 
       #    sigma   = sqrt( pow(h[ring].GetRMS(),2) -.018*.018)
        sigmaerr= h[ring].GetRMS()/sqrt(2*h[ring].GetEntries())
	print "Ring ",ring," RMS  ",sigma,"  err  ",sigmaerr	    
	
	precision.append(sigma*100)
 #       precision.append(sqrt(sigma*sigma - .05*.05) * 100)
        precision_err.append(sigmaerr*100)

        ar=a[ring].GetRMS()
        areac.append(ar*100)

    x = array('f',[i+1 for i in range(len(precision))])
    xe= array('f',[0 for i in range(len(precision))])
    y=  array('f',[i for i in precision])
    ye= array('f',[i for i in precision_err])

    a = array('f',[i for i in areac])

    rfile.cd()

    g= TGraphErrors (len(precision),x,y,xe,ye)
 
    g.SetName(prefix+"precvsringEE")
    g.SetTitle("precision vs ring")
    g.SetMarkerStyle(8)
    g.SetMarkerColor(2)
    g.Write()     

    gg = TGraph(len(x),x,a)
    gg.SetName(prefix+"areacorrspread")
    gg.SetMarkerStyle(8)
    gg.Write()
    
    return  y,ye



def annulus(ix,iy,iz):
    
    if endcapring(ix,iy,iz) < 10 : return 0
    if endcapring(ix,iy,iz) < 20 : return 1
    if endcapring(ix,iy,iz) < 30 : return 2
    return 3

def calculatedifferencesEE(c_i,c_i_p):
    """calculate average differences in EE in 4 rings, 72 sectors """

    differencesp = [[0.0 for col in range(72)] for row in range (4) ]
    differencesm = [[0.0 for col in range(72)] for row in range (4) ]


    rmssp        = [[0.0 for col in range(72)] for row in range (4) ]
    rmssm        = [[0.0 for col in range(72)] for row in range (4) ] 



    for ann in range(4):
       for sec in range(72):
         n=0  
         for hash in range(hashsizeEE): 
           
            ix,iy,iz= unhashEEIndex(hash)

            if annulus(ix,iy,iz) == ann and sector(ix,iy,iz)==sec:
               n+=1  
               diff = c_i[hash] - c_i_p[hash]
               if iz>0 :differencesp[ann][sec]+=diff
               else    :differencesm[ann][sec]+=diff
             
         differencesp[ann][sec]/=n
         differencesm[ann][sec]/=n


    for ann in range(4):
       for sec in range(72):
         n=0  
         for hash in range(hashsizeEE): 
           
            ix,iy,iz= unhashEEIndex(hash)

            if annulus(ix,iy,iz) == ann and sector(ix,iy,iz)==sec:
               n+=1  
               diff = c_i[hash] - c_i_p[hash]
               if iz>0 :rmssp[ann][sec]+=pow(diff - differencesp[ann][sec],2)
               else    :rmssm[ann][sec]+=pow(diff - differencesp[ann][sec],2)
             
         rmssp[ann][sec] = sqrt(rmssp[ann][sec]/n/(n-1))
         rmssm[ann][sec] = sqrt(rmssp[ann][sec]/n/(n-1))

    return differencesp,rmssp,differencesm,rmssm


def calculatedifferencesEEallrings(c_i,c_i_p):
    """calculate average differences in EE in 39 rings, 72 sectors """

    
    differencesp = [[0.0 for col in range(72)] for row in range (39) ]
    differencesm = [[0.0 for col in range(72)] for row in range (39) ]


    rmssp        = [[0.0 for col in range(72)] for row in range (39) ]
    rmssm        = [[0.0 for col in range(72)] for row in range (39) ] 



    for rng in range(39):
       for sec in range(72):
         n=0  
         for hash in range(hashsizeEE): 
           
            ix,iy,iz= unhashEEIndex(hash)

            if endcapring(ix,iy,iz) == rng and sector(ix,iy,iz)==sec:
               n+=1  
               diff = c_i[hash] - c_i_p[hash]
               if iz>0 :differencesp[rng][sec]+=diff
               else    :differencesm[rng][sec]+=diff

         if n:    
            differencesp[rng][sec]/=n
            differencesm[rng][sec]/=n


    for rng in range(39):
       for sec in range(72):
         n=0  
         for hash in range(hashsizeEE): 
           
            ix,iy,iz= unhashEEIndex(hash)

            if endcapring(ix,iy,iz) == rng and sector(ix,iy,iz)==sec:
               n+=1  
               diff = c_i[hash] - c_i_p[hash]
               if iz>0 :rmssp[rng][sec]+=pow(diff - differencesp[rng][sec],2)
               else    :rmssm[rng][sec]+=pow(diff - differencesp[rng][sec],2)
         if n:    
            rmssp[rng][sec] = sqrt(rmssp[rng][sec]/n/(n-1))
            rmssm[rng][sec] = sqrt(rmssp[rng][sec]/n/(n-1))

    return differencesp,rmssp,differencesm,rmssm

def plotdifferencesEE(diffp,diffm,rmsp,rmsm,prefix,rfile):

    rfile.cd()

    for ann in range(len(diffp)):
        x    = array('f',[i for i in range(len(diffp[ann]))])
        xerr = array('f',[0 for i in range(len(x))])


        yp    = array('f',[i for i in diffp[ann]])
        yperr = array('f',[i for i in rmsp[ann]])

        ym    = array('f',[i for i in diffm[ann]])
        ymerr = array('f',[i for i in rmsm[ann]])


        g=TGraphErrors(len(diffp[ann]),x,yp,xerr,yperr)
        g.SetName(prefix+"systematics-EEP"+repr(ann))
        g.SetTitle("")
        g.SetMinimum(-0.15)
        g.SetMaximum(0.15)
        g.Write()


        g=TGraphErrors(len(diffp[ann]),x,ym,xerr,yperr)
        g.SetName(prefix+"systematics-EEM"+repr(ann))
        g.SetTitle("")
        g.SetMinimum(-0.15)
        g.SetMaximum(0.15)
        g.Write()


def eetbprecision(c_i,prefix,rfile):
    """estimate precision from tb crystals """

    rfile.cd()
    h=TH1F("eetbprecision","eetbprecision",60,0.7,1.3)
    hr=[]

    dir=rfile.mkdir("tbprecisionEE"+prefix)    
    dir.cd()

    for ring in range(39):
        hr.append(TH1F("tb_r"+repr(ring),"tb_r"+repr(ring),\
                      50,0.5,1.5))

    
    
    for ix in range(100)  :
       for iy in range(100):
        for iz in [-1,1]:
          idx = hashedIndexEE(ix+1,iy+1,iz)
          if idx:
#             if istbcrystalEE(ix+1,iy+1,-1):h.Fill(c_i[idx]*areacorrection(ix+1,iy+1,-1))
             if istbcrystalEE(ix+1,iy+1,iz):
                 h.Fill(c_i[idx])
                 ring = endcapring(ix+1,iy+1,iz)
                 hr[ring].Fill(c_i[idx])
                 
    h.Fit("gaus","q")          
    h.Write()             

    precision=[]
    precisione=[]
    for ring in range(39):
        
        if hr[ring].GetEntries()> 15:
            hr[ring].Fit("gaus","q")
            precision.append(hr[ring].GetRMS()*100)
            precisione.append(hr[ring].GetRMS()/sqrt(2*hr[ring].GetEntries())*100)
        else :
            precision.append(999)
            precisione.append(0)
            
        hr[ring].Write()

    x    = array('f',[i for i in range(len(precision))])
    xerr = array('f',[0 for i in range(len(x))])

    y    = array('f',[i for i in precision])
    yerr = array('f',[i for i in precisione])

    g=TGraphErrors(len(x),x,y,xerr,yerr)
    g.SetName("tbprecvsringEE")
    g.SetTitle("")
    g.SetMinimum(0)
    g.SetMaximum(10)
    g.Write()

def calc_ratio(c_1,c_2,rfile):
     histo_r= TH1F("IC Ratio","",100,0.95,1.05)
     
     c_ratio = [ 0.0 for i in range(len(c_1)) ]   
     for i in range(len(c_1)) :
      
       if c_1[i]!=0.0:   
          c_ratio[i] = c_2[i]/c_1[i] 
          #print "Ratio ",i, '  ', c_1[i] , "  " ,c_2[i] , "  ", c_ratio[i]	
	  if c_ratio[i]!=1.0:
	   #  ieta,iphi=unhashEBIndex(i)
	   #  if ieta>-45 and ieta<45:
	       histo_r.Fill(c_ratio[i])
	  else:       
	       ieta,iphi=unhashEBIndex(i)
	       print ieta,"  ",i,"  ",c_ratio[i]  
   #return 
     histo_r.Fit('gaus','q')
     histo_r.Write()
     return c_ratio,histo_r


def comparesets(c_1,c_2,prefix,rfile):
    """Compare two sets of constants, ring by ring and overall"""

    dir=rfile.mkdir(prefix+'-compare')
    dir.cd()
    map  = TH2D("diffmap","",360,1,360, 171, -85,86)
    histo= TH1F("differences","",50,-0.05,0.05)

    histo2 = TH2D("correlation",";c_{1};c_{2}",50,0.5,1.5,50,0.5,1.5)
    
    c_diff = [ c_1[i] - c_2[i] for i in range(len(c_1)) ]
    #c_diff = [ 1.0 for i in range(len(c_1)) ]
    #for i in range(len(c_diff)) :
    #   if c_diff[i]>0.049 or c_diff[i]<-0.049:
    #       c_diff[i] = c_1[i] - c_2[i]
     #  else:
     #      c_diff[i] = 1.0 
     #       print " const ",i, '  ', c_1[i] , "  " ,c_2[i] , "  " ,c_diff[i] 	
	    
    for i,diff in enumerate(c_diff) :
       ieta,iphi= unhashEBIndex(i)  
       #print "DIFF ", i, diff
       histo.Fill(diff)
       if c_1[i]!=1.0 and c_2[i]!=1.0:
       #if fabs(c_1[i]-1.0)>0.0000001 and fabs(c_2[i]-1.0)>0.0000001:
             map.Fill(iphi,ieta,diff)
       else:
          map.Fill(iphi,ieta,-1)
	  print "EB const =1 ",i, '  ', c_1[i] , "  " ,c_2[i]    
       #if diff>0.01 and diff<0.051:
       #     print "Cat 1 ",i,  '  ', ieta , "  " ,iphi,'  ', c_1[i] , "  " ,c_2[i] , "  " ,c_diff[i] 
       #if diff>0.05:
       #     print "Cat 2 ",i,  '  ', ieta , "  " ,iphi,'  ', c_1[i] , "  " ,c_2[i] , "  " ,c_diff[i] 
       #if diff>-0.05 and diff<-0.01:
       #     print "Cat 3 ",i,  '  ', ieta , "  " ,iphi,'  ', c_1[i] , "  " ,c_2[i] , "  " ,c_diff[i] 
       #if diff<-0.05:
       #     print "Cat 4 ",i,  '  ', ieta , "  " ,iphi,'  ', c_1[i] , "  " ,c_2[i] , "  " ,c_diff[i] 
       #print "Per me ",i, '  ', ieta , "  " ,iphi
    
    for i in range(len(c_1)) :
       histo2.Fill(c_1[i],c_2[i])

    histo.Fit('gaus','q')

    histo.Write()
    map.Write()
    histo2.Write()

    gspread,mIC1_b,mIC2_b,mICr_b,h1_all_b,h2_all_b,hr_all_b=plotspread(c_diff,c_1,c_2,rfile,prefix+"diff",-0.05,0.05,50)

    #return overall differences and differences vs eta
    return histo,map,gspread,mIC1_b,mIC2_b,mICr_b,histo2,h1_all_b,h2_all_b,hr_all_b

def comparesetsEE(c_1,c_2,prefix,rfile):
    """Compare two sets of constants, ring by ring and overall"""

    dir=rfile.mkdir(prefix+'-compare')
    dir.cd()
    mapp  = TH2D("diffmapEEp","",100,1,100, 100,1,100)
    mapm  = TH2D("diffmapEEm","",100,1,100, 100,1,100)
    histo= TH1F("differences","",50,-0.05,0.05)
    
    histo2 = TH2D("correlation",";c_{1};c_{2}",50,0.5,1.5,50,0.5,1.5)

    c_diff = [ c_1[i] - c_2[i] for i in range(len(c_1)) ]
   # c_diff = [ 1.0 for i in range(len(c_1)) ]
   # for i in range(len(c_1)) :
   #    if c_1[i]!=1.0 and c_2[i]!=1.0:
   #        c_diff[i] = c_1[i] - c_2[i]
    #   else:
     #      c_diff[i] = 1.0 
    #        print "EE const ",i, "  " , c_1[i] , "  " ,c_2[i] , "  " ,c_diff[i] 	


    for ix in range(100)  :
       for iy in range(100):
          for iz in [-1,1]:
             idx = hashedIndexEE(ix+1,iy+1,iz)
             print "Per me EE ",idx, "  " , ix , "  " ,iy , "  " ,iz
             if idx:
	        histo.Fill(c_diff[idx])
               # if c_diff[idx] >0.049 or c_diff[idx] <-0.049:
               #     if c_1[idx]!=1.0 and c_2[idx]!=1.0:
               #         print  "HighDiff  ", ix+1 , "  " ,iy+1 , "  " ,iz,"  ", c_diff[idx],"   ",c_1[idx],"   ",c_2[idx]
                if iz>0 :
                   if c_1[idx]!=1.0 and c_2[idx]!=1.0 :
		     mapp.Fill(ix,iy,c_diff[idx])
		     if c_diff[idx] >0.1 or c_diff[idx] <-0.1:                    
                        print  "HighDiff  ", ix+1 , "  " ,iy+1 , "  " ,iz,"  ", c_diff[idx],"   ",c_1[idx],"   ",c_2[idx]		   
		   else:
		     mapp.Fill(ix,iy,-1) 
		      
		  #if c_diff[idx]>0.01 and c_diff[idx]<0.051:
                  #     print "EE+Cat 1 ",i,  " ", ix , " " ,iy," ", c_1[i] , " " ,c_2[i] , " " ,c_diff[i] 
                  #if c_diff[idx]>0.05:
                  #     print "EE+Cat 3 ",i,  " ", ix , " " ,iy," ", c_1[i] , " " ,c_2[i] , " " ,c_diff[i] 
                  #if c_diff[idx]>-0.05 and c_diff[idx]<-0.01:
                  #     print "EE+Cat 2 ",i,  " ", ix , " " ,iy," ", c_1[i] , " " ,c_2[i] , " " ,c_diff[i] 
               #    if c_diff[idx]<-0.05:
               #        print "EE+Cat 4 ",i,  " ", ix , " " ,iy," ", c_1[i] , " " ,c_2[i] , " " ,c_diff[i] 
		if iz<0 :
#                  if fabs(c_1[i]-1.0)>0.0000001 and fabs(c_2[i]-1.0)>0.0000001:
                  if c_1[idx]!=1.0 and c_2[idx]!=1.0:
		      mapm.Fill(ix,iy,c_diff[idx])
		      if c_diff[idx] >0.10 or c_diff[idx] <-0.10:                    
                        print  "HighDiff  ", ix+1 , "  " ,iy+1 , "  " ,iz,"  ", c_diff[idx],"   ",c_1[idx],"   ",c_2[idx]
                  else:
		      mapm.Fill(ix,iy,-1) 
		  
		  #if c_diff[idx]>0.01 and c_diff[idx]<0.051:
                  #     print "EE-Cat 1 ",i,  " ", ix , " " ,iy," ", c_1[i] , " " ,c_2[i] , " " ,c_diff[i] 
                  #if c_diff[idx]>0.05:
                  #    print "EE-Cat 3 ",i,  " ", ix , " " ,iy," ", c_1[i] , " " ,c_2[i] , " " ,c_diff[i] 
                  #if c_diff[idx]>-0.05 and c_diff[idx]<-0.01:
                  #    print "EE-Cat 2 ",i,  " ", ix , " " ,iy," ", c_1[i] , " " ,c_2[i] , " " ,c_diff[i] 
         #         if c_diff[idx]<-0.05:
         #             print "EE-Cat 4 ",i,  " ", ix , " " ,iy," ", c_1[i] , " " ,c_2[i] , " " ,c_diff[i] 
             else:		  
 		  mapp.Fill(ix,iy,-1)
 		  mapm.Fill(ix,iy,-1)

    for i in range(len(c_1)) :
        histo2.Fill(c_1[i],c_2[i])


#########################################
#    for i,diff in enumerate(c_diff) :
#       ix,iy,iz = unhashEEIndex(i)  
# #      print "Const ", c_1[i]," ", ix," ", iy
#       histo.Fill(diff)
#       if diff == 0.0: diff=-100 
#       if iz>0 :
#           if hashedIndexEE(ix,iy,iz) :
#               mapp.Fill(ix,iy,diff)
# #              print "Const  ", ix," ", iy," ", c_1[i]
#       else:
#           if hashedIndexEE(ix,iy,iz) :
#               mapm.Fill(ix,iy,diff)       
###########################################

    histo.Fit('gaus','q')

    histo.Write()
    mapp.Write()
    mapm.Write()
    histo2.Write()

    gspread,mIC1_e,mIC2_e,mICr_e,h1_all_e,h2_all_e,hr_all_e=plotspreadEE(c_diff,c_1,c_2,rfile,prefix+"diff",-0.03,0.03,100)

    #return overall differences and differences vs eta
    #return histo,map,gspread
    return histo, mapp, mapm, gspread,mIC1_e,mIC2_e,mICr_e,histo2,h1_all_e,h2_all_e,hr_all_e


def readetsums(ebfilename,eefilename):
    """Read in etsums and fill arrays in the same order as ic's """

    etsums_b= [0 for i in range(61200)]
    etsums_e= [0 for i in range(20000)]
    nhits_b= [0 for i in range(61200)]
    nhits_e= [0 for i in range(20000)]

    

    ebfile=open(ebfilename)


    for line in ebfile :
       sline=line.split() 
       ieta= int(sline[0]) + 1
       iphi= int(sline[1]) + 1 
       side= int(sline[2])
       et  = float(sline[3])
       nhits  = float(sline[4])

       if not side : ieta = -1* ieta

       idx=hashedIndex(ieta,iphi)
       etsums_b[idx]= et
       nhits_b[idx]= nhits
       
    eefile=open(eefilename)


    for line in eefile :
       sline=line.split() 
       ix= int(sline[0]) + 1
       iy= int(sline[1]) + 1 
       zside= int(sline[2])
       et  = float(sline[3])
       nhits  = float(sline[4])

       if not zside : zside=-1

       idx=hashedIndexEE(ix,iy,zside)
       
       if idx: 
           etsums_e[idx]= et
           nhits_e[idx]= nhits
	   
    return etsums_b,etsums_e,nhits_b,nhits_e

def read_ck_etsums(ebfilename,eefilename,ebmfilename,eemfilename,c_b,c_e):

    """Read in etsums and fill arrays in the same order as ic's """

    etsums_b= [0 for i in range(61200)]
    etsums_e= [0 for i in range(20000)]
    etsumM_b= [0 for i in range(86)]
    etsumM_e= [0 for i in range(40)]


    ebfileM=open(ebmfilename)
             
    for line in ebfileM :
       sline=line.split()   
       ietam= int(sline[0]) + 1
       etm  = float(sline[1])
       #print "EtMean", ietam, etm,sline[2],sline[3] 
       etsumM_b[ietam]= etm

    ebfile=open(ebfilename)


    for line in ebfile :
       sline=line.split()
       ieta= int(sline[0]) + 1
       iphi= int(sline[1]) + 1
       side= int(sline[2])
       et  = float(sline[3])
       
       etm_t= etsumM_b[ieta] 
              
       if not side : ieta = -1* ieta

       idx=hashedIndex(ieta,iphi)
       etsums_b[idx]= et
       
       #if et<0.7*etm_t and c_b[idx] != 1 :
       if et<0.7*etm_t :
          print "Small Etsum", ieta, iphi, side, etm_t, et, c_b[idx]
	  c_b[idx] = -1
          print "Corr", ieta, iphi, c_b[idx]

       if et>1.3*etm_t and c_b[idx] != 1 :
          print "Big Etsum", ieta, iphi, side, etm_t, et, c_b[idx]
          c_b[idx] = -1
          print "Corr", ieta, iphi, c_b[idx]

    eefile=open(eefilename)


    for line in eefile :
       sline=line.split()
       ix= int(sline[0]) + 1
       iy= int(sline[1]) + 1
       zside= int(sline[2])
       et  = float(sline[3])

       if not zside : zside=-1

       idx=hashedIndexEE(ix,iy,zside)

       if idx: etsums_e[idx]= et

    return etsums_b,etsums_e


def normalize(array, normalization):
    """ Divide an array by normalization"""

    for i,x in enumerate(array):
        array[i]=x/normalization

def etsumvseta(etsums,nhits, rfile,prefix):
    """Plot average (on ring) etsum vs eta """
    mapets  = TH2D("EtSumMap","",360,1,360, 171, -85,86)
    mapnhits  = TH2D("NHitMap","",360,1,360, 171, -85,86)
    dir=rfile.mkdir(prefix+"-etsums")
    dir.cd()
    norm=0.0
    for ii in range(0,61199):
         norm+= etsums[ii]/61200.
    print "Norm ",norm
     
    average=[0 for i in range(85)]
    
    for ieta in range(1,86):
       for iphi in range(1,361):
          hash=hashedIndex(ieta,iphi)
          average[ieta-1]+= etsums[hash]/720.
	  mapets.Fill(iphi,ieta,etsums[hash]/norm)
	  mapnhits.Fill(iphi,ieta,nhits[hash])
          #print "Etsum ", ieta," ", iphi," ",hash,"  ",etsums[hash] 
	  if etsums[hash] > 200000.0:
	      print "Etsum ", ieta," ", iphi," ",etsums[hash] 
	  
	  hash=hashedIndex(-1*ieta,iphi)
          average[ieta-1]+= etsums[hash]/720.
          mapets.Fill(iphi,-1*ieta,etsums[hash]/norm)
          mapnhits.Fill(iphi,-1*ieta,nhits[hash])
          if etsums[hash] > 200000.0:
	      print "Etsum ", -1*ieta," ", iphi," ",etsums[hash] 
	  
	
    mapets.Write()
    	  
    x = array('f',[i+1 for i in range(len(average))])      
    y = array('f',[i for i in average])

    g=TGraph(len(average),x,y)      
    g.SetName("Norm. etsum")
    g.Write()      

    #return the TGraph
    return g,mapets,mapnhits



def etsumvsring(etsums,nhits,rfile,prefix):
    """Plot average (on ring) etsum vs ring (EE) """
#MO 4
    mapets_eep  = TH2D("EtSumMap EE+","",100,0,100, 100, 0,100)
    mapnhits_eep  = TH2D("NHitMap EE+","",100,0,100, 100, 0,100)
    mapets_eem  = TH2D("EtSumMap EE-","",100,0,100, 100, 0,100)
    mapnhits_eem  = TH2D("NHitMap EE-","",100,0,100, 100, 0,100)

    dir=rfile.mkdir(prefix+"-etsums_EE")
    dir.cd()
 
#MO 11
    normp=0.0
    normm=0.0
    normhp=0.0
    normhm=0.0
    cont=0
    for ix in range(100):
       for iy in range(100):
    	   idxp = hashedIndexEE(ix+1,iy+1,1)
    	   if idxp:
	      normp+= etsums[idxp]/7324.
	      normhp+= nhits[idxp]/7324.
     	   idxm = hashedIndexEE(ix+1,iy+1,-1)
    	   if idxm:
   	      normm+= etsums[idxm]/7324.
	      normhm+= nhits[idxm]/7324.
	      cont+=1
    print "EE+ Norm ",normp,"  EE- norm ",normm, " Cristalli ", cont   	   
    
    average=[0 for i in range(39)]
    ncells=[0 for i in range(39)]
    
    for ring in range(39):

        for ix in range(100):
            for iy in range(100):
                for iz in [-1,1]:

                    if ring==endcapring(ix+1,iy+1,iz) :
                        idx = hashedIndexEE(ix+1,iy+1,iz)
                        if idx:
                            average[ring]+= etsums[idx]
                            ncells[ring]+= 1.
	                    if iz>0:
			       mapets_eep.Fill(ix,iy,etsums[idx]/normp)
	                       mapnhits_eep.Fill(ix,iy,nhits[idx]/normhp)
	                    if iz<0:
			       mapets_eem.Fill(ix,iy,etsums[idx]/normm)
	                       mapnhits_eem.Fill(ix,iy,nhits[idx]/normhm)

        average[ring]/=ncells[ring]
        

    x = array('f',[i+1 for i in range(len(average))])      
    y = array('f',[i for i in average])

    g=TGraph(len(average),x,y)      
    g.SetName("Norm etsum EE")
    g.Write()      

    #return the TGraph
    return g,mapets_eep,mapnhits_eep,mapets_eem,mapnhits_eem

def ICmapEB(cb,prefix,rfile):
    """Draw IC map EB"""

    dir=rfile.mkdir(prefix+'-mapEB')
    dir.cd()
    map  = TH2D("ICmapEB","",360,1,360, 171, -85,86)
    
#    for i,ic in enumerate(cb) :
#       if ic[i]!=1.0:
#          ieta,iphi= unhashEBIndex(i)  
#          map.Fill(iphi,ieta,ic)
    for i in range(len(cb)) :
       if cb[i]!=1.0:
          ieta,iphi= unhashEBIndex(i)  
          map.Fill(iphi,ieta,cb[i])

    map.Write()

    return map


def ICmapEE(ce,prefix,rfile):
    """Draw IC map EB"""

    dir=rfile.mkdir(prefix+'-mapEE')
    dir.cd()
    mapp  = TH2D("ICmapEEp","",100,1,100, 100,1,100)
    mapm  = TH2D("ICmapEEm","",100,1,100, 100,1,100)
        
#    for i,ic in enumerate(ce) :
#       ix,iy,iz = unhashEEIndex(i)  
#       if iz>0 :
#           if hashedIndexEE(ix,iy,iz) :
#               mapp.Fill(ix,iy,ic)
#       else:
#           if hashedIndexEE(ix,iy,iz) :
#               mapm.Fill(ix,iy,ic)       
    for i  in range(len(ce)) :
       if ce[i]!=1.0:
          ix,iy,iz = unhashEEIndex(i)  
          if iz>0 :
              if hashedIndexEE(ix,iy,iz) :
                   mapp.Fill(ix,iy,ce[i])
          else:
              if hashedIndexEE(ix,iy,iz) :
                   mapm.Fill(ix,iy,ce[i])       

    mapp.Write()
    mapm.Write()

    return mapp, mapm

def writeprecisionEE(c_i):

    prfile=open("precisionEE_tmp.txt","w")    
    
    for ix in range(100)  :
       for iy in range(100):
          for iz in [-1,1]:
           
	     idx = hashedIndexEE(ix+1,iy+1,iz)
	     if idx>0:
	       ring= endcapring(ix+1,iy+1,iz)
               #if iz<0: iz=0
	       if ring<1: 
	     	 print >>prfile,"%2d %2d %2d %2d %5.3f"% (ring,ix+1,iy+1,iz,0.180)
               if ring>0 and ring<9: 
	     	 print >>prfile,"%2d %2d %2d %2d %5.3f"% (ring,ix+1,iy+1,iz,0.076)
	       if ring>8 and ring<17: 
	     	 print >>prfile,"%2d %2d %2d %2d %5.3f"% (ring,ix+1,iy+1,iz,0.035)
	       if ring>16 and ring<30: 
	     	 print >>prfile,"%2d %2d %2d %2d %5.3f"% (ring,ix+1,iy+1,iz,0.043)
	       if ring>29 and ring<37: 
	     	 print >>prfile,"%2d %2d %2d %2d %5.3f"% (ring,ix+1,iy+1,iz,0.060)
	       if ring>36: 
	     	 print >>prfile,"%2d %2d %2d %2d %5.3f"% (ring,ix+1,iy+1,iz,0.100)

    return 3



def IcEtaProfile(c_i):
    '''Make an histo of coefficients in each ring and fit, differentiating test beam SM from non testbeam SM '''

    print "IC Mean per ring in EB"
     
    for ieta in range(85):

        # histo of ic in that ring
        hp=TH1F("ietap"+repr(ieta),"ietap"+repr(ieta),60,0.4,2.5)
        hm=TH1F("ietam"+repr(ieta),"ietam"+repr(ieta),60,0.4,2.5)

        for iphi in range(360):


            hash= hashedIndex(ieta+1,iphi+1)
            c = c_i[hash]
            hp.Fill(c)
	    
            hash= hashedIndex(-1*(ieta+1),iphi+1)
            c = c_i[hash]            
            hm.Fill(c)
	    
        hp.Fit("gaus","Q")
        hp.Write()
        sigmap   = hp.GetFunction("gaus").GetParameter(1)
        sigmaerrp= hp.GetFunction("gaus").GetParError(1)
        meanp     = hp.GetMean()
        print ieta,sigmap,sigmaerrp,meanp

        hm.Fit("gaus","Q")
        hm.Write()
        sigmam   = hm.GetFunction("gaus").GetParameter(1)
        sigmaerrm = hm.GetFunction("gaus").GetParError(1)
        meanm     = hm.GetMean()
        print -ieta,sigmam,sigmaerrm,meanm
 
    
    return 3

def printsmnumber(c_i):
    '''Make an histo of coefficients in each ring and fit, differentiating test beam SM from non testbeam SM '''
    map_sm  = TH2D("ICmapSM","",360,1,360, 170, -85,85)

    prfile_p=open("SM_number_EBp_tmp.txt","w")    
    prfile_m=open("SM_number_EBm_tmp.txt","w")    

    for ieta in range(85):
        for iphi in range(360):

	    nsm_p = ism(ieta+1,iphi+1)
	    map_sm.Fill(iphi+1,ieta+1,nsm_p)

	    nsm_m = ism(-1*(ieta+1),iphi+1)         
	    map_sm.Fill(iphi+1,-1*(ieta+1),nsm_m)
	    
	    print >>prfile_p,"%2d %2d %2d"% (ieta+1,iphi+1,nsm_p)
	    print >>prfile_m,"%2d %2d %2d"% (-1*(ieta+1),iphi+1,nsm_m)

    return map_sm


#  LocalWords:  usr
