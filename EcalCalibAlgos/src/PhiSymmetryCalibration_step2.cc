#include "PhiSym/EcalCalibAlgos/interface/PhiSymmetryCalibration_step2.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "CondFormats/EcalObjects/interface/EcalIntercalibConstants.h"
#include "CondTools/Ecal/interface/EcalIntercalibConstantsXMLTranslator.h"
#include "CondFormats/DataRecord/interface/EcalIntercalibConstantsRcd.h"
#include "CondFormats/DataRecord/interface/EcalChannelStatusRcd.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "TH2F.h"

#include "TH1F.h"
#include "TF1.h"

#include "TFile.h"

#include <fstream>
#include "boost/filesystem/operations.hpp"

#include "FWCore/Framework/interface/MakerMacros.h"

using namespace std;




PhiSymmetryCalibration_step2::~PhiSymmetryCalibration_step2(){}


PhiSymmetryCalibration_step2::PhiSymmetryCalibration_step2(const edm::ParameterSet& iConfig){

  statusThreshold_ =
       iConfig.getUntrackedParameter<int>("statusThreshold",0);
  have_initial_miscalib_=
       iConfig.getUntrackedParameter<bool>("haveInitialMiscalib",false);
  initialmiscalibfile_=
    iConfig.getUntrackedParameter<std::string>("initialmiscalibfile",
					       "InitialMiscalib.xml"); 
  oldcalibfile_=
    iConfig.getUntrackedParameter<std::string>("oldcalibfile",
					       "EcalIntercalibConstants.xml");
  reiteration_ = iConfig.getUntrackedParameter<bool>("reiteration",false);
  firstpass_=true;
}

void PhiSymmetryCalibration_step2::analyze( const edm::Event& ev, 
					    const edm::EventSetup& se){

  if (firstpass_) {
    setUp(se);
    firstpass_=false;    
  }
}






void PhiSymmetryCalibration_step2::setUp(const edm::EventSetup& se){

  edm::ESHandle<EcalChannelStatus> chStatus;
  se.get<EcalChannelStatusRcd>().get(chStatus);

  edm::ESHandle<CaloGeometry> geoHandle;
  se.get<CaloGeometryRecord>().get(geoHandle);

  barrelCells = geoHandle->getValidDetIds(DetId::Ecal, EcalBarrel);
  endcapCells = geoHandle->getValidDetIds(DetId::Ecal, EcalEndcap);

  e_.setup(&(*geoHandle), &(*chStatus), statusThreshold_);

  /// if a miscalibration was applied, load it, if not put it to 1                                                                                                                                                                                                                                                                                                                                                                                                  
  if (have_initial_miscalib_){

    EcalCondHeader h;
    namespace fs = boost::filesystem;
    //    fs::path p(initialmiscalibfile_.c_str(),fs::native);                                                                                                                                                                                                                                                                                                                                                                                                          
    fs::path p(initialmiscalibfile_.c_str());
    if (!fs::exists(p)) edm::LogError("PhiSym") << "File not found: "
                                                << initialmiscalibfile_ <<endl;

    int ret=
      EcalIntercalibConstantsXMLTranslator::readXML(initialmiscalibfile_,h,miscalib_);
    if (ret) edm::LogError("PhiSym")<<"Error reading XML files"<<endl;;
  } else {

    for (vector<DetId>::iterator it=barrelCells.begin(); it!=barrelCells.end(); ++it){
      miscalib_[*it]=1;
    }

    for (vector<DetId>::iterator it=endcapCells.begin(); it!=endcapCells.end(); ++it){
      miscalib_[*it]=1;

    }
  }

  // if we are reiterating, read constants from previous iter                                                                                                                                                                                                                                                                                                                                                                                                       
  // if not put them to one                                                                                                                                                                                                                                                                                                                                                                                                                                         
  if (reiteration_){


    EcalCondHeader h;
    namespace fs = boost::filesystem;
    //fs::path p(oldcalibfile_.c_str(),fs::native);                                                                                                                                                                                                                                                                                                                                                                                                                 
    fs::path p(oldcalibfile_.c_str());
    if (!fs::exists(p)) edm::LogError("PhiSym") << "File not found: "
                                                << oldcalibfile_ <<endl;

    int ret=
      EcalIntercalibConstantsXMLTranslator::readXML(oldcalibfile_,h,
                                                    oldCalibs_);

    if (ret) edm::LogError("PhiSym")<<"Error reading XML files"<<endl;;

  } else {

    for (vector<DetId>::iterator it=barrelCells.begin();
         it!=barrelCells.end(); ++it)
      oldCalibs_[*it]=1;


    for (vector<DetId>::iterator it=endcapCells.begin();
         it!=endcapCells.end(); ++it)
      oldCalibs_[*it]=1;


  } // else                                                                                                                                                                                                                                                                                                                                        

}


void PhiSymmetryCalibration_step2::beginJob(){
  

  for (int ieta=0; ieta<kBarlRings; ieta++) {
    for (int iphi=0; iphi<kBarlWedges; iphi++) {
      for (int sign=0; sign<kSides; sign++) {
	etsum_barl_[ieta][iphi][sign]=0.;
	nhits_barl_[ieta][iphi][sign]=0;
	esum_barl_[ieta][iphi][sign]=0.;
	  
      }
    }
  }

  for (int ix=0; ix<kEndcWedgesX; ix++) {
    for (int iy=0; iy<kEndcWedgesY; iy++) {
      for (int sign=0; sign<kSides; sign++) {
	etsum_endc_[ix][iy][sign]=0.;
	nhits_endc_[ix][iy][sign]=0;
	esum_endc_[ix][iy][sign]=0.;

      }
    }
  }

  readEtSums();
  setupResidHistos();
}

