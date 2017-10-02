#!/usr/bin/env python
# import ROOT in batch mode
import sys
import os
import json
import subprocess
import copy
import tempfile
import time
from commands import getstatusoutput
from joblib import Parallel, delayed, load, dump

oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
from optparse import OptionParser
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

# load FWLite C++ librarie
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.gSystem.Load("libDataFormatsEcalDetId.so");
ROOT.gSystem.Load("libPhiSymEcalCalibDataFormats.so");
ROOT.AutoLibraryLoader.enable()

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events, Lumis

from FWCore.PythonUtilities.LumiList import LumiList

# Load TFile and TTree
from ROOT import TTree, TFile

# getting arrays
#from array import array
import numpy as n

def resetInterval(interval, index):
    interval["index"] = index
    interval["firstRun"] = 0
    interval["firstLumi"] = 0
    interval["unixTimeStart"] = 0
    interval["lastRun"] = 0
    interval["lastLumi"] = 0
    interval["unixTimeEnd"] = 0
    interval["norm"] = 0
    interval["nHit"] = 0
    interval["nLS"] =0
    interval["unixTimeMean"] = 0
    interval["flag"] = ""

def closeInterval(interval):
    interval["unixTimeMean"]=interval["unixTimeStart"]+float(interval["unixTimeMean"])/float(interval["norm"])

def startInterval(interval, run, lumi, start):
    interval["firstRun"] = run
    interval["firstLumi"] = lumi
    interval["unixTimeStart"] = start

