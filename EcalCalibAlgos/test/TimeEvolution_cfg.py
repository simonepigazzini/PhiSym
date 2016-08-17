import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.absoluteICs = cms.bool(True)
process.applyCorrections = cms.bool(False)
process.variables = cms.vstring("IC")
process.ioFilesOpt = cms.PSet(    
    inputFiles = cms.vstring(
        ## weights vs multifit
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251562_251562.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415_m/summed_251562_251562.root"

        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015C_7415/summed_254790_254790.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015C_7415_m/summed_254790_254790.root"

        ## TRANSPORT
        
        # # 2012C Boff
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012C_v1/summed_200781_200798.root",
        
        # # 2015A Boff
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015A_v2/summed_250896_250896.root",
        
        # # 2012D Bon
        #"$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2012D_newThr/summed_208538_208686.root",
        
        # # 2015B Bon
        #"$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015B_7415/summed_251562_251562.root",
        #"$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/summed_256843_256843.root"

        # 2015D Boff
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Run2015D_Boff_v1/summed_259971-1_260043-410.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Run2015D_Boff_v1/summed_260043-411_260108-355.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Run2015D_Boff_v1/summed_260132-1_260235-25.root",
        
        # Comm2016
        # weights
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/summed_268930-1_269000-30.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_weights/summed_269012-1_269073-68.root"

        # multifit
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Comm2016_multifit/summed_268930-1_269000-30.root"

        # Run2015D
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_256677-366_256729-326.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_256729-1100_256729-1510.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_256729-1511_256801-84.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_256729-327_256729-708.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_256729-709_256729-1099.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_256801-85_256843-158.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_256843-1300_256868-200.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_256843-159_256843-528.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_256843-529_256843-1299.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_256868-202_256926-35.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_256926-36_256941-294.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257394-41_257397-56.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257397-57_257399-271.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257400-1354_257487-220.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257400-1_257400-357.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257400-358_257400-735.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257400-736_257400-1353.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257487-1069_257490-254.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257487-221_257487-492.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257487-493_257487-773.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257487-774_257487-1068.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257490-255_257490-585.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257613-1119_257645-374.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257613-14_257613-541.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257613-542_257613-1118.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257645-375_257645-931.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257645-932_257682-342.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257682-343_257751-267.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257751-268_257816-98.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257816-99_257822-33.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257822-1363_257969-147.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257822-34_257822-669.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257822-670_257822-1362.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_257969-148_257969-634.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258129-30_258158-344.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258158-1572_258159-483.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258158-345_258158-925.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258158-926_258158-1571.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258159-484_258177-579.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258177-1260_258211-122.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258177-580_258177-1259.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258211-123_258287-193.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258425-3_258434-144.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258434-145_258440-320.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258440-321_258443-290.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258443-291_258448-731.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258655-60_258703-237.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258703-238_258706-344.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258706-345_258712-255.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258712-256_258742-361.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_258742-362_258750-197.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_259626-83_259685-132.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_259685-133_259686-252.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_259686-253_259721-233.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_259721-234_259721-408.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_259809-53_259821-104.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_259821-105_259862-433.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_history/summed_259862-434_259891-108.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_tag2012_thr2016/summed_259626-134_259685-183.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_tag2012_thr2016/summed_259685-184_259721-408.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2015D_tag2012_thr2016/summed_259809-53_259862-343.root",
        
        # Run2016B
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272760-72_272775-150.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272775-151_272784-75.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272784-76_272786-51.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272786-52_272798-481.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272798-1385_272811-172.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272798-482_272798-924.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272798-925_272798-1384.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272811-173_272818-7.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272818-8_272827-104.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_272930-1_273013-214.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/summed_273013-215_273017-646.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273158-1_273158-744.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273158-745_273158-1279.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273302-1_273402-162.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273402-163_273425-203.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273425-204_273450-647.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273492-71_273503-598.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273554-77_273555-173.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273725-83_273730-321.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_273730-322_273730-2126.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_274094-105_274146-67.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/summed_274159-1_274172-95.root"

        # # Run2016B thr700
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_273158-1_273158-1279.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_273302-1_273402-162.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_273402-163_273449-67.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_273449-68_273450-647.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_273554-77_273555-173.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_273730-1056_273730-2126.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_274094-108_274146-67.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_274241-817_274251-546.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_274283-2_274319-225.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_274335-60_274345-170.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_274382-94_274388-1820.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_274420-94_274440-207.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_274440-208_274442-752.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_274954-37_274969-461.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_274969-462_274999-94.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_274999-95_275001-2061.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_275059-78_275074-647.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_275124-106_275125-989.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_275282-91_275310-1012.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_275310-1013_275337-413.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_275337-414_275371-569.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr700/summed_275375-127_275376-2374.root"
        
        # # Run2016B thr1000
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_273158-1_273158-1279.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_273302-1_273402-162.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_273402-163_273449-67.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_273449-68_273450-647.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_273554-77_273555-173.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_273730-1056_273730-2126.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_274094-108_274146-67.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_274241-817_274251-546.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_274283-2_274319-225.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_274335-60_274345-170.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_274382-94_274388-1820.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_274420-94_274440-207.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_274440-208_274442-752.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_274954-37_274969-461.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_274969-462_274999-94.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_274999-95_275001-2061.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_275059-78_275074-647.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_275124-106_275125-989.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_275282-91_275310-1012.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_275310-1013_275337-413.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_275337-414_275371-569.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1000/summed_275375-127_275376-2374.root"

        # Run2016B thr1200
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_273158-1_273158-1279.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_273302-1_273402-162.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_273402-163_273449-67.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_273449-68_273450-647.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_273554-77_273555-173.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_273730-1056_273730-2126.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_274094-108_274146-67.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_274241-817_274251-546.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_274283-2_274319-225.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_274335-60_274345-170.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_274382-94_274388-1820.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_274420-94_274440-207.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_274440-208_274442-752.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_274954-37_274969-461.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_274969-462_274999-94.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_274999-95_275001-2061.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_275059-78_275074-647.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_275124-106_275125-989.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_275282-91_275310-1012.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_275310-1013_275337-413.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_275337-414_275371-569.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_thr1200/summed_275375-127_275376-2374.root"

    ),

    correctionsFiles = cms.vstring(
        # #---Boff
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2012C_v1/corrections_200781_200798.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_12_patch4/src/PhiSym/EcalCalibAlgos/ntuples/2015A_v2/corrections_250896_250896.txt"

        #---Bon
        #"/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_15/src/PhiSym/EcalCalibAlgos/ntuples/2012D_newThr/corrections_208538_208686.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_15/src/PhiSym/EcalCalibAlgos/corrections_208538_208686.txt",
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_15/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT_v5/corrections_251562_251562.txt"
        #"/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_15/src/PhiSym/EcalCalibAlgos/ntuples/2015D_7415/corrections_256843_256843.txt"
        # "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_15/src/PhiSym/EcalCalibAlgos/corrections_256843_256843.txt"
        
        # Run2016B
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/corrections_272760-72_272775-150.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/corrections_272775-151_272784-75.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/corrections_272784-76_272786-51.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/corrections_272786-52_272798-481.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/corrections_272798-1385_272811-172.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/corrections_272798-482_272798-924.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/corrections_272798-925_272798-1384.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/corrections_272811-173_272818-7.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/corrections_272818-8_272827-104.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/corrections_272930-1_273013-214.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/corrections_273013-215_273017-646.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/corrections_273158-1_273158-744.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/corrections_273158-745_273158-1279.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/corrections_273302-1_273402-162.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/corrections_273402-163_273425-203.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/corrections_273425-204_273450-647.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/corrections_273492-71_273503-598.txt",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/corrections_273554-77_273555-173.txt",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/corrections_273725-83_273730-321.txt",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/corrections_273730-322_273730-2126.txt",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/corrections_274094-105_274146-67.txt",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/corrections_274159-1_274172-95.txt"
    )
)