void PhiSymmetryCalibration_step2::endJob(){

  if (firstpass_) {
    edm::LogError("PhiSym")<< "Must process at least one event-Exiting" <<endl;
    return;
      
  }

  // Here the real calculation of constants happens

  // perform the area correction for endcap etsum
  // NOT  USED  ANYMORE

  
  for (int ix=0; ix<kEndcWedgesX; ix++) {
    for (int iy=0; iy<kEndcWedgesY; iy++) {

      int ring = e_.endcapRing_[ix][iy];

      if (ring!=-1) {
	for (int sign=0; sign<kSides; sign++) {
	  etsum_endc_uncorr[ix][iy][sign] = etsum_endc_[ix][iy][sign];
	  etsum_endc_[ix][iy][sign]*=e_.meanCellArea_[ring]/e_.cellArea_[ix][iy];
	}
      }
    }
  }
  

  // ETsum histos, maps and other usefull histos (area,...)
  // are filled and saved here
  fillHistos();

  // write ETsum mean for all rings
  std::ofstream etsumMean_barl_out("etsumMean_barl.dat",ios::out);
  for (int ieta=0; ieta<kBarlRings; ieta++) {
    etsumMean_barl_out << ieta << " " << etsumMean_barl_[ieta][0] << " " << etsumMean_barl_[ieta][1] << endl;
  }
  etsumMean_barl_out.close();

  std::ofstream etsumMean_endc_out("etsumMean_endc.dat",ios::out);
  for (int ring=0; ring<kEndcEtaRings; ring++) {
    etsumMean_endc_out << e_.cellPos_[ring][50].eta() << " " << etsumMean_endc_[ring][0] << " " << etsumMean_endc_[ring][1] << endl;
  }
  etsumMean_endc_out.close();
  

  // determine barrel calibration constants
  for (int ieta=0; ieta<kBarlRings; ieta++) {
    for (int iphi=0; iphi<kBarlWedges; iphi++) {
      for (int sign=0; sign<kSides; sign++) {
	if(e_.goodCell_barl[ieta][iphi][sign]){
	  float etsum = etsum_barl_[ieta][iphi][sign];
	  float epsilon_T = (etsum/etsumMean_barl_[ieta][sign]) - 1.;
	  rawconst_barl[ieta][iphi][sign]  = epsilon_T + 1.;
	  epsilon_M_barl[ieta][iphi][sign] = epsilon_T/k_barl_[ieta][sign];
	} else {
	  rawconst_barl[ieta][iphi][sign]  = 1.;
	  epsilon_M_barl[ieta][iphi][sign] = 0.;
	} //if
      } //sign
    } //iphi
  } //ieta

    // determine endcap calibration constants
  for (int ix=0; ix<kEndcWedgesX; ix++) {
    for (int iy=0; iy<kEndcWedgesY; iy++) {
      for (int sign=0; sign<kSides; sign++) {
	int ring = e_.endcapRing_[ix][iy];
	if (ring!=-1 && e_.goodCell_endc[ix][iy][sign]) {
	  float etsum = etsum_endc_[ix][iy][sign];
	  float epsilon_T = (etsum/etsumMean_endc_[ring][sign]) - 1.;
	  rawconst_endc[ix][iy][sign]  = epsilon_T + 1.;
	  epsilon_M_endc[ix][iy][sign] = epsilon_T/k_endc_[ring][sign];	    
	} else {
	  epsilon_M_endc[ix][iy][sign] = 0.;
	  rawconst_endc[ix][iy][sign]  = 1.;
	} //if
      } //sign
    } //iy
  } //ix



  std::string newcalibfile("EcalIntercalibConstants_new.xml");



  TFile ehistof("ehistos.root","recreate");  

  TH1D ebhisto("eb","eb",100, 0.,2.);

  std::vector<DetId>::const_iterator barrelIt=barrelCells.begin();
  for (; barrelIt!=barrelCells.end(); barrelIt++) {
    EBDetId eb(*barrelIt);
    int ieta = abs(eb.ieta())-1;
    int iphi = eb.iphi()-1;
    int sign = eb.zside()>0 ? 1 : 0;

    /// this is the new constant, or better, the correction to be applied
    /// to the old constant (EB)
    if(e_.goodCell_barl[ieta][iphi][sign]){
      newCalibs_[eb] =  oldCalibs_[eb]/(1+epsilon_M_barl[ieta][iphi][sign]);

      ebhisto.Fill(newCalibs_[eb]);
      
      // residual miscalibraition  / expected precision
      int index_b = ieta+sign*kBarlRings;
      miscal_resid_barl_histos[index_b]->Fill(miscalib_[eb]*newCalibs_[eb]);
      correl_barl_histos[index_b]->Fill(miscalib_[eb],newCalibs_[eb]);	
    }
    else
      newCalibs_[eb] = 1.0;
      
  }// barrelit

  TH1D eehisto("ee","ee",100, 0.,2.);
  std::vector<DetId>::const_iterator endcapIt=endcapCells.begin();

  for (; endcapIt!=endcapCells.end(); endcapIt++) {
    EEDetId ee(*endcapIt);
    int ix = ee.ix()-1;
    int iy = ee.iy()-1;
    int sign = ee.zside()>0 ? 1 : 0;
            
      
    /// this is the new constant, or better, the correction to be applied
    /// to the old constant (EB)
    if(e_.goodCell_endc[ix][iy][sign]){
      newCalibs_[ee] = oldCalibs_[ee]/(1+epsilon_M_endc[ix][iy][sign]);

      eehisto.Fill(newCalibs_[ee]);

      // residual miscalibraition  / expected precision
      int index_e = e_.endcapRing_[ix][iy]+sign*kEndcEtaRings;
      miscal_resid_endc_histos[index_e]->Fill(miscalib_[ee]*newCalibs_[ee]);;
      correl_endc_histos[index_e]->Fill(miscalib_[ee],newCalibs_[ee]);
    }
    else
      newCalibs_[ee] = 1.0;


  }//endcapit

  // Write xml file
  EcalCondHeader header;
  header.method_="phi symmetry";
  header.version_="0";
  header.datasource_="testdata";
  header.since_=1;
  header.tag_="unknown";
  header.date_="Mar 24 1973";
 
  EcalIntercalibConstantsXMLTranslator::writeXML(newcalibfile,header,
						 newCalibs_ );  

  eehisto.Write();
  ebhisto.Write();
  ehistof.Close();

  fillConstantsHistos();
  
  outResidHistos();
 
  // finally output global etsums
  fstream ebf("etsummary_barl.dat",ios::out);
  fstream eef("etsummary_endc.dat",ios::out);
  
  for (int ieta=0; ieta<kBarlRings; ieta++) {
    for (int iphi=0; iphi<kBarlWedges; iphi++) {
      for (int sign=0; sign<kSides; sign++) {

	ebf<< ieta<< " " << iphi << " " <<sign <<" " 
	   << etsum_barl_[ieta][iphi][sign]<<"  " << nhits_barl_[ieta][iphi][sign] << endl;
	  
      }
    }
  }
  
  for (int ix=0; ix<kEndcWedgesX; ix++) {
    for (int iy=0; iy<kEndcWedgesY; iy++) {
      for (int sign=0; sign<kSides; sign++) {
	eef<<ix<<" " <<iy<<" " <<sign<<" "
	   <<  etsum_endc_[ix][iy][sign] << "  "<<  nhits_endc_[ix][iy][sign] <<endl;
	  
	  
      }
    }
  }
  
}




void  PhiSymmetryCalibration_step2::fillConstantsHistos(){
  
  TFile f("CalibHistos.root","recreate");  

  TH2F barreletamap("barreletamap","barreletamap",171, -85,86,100,0.,2.);
  TH2F barreletamapraw("barreletamapraw","barreletamapraw",171, -85,86,100,0.,2.);

  TH2F barrelmapold("barrelmapold","barrelmapold",360,1.,361.,171,-85.,86.);
  TH2F barrelmapnew("barrelmapnew","barrelmapnew",360,1.,361.,171,-85.,86.);
  TH2F barrelmapratio("barrelmapratio","barrelmapratio",360,1.,361.,171,-85.,86.);

  TH1F rawconst_endc_h("rawconst_endc","rawconst_endc",100,0.,2.);
  TH1F const_endc_h("const_endc","const_endc",100,0.,2.);

  TH1F oldconst_endc_h("oldconst_endc","oldconst_endc;oldCalib;",200,0,2);
  TH2F newvsraw_endc_h("newvsraw_endc","newvsraw_endc;rawConst;newCalib",200,0,2,200,0,2);

  TH2F endcapmapold_plus("endcapmapold_plus","endcapmapold_plus",100,1.,101.,100,1.,101.);
  TH2F endcapmapnew_plus("endcapmapnew_plus","endcapmapnew_plus",100,1.,101.,100,1.,101.);
  TH2F endcapmapratio_plus("endcapmapratio_plus","endcapmapratio_plus",100,1.,101.,100,1.,101.);

  TH2F endcapmapold_minus("endcapmapold_minus","endcapmapold_minus",100,1.,101.,100,1.,101.);
  TH2F endcapmapnew_minus("endcapmapnew_minus","endcapmapnew_minus",100,1.,101.,100,1.,101.);
  TH2F endcapmapratio_minus("endcapmapratio_minus","endcapmapratio_minus",100,1.,101.,100,1.,101.);

  TH2F endcapmapratio("endcapmapratio","endcapmapratio",100,1.,101.,100,1.,101.);
    TH1F endcapratio("endcapratio","ratio EE+/EE-",50,0,2);

  for (int sign=0; sign<kSides; sign++) {

    int thesign = sign==1 ? 1:-1;

    for (int ieta=0; ieta<kBarlRings; ieta++) {
      for (int iphi=0; iphi<kBarlWedges; iphi++) {
	if(e_.goodCell_barl[ieta][iphi][sign]){

	  EBDetId eb(thesign*( ieta+1 ), iphi+1);
	  //int mod20= (iphi+1)%20;
	  //if (mod20==0 || mod20==1 ||mod20==2) continue;  // exclude SM boundaries
	  barreletamap.Fill(ieta*thesign + thesign,newCalibs_[eb]);
	  barreletamapraw.Fill(ieta*thesign + thesign,rawconst_barl[ieta][iphi][sign]);
	  
	  barrelmapold.Fill(iphi+1,ieta*thesign + thesign, oldCalibs_[eb]);
	  barrelmapnew.Fill(iphi+1,ieta*thesign + thesign, newCalibs_[eb]);
	  barrelmapratio.Fill(iphi+1,ieta*thesign + thesign, newCalibs_[eb]/oldCalibs_[eb]);
	}//if
      }//iphi
    }//ieta

    for (int ix=0; ix<kEndcWedgesX; ix++) {
      for (int iy=0; iy<kEndcWedgesY; iy++) {
	if (e_.goodCell_endc[ix][iy][sign]){
	  if (! EEDetId::validDetId(ix+1, iy+1,thesign)) continue;
	  EEDetId ee(ix+1, iy+1,thesign);

	  rawconst_endc_h.Fill(rawconst_endc[ix][iy][sign]);
	  const_endc_h.Fill(newCalibs_[ee]);
	  oldconst_endc_h.Fill(oldCalibs_[ee]);
	  newvsraw_endc_h.Fill(rawconst_endc[ix][iy][sign],newCalibs_[ee]);

	  if(sign==1){
	    endcapmapold_plus.Fill(ix+1,iy+1,oldCalibs_[ee]);
	    endcapmapnew_plus.Fill(ix+1,iy+1,newCalibs_[ee]);
	    endcapmapratio_plus.Fill(ix+1,iy+1,newCalibs_[ee]/oldCalibs_[ee]);
	    
	  }
	  else{
	    endcapmapold_minus.Fill(ix+1,iy+1,oldCalibs_[ee]);
	    endcapmapnew_minus.Fill(ix+1,iy+1,newCalibs_[ee]);
	    endcapmapratio_minus.Fill(ix+1,iy+1,newCalibs_[ee]/oldCalibs_[ee]);
	  }

	}//if
      }//iy
    }//ix
    
  } // sides


for(int ix =1; ix <101; ix++)
{
for(int iy =1; iy <101; iy++)
{
double icp = endcapmapnew_plus.GetBinContent(ix, iy);
double icm = endcapmapnew_minus.GetBinContent(ix, iy);
if(icp!=0 && icm!=0)
{
endcapratio.Fill(icp/icm);
endcapmapratio.SetBinContent(ix,iy, icp/icm);
}
}

}
  barreletamap.Write();
  barreletamapraw.Write();
  rawconst_endc_h.Write();
  const_endc_h.Write();
  oldconst_endc_h.Write();
  newvsraw_endc_h.Write();
  barrelmapold.Write();
  barrelmapnew.Write();
  barrelmapratio.Write();
  endcapmapold_plus.Write();
  endcapmapnew_plus.Write();
  endcapmapratio_plus.Write();
  endcapmapold_minus.Write();
  endcapmapnew_minus.Write();
  endcapmapratio_minus.Write();
  endcapmapratio.Write();
  endcapratio.Write();

  f.Close();
}