def readLumisFromFile(fullpath_file, puJsonN_shm_file, lumiList_shm_file, debug=True):
    """
    Read lumis from a single file and store the relevant information in a common map.
    NB: this function is run in parallel
    """

    puJson = load(puJson_shm_file, mmap_mode='r')
    lumiList = load(lumiList_shm_file, mmap_mode='r')
    readMap = {}
    if debug:
        print "Reading files:", fullpath_file
    try:
        lumis = Lumis(fullpath_file)
    except:
        print "File "+fullpath_file+" NOT FOUND!"
        return;

    for i,lumi in enumerate(lumis):
        lumi.getByLabel(labelPhiSymInfo,handlePhiSymInfo)
        phiSymInfo = handlePhiSymInfo.product()
        # skipping BAD lumiSections
        if lumiList and not lumiList.contains(phiSymInfo.back().getStartLumi().run(),
                                              phiSymInfo.back().getStartLumi().luminosityBlock()):
            if debug:
                print "Lumi section not in json file"
            continue
        
        # normalization is rate * PU
        beginTime = lumi.luminosityBlockAuxiliary().beginTime().unixTime()
        run_num = str(lumi.luminosityBlockAuxiliary().run())
        lumi_num = str(lumi.luminosityBlockAuxiliary().luminosityBlock())
        if run_num not in puJson.keys() or lumi_num not in puJson[run_num].keys():
            print run_num
            print lumi_num
            #print puJson[run_num][lumi_num]
            print "Lumi skipped since not in puJson"
            continue
        timeMap[beginTime] = {
            "run" : copy.deepcopy(phiSymInfo.back().getStartLumi().run()),
            "lumi" : copy.deepcopy(phiSymInfo.back().getStartLumi().luminosityBlock()),
            "totHitsEB" : copy.deepcopy(phiSymInfo.back().GetTotHitsEB()),
            "norm" : copy.deepcopy(phiSymInfo.back().GetNEvents()*float(puJson[run_num][lumi_num]))
        }

        if debug:
            print "====>"
            print "Run "+str(phiSymInfo.back().getStartLumi().run())+" Lumi "+str(phiSymInfo.back().getStartLumi().luminosityBlock())+" beginTime "+str(beginTime)
            print "NEvents in this LS "+str(phiSymInfo.back().GetNEvents())
            print "TotHits EB "+str(phiSymInfo.back().GetTotHitsEB())+" Avg occ EB "+str(float(phiSymInfo.back().GetTotHitsEB())/phiSymInfo.back().GetNEvents()) 
            print "TotHits EE "+str(phiSymInfo.back().GetTotHitsEE())+" Avg occ EE "+str(float(phiSymInfo.back().GetTotHitsEE())/phiSymInfo.back().GetNEvents()) 
    
    # close current file
    lumis._tfile.Close()

    return readMap


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("", "--debug", dest="debug", action='store_true')
    parser.add_option("", "--saveIsolatedIntervals", dest="saveIsolatedIntervals", action='store_true')
    parser.add_option("-n", "--maxHit", dest="maxHit", type="int", default=7000000000)
    parser.add_option("-f", "--fileList", dest="fileList", type="string", default="fileList.txt")
    parser.add_option("-d", "--dataset", dest="dataset", type="string", default="")
    parser.add_option("-o", "--output", dest="output", type="string", default="readMap.root")
    parser.add_option("-p", "--prefix", dest="prefix", type="string", default="root://xrootd-cms.infn.it/")
    parser.add_option("-t","--maxTime", dest="maxTime", type = "int", default=86400)
    parser.add_option("-l","--lumiFile", dest="lumiFile", type = "string", default="")
    parser.add_option("-j","--jobs", dest="jobs", type = int, default=4, help="number of parallel jobs")
    (options, args) = parser.parse_args()

    current_time = str(time.time()).replace(".", "_")
    
    if options.dataset != "":
        print "Getting files from DAS for dataset "+options.dataset
        if getstatusoutput("das_client.py --query='file dataset="+options.dataset+" instance=prod/phys03' --limit 0 | grep '/store/' > /tmp/filelist_"+current_time+".dat"):
            options.fileList = '/tmp/filelist_%s.dat' % current_time

    with open(options.fileList,'r') as textfile:
        files = [line.strip() for line in textfile]

    handlePhiSymInfo  = Handle ("std::vector<PhiSymInfo>")
    labelPhiSymInfo = ("PhiSymProducer")

    ### get PU informations
    if options.lumiFile != "":
        lumiList = LumiList(os.path.expandvars(options.lumiFile))
        with open(options.lumiFile) as lumis_file:
            lumiJson = json.load(lumis_file)
            runs = lumiJson.keys()
    else:
        cmd_lumi = subprocess.Popen(['${CMSSW_BASE}/src/PhiSym/EcalCalibAlgos/scripts/get_dataset_lumi_json.sh', options.dataset, 'phys03'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        lumi_string, err_lumi = cmd_lumi.communicate()
        lumiJson = json.loads(lumi_string)
        runs = lumiJson.keys()

    runs_string = ','.join(runs)

    # cmd_pu = subprocess.Popen(['${CMSSW_BASE}/src/PhiSym/EcalCalibAlgos/scripts/get_pu_info.sh '+runs_string+' > /tmp/pu_list_'+current_time+'.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # pu_string, err_pu = cmd_pu.communicate()
    puJson = {}
    # with open('/tmp/pu_list_%s.txt' % current_time) as pu_file:
    with open('/tmp/pu_list_1506358477_14.txt') as pu_file:
        puJson = json.load(pu_file)

    ### Read lumis from files and store information in timeMap
    #   The loop on the files is run in parallel
    #   timeMap, puJson and lumiList are shared memory
    timeMap={}
    temp_folder = tempfile.mkdtemp()
    ### shared timeMap
    # timeMap_shm_file = os.path.join(temp_folder, 'timeMap_shm.mmap')
    # if os.path.exists(timeMap_shm_file): os.unlink(timeMap_shm_file)
    # dump(timeMap, timeMap_shm_file)
    # timeMap = load(timeMap_shm_file, mmap_mode='w+')
    ### shared lumiList
    lumiList_shm_file = os.path.join(temp_folder, 'lumiList_shm.mmap')
    if os.path.exists(lumiList_shm_file): os.unlink(lumiList_shm_file)
    dump(lumiList, lumiList_shm_file)
    ### shared puJson
    puJson_shm_file = os.path.join(temp_folder, 'puJson_shm.mmap')
    if os.path.exists(puJson_shm_file): os.unlink(puJson_shm_file)
    dump(puJson, puJson_shm_file)

    for aline in files:
        fullpath_file = options.prefix+aline
        maps = Parallel(n_jobs=options.jobs)(delayed(readLumisFromFile)
                                             (options.prefix+ifile, puJson_shm_file, lumiList_shm_file, False)
                                             for ifile in files)

    print(maps)
        
    nMaxHits=options.maxHit
    maxStopTime=options.maxTime

    interval={}

    full_interval_count=0
    isolated_interval_count=0

    currentInterval={}
    resetInterval( currentInterval , 0 )

    # splitting logic
    print("### Start splitting logic")
    for key in sorted(timeMap):    
        if currentInterval["nLS"]==0 and currentInterval["unixTimeStart"]==0:
           #start a new interval
            startInterval( currentInterval, timeMap[key]["run"], timeMap[key]["lumi"], key)

        if key-currentInterval["unixTimeStart"]>=maxStopTime and currentInterval["unixTimeStart"] != 0:

            if currentInterval["norm"] >= nMaxHits/2.:
                # Enough statistics. Closing previous interval 
                if options.debug:
                    print "Closing interval by time condition"

                closeInterval( currentInterval )
                currentInterval["flag"]="S"
                interval[ currentInterval["unixTimeStart" ] ]=dict(currentInterval)
                full_interval_count+=1

            else:
                lastInterval=-1
                if len(interval.keys())>0:
                    lastInterval=sorted(interval.keys())[-1]
                if lastInterval>0:
                    if (currentInterval["unixTimeEnd"]-interval[lastInterval]["unixTimeStart"]<=maxStopTime):
                    #merging with last interval
                        if options.debug:
                            print "Merging interval"
                        closeInterval( currentInterval )
                        interval[lastInterval]["lastRun"]=currentInterval["lastRun"]
                        interval[lastInterval]["lastLumi"]=currentInterval["lastLumi"]
                        interval[lastInterval]["unixTimeEnd"]=currentInterval["unixTimeEnd"]
                        interval[lastInterval]["unixTimeMean"]=(interval[lastInterval]["unixTimeMean"]*interval[lastInterval]["norm"]+currentInterval["unixTimeMean"]*currentInterval["norm"])/(float(interval[lastInterval]["norm"]+currentInterval["norm"]))
                        interval[lastInterval]["nHit"]+=currentInterval["nHit"]
                        interval[lastInterval]["norm"]+=currentInterval["norm"]
                        interval[lastInterval]["flag"]="M"
                    else:
                        if options.saveIsolatedIntervals:
                            if options.debug:
                                print "Save short interval"
                            closeInterval( currentInterval )
                            currentInterval["flag"]="I"
                            interval[ currentInterval["unixTimeStart" ] ]=dict(currentInterval)
                            full_interval_count+=1
                        else:
                            if options.debug:
                                print "Dropping interval"
                            #dropping interval
                            isolated_interval_count+=1
                else:
                    if options.debug:
                        print "First interval is a short one!"
                    if options.saveIsolatedIntervals:
                        if options.debug:
                            print "Save short interval"
                        closeInterval( currentInterval )
                        currentInterval["flag"]="I"
                        interval[ currentInterval["unixTimeStart" ] ]=dict(currentInterval)
                        full_interval_count+=1
                    else:
                        if options.debug:
                            print "Dropping interval"
                        #dropping interval
                        isolated_interval_count+=1

            # Start a new interval
            resetInterval( currentInterval, full_interval_count )
            startInterval( currentInterval, timeMap[key]["run"], timeMap[key]["lumi"], key)

        currentInterval["lastRun"] = timeMap[key]["run"]
        currentInterval["lastLumi"] = timeMap[key]["lumi"]
        currentInterval["unixTimeEnd"] = key+23.1
        #currentInterval["nHit"] += timeMap[key]["totHitsEB"]
        currentInterval["norm"] += timeMap[key]["norm"]
        currentInterval["nLS"] +=1
        currentInterval["unixTimeMean"] += float((key-currentInterval["unixTimeStart"]+11.55)*timeMap[key]["norm"])

        if currentInterval["norm"] >= nMaxHits:
            # adding as new interval
            closeInterval( currentInterval )
            currentInterval["flag"]="F"
            interval[ currentInterval["unixTimeStart"] ]=dict(currentInterval)
            full_interval_count+=1
            # resetting for next interval
            resetInterval( currentInterval, full_interval_count )

    interval_number=n.zeros(1,dtype=int)
    hit=n.zeros(1,dtype=long)
    norm=n.zeros(1,dtype=float)
    flag=bytearray(2)
    nLSBranch=n.zeros(1,dtype=int)
    firstRunBranch=n.zeros(1,dtype=int)
    lastRunBranch=n.zeros(1,dtype=int)
    firstLumiBranch=n.zeros(1,dtype=int)
    lastLumiBranch=n.zeros(1,dtype=int)
    unixTimeStartBranch=n.zeros(1,dtype=float)
    unixTimeEndBranch=n.zeros(1,dtype=float)
    unixTimeMeanBranch=n.zeros(1,dtype=float)

    outFile = ROOT.TFile(options.output, "RECREATE")
    if not outFile:
        print "Cannot open outputFile "+options.output

    tree = ROOT.TTree('iov_map', 'IOV map')
    tree.Branch('index', interval_number, 'index/I')
    tree.Branch('flag', flag, 'flag/C')
    tree.Branch('nHit', hit, 'nHit/L')
    tree.Branch('norm', norm, 'norm/D')
    tree.Branch('nLS', nLSBranch, 'nLS/I')
    tree.Branch('firstRun', firstRunBranch, 'firstRun/I')
    tree.Branch('lastRun', lastRunBranch, 'lastRun/I')
    tree.Branch('firstLumi', firstLumiBranch, 'firstLumi/I')
    tree.Branch('lastLumi', lastLumiBranch, 'lastLumi/I')
    tree.Branch('unixTimeStart', unixTimeStartBranch, 'unixTimeStart/D')
    tree.Branch('unixTimeEnd', unixTimeEndBranch, 'unixTimeEnd/D')
    tree.Branch('unixTimeMean', unixTimeMeanBranch, 'unixTimeMean/D')

    for key in sorted(interval):
        interval_number[0]=interval[key]["index"]
        flag[0]=interval[key]["flag"][0]
        hit[0]=interval[key]["nHit"]
        norm[0]=interval[key]["norm"]
        nLSBranch[0]=interval[key]["nLS"]
        firstRunBranch[0]=interval[key]["firstRun"]
        lastRunBranch[0]=interval[key]["lastRun"]
        firstLumiBranch[0]=interval[key]["firstLumi"]
        lastLumiBranch[0]=interval[key]["lastLumi"]
        unixTimeStartBranch[0]=interval[key]["unixTimeStart"]
        unixTimeEndBranch[0]=interval[key]["unixTimeEnd"]
        unixTimeMeanBranch[0]=interval[key]["unixTimeMean"]
        tree.Fill()

    outFile.Write()
    outFile.Close()

    if options.debug:
        for key in sorted(interval):
            print "------------------"
            print "Index: " + str(interval[key]["index"])
            print "nHit: " + str(interval[key]["nHit"])
            print "norm: " + str(interval[key]["norm"])
            print "nLS: " + str(interval[key]["nLS"])
            print "First Run: " + str(interval[key]["firstRun"])
            print "Last Run: " + str(interval[key]["lastRun"])
            print "First Lumi: " + str(interval[key]["firstLumi"])
            print "Last Lumi: " + str(interval[key]["lastLumi"])
            print "Unix Time Start: " + str(interval[key]["unixTimeStart"])
            print "Unix Time End: " + str(interval[key]["unixTimeEnd"])
            print "Unix Time Mean: " + str(interval[key]["unixTimeMean"])
            print "------------------"

    print "====> FULL_INTERVALS:"+str(full_interval_count) + " ISOLATED INTERVALS:" + str(isolated_interval_count)



                  