//_____________________________________________________________________________

void PhiSymmetryCalibration_step2::fillHistos()
{

  //  cout << "Call FillHistos" << endl;
  TFile f("PhiSymmetryCalibration.root","recreate");
  TH2F *Xtals_Removed_EB = new TH2F("Xtals_Removed_EB","Xtals_Removed_EB ",360, 0, 360, 170, -85, 85);
  TH2F *Xtals_Removed_EE = new TH2F("Xtals_Removed_EE","Xtals_Removed_EB",200, -100, 100, 100, 0, 100);

  std::vector<TH1F*> etsum_barl_histos(2*kBarlRings);
  std::vector<TH1F*> etsum_barl_histos_cut(2*kBarlRings);

  std::vector<TH1F*> esum_barl_histos(2*kBarlRings);
  std::vector<TH1F*> NH_barl_histos(2*kBarlRings);
  std::vector<TH1F*> NHTT_barl_histos(2*kBarlRings);

  TH2F* diffNH_histo_map;
  TH2F* NHEB_histo;
  //TH2F* NHEE_histo;
  //TH2F* NHTT_histo_map;
  TH2F* NHTTbad_histo_map;

  TH1F *NHEB_trend; 
  //TH1F *NHEE_trend;
  TH1F *ETEB_trend;
  //TH1F *ETEE_trend;
  TH1F *ErecEB_trend;
  //TH1F *ErecEE_trend;
  TH2F *NHTT_map;
  
  // determine ranges of ET sums to get histo bounds and book histos (barrel)
  //double StDevETRingEB[kBarlRings][kSides] ; // ET spread in each ring
  //double StDevETRingEB1[kBarlRings][kSides] ; // ET spread in each ring
  double StDevNHRingEB1[kBarlRings][kSides] ; // ET spread in each ring
  double etsumMean_barl1[kBarlRings][kSides] ;
  double esumMean_barl1[kBarlRings][kSides] ;
  double NHitsMean_barl1[kBarlRings][kSides] ;

  //double StDevETRingEE[kEndcEtaRings][kSides] ; // ET spread in each ring
  //double StDevETRingEE1[kEndcEtaRings][kSides] ; // ET spread in each ring
  //double StDevNHRingEE1[kEndcEtaRings][kSides] ; // ET spread in each ring
  //double etsumMean_endc1[kEndcEtaRings][kSides] ;
  //double esumMean_endc1[kEndcEtaRings][kSides] ;
  //double NHitsMean_endc1[kEndcEtaRings][kSides] ;
  
  float NHTTcry[kBarlRings][kBarlWedges][kSides];
  float TTNHsum[kBarlRings][kBarlWedges][kSides];
  float TTNBC[kBarlRings][kBarlWedges][kSides];
  float NBCTTcry[kBarlRings][kBarlWedges][kSides];

  NHEB_histo= new TH2F("NH_profile_EB", "", 100, -10, 90, 1000, 700000, 3000000);
  //NHEE_histo= new TH2F("NH_profile_EE", "", 50,-5, 45 , 1000, 30000, 130000);

  ETEB_trend=new TH1F("ET_trend_EB", "", 100, -10, 90);
  //ETEE_trend= new TH1F("ET_trend_EE", "", 50,-5, 45);
  NHEB_trend=new TH1F("NH_trend_EB", "", 100, -10, 90);
  //NHEE_trend= new TH1F("NH_trend_EE", "", 50,-5, 45);
  ErecEB_trend=new TH1F("Erec_trend_EB", "", 100, -10, 90);
  //ErecEE_trend= new TH1F("Erec_trend_EE", "", 50,-5, 45);

    NHTTbad_histo_map = new TH2F("NHTTbad_map", "",360,1,360, 171, -85,86 );
  diffNH_histo_map = new TH2F("diffNH_map", "",360,1,360, 171, -85,86 );
  NHTT_map = new TH2F("NHTT_map", "",360,1,360, 171, -85,86 );
  


  //cout << "checking EB TT" << endl;

  int NbadTT=0;
  for (int sign=0; sign<kSides; sign++) {
    for (int ieta=0; ieta<kBarlRings; ieta++) {

      float TTNHsum_dummy=0;
  
      for (int iphi=0; iphi<kBarlWedges; iphi++) 
	{
	  if(!e_.goodCell_barl[ieta][iphi][sign])
	    NbadTT++;
      
	  TTNHsum_dummy+=nhits_barl_[ieta][iphi][sign];
  
	  if((iphi+1)%5==0)
	    {
	      for(int j=0; j<5; j++)
		{
		  TTNHsum[ieta][iphi-j][sign]=TTNHsum_dummy;
		  TTNBC[ieta][iphi-j][sign]=NbadTT;
		}
	      TTNHsum_dummy=0;
	      NbadTT=0;
	    }
	}
      
      if((ieta+1)%5==0)
        {
	  for(int iphi =0; iphi<kBarlWedges; iphi++)
	    {
	      float NHr=0;
	      int NBCr=0;
	      for(int j=0; j<5; j++)
		{
		  NHr+=TTNHsum[ieta-j][iphi][sign];
		  NBCr+=TTNBC[ieta-j][iphi][sign];
		}
	      for(int j=0; j<5; j++)
		{  
		  NHTTcry[ieta-j][iphi][sign]=NHr;
		  NBCTTcry[ieta-j][iphi][sign]=NBCr;
		}
	         
	    }
        }
    }
  }

  
  //cout << "check completed" << endl;
  
  // determine ranges of ET sums to get histo bounds and book histos (barrel)
  for (int ieta=0; ieta<kBarlRings; ieta++) {
    float low=999999.;
    float high=0.;
    float low_e=999999.;
    float high_e=0.;
    int low_hit=9999999;
    int high_hit=0;

    //cout << "ieta =  "<< ieta << endl;
    for (int sign=0; sign<kSides; sign++) {
      
      for (int iphi=0; iphi<kBarlWedges; iphi++) {
	float etsum = etsum_barl_[ieta][iphi][sign];
	if (etsum<low && etsum!=0.) low=etsum;
	if (etsum>high) high=etsum;
	
	float esum = esum_barl_[ieta][iphi][sign];
	if (esum<low_e && esum!=0.) low_e=esum;
	if (esum>high_e) high_e=esum;
	
	int nhit= nhits_barl_[ieta][iphi][sign];
	if (nhit<low_hit && nhit!=0.) low_hit=nhit;
	if (nhit>high_hit) high_hit=nhit;
      }
    
      
      int index_b = ieta+sign*kBarlRings;
      //cout << "iindex= "<< index_b << endl;
      //cout << "sign = " << sign << endl;
      
      ostringstream t;
      t << "etsum_barl_" << ieta+1 << "_" << sign;
      etsum_barl_histos[index_b]=new TH1F(t.str().c_str(),"",50,low-.2*low,high+.1*high);
      t.str("");
      
      t << "etsum_barl_cut" << ieta+1 << "_" << sign;
      etsum_barl_histos_cut[index_b]=new TH1F(t.str().c_str(),"",50,low-.2*low,high+.1*high);
      t.str("");
      
      t << "esum_barl_" << ieta+1 << "_" << sign;
      esum_barl_histos[index_b]=new TH1F(t.str().c_str(),"",50,low_e-.2*low_e,high_e+.1*high_e);
      t.str("");
      
         t << "NH_barl_" << ieta+1 << "_" << sign;
 	  NH_barl_histos[index_b]=new
   TH1F(t.str().c_str(),"",100,low_hit-0.2*low_hit,high_hit+0.1*high_hit);
    t.str("");
      
       
t << "NHTT_barl_" << ieta+1 << "_" << sign;
 	  NHTT_barl_histos[index_b]=new
   TH1F(t.str().c_str(),"",1000,25*(low_hit-0.2*low_hit),25*(high_hit+0.1*high_hit));
    t.str("");
      
      // fill barrel ET sum histos
      int ngc=0;
      int ngtt=0;
      for (int iphi=0; iphi<kBarlWedges; iphi++) {
		//cout << iphi <<endl; 
	
	if(e_.goodCell_barl[ieta][iphi][sign]){
	  float etsum = etsum_barl_[ieta][iphi][sign];
	  float esum  = esum_barl_[ieta][iphi][sign];
	  etsumMean_barl1[ieta][sign]+=etsum;
	  esumMean_barl1[ieta][sign]+=esum;
	  ngc++;
	  }
        //cout << "good ok " << endl;
	//cout << NBCTTcry[ieta][iphi][sign] << endl;
	if((iphi+1)%5==0)
	  {
	    if(NBCTTcry[ieta][iphi][sign]<20)
	      {
	     
                  NHTT_barl_histos[index_b]->Fill(NHTTcry[ieta][iphi][sign]*(25./(25.-NBCTTcry[ieta][iphi][sign])));
		  //NHitsMean_barl1[ieta][sign]+=NHTTcry[ieta][iphi][sign]*(25./(25.-NBCTTcry[ieta][iphi][sign]));
		  NHEB_histo->Fill(ieta, NHTTcry[ieta][iphi][sign]*(25./(25.-NBCTTcry[ieta][iphi][sign])));
		  ngtt++;
	      } 
	  }
      }
      //cout << "loop 1 ok" << endl;   
      NHitsMean_barl1[ieta][sign] = NHTT_barl_histos[index_b]->GetMean();
      StDevNHRingEB1[ieta][sign] = NHTT_barl_histos[index_b]->GetRMS();
      // if ((720-ngc)!=e_.nBads_barl[ieta]) cout  << ieta << "  " << ngc<< "  " << e_.nBads_barl[ieta] << endl; 
 
      etsumMean_barl1[ieta][sign]=etsumMean_barl1[ieta][sign]/ngc;
      esumMean_barl1[ieta][sign]=esumMean_barl1[ieta][sign]/ngc;
      //NHitsMean_barl1[ieta][sign]=NHitsMean_barl1[ieta][sign]/ngtt;
      
      /*
      cout << "scritti " << ngtt <<  endl;
      for (int iphi=0; iphi<kBarlWedges; iphi++) {
	if((iphi+1)%5==0 && NBCTTcry[ieta][iphi][sign]<20){ 
	  StDevNHRingEB1[ieta][sign]+=(NHTTcry[ieta][iphi][sign]*(25./(25.-NBCTTcry[ieta][iphi][sign]))- NHitsMean_barl1[ieta][sign])*(NHTTcry[ieta][iphi][sign]*(25./(25.-NBCTTcry[ieta][iphi][sign]))- NHitsMean_barl1[ieta][sign]);
	}
      }
     */
      //StDevNHRingEB1[ieta][sign] = sqrt(StDevNHRingEB1[ieta][sign]/ngtt);
      
      // fill barrel ET sum histos
      etsumMean_barl_[ieta][sign]=0.;
      esumMean_barl_[ieta][sign]=0.;
      NHitsMean_barl_[ieta][sign]=0.;
      int ngc2=0;
      int nbads = 0;

      for (int iphi=0; iphi<kBarlWedges; iphi++) {
	  //cout << "iphi =" << iphi << endl;
	  float etsum = etsum_barl_[ieta][iphi][sign];
	  float esum  = esum_barl_[ieta][iphi][sign];
	  //float etsumMean = etsumMean_barl1[ieta][sign];
	  //float etsumStDev = StDevETRingEB1[ieta][sign];
	  //float diff = abs(etsum-etsumMean)/etsumStDev;
      
	  float nhits = NHTTcry[ieta][iphi][sign]*(25./(25.-NBCTTcry[ieta][iphi][sign]));
	  float nhitsMean = NHitsMean_barl1[ieta][sign];
	  float nhitsStDev = StDevNHRingEB1[ieta][sign];
	  float diffNH = (nhits-nhitsMean)/nhitsStDev;      
	  //cout << ieta << "  " << iphi << "  " << sign << "  " <<  diffNH << "  "<<
	  //	  nhits << "   " << nhitsMean << "   "<< nhitsStDev <<  endl;
	  int thesign = sign==1 ? 1:-1;
	  NHTT_map->Fill(iphi+1,ieta*thesign+ thesign, NHTTcry[ieta][iphi][sign]);  
 //cout << "sign = " << sign << "    thesign =" << thesign << endl;	
	  //float HotCryFlag=(nhits_barl_[ieta][iphi][sign]/(nhitsMean/25.));
	  diffNH_histo_map->Fill(iphi+1,ieta*thesign+ thesign, diffNH);
	  float cut = -3;
	  if((iphi>4 && iphi<15) || (iphi>184 && iphi<195)) cut = -4;
	  
	  if(e_.goodCell_barl[ieta][iphi][sign] && diffNH > cut)// && HotCryFlag<8.)
	    {
	//    cout << "isgood" << endl;  
	      //etsumMean_barl_[ieta][sign]+=etsum;
	      //esumMean_barl_[ieta][sign]+=esum;
	      //NHitsMean_barl_[ieta][sign]+=nhits_barl_[ieta][iphi][sign];
	      etsum_barl_histos[index_b]->Fill(etsum);
	      esum_barl_histos[index_b]->Fill(esum);
	      NH_barl_histos[index_b]->Fill(nhits_barl_[ieta][iphi][sign]);
	      ngc2++;  
	    } 
	  else 
	    { 
	      //cout << " bad crystal " ;
	      if(e_.goodCell_barl[ieta][iphi][sign])
		{
		  //cout << " (new)  " ;
		  //e_.nBads_barl[ieta][sign]++;
		}
	      //cout << ieta<<", "<<iphi<<", "<<sign<<endl;
	      if(e_.goodCell_barl[ieta][iphi][sign])
		NHTTbad_histo_map->Fill(iphi+1,ieta*thesign+ thesign, 1);
	      else
		NHTTbad_histo_map->Fill(iphi+1,ieta*thesign+ thesign, -1);  
	      e_.goodCell_barl[ieta][iphi][sign] = false;
	     }
      }
    //cout <<" " << endl;
    //cout << "end TT stuff " << endl;   
    //cout << etsum_barl_histos[index_b]->GetEntries() << endl;
   //Quantile extraction for the number of rechits per xtal   
    Double_t EBxq[2];  // position where to compute the quantiles in [0,1]                                                 
    Double_t EByq[2];  // array to contain the quantiles                                                                                    
    EBxq[0]  = 0.05;
    EBxq[1]  = 0.95;
    etsum_barl_histos[index_b]->GetQuantiles(2,EByq,EBxq);
 
    //cout << "quantiles OK " << EByq[0] << "  " << EByq[1] << endl; 
    // fill barrel ET sum histos: finally we calculate the etsum
    etsumMean_barl_[ieta][sign]=0.;
    esumMean_barl_[ieta][sign]=0.;
    NHitsMean_barl_[ieta][sign]=0.;
      
      for (int iphi=0; iphi<kBarlWedges; iphi++) {
	  float etsum = etsum_barl_[ieta][iphi][sign];
	  float esum  = esum_barl_[ieta][iphi][sign];
	    int thesign = sign==1 ? 1:-1;
	  if(e_.goodCell_barl[ieta][iphi][sign] && etsum
	  >EByq[0] && etsum <EByq[1])
	    { 
	      etsum_barl_histos_cut[index_b]->Fill(etsum);
	     
	      Xtals_Removed_EB->Fill(iphi, ieta*thesign, 1);  
	      etsumMean_barl_[ieta][sign]+=etsum;
	      esumMean_barl_[ieta][sign]+=esum;
	      NHitsMean_barl_[ieta][sign]+=nhits_barl_[ieta][iphi][sign];
	    } 
	  else 
	    {   
	    Xtals_Removed_EB->Fill(iphi, ieta*thesign, 2);  
	      nbads++;
	    }
      }
      
      //etsumMean_barl_[ieta][sign]=etsum_barl_histos[index_b]->GetMean();
      etsumMean_barl_[ieta][sign]/=(360.-nbads);
      esumMean_barl_[ieta][sign]/=(360.-nbads);
      NHitsMean_barl_[ieta][sign]/=(360.-nbads);
      
      cout << index_b<<"   " << etsum_barl_histos_cut[index_b]->GetMean() << "   " << etsumMean_barl_[ieta][sign]<< endl;
	
      etsumMean_barl_[ieta][sign]=etsum_barl_histos_cut[index_b]->GetMean();
           
           etsum_barl_histos[index_b]->Write();
      esum_barl_histos[index_b]->Write();
      NH_barl_histos[index_b]->Write();
      NHTT_barl_histos[index_b]->Write();
  
      delete etsum_barl_histos[index_b];
      delete esum_barl_histos[index_b]; 
      delete NH_barl_histos[index_b];
    }
  }
  NHEB_histo->Write();
  delete NHEB_histo; 
  NHTTbad_histo_map ->Write();
  NHTTbad_histo_map ->Delete();
  diffNH_histo_map->Write();
  diffNH_histo_map->Delete();
  NHTT_map->Write();
  ETEB_trend->Write();
  NHEB_trend->Write();
  ErecEB_trend->Write();  
  Xtals_Removed_EB->Write();
  // EB END -------------------------------------------------------------------------



  //EE START -----------------------------------------------------------------------
  
  std::vector<TH1F*> etsum_endc_histos(kEndcEtaRings*2);
  std::vector<TH1F*> etsum_endc_histos_cut(kEndcEtaRings*2);
  
  std::vector<TH1F*> etsum_endc_uncorr_histos(kEndcEtaRings*2);
  std::vector<TH1F*> esum_endc_histos(kEndcEtaRings*2);
  
  std::vector<TH2F*> etsumvsarea_endc_histos(kEndcEtaRings*2);
  std::vector<TH2F*> esumvsarea_endc_histos(kEndcEtaRings*2);

  float NHTTcry_EE[kEndcWedgesX][kEndcWedgesY][kSides];
  float TTNHsum_EE[kEndcWedgesX][kEndcWedgesY][kSides];
  float TTNBC_EE[kEndcWedgesX][kEndcWedgesY][kSides];
  float NBCTTcry_EE[kEndcWedgesX][kEndcWedgesY][kSides];

  TH2F StatusEEplus_before("StatusEEplus_before", "EE+ channel status before TT selection",100,0,100,100,0,100);
  TH2F StatusEEplus_after("StatusEEplus_after", "EE+ channel status after TT selection",100,0,100,100,0,100);

  TH2F StatusEEminus_before("StatusEEminus_before", "EE- channel status before TT selection",100,0,100,100,0,100);
  TH2F StatusEEminus_after("StatusEEminus_after", "EE- channel status after TT selection",100,0,100,100,0,100);
 




  NbadTT=0;
  for (int sign=0; sign<kSides; sign++) {    // Loops over the two sides  
    for (int ix=0; ix<kEndcWedgesX; ix++) {   // reads the x-rows in the EE
      float TTNHsum_dummy=0;   // dummy variable: it contains the hit sum in a 5 xtals row
  
      for (int iy=0; iy<kEndcWedgesY; iy++) {

	if( e_.goodCell_endc[ix][iy][1]) StatusEEplus_before.Fill(ix,iy,1);
	else  StatusEEplus_before.Fill(ix,iy,0);


	if( e_.goodCell_endc[ix][iy][0]) StatusEEminus_before.Fill(ix,iy,1);
	else  StatusEEplus_before.Fill(ix,iy,0);


	if(e_.endcapRing_[ix][iy]==-1)
	  {
	    e_.goodCell_endc[ix][iy][0] = false;
	    e_.goodCell_endc[ix][iy][1] = false;
	  }    
  
	if(!e_.goodCell_endc[ix][iy][sign]) // if the crystal is bad adds 1 to te number of BC in the TT
	  NbadTT++;
	else    // adds the number of hits to the dummy variable
	  TTNHsum_dummy+=nhits_endc_[ix][iy][sign];
	
	if((iy+1)%5==0) // every five xtals...
	  {
	    for(int j=0; j<5; j++)
	      {
		TTNHsum_EE[ix][iy-j][sign]=TTNHsum_dummy;
		TTNBC_EE[ix][iy-j][sign]=NbadTT;
	      }
	    TTNHsum_dummy=0;
	    NbadTT=0;
	  }
      }
      
      if((ix+1)%5==0)
        {
	  for (int iy=0; iy<kEndcWedgesY; iy++) {
	    float NHr=0;
	    int NBCr=0;
	    for(int j=0; j<5; j++)
	      {
		NHr+=TTNHsum_EE[ix-j][iy][sign];
		NBCr+=TTNBC_EE[ix-j][iy][sign];
	      }
	    for(int j=0; j<5; j++)
	      {  
		NHTTcry_EE[ix-j][iy][sign]=NHr;
		NBCTTcry_EE[ix-j][iy][sign]=NBCr;
	      }
	       
	  }
        }
    }
  }





  TH2F NHEEplus_map("NHEEplus_map", "EE+ hitmap",100,0,100,100,0,100);
  TH2F NHEEminus_map("NHEEminus_map", "EE- hitmap",100,0,100,100,0,100);
  TH2F NHEEdiff_map("NHEEdiff_map", "diff hitmap",100,0,100,100,0,100);
  TH2F NHEEdiffnorm_map("NHEEdiffnorm_map", "normalized diff hitmap",100,0,100,100,0,100);
  TH2F NHEEsigma_map("NHEEsigma_map", "sigma hitmap",100,0,100,100,0,100);
  TH1F NHEEsigma("NHEEsigma", "normalized diff histo",160,-400,400);

  TH2F EEminus_killed("EEminus_killed", "killed TT map in EE-",100,0,100,100,0,100);
  TH2F EEplus_killed("EEplus_killed", "killed TT map in EE+",100,0,100,100,0,100);
  TH2F NHEEratio_map("NHEEratio_map", "EE+/EE- map",100,0,100,100,0,100);
  TH1F NHEEratio("NHEEratio", "EE+/EE-",200,0,2);


  //sets the "crystals" outside the EE boundiary as bad
  for (int ix=0; ix<kEndcWedgesX; ix++) {
    for (int iy=0; iy<kEndcWedgesY; iy++) {
      if(e_.endcapRing_[ix][iy]==-1)
	{
	  EEminus_killed.Fill(ix, iy, -100);
	  EEplus_killed.Fill(ix, iy, -100);
          NHEEdiff_map.Fill(ix,iy,-100);
          NHEEdiffnorm_map.Fill(ix,iy,-100);
	}
    }
  }
      
  //Loops over all the xstals in order to calculate the differences
  //float sigma_prec =0; //dummy variable used as flag for an histrogram filling;
  for (int ix=0; ix<kEndcWedgesX; ix++) {
    for (int iy=0; iy<kEndcWedgesY; iy++) {

      float nplus=0;
      float nminus=0;

      if( e_.goodCell_endc[ix][iy][1]) StatusEEplus_after.Fill(ix,iy,1);
      else  StatusEEplus_after.Fill(ix,iy,0);


      if( e_.goodCell_endc[ix][iy][0]) StatusEEminus_after.Fill(ix,iy,1);
      else  StatusEEplus_after.Fill(ix,iy,0);

    
      if(e_.goodCell_endc[ix][iy][1] && NBCTTcry_EE[ix][iy][1] < 25) // if all the xtal is bad skips
	{
	  nplus = NHTTcry_EE[ix][iy][1]*25./(25.-NBCTTcry_EE[ix][iy][1]);
	  NHEEplus_map.Fill(ix, iy, nplus);
	}   
      if(e_.goodCell_endc[ix][iy][0] && NBCTTcry_EE[ix][iy][0] < 25 ) // if all the xtal is bad skips
	{
	  nminus = NHTTcry_EE[ix][iy][0]*25./(25.-NBCTTcry_EE[ix][iy][0]);
	  NHEEminus_map.Fill(ix, iy, nminus);
	}

      if(nplus>0 && nminus>0)
	{
	  NHEEdiff_map.Fill(ix,iy,(nplus-nminus)); 
	  NHEEdiffnorm_map.Fill(ix,iy,(nplus-nminus)/sqrt(nplus+nminus));
	  float sigma = (nplus-nminus)/sqrt(nplus+nminus);
	  if((iy+1)%5==0 && (ix+1)%5==0) // prevents the histogram to be filled too many times with the same value
	    {
	      NHEEsigma.Fill(sigma);
	      NHEEratio.Fill(nplus/nminus);
	      //sigma_prec=sigma;
	    }
	}
      
    }
  }

  
  // NHEEsigma.Fit("gaus", "Q");
  NHEEratio.Fit("gaus", "Q");
  double sigmaEE = NHEEratio.GetFunction("gaus")->GetParameter(2);
  double meanEE = NHEEratio.GetFunction("gaus")->GetParameter(1);

  for (int ix=0; ix<kEndcWedgesX; ix++) {
    for (int iy=0; iy<kEndcWedgesY; iy++) {
      if(!e_.goodCell_endc[ix][iy][1])
	EEplus_killed.Fill(ix, iy, -1);
      if(!e_.goodCell_endc[ix][iy][0])
	EEminus_killed.Fill(ix, iy, -1);

      if( NBCTTcry_EE[ix][iy][1] > 24 ||   NBCTTcry_EE[ix][iy][0] > 24) 
	{ 
          NHEEratio_map.Fill(ix,iy,-1);
	  NHEEsigma_map.Fill(ix,iy,-101);
	  continue;
	}
      
      float nplus = NHTTcry_EE[ix][iy][1]*25./(25.-NBCTTcry_EE[ix][iy][1]);
      float nminus = NHTTcry_EE[ix][iy][0]*25./(25.-NBCTTcry_EE[ix][iy][0]);

      if(nplus<1 || nminus < 1 )
	{ 
          NHEEratio_map.Fill(ix,iy,-1);
	  NHEEsigma_map.Fill(ix,iy,-101);
	  continue;
	}

      else{
	float diffvalue= nplus/nminus;
	float relativediffvalue =(diffvalue-meanEE)/sigmaEE; 
	NHEEsigma_map.Fill(ix,iy,relativediffvalue);
	NHEEratio_map.Fill(ix,iy, nplus/nminus);
	if(e_.goodCell_endc[ix][iy][0])
	  {
	    EEminus_killed.Fill(ix, iy, 0);
	     
	    if(relativediffvalue>3)
	      {
		EEminus_killed.Fill(ix, iy, 1);
		e_.goodCell_endc[ix][iy][0] = false;
	      }
	     
	  }
	if(e_.goodCell_endc[ix][iy][1])
	  {
	    EEplus_killed.Fill(ix, iy, 0);
	      
	    if(relativediffvalue<-3)
	      {
		EEplus_killed.Fill(ix, iy, 1);
		e_.goodCell_endc[ix][iy][1] = false;
	      }
	      
	  }
      }
    }
  }
  






  // determine ranges of ET sums to get histo bounds and book histos (endcap)
  for (int ring=0; ring<kEndcEtaRings; ring++) {

    float low=FLT_MAX;
    float low_uncorr=FLT_MAX;
    float high=0.;
    float high_uncorr=0;
    float low_e=FLT_MAX;
    float high_e=0.;
    float low_a=1.;
    float high_a=0.;

    for (int sign=0; sign<kSides; sign++) {

      for (int ix=0; ix<kEndcWedgesX; ix++) {
	for (int iy=0; iy<kEndcWedgesY; iy++) {
	  if (e_.endcapRing_[ix][iy]==ring) {
	    float etsum = etsum_endc_[ix][iy][sign];
	    if (etsum<low && etsum!=0.) low=etsum;
	    if (etsum>high) high=etsum;

	    float etsum_uncorr = etsum_endc_uncorr[ix][iy][sign];
	    if (etsum_uncorr<low_uncorr && etsum_uncorr!=0.) low_uncorr=etsum_uncorr;
	    if (etsum_uncorr>high_uncorr) high_uncorr=etsum_uncorr;

	    float esum = esum_endc_[ix][iy][sign];
	    if (esum<low_e && esum!=0.) low_e=esum;
	    if (esum>high_e) high_e=esum;

	    float area = e_.cellArea_[ix][iy];
	    if (area<low_a) low_a=area;
	    if (area>high_a) high_a=area;
	  }
	}
      }
    
      int index_e = ring+sign*kEndcEtaRings;

      ostringstream t;
      t<<"etsum_endc_" << ring+1 << "_" << sign;
      etsum_endc_histos[index_e]= new TH1F(t.str().c_str(),"",50,low-.2*low,high+.1*high);
      t.str("");

      t<<"etsum_endc_cut" << ring+1 << "_" << sign;
      etsum_endc_histos_cut[index_e]= new TH1F(t.str().c_str(),"",50,low-.2*low,high+.1*high);
      t.str("");

      t<<"etsum_endc_uncorr_" << ring+1 << "_" << sign;
      etsum_endc_uncorr_histos[index_e]= new TH1F(t.str().c_str(),"",50,low_uncorr-.2*low_uncorr,high_uncorr+.1*high_uncorr);
      t.str("");

      t<<"esum_endc_" << ring+1 << "_" << sign;
      esum_endc_histos[index_e]= new TH1F(t.str().c_str(),"",50,low_e-.2*low_e,high_e+.1*high_e);
      t.str("");

      t<<"etsumvsarea_endc_" << ring+1 << "_" << sign;
      etsumvsarea_endc_histos[index_e]= new TH2F(t.str().c_str(),";A_{#eta#phi};#Sigma E_{T}",50,low_a,high_a,50,low,high);
      t.str("");

      t<<"esumvsarea_endc_" << ring+1 << "_" << sign;
      esumvsarea_endc_histos[index_e]= new TH2F(t.str().c_str(),";A_{#eta#phi};#Sigma E",50,low_a,high_a,50,low_e,high_e);
      t.str("");

      // fill endcap ET sum histos
      etsumMean_endc_[ring][sign]=0.;
      esumMean_endc_[ring][sign]=0.;
      nBads_endc[ring][sign]=0;
      for (int ix=0; ix<kEndcWedgesX; ix++) {
	for (int iy=0; iy<kEndcWedgesY; iy++) {
	  if (e_.endcapRing_[ix][iy]==ring) {
	    if(e_.goodCell_endc[ix][iy][sign]){
	      float etsum = etsum_endc_[ix][iy][sign];
	      float esum  = esum_endc_[ix][iy][sign];
	      float etsum_uncorr = etsum_endc_uncorr[ix][iy][sign];
	      etsum_endc_histos[index_e]->Fill(etsum);
	      etsum_endc_uncorr_histos[index_e]->Fill(etsum_uncorr);
	      esum_endc_histos[index_e]->Fill(esum);
     
	    }
	  }
	}
      }
      /*
	Double_t EExq[2];  // position where to compute the quantiles in [0,1]                                                 
	Double_t EEyq[2];  // array to contain the quantiles                                                                                  
	EExq[0]  = 0.05;
	EExq[1]  = 0.95;
	etsum_endc_histos[index_e]->GetQuantiles(2,EEyq,EExq);
      */
      int thesign=1;

      double rmsEE = etsum_endc_histos[index_e]->GetRMS();
      double meanEE = etsum_endc_histos[index_e]->GetMean();
      double upperCut = meanEE+2*rmsEE;
      double lowerCut = meanEE-2*rmsEE;
      if(sign ==0) thesign=-1;	    
      
      for (int ix=0; ix<kEndcWedgesX; ix++) {
	for (int iy=0; iy<kEndcWedgesY; iy++) {
	  if (e_.endcapRing_[ix][iy]==ring) {
	    float etsum = etsum_endc_[ix][iy][sign];
	    float esum  = esum_endc_[ix][iy][sign];
	    //float etsum_uncorr = etsum_endc_uncorr[ix][iy][sign];
	    
	    if(e_.goodCell_endc[ix][iy][sign] && etsum >lowerCut && etsum <upperCut){
	      Xtals_Removed_EE->Fill(ix*thesign, iy, 1); 
	      etsumMean_endc_[ring][sign]+=etsum;
	      esumMean_endc_[ring][sign]+=esum;
	      etsum_endc_histos_cut[index_e]->Fill(etsum);
	    
	      float area = e_.cellArea_[ix][iy];
	      etsumvsarea_endc_histos[index_e]->Fill(area,etsum);
	      esumvsarea_endc_histos[index_e]->Fill(area,esum);
	    }
	    else {
	      nBads_endc[ring][sign]++;
	      Xtals_Removed_EE->Fill(ix*thesign, iy, 2);
	    }
	  }
	}
      }
      
      etsumMean_endc_[ring][sign]/=(float(e_.nRing_[ring]-nBads_endc[ring][sign]));
      esumMean_endc_[ring][sign]/= (float(e_.nRing_[ring]-nBads_endc[ring][sign]));

      cout << "Controllo Etsum ring = "<< ring << " sign = "<< sign <<";  math: "<< etsumMean_endc_[ring][sign] << ", histo:" << etsum_endc_histos_cut[index_e]->GetMean() << endl;
      etsum_endc_histos[index_e]->Write();
      etsum_endc_uncorr_histos[index_e]->Write();
      esum_endc_histos[index_e]->Write();
      etsumvsarea_endc_histos[index_e]->Write();
      esumvsarea_endc_histos[index_e]->Write();

      delete etsum_endc_histos[index_e];
      delete etsum_endc_uncorr_histos[index_e];
      delete esum_endc_histos[index_e];
      delete etsumvsarea_endc_histos[index_e];
      delete esumvsarea_endc_histos[index_e];

    }//sign  
  }//ring
  
  NHEEplus_map.Write();
  NHEEminus_map.Write();
  NHEEdiff_map.Write();
 NHEEdiffnorm_map.Write();
NHEEsigma_map.Write();
NHEEsigma.Write();

  EEminus_killed.Write();
  EEplus_killed.Write();
  NHEEratio_map.Write();
  NHEEratio.Write();
  Xtals_Removed_EE->Write();

  // Maps of etsum in EB and EE
  TH2F barreletamap("barreletamap","barreletamap",171, -85,86,100,0,2);
  TH2F barrelmap("barrelmap","barrelmap - #frac{#Sigma E_{T}}{<#Sigma E_{T}>_{0}}",360,1,360, 171, -85,86);
  TH2F barrelmap_e("barrelmape","barrelmape - #frac{#Sigma E}{<#Sigma E>_{0}}",360,1,360, 171, -85,86);
  TH2F barrelmap_divided("barrelmapdiv","barrelmapdivided - #frac{#Sigma E_{T}}{hits}",360,1,360,171,-85,86);
  TH2F barrelmap_e_divided("barrelmapediv","barrelmapedivided - #frac{#Sigma E}{hits}",360,1,360,171,-85,86);
  TH2F endcmap_plus_corr("endcapmapplus_corrected","endcapmapplus - #frac{#Sigma E_{T}}{<#Sigma E_{T}>_{38}}",100,1,101,100,1,101);
  TH2F endcmap_minus_corr("endcapmapminus_corrected","endcapmapminus - #frac{#Sigma E_{T}}{<#Sigma E_{T}>_{38}}",100,1,101,100,1,101);
  TH2F endcmap_plus_uncorr("endcapmapplus_uncorrected","endcapmapplus_uncor - #frac{#Sigma E_{T}}{<#Sigma E_{T}>_{38}}",100,1,101,100,1,101);
  TH2F endcmap_minus_uncorr("endcapmapminus_uncorrected","endcapmapminus_uncor - #frac{#Sigma E_{T}}{<#Sigma E_{T}>_{38}}",100,1,101,100,1,101);
  TH2F endcmap_e_plus("endcapmapeplus","endcapmapeplus - #frac{#Sigma E}{<#Sigma E>_{38}}",100,1,101,100,1,101);
  TH2F endcmap_e_minus("endcapmapeminus","endcapmapeminus - #frac{#Sigma E}{<#Sigma E>_{38}}",100,1,101,100,1,101);

  for (int sign=0; sign<kSides; sign++) {

    int thesign = sign==1 ? 1:-1;

    for (int ieta=0; ieta<kBarlRings; ieta++) {
      for (int iphi=0; iphi<kBarlWedges; iphi++) {
	if(e_.goodCell_barl[ieta][iphi][sign]){
	  barrelmap.Fill(iphi+1,ieta*thesign + thesign, etsum_barl_[ieta][iphi][sign]/etsumMean_barl_[0][sign]);
	  barrelmap_e.Fill(iphi+1,ieta*thesign + thesign, esum_barl_[ieta][iphi][sign]/esumMean_barl_[0][sign]); //VS
	  if (!nhits_barl_[ieta][iphi][sign]) nhits_barl_[ieta][iphi][sign] =1;
	  barrelmap_divided.Fill( iphi+1,ieta*thesign + thesign, etsum_barl_[ieta][iphi][sign]/nhits_barl_[ieta][iphi][sign]);
	  barrelmap_e_divided.Fill( iphi+1,ieta*thesign + thesign, esum_barl_[ieta][iphi][sign]/nhits_barl_[ieta][iphi][sign]); //VS
	  //int mod20= (iphi+1)%20;
	  //if (mod20==0 || mod20==1 ||mod20==2) continue;  // exclude SM boundaries
	  barreletamap.Fill(ieta*thesign + thesign,etsum_barl_[ieta][iphi][sign]/etsumMean_barl_[0][sign]);
	}//if
      }//iphi
    }//ieta

    for (int ix=0; ix<kEndcWedgesX; ix++) {
      for (int iy=0; iy<kEndcWedgesY; iy++) {
	if (sign==1) {
	  endcmap_plus_corr.Fill(ix+1,iy+1,etsum_endc_[ix][iy][sign]/etsumMean_endc_[38][sign]);
	  endcmap_plus_uncorr.Fill(ix+1,iy+1,etsum_endc_uncorr[ix][iy][sign]/etsumMean_endc_[38][sign]);
	  endcmap_e_plus.Fill(ix+1,iy+1,esum_endc_[ix][iy][sign]/esumMean_endc_[38][sign]);
	}
	else{ 
	  endcmap_minus_corr.Fill(ix+1,iy+1,etsum_endc_[ix][iy][sign]/etsumMean_endc_[38][sign]);
	  endcmap_minus_uncorr.Fill(ix+1,iy+1,etsum_endc_uncorr[ix][iy][sign]/etsumMean_endc_[38][sign]);
	  endcmap_e_minus.Fill(ix+1,iy+1,esum_endc_[ix][iy][sign]/esumMean_endc_[38][sign]);
	}
      }//iy
    }//ix

  }  //sign
  
 

  barreletamap.Write();
  barrelmap_divided.Write();
  barrelmap.Write();
  barrelmap_e_divided.Write();
  barrelmap_e.Write();
  endcmap_plus_corr.Write();
  endcmap_minus_corr.Write();
  endcmap_plus_uncorr.Write();
  endcmap_minus_uncorr.Write();
  endcmap_e_plus.Write();
  endcmap_e_minus.Write();


  vector<TH1F*> etavsphi_endc(kEndcEtaRings*kSides);
  vector<TH1F*> areavsphi_endc(kEndcEtaRings*kSides);
  vector<TH1F*> etsumvsphi_endcp_corr(kEndcEtaRings*kSides);
  vector<TH1F*> etsumvsphi_endcm_corr(kEndcEtaRings*kSides);
  vector<TH1F*> etsumvsphi_endcp_uncorr(kEndcEtaRings*kSides);
  vector<TH1F*> etsumvsphi_endcm_uncorr(kEndcEtaRings*kSides);
  vector<TH1F*> esumvsphi_endcp(kEndcEtaRings*kSides);
  vector<TH1F*> esumvsphi_endcm(kEndcEtaRings*kSides);

  for (int sign=0; sign<kSides; sign++) {
    for(int ring =0; ring<kEndcEtaRings;++ring){
    
      int index_e = ring+sign*kEndcEtaRings;

      ostringstream t;
      t<< "etavsphi_endc_" << ring << "_" << sign;
      etavsphi_endc[index_e] = new TH1F(t.str().c_str(), t.str().c_str(),e_.nRing_[ring],0,e_.nRing_[ring]);
      t.str("");

      t<< "areavsphi_endc_" << ring << "_" << sign;
      areavsphi_endc[index_e] = new TH1F(t.str().c_str(), t.str().c_str(),e_.nRing_[ring],0,e_.nRing_[ring]);
      t.str("");

      t<< "etsumvsphi_endcp_corr_" << ring << "_" << sign;
      etsumvsphi_endcp_corr[index_e] = new TH1F(t.str().c_str(), t.str().c_str(),e_.nRing_[ring],0,e_.nRing_[ring]);
      t.str("");

      t << "etsumvsphi_endcm_corr_" << ring << "_" << sign;
      etsumvsphi_endcm_corr[index_e] = new TH1F(t.str().c_str(), t.str().c_str(),e_.nRing_[ring],0,e_.nRing_[ring]);
      t.str("");

      t << "etsumvsphi_endcp_uncorr_" << ring << "_" << sign;
      etsumvsphi_endcp_uncorr[index_e] = new TH1F(t.str().c_str(), t.str().c_str(),e_.nRing_[ring],0,e_.nRing_[ring]);
      t.str("");

      t << "etsumvsphi_endcm_uncorr_" << ring << "_" << sign;
      etsumvsphi_endcm_uncorr[index_e] = new TH1F(t.str().c_str(), t.str().c_str(),e_.nRing_[ring],0,e_.nRing_[ring]);
      t.str("");
    
      t << "esumvsphi_endcp_" << ring << "_" << sign;
      esumvsphi_endcp[index_e] = new TH1F(t.str().c_str(), t.str().c_str(),e_.nRing_[ring],0,e_.nRing_[ring]);
      t.str("");

      t << "esumvsphi_endcm_" << ring << "_" << sign;
      esumvsphi_endcm[index_e] = new TH1F(t.str().c_str(), t.str().c_str(),e_.nRing_[ring],0,e_.nRing_[ring]);
      t.str("");

    }//ring

    for (int ix=0; ix<kEndcWedgesX; ix++) {
      for (int iy=0; iy<kEndcWedgesY; iy++) {

	int ring = e_.endcapRing_[ix][iy];
	int index_e = ring+sign*kEndcEtaRings;

	if (ring!=-1) {
	  int iphi_endc=-1;
	  for (int ip=0; ip<e_.nRing_[ring]; ip++) {
	    if (e_.cellPhi_[ix][iy]==e_.phi_endc_[ip][ring]) iphi_endc=ip;
	  }

	  if(iphi_endc!=-1){
	    if(e_.goodCell_endc[ix][iy][sign]){
	      if (sign==1){
		etsumvsphi_endcp_corr[index_e]->Fill(iphi_endc,etsum_endc_[ix][iy][sign]);
		etsumvsphi_endcp_uncorr[index_e]->Fill(iphi_endc,etsum_endc_uncorr[ix][iy][sign]);
		esumvsphi_endcp[index_e]->Fill(iphi_endc,esum_endc_[ix][iy][sign]);
	      } else {
		etsumvsphi_endcm_corr[index_e]->Fill(iphi_endc,etsum_endc_[ix][iy][sign]);
		etsumvsphi_endcm_uncorr[index_e]->Fill(iphi_endc,etsum_endc_uncorr[ix][iy][sign]);
		esumvsphi_endcm[index_e]->Fill(iphi_endc,esum_endc_[ix][iy][sign]);
	      }
	    }//if
	    etavsphi_endc[index_e]->Fill(iphi_endc,e_.cellPos_[ix][iy].eta());
	    areavsphi_endc[index_e]->Fill(iphi_endc,e_.cellArea_[ix][iy]);
	  } //if iphi_endc
	  
	}//if ring
      }//iy
    } //ix

    for(int ring =0; ring<kEndcEtaRings;++ring){

      int index_e = ring+sign*kEndcEtaRings;
      
      etavsphi_endc[index_e]->Write();
      areavsphi_endc[index_e]->Write();
      etsumvsphi_endcp_corr[index_e]->Write();
      etsumvsphi_endcm_corr[index_e]->Write();
      etsumvsphi_endcp_uncorr[index_e]->Write();
      etsumvsphi_endcm_uncorr[index_e]->Write();
      esumvsphi_endcp[index_e]->Write();
      esumvsphi_endcm[index_e]->Write();

      delete etsumvsphi_endcp_corr[index_e];
      delete etsumvsphi_endcm_corr[index_e];
      delete etsumvsphi_endcp_uncorr[index_e];
      delete etsumvsphi_endcm_uncorr[index_e];
      delete etavsphi_endc[index_e];
      delete areavsphi_endc[index_e];
      delete esumvsphi_endcp[index_e];
      delete esumvsphi_endcm[index_e];
    }
  }//sign

  f.Close();
}


void PhiSymmetryCalibration_step2::readEtSums(){

  //read in ET sums
  
  int ieta,iphi,sign,ix,iy,dummy;
  double etsum;
  unsigned int nhits;
  std::ifstream etsum_barl_in("etsum_barl.dat", ios::in);
  while ( etsum_barl_in >> dummy >> ieta >> iphi >> sign >> etsum >> nhits ) {
    etsum_barl_[ieta][iphi][sign]+=etsum;
    nhits_barl_[ieta][iphi][sign]+=nhits;

  }

  std::ifstream etsum_endc_in("etsum_endc.dat", ios::in);
  while ( etsum_endc_in >> dummy >> ix >> iy >> sign >> etsum >> nhits>>dummy ) {
    etsum_endc_[ix][iy][sign]+=etsum;
    nhits_endc_[ix][iy][sign]+=nhits;
  }

  std::ifstream k_barl_in("k_barl.dat", ios::in);
  for (int ieta=0; ieta<kBarlRings; ieta++) {
    k_barl_in >> dummy >> k_barl_[ieta][0] >> k_barl_[ieta][1];
  }

  std::ifstream k_endc_in("k_endc.dat", ios::in);
  for (int ring=0; ring<kEndcEtaRings; ring++) {
    k_endc_in >> dummy >> k_endc_[ring][0] >> k_endc_[ring][1];
  }  

}



void PhiSymmetryCalibration_step2::setupResidHistos(){

  miscal_resid_barl_histos.resize(kBarlRings*kSides);
  correl_barl_histos.resize(kBarlRings*kSides);   

  miscal_resid_endc_histos.resize(kEndcEtaRings*kSides);
  correl_endc_histos.resize(kEndcEtaRings*kSides);

  for (int sign=0; sign<kSides; sign++) {
    for (int ieta=0; ieta<kBarlRings; ieta++) {
      int index_b = ieta+sign*kBarlRings;
      ostringstream t1; 
      t1<<"mr_barl_" << ieta+1 << "_" << sign;
      miscal_resid_barl_histos[index_b] = new TH1F(t1.str().c_str(),"",100,0.,2.);
      ostringstream t2;
      t2<<"co_barl_" << ieta+1 << "_" << sign;
      correl_barl_histos[index_b] = new TH2F(t2.str().c_str(),"",50,.5,1.5,50,.5,1.5);
    }

    for (int ring=0; ring<kEndcEtaRings; ring++) {
      int index_e = ring+sign*kEndcEtaRings;
      ostringstream t1;
      t1<<"mr_endc_" << ring+1 << "_" << sign;
      miscal_resid_endc_histos[index_e] = new TH1F(t1.str().c_str(),"",100,0.,2.);
      ostringstream t2;
      t2<<"co_endc_" << ring+1 << "_" << sign;
      correl_endc_histos[index_e] = new TH2F(t2.str().c_str(),"",50,.5,1.5,50,.5,1.5);
    }
  }//sign  

}


void  PhiSymmetryCalibration_step2::outResidHistos(){

  // output histograms of residual miscalibrations
  TFile f("PhiSymmetryCalibration_miscal_resid.root","recreate");

  for (int sign=0; sign<kSides; sign++) {
    for (int ieta=0; ieta<85; ieta++) {
      int index_b = ieta+sign*kBarlRings;
      miscal_resid_barl_histos[index_b]->Write();
      correl_barl_histos[index_b]->Write();
      delete miscal_resid_barl_histos[index_b];
      delete correl_barl_histos[index_b];
    }
  
    for (int ring=0; ring<39; ring++) {
      int index_e = ring+sign*kEndcEtaRings;
      miscal_resid_endc_histos[index_e]->Write();
      correl_endc_histos[index_e]->Write();      
      delete  miscal_resid_endc_histos[index_e];
      delete  correl_endc_histos[index_e];
    }
  }//sign

  f.Close(); 
}

DEFINE_FWK_MODULE(PhiSymmetryCalibration_step2);
