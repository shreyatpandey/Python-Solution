#cell 0
import csv as cv
import re as re
import os as os



#cell 1
#rootDir:- This is the path from which the file extraction would start
#rootDir = r'''C:\Users\shreyatp\Desktop\4G\trial'''
rootDir = r'\\mucfsv01b.imu.intel.com\KPI\00_Test_Results\INFRA\7560'

#cell 2
#path of output csv file
csvoutput_file = r'''C:\Users\shreyatp\Desktop\4G\infra_output_final_allfiles_modified_makingperfect_trial_final.csv'''

#cell 3
#column header of the csv file:- modifiable to include other parameter
list = ["Test_Case_Start_Day","Test_Case_Start_Time","HW_Version","SW_Version","Model","Revision","Infra_Place","TX","RX","TC_ID","TC_Group","Test_Type","Cell1_Duplex","Cell2_Duplex","Cell1_Band","Cell2_Band","Cell1_Bandwidth","Cell2_Bandwidth","TC_RSRP","Transfer_Type","Transfer_Direction","Cell1_Fading","Cell2_Fading","SNR","DL_Throughput","UL_Throughput","RSRP","Path_loss","DUT1_Polqa_Mos","DUT1_Polqa_Mos_Delay","DUT1_Below_Threshold","DUT2_polqa_mos","DUT2_polqa_mos_delay","DUT2_below_threshold","DUT1_Avg_Success_Rate","DUT2_Avg_Success_Rate","Path"]

#cell 4
#first column header would be written into csv file
with open(csvoutput_file, "w") as output:
    writer = cv.writer(output,delimiter=',',lineterminator='\n')
    writer.writerow(list)

#cell 5
#used for string_splitting_when_identifier_is_:
def function_split1(string_input,position,delim):
    found_word_line = string_input.partition(delim)[position]
    return found_word_line

#cell 6
#used for string_splitting_when_identifier = ','
def function_convert_string_to_list(nums):
    list_value = []
    value_string = str(nums)
    list_value = value_string.split(",")
    if list_value[0].isspace():
        list_value = list_value[:0]
    list_value = list_value[:-1]
    return list_value;

#cell 7
#used for string_splitting_when_identifier = '_'
def function_convert_string_to_list_1(nums):
    value_string = str(nums)
    value_string_space = value_string.replace("_"," ")
    list_value = value_string_space.split()
    return list_value;

#cell 8
for dirName,subdirList,fileList in os.walk(rootDir):
    for fname in fileList:
        regex_search_verdict = re.findall(r'verdict',fname,re.I)
        regex_search_result = re.findall(r'result',fname,re.I)
        if(regex_search_verdict or regex_search_result):
            print("fname:",fname)
            with open(csvoutput_file, "a",encoding ='utf-8' ) as output:
                fname_new = os.path.join(dirName,fname)
                try:
                    f_open = open(fname_new,'r')
                    filename_output = os.path.normpath(fname_new)
                    print("file_path:",filename_output)
                    flag = 0
                    flag_tcparam = 0
                    flag_tcs= 0
                    hw_board_version = []
                    sw_board_version = []
                    model = []
                    revision = []
                    test_case_trial = []
                    test_case_finished = []
                    snr_value = []
                    dl_throughput = []
                    ul_throughput = []
                    polqa_mos = []
                    iphone6s_mos = []
                    polqa_mos_delay = []
                    iphone6s_mos_delay = []
                    below_threshold = []
                    iphone6s_below_threshold = []
                    cell1_fading_profile = []
                    cell2_fading_profile = []
                    cell1_duplex = []
                    cell2_duplex = []
                    cell1_band = []
                    cell2_band = []
                    cell1_bandwidth =[]
                    cell2_bandwidth = []
                    test_type = []
                    tc_group = []
                    tc_id = []
                    ice7560 = []
                    iphone7p = []
                    xmm_rsrp = []
                    path_loss = []
                    infra_place = []
                    rxtx = []
                    transfer_direction = []
                    transfer_type = []
                    tc_rsrp = []
                   
                    flag_xmm7560_success_rate = 0
                    flag_iphone7p_new = 0
                    flag_snr_volte_global = 0
                    flag_rsrp_volte_global = 0
                    flag_path_loss_volte_global = 0
                    flag_xmm7560_srvcc_global = 0
                    
                    for line in f_open:
                        #extraction for HW Board Version,SW Board Version,Revision,Model
                        regex_hw_board_version = re.compile(r'HW Board Version',re.IGNORECASE)
                        regex_revision = re.compile(r'Revision',re.IGNORECASE)
                        regex_sw_board_version = re.compile(r'SW Build Version:',re.IGNORECASE)
                        regex_model = re.compile(r'Model',re.IGNORECASE)
                        
                        if(regex_hw_board_version.search(line)):
                            store_hw_board_version = function_split1(line,2,":")
                            hw_board_version.append(store_hw_board_version)
                        
                        if(regex_sw_board_version.search(line)):
                            store_sw_board_version = function_split1(line,2,":")
                            sw_board_version.append(store_sw_board_version)
                        
                        if(regex_revision.search(line)):
                            store_revision = function_split1(line,2,":")
                            revision.append(store_revision)
                        
                        if(regex_model.search(line)):
                            store_model = function_split1(line,2,":")
                            model.append(store_model)
                            
                        #extraction for information of tc_id
                        line_regex_tc_id = re.findall(r'tc_id:',line,re.I)
                        if(line_regex_tc_id):
                            flag_cell1_fading = 0
                            flag_cell2_fading = 0
                            flag_infra_place = 0
                            flag_low = 0
                            flag_high = 0
                            flag_tc_id = 0
                            #print("tc_id")
                            regex = (r'tc_id:\s+([^ ]+).*')
                            tc_regex = re.findall(regex,line)
                            #print("tc_regex:",tc_regex)
                            tc_regex_1 = function_convert_string_to_list_1(tc_regex[0])
                            #print("tc_regex_1:",tc_regex_1)
                            
                            #tc_id
                            tc_id.append(tc_regex_1[2])
                            
                            for i in range(0,len(tc_regex_1)):
                                regex_epa5 = re.findall(r'EPA5',tc_regex_1[i],re.I)
                                regex_static = re.findall(r'Static',tc_regex_1[i],re.I)
                                regex_etu = re.findall(r'ETU',tc_regex_1[i],re.I)
                                regex_eva = re.findall(r'EVA',tc_regex_1[i],re.I)
                                regex_pb3 = re.findall(r'PB3',tc_regex_1[i],re.I)
                                regex_near  = re.findall(r'near',tc_regex_1[i],re.I)
                                regex_far = re.findall(r'far',tc_regex_1[i],re.I)
                                regex_mid = re.findall(r'mid',tc_regex_1[i],re.I)
                                regex_muc = re.findall(r'MUC',tc_regex_1[i],re.I)
                                regex_nbg = re.findall(r'NBG',tc_regex_1[i],re.I)
                                regex_beizte = re.findall(r'BEIZTE',tc_regex_1[i],re.I)
                                regex_bei = re.findall(r'BEI',tc_regex_1[i],re.I)
                                regex_zte = re.findall(r'ZTE',tc_regex_1[i],re.I)
                                regex_beij = re.findall(r'Beij',tc_regex_1[i],re.I)
                                regex_hua = re.findall(r'HUA',tc_regex_1[i],re.I)
                                regex_AAL = re.findall(r'AAL',tc_regex_1[i],re.I)
                                regex_low = re.match(r'Lo',tc_regex_1[i])
                                regex_high = re.match(r'Hi',tc_regex_1[i])
                                
                               
                                
                                if(regex_epa5 or regex_static or regex_etu or regex_eva or regex_pb3):
                                    flag_cell1_fading = 1
                                    string_upload = tc_regex_1[i]
                                
                                if(regex_low and flag_cell1_fading == 1):
                                    flag_low = 1
                                   
                                elif(regex_high and flag_cell1_fading == 1):
                                    flag_high = 1
                                    
                                    
                                    
                                if((regex_near) or (regex_far) or (regex_mid)):
                                    flag_cell2_fading = 1
                                    cell2_fading_profile.append(tc_regex_1[i])
                                if(regex_beij or regex_zte or regex_beizte):
                                    flag_infra_place = 1
                                    infra_place.append("BEIZTE")
                                if(regex_hua or regex_bei):
                                    flag_infra_place = 1
                                    infra_place.append("BEIHUA")
                                if(regex_AAL):
                                    flag_infra_place = 1
                                    infra_place.append("AALNSN")
                                    
                                if(regex_muc or regex_nbg):
                                    flag_infra_place = 1
                                    infra_place.append(tc_regex_1[i])
                                    
                            if(flag_low == 1 and flag_cell1_fading == 1):
                                cell1_fading_profile.append(string_upload + "Low")
                            elif(flag_high == 1 and flag_cell1_fading == 1):
                                cell1_fading_profile.append(string_upload + "High")
                            elif(flag_low == 0 and flag_high == 0 and flag_cell1_fading == 1):
                                cell1_fading_profile.append(string_upload)
                                
                            if(flag_cell1_fading == 0):
                                cell1_fading_profile.append(" ")
                    
                            if(flag_cell2_fading == 0):
                                cell2_fading_profile.append(" ")
                            if(flag_infra_place == 0):
                                infra_place.append(" ")
                        
                        #extraction for cell_duplex,cell_bandwidth,cell_band,rx_tx,transfer_direction,transfer_type from tc parameters
                        if line.startswith("TC parameters"):
                            flag_tcparam = 1
                            flag_cell1_duplex = 0
                            flag_cell2_duplex = 0
                            flag_cell1_band = 0
                            flag_cell2_band = 0
                            flag_cell1_bandwidth = 0
                            flag_cell2_bandwidth = 0
                            flag_kpi_type = 0
                            flag_tc_group = 0
                            flag_rx_tx = 0
                            flag_transfer_direction = 0
                            flag_transfer_type = 0
                            flag_tc_rsrp = 0
                            flag_rsrp_dl_stop = 0
                        
                        elif(line.startswith("Test Case start:")):
                            flag_tcparam = 0
                            test_case_trial.append(line)
                            if(flag_cell1_duplex == 0):
                                cell1_duplex.append(" ")
                            if(flag_cell2_duplex == 0):
                                cell2_duplex.append(" ")
                            if(flag_cell1_band == 0):
                                cell1_band.append(" ")
                            if(flag_cell2_band == 0):
                                cell2_band.append(" ")
                            if(flag_cell1_bandwidth == 0):
                                cell1_bandwidth.append(" ")
                            if(flag_cell2_bandwidth == 0):
                                cell2_bandwidth.append(" ")
                            if(flag_kpi_type == 0):
                                test_type.append(" ")
                            if(flag_tc_group == 0):
                                tc_group.append(" ")
                            if(flag_rx_tx == 0):
                                rxtx.append([" "," "])
                            if(flag_transfer_direction == 0):
                                transfer_direction.append(" ")
                            if(flag_transfer_type == 0):
                                transfer_type.append(" ")
                            if(flag_tc_rsrp == 0):
                                tc_rsrp.append(" ")
                                
                                
                        elif (flag_tcparam == 1):
                            line_regex_cell1_rat = re.findall(r'cell1_rat:',line,re.I)
                            line_regex_rat = re.findall(r'rat:',line,re.I)
                            if(line_regex_cell1_rat):
                                regex = (r'cell1_rat:\s+([^ ]+).*')
                                cell1_duplex = re.findall(regex,line)
                                flag_cell1_duplex = 1
                                
                            if(line_regex_rat):
                                regex = (r'rat:\s+([^ ]+).*')
                                cell1_duplex = re.findall(regex,line)
                                flag_cell1_duplex = 1
                                
                            line_regex_cell2_rat = re.findall(r'cell2_rat:',line,re.I)
                            if(line_regex_cell2_rat):
                                regex = (r'cell2_rat:\s+([^ ]+).*')
                                cell2_duplex = re.findall(regex,line)
                                flag_cell2_duplex = 1
                            
                            line_regex_cell1_band = re.findall(r'cell1_band:',line,re.I)
                            line_regex_band = re.findall(r'band:',line,re.I)
                            if(line_regex_cell1_band):
                                regex = (r'cell1_band:\s+([^ ]+).*')
                                cell1_band = re.findall(regex,line)
                                flag_cell1_band = 1
                            if(line_regex_band):
                                regex = (r'band:\s+([^ ]+).*')
                                cell1_band = re.findall(regex,line)
                                flag_cell1_band = 1
                            
                            line_regex_cell2_band = re.findall(r'cell2_band:',line,re.I)
                            if(line_regex_cell2_band):
                                regex = (r'cell2_band:\s+([^ ]+).*')
                                cell2_band = re.findall(regex,line)
                                flag_cell2_band = 1
                                
                            line_regex_cell1_bandwidth = re.findall(r'cell1_bandwidth:',line,re.I)
                            if(line_regex_cell1_bandwidth):
                                regex = (r'cell1_bandwidth:\s+([^ ]+).*')
                                cell1_bandwidth = re.findall(regex,line)
                                flag_cell1_bandwidth = 1
                            
                            line_regex_bandwidth = re.findall(r'bandwidth:',line,re.I)    
                            if(line_regex_bandwidth):
                                regex = (r'bandwidth:\s+([^ ]+).*')
                                cell1_bandwidth = re.findall(regex,line)
                                flag_cell1_bandwidth = 1

                            line_regex_cell2_bandwidth = re.findall(r'cell2_bandwidth:',line,re.I)
                            if(line_regex_cell2_bandwidth):
                                regex = (r'cell2_bandwidth:\s+([^ ]+).*')
                                cell2_bandwidth = re.findall(regex,line)
                                flag_cell2_bandwidth = 1
                            
                            line_regex_transfer_direction = re.findall(r'transfer_direction:',line,re.I)
                            if(line_regex_transfer_direction):
                                regex = (r'transfer_direction:\s+([^ ]+).*')
                                transfer_direction_trial = re.findall(regex,line)
                                transfer_direction.append(transfer_direction_trial[0])
                                flag_transfer_direction = 1
                        
                            line_regex_transfer_direction = re.findall(r'transfer_type:',line,re.I)
                            if(line_regex_transfer_direction):
                                regex = (r'transfer_type:\s+([^ ]+).*')
                                transfer_type_trial = re.findall(regex,line)
                                transfer_type.append(transfer_type_trial[0])
                                flag_transfer_type = 1
                            
                            #line_regex_tc_rsrp = re.findall(r'rsrp:',line)
                            line_regex_tc_rsrsp_dl_stop =  re.findall(r'rsrp_dl_stop:',line,re.I)
                            if(line_regex_tc_rsrsp_dl_stop):
                                    regex = (r'rsrp_dl_stop:\s+([^ ]+).*')
                                    tc_rsrp_trial = re.findall(regex,line)
                                    tc_rsrp.append(tc_rsrp_trial[0])
                                    flag_tc_rsrp = 1 
                                    flag_rsrp_dl_stop = 1      
                                
                            if(line.startswith("* rsrp:") and (flag_rsrp_dl_stop == 0)):
                                    regex = (r'[a-zA-Z0-9]* rsrp:\s+([^ ]+).*')
                                    tc_rsrp_trial_new = re.findall(regex,line)
                                    tc_rsrp.append(tc_rsrp_trial_new[0])
                                    flag_tc_rsrp = 1
                        
                            line_regex_kpi_type = re.findall(r'kpi_type:',line,re.I)
                            line_regex_sweep_type = re.findall(r'sweep_type:',line,re.I)
                            line_regex_sweeps_type = re.findall(r'sweeps_type:',line,re.I)
                            if(line_regex_kpi_type):
                                flag_kpi_type = 1
                                #print("kpi_type:",line_regex_kpi_type)
                                regex = (r'kpi_type:\s+([^ ]+).*')
                                kpi_trial = re.findall(regex,line)
                                #print("kpi_trial:",kpi_trial)
                                test_type.append(kpi_trial[0])

                            if(line_regex_sweep_type):
                                flag_kpi_type = 1
                                #print("sweep_type:",line_regex_kpi_type)
                                regex = (r'sweep_type:\s+([^ ]+).*')
                                sweep_trial = re.findall(regex,line)
                                #print("sweep_trial:",sweep_trial)
                                test_type.append(sweep_trial[0])
                            if(line_regex_sweeps_type):
                                flag_kpi_type = 1
                                #print("sweep_type:",line_regex_kpi_type)
                                regex = (r'sweeps_type:\s+([^ ]+).*')
                                sweeps_trial = re.findall(regex,line)
                                #print("sweep_trial:",sweep_trial)
                                test_type.append(sweeps_trial[0])
                            
                            line_regex_tc_group = re.findall(r'tc_group:',line,re.I)
                            if(line_regex_tc_group):
                                flag_tc_group = 1
                                regex = (r'tc_group:\s+([^ ]+).*')
                                tc_group_trial = re.findall(regex,line)
                                tc_group.append(tc_group_trial[0])
                            
                            line_regex_rxtx = re.findall(r'fading_profile:',line,re.I)
                            if(line_regex_rxtx):
                                flag_rx_tx = 1
                                regex = (r'fading_profile:\s+([^ ]+).*')
                                rxtx_trial = re.findall(regex,line)
                                rxtx_trial_1 = function_convert_string_to_list_1(rxtx_trial[0])
                                for i in range(0,len(rxtx_trial_1)):
                                    regex_2x2 = re.findall(r'2x2',rxtx_trial_1[i],re.I)
                                    regex_4x4 = re.findall(r'4x4',rxtx_trial_1[i],re.I)
                                    regex_2x4 = re.findall(r'2x4',rxtx_trial_1[i],re.I)
                                    regex_1x4 = re.findall(r'1x4',rxtx_trial_1[i],re.I)
                                    regex_8x4 = re.findall(r'8x4',rxtx_trial_1[i],re.I)
                                    if(regex_2x2):
                                        #rxtx_final_insert = rxtx_trial_1[i].split("x")
                                        #print("rxtx_final_want:",rxtx_final_insert)
                                        rxtx.append(["2","2"])
                                    if(regex_4x4):
                                        rxtx.append(["4","4"])
                                    if(regex_2x4):
                                        rxtx.append(["2","4"])
                                    if(regex_1x4):
                                        rxtx.append(["1","4"])
                                    if(regex_8x4):
                                        rxtx.append(["8","4"])

                                        
                                
                        
                            line_regex_rxtx_dl = re.findall(r'fading_profile_dl:',line,re.I)
                            if(line_regex_rxtx_dl):
                                flag_rx_tx = 1
                                regex = (r'fading_profile_dl:\s+([^ ]+).*')
                                rxtx_trial = re.findall(regex,line)
                                rxtx_trial_1 = function_convert_string_to_list_1(rxtx_trial[0])
                                for i in range(0,len(rxtx_trial_1)):
                                    regex_2x2 = re.findall(r'2x2',rxtx_trial_1[i],re.I)
                                    regex_4x4 = re.findall(r'4x4',rxtx_trial_1[i],re.I)
                                    regex_2x4 = re.findall(r'2x4',rxtx_trial_1[i],re.I)
                                    regex_1x4 = re.findall(r'1x4',rxtx_trial_1[i],re.I)
                                    regex_8x4 = re.findall(r'8x4',rxtx_trial_1[i],re.I)
                                    if(regex_4x4):
                                        rxtx.append(["4","4"])
                                    if(regex_2x4):
                                        rxtx.append(["2","4"])
                                    if(regex_1x4):
                                        rxtx.append(["1","4"])
                                    if(regex_8x4):
                                        rxtx.append(["8","4"])
                            
        
                        
                                

                            
                        #extraction of dl_throuhgput,ul_throuhgput,polq_values,snr_values starts from here
                        if line.startswith("Test Case finished:"):
                            test_case_finished.append(line)
                            flag = 1
                            flag_ice_monitor = 0
                            flag_iphonep_monitor = 0
                            flag_snr = 0
                            flag_dl_throughput = 0
                            flag_ul_throughput = 0
                            flag_ice7560_dl_throughput = 0
                            flag_polqa_mos = 0
                            flag_polqa_mos_delay = 0
                            flag_below_threshold = 0
                            flag_xmm_rsrp_local = 0
                            flag_iphone6s_mos = 0
                            flag_iphone6s_mos_delay = 0
                            flag_iphone6s_below_threshold = 0
                            flag_path_loss = 0
                            flag_finished_fading_profile = 0
                            
                            

                        elif (line.startswith("Test Case start:") or line.startswith("Test Campaign end:") or line.startswith("PAT shutdown:")):
                            flag_tcs+=1
                            if(flag_tcs > 1):
                                if(flag_ice_monitor == 0):
                                    ice7560.append(" ")
                                if(flag_iphonep_monitor == 0):
                                    iphone7p.append(" ")
                                if(flag_snr == 0):
                                    snr_value.append(" ")
                                if(flag_dl_throughput == 0):
                                    dl_throughput.append(" ")
                                if(flag_ul_throughput == 0):
                                    ul_throughput.append(" ")
                                if(flag_polqa_mos == 0):
                                    polqa_mos.append(" ")
                                if(flag_polqa_mos_delay == 0):
                                    polqa_mos_delay.append(" ")
                                if(flag_below_threshold == 0):
                                    below_threshold.append(" ")
                                if(flag_xmm_rsrp_local == 0):
                                    xmm_rsrp.append(" ")
                                if(flag_iphone6s_mos == 0):
                                    iphone6s_mos.append(" ")
                                if(flag_iphone6s_mos_delay == 0):
                                    iphone6s_mos_delay.append(" ")
                                if(flag_iphone6s_below_threshold == 0):
                                    iphone6s_below_threshold.append(" ")
                                if(flag_path_loss == 0):
                                    path_loss.append(" ")         


                            flag = 0


                        elif flag:
                            #string matching for Throughput, use either re.match or re.findall
                            regex_dl_throughput = re.compile(r'DL Throughput',re.I)
                            #regex_dl_throughput = re.findall(r'Throughput',line,re.I)
                            regex_polqa_mos = re.match(r"POLQA MOS,",line)
                            regex_polqa_delay = re.match(r"POLQA MOS Delay",line)
                            regex_below_threshold = re.match(r"Below Threshold",line)
                            regex_ice7560 = re.match(r"ICE7560_pcie Success rate",line)
                            regex_iphone7p = re.match(r"iphone7P Success rate",line)
                            regex_rsrp = re.compile(r',RSRP',re.I)
                            ice7560_dl_throughput = line.startswith("ICE7560 DL Throughput,")
                            ice7560_ul_throughput = line.startswith("ICE7560 UL Throughput,")
                            dut_dl_throughput = line.startswith("DUT DL Throughput,")
                            samsung_galaxy_s7 = line.startswith("Samsung_Galaxy_S7 DL Throughput,")
                            dut_ul_throughput = line.startswith("DUT UL Throughput,")
                            iphone7_dl_throughput = line.startswith("iPhone_7 DL Throughput,")
                            

                            if(line.startswith(",SNR")): 
                                snr_value.append(line)
                                flag_snr = 1
                                
                            if(line.startswith("XMM7560_ICE_PCIe: ,SNR")):
                                snr_value.append(line)
                                flag_snr = 1
                                flag_snr_volte_global = 1
                            
                            if(line.startswith("Fading profile:")):
                                flag_finished_fading_profile = 1
                            
                            if(line.startswith(",RSRP") and flag_finished_fading_profile == 1):
                                flag_xmm_rsrp_local = 1
                                xmm_rsrp.append(line)
                            
                            if(line.startswith("XMM7560_ICE_PCIe: ,RSRP")):
                                flag_xmm_rsrp_local = 1
                                flag_rsrp_volte_global = 1
                                xmm_rsrp.append(line)
                                
                            if(line.startswith(",PL")):
                                flag_path_loss = 1
                                path_loss.append(line)
                            
                            if(line.startswith("XMM7560_ICE_PCIe: ,PL")):
                                flag_path_loss = 1
                                flag_path_loss_volte_global = 1
                                path_loss.append(line)
                            
                            if(ice7560_dl_throughput or dut_dl_throughput or samsung_galaxy_s7 or iphone7_dl_throughput): 
                                flag_ice7560_dl_throughput = 1
                                flag_dl_throughput = 1
                                dl_throughput.append(line)

                            if(regex_dl_throughput.search(line) and flag_ice7560_dl_throughput == 0):
                                dl_throughput.append(line)
                                flag_dl_throughput = 1
                            
                            if(dut_ul_throughput or ice7560_ul_throughput):
                                flag_ul_throughput = 1
                                ul_throughput.append(line)
                            
                            if(regex_polqa_mos):
                                polqa_mos.append(line)
                                flag_polqa_mos = 1
                            
                            if(re.match("XMM7560_ICE_PCIe: POLQA MOS,",line)):
                                flag_polqa_mos = 1
                                flag_snr_volte_global = 1
                                polqa_mos.append(line)
                            
                            
                            if(re.match(r"iPhone6SPlus_Infra1: POLQA MOS,",line)):
                                flag_iphone6s_mos = 1
                                iphone6s_mos.append(line)
                                

                            if(regex_polqa_delay and flag_snr == 1):
                                #print("polqa_delay")
                                polqa_mos_delay.append(line)
                                flag_polqa_mos_delay = 1
                                
                            if(line.startswith("XMM7560_ICE_PCIe: POLQA MOS Delay(avg)")):
                                flag_snr_volte_global = 1
                                flag_polqa_mos_delay = 1
                                polqa_mos_delay.append(line)
                                
                            
                            if(line.startswith("iPhone6SPlus_Infra1: POLQA MOS Delay(avg)")):
                                flag_iphone6s_mos_delay = 1
                                iphone6s_mos_delay.append(line)


                            if(regex_below_threshold):
                                #print("below_threshold")
                                below_threshold.append(line)
                                flag_below_threshold = 1
                            
                            if(line.startswith("XMM7560_ICE_PCIe: Below Threshold (%)")):
                                flag_below_threshold = 1
                                flag_snr_volte_global = 1
                                below_threshold.append(line)
                                
                            
                            
                            if(line.startswith("iPhone6SPlus_Infra1: Below Threshold (%)")):
                                flag_iphone6s_below_threshold = 1
                                iphone6s_below_threshold.append(line)
                            

                            if(regex_ice7560 or line.startswith("Average success rate:") or line.startswith("Success rate:")):
                                flag_ice_monitor = 1
                                ice7560.append(line)
                            
                            if(line.startswith("XMM7560:") ):
                                flag_ice_monitor = 1
                                flag_xmm7560_success_rate = 1
                                ice7560.append(line)
                                
                            
                            if(line.startswith("XMM7560_ICE_PCIe: Success rate:") or line.startswith("XMM7560_ICE_PCIe: Average success rate:")):
                                flag_ice_monitor = 1
                                flag_xmm7560_srvcc_global = 1
                                ice7560.append(line)
                               
                                

                            if(regex_iphone7p):
                                flag_iphonep_monitor = 1
                                iphone7p.append(line)
                            
                            if(line.startswith("iPhone7P:")):
                                flag_iphonep_monitor = 1
                                flag_iphone7p_new = 1
                                iphone7p.append(line)
                    

                    #case for verdict file which is completely empty
                    if not hw_board_version:
                        hw_board_version.append(" ")
                    if not sw_board_version:
                        sw_board_version.append(" ")
                    if not model:
                        model.append(" ")
                    if not revision:
                        revision.append(" ")
                    if not cell1_duplex:
                        cell1_duplex.append(" ")
                    if not cell1_band:
                        cell1_band.append(" ")
                    if not cell1_bandwidth:
                        cell1_bandwidth.append(" ")
                    if not cell2_duplex: 
                        cell2_duplex.append(" ")
                    if not cell2_band:
                        cell2_band.append(" ")
                    if not cell2_bandwidth:
                        cell2_bandwidth.append(" ")
                    if not cell1_fading_profile:
                        cell1_fading_profile.append(" ")
                    if not cell2_fading_profile:
                        cell2_fading_profile.append(" ")
                    if not tc_group:
                        tc_group.append(" ")
                    if not tc_id:
                        tc_id.append(" ")
                    if not rxtx:
                        rxtx.append([" "," "])

                    if not snr_value:
                        snr_value.append(" ")
                    if not dl_throughput:
                        dl_throughput.append(" ")
                    if not ul_throughput:
                        ul_throughput.append(" ")
                    if not polqa_mos:
                        polqa_mos.append(" ")
                    if not polqa_mos_delay:
                        polqa_mos_delay.append(" ")
                    if not below_threshold:
                        below_threshold.append(" ")
                    if not ice7560:
                        ice7560.append(" ")
                    if not iphone7p:
                        iphone7p.append(" ")
                    if not iphone6s_mos:
                        iphone6s_mos.append(" ")
                    if not iphone6s_mos_delay:
                        iphone6s_mos_delay.append(" ")
                    if not iphone6s_below_threshold:
                        iphone6s_below_threshold.append(" ")
                    if not xmm_rsrp:
                        xmm_rsrp.append(" ")
                    if not path_loss:
                        path_loss.append(" ")
                    if not test_type:
                        test_type.append(" ")
                    
                    print("tc_id:",tc_id)
                    #print("test_case_start:",)
                    #print("Cell1_rat:",cell1_duplex[0])
                    #print("Cell2_rat:",cell2_duplex[0])
                    #print("Cell1_band:",cell1_band[0])
                    #print("Cell2_band:",cell2_band[0])
                    #print("cell1_fading_profile:",cell1_fading_profile)
                    #print("cell2_fading_profile:",cell2_fading_profile)
                    
                    #print("tc_transfer_type",transfer_type)
                    #print("tc_transfer_direction",transfer_direction)
                    #print("tc_rsrp",tc_rsrp)
                    #print("RXTX:",rxtx)
                    #print("Snr_value:",snr_value)
                    #print("Dl Throughput:",dl_throughput)
                    #print("polqa_mos:",polqa_mos)
                    #print("iphone6s_mos:",iphone6s_mos)
                    #print("polqa_mos_delay:",polqa_mos_delay)
                    #print("iphone6s_mos_delay:",iphone6s_mos_delay)
                    #print("below_threshold:",below_threshold)
                    #print("iphone6s_below_threshold:",iphone6s_below_threshold)
                    #print("ice7560:",ice7560)
                    #print("iphone7p",iphone7p)
                    #print("xmm_rsrp:",xmm_rsrp)

                    #part-II:- csv
                    #base case:- cell1_fading profile

                    #print("Len_test_Case_finished:",len(test_case_finished))
                    #print("test_Case_finished:",test_case_finished)
                    #print("test_case_start",test_case_trial)
                    
                    #writing into csv file starts from here
                    loop_result = min(len(test_case_finished),len(test_case_trial))
                    for i in range(0,loop_result):
                        ice7560_final = []
                        iphone7p_final = []
                        snr_final = []
                        dl_throughput_final = []
                        ul_throughput_final = []
                        polqa_mos_final = []
                        iphone6s_mos_final = []
                        polqa_mos_delay_final = []
                        iphone6s_mos_delay_final = []
                        below_threshold_final = []
                        iphone6s_below_threshold_final = []
                        test_case_start_final = []
                        xmm_rsrp_final = []
                        path_loss_final = []

                        for y in range(0,len(test_case_trial)):
                            store_word_result = function_split1(test_case_trial[y],2,":")
                            store_word_result = store_word_result.split() 
                            test_case_start_final.append(store_word_result)

                        snr_final_min = min(i,len(snr_value)-1)
                        if(snr_value[snr_final_min] != " " and flag_snr_volte_global == 0):
                            snr_final = function_convert_string_to_list(snr_value[snr_final_min])
                            del snr_final[:1]
                            #print("snr_final_delete:",snr_final)
                            #print("len_snr_final_delete:",len(snr_final))
                            for x in range(0,len(snr_final)):
                                snr_final[x] = re.sub(r'SNR',"",snr_final[x])
                        elif(snr_value[snr_final_min] != " " and flag_snr_volte_global == 1):
                            snr_value_trial = (function_split1(snr_value[snr_final_min],2,":"))
                            snr_final = function_convert_string_to_list(snr_value_trial)
                            for x in range(0,len(snr_final)):
                                snr_final[x] = re.sub(r'SNR',"",snr_final[x])            
                        else:
                            snr_final.append(snr_value[snr_final_min])
                        
                        xmm_rsrp_min = min(i,len(xmm_rsrp)-1)
                        if(xmm_rsrp[xmm_rsrp_min]!= " " and flag_rsrp_volte_global == 0):
                            xmm_rsrp_final = function_convert_string_to_list(xmm_rsrp[xmm_rsrp_min])
                            del xmm_rsrp_final[:1]
                            for x in range(0,len(xmm_rsrp_final)):
                                xmm_rsrp_final[x] = re.sub(r'RSRP',"",xmm_rsrp_final[x])
                        elif(xmm_rsrp[xmm_rsrp_min]!= " " and flag_rsrp_volte_global == 1):
                            xmm_rsrp_trial = (function_split1(xmm_rsrp[xmm_rsrp_min],2,":"))
                            xmm_rsrp_trial = xmm_rsrp_trial.strip()
                            #print("xmm_rsrp_trial:",xmm_rsrp_trial)
                            xmm_rsrp_final = function_convert_string_to_list(xmm_rsrp_trial)
                            #print("xmm_rsrp_before_loop:",xmm_rsrp_final)
                            for x in range(0,len(xmm_rsrp_final)):
                                xmm_rsrp_final[x] = re.sub(r'RSRP',"",xmm_rsrp_final[x])
                        else:
                            xmm_rsrp_final.append(xmm_rsrp[xmm_rsrp_min])

                        dl_throughput_min = min(i,len(dl_throughput)-1)    
                        if(dl_throughput[dl_throughput_min] != " "):
                            dl_throughput_final = function_split1(dl_throughput[dl_throughput_min],2,",")
                            #print("dl_throuhgput_testing:",dl_throughput_final)
                            dl_throughput_final = function_convert_string_to_list(dl_throughput_final)
                            if not dl_throughput_final:
                                dl_throughput_final.append(" ")
                        else:
                            dl_throughput_final.append(dl_throughput[dl_throughput_min])
                        
                        ul_throughput_min = min(i,len(ul_throughput)-1)    
                        if(ul_throughput[ul_throughput_min] != " "):
                            ul_throughput_final = function_split1(ul_throughput[ul_throughput_min],2,",")
                            #print("dl_throuhgput_testing:",dl_throughput_final)
                            ul_throughput_final = function_convert_string_to_list(ul_throughput_final)
                            if not ul_throughput_final:
                                ul_throughput_final.append(" ")
                        else:
                            ul_throughput_final.append(ul_throughput[ul_throughput_min])

                        polqa_mos_min = min(i,len(polqa_mos)-1)
                        if(polqa_mos[polqa_mos_min]!= " " and flag_snr_volte_global == 0):
                            polqa_mos_final = function_convert_string_to_list(polqa_mos[polqa_mos_min])
                            del polqa_mos_final[:2]
                            if not polqa_mos_final:
                                polqa_mos_final.append("No Value")
                        elif(polqa_mos[polqa_mos_min]!=" " and flag_snr_volte_global == 1):
                            polqa_mos_trial = (function_split1(polqa_mos[polqa_mos_min],2,":"))
                            polqa_mos_final = function_convert_string_to_list(polqa_mos_trial)
                            del polqa_mos_final[:2]
                            if not polqa_mos_final:
                                polqa_mos_final.append("No Value")
                        else:
                            polqa_mos_final.append(polqa_mos[polqa_mos_min])
                        
                        iphone6s_mos_min = min(i,len(iphone6s_mos)-1)
                        if(iphone6s_mos[iphone6s_mos_min] != " "):
                            iphone6s_trial = (function_split1(iphone6s_mos[iphone6s_mos_min],2,":"))
                            iphone6s_mos_final = function_convert_string_to_list(iphone6s_trial)
                            del iphone6s_mos_final[:2]
                            if not iphone6s_mos_final:
                                iphone6s_mos_final.append("No Value")
                        else:
                            iphone6s_mos_final.append(iphone6s_mos[iphone6s_mos_min])
                        
                        

                                

                        polqa_mos_delay_min = min(i,len(polqa_mos_delay)-1)
                        if(polqa_mos_delay[polqa_mos_delay_min] != " " and flag_snr_volte_global == 0):
                            polqa_mos_delay_final = function_convert_string_to_list(polqa_mos_delay[polqa_mos_delay_min])
                            del polqa_mos_delay_final[:3]
                            if not polqa_mos_delay_final:
                                polqa_mos_delay_final.append("No Value")
                        elif(polqa_mos_delay[polqa_mos_delay_min]!=" " and flag_snr_volte_global == 1):
                            polqa_mos_delay_trial = (function_split1(polqa_mos_delay[polqa_mos_delay_min],2,":"))
                            polqa_mos_delay_final = function_convert_string_to_list(polqa_mos_delay_trial)
                            del polqa_mos_delay_final[:3]
                            if not polqa_mos_delay_final:
                                polqa_mos_delay_final.append("No Value")
                        else:
                            polqa_mos_delay_final.append(polqa_mos_delay[polqa_mos_delay_min])
                        
                        iphone6s_mos_delay_min = min(i,len(iphone6s_mos_delay)-1)
                        if(iphone6s_mos_delay[iphone6s_mos_delay_min] != " "):
                            iphone6s_trial = (function_split1(iphone6s_mos_delay[iphone6s_mos_delay_min],2,":"))
                            iphone6s_mos_delay_final = function_convert_string_to_list(iphone6s_trial)
                            del iphone6s_mos_delay_final[:3]
                            if not iphone6s_mos_delay_final:
                                iphone6s_mos_delay_final.append("No Value")
                        else:
                            iphone6s_mos_delay_final.append(iphone6s_mos_delay[iphone6s_mos_delay_min])
                        

                            
                        below_threshold_min = min(i,len(below_threshold)-1)
                        if(below_threshold[below_threshold_min] != " " and flag_snr_volte_global == 0):
                            below_threshold_final = function_convert_string_to_list(below_threshold[below_threshold_min])
                            del below_threshold_final[:3]
                            if not below_threshold_final:
                                below_threshold_final.append("No Value")
                        elif(below_threshold[below_threshold_min] != " " and flag_snr_volte_global == 1):
                            below_threshold_trial = (function_split1(below_threshold[below_threshold_min],2,":"))
                            below_threshold_final = function_convert_string_to_list(below_threshold_trial)
                            del below_threshold_final[:3]
                            if not below_threshold_final:
                                below_threshold_final.append("No Value")
                        else:
                            below_threshold_final.append(below_threshold[below_threshold_min])
                        
                        iphone6s_below_threshold_min = min(i,len(iphone6s_below_threshold)-1)
                        if(iphone6s_below_threshold[iphone6s_below_threshold_min] != " "):
                            iphone6s_below_threshold_trial = (function_split1(iphone6s_below_threshold[iphone6s_below_threshold_min],2,":"))
                            iphone6s_below_threshold_final = function_convert_string_to_list(iphone6s_below_threshold_trial)
                            del iphone6s_below_threshold_final[:3]
                            if not iphone6s_below_threshold_final:
                                iphone6s_below_threshold_final.append("No Value")
                        else:
                            iphone6s_below_threshold_final.append(iphone6s_below_threshold[iphone6s_below_threshold_min])
                        
            
                            
                            
                        ice7560_min = min(i,len(ice7560)-1)
                        if( (ice7560[ice7560_min] != " ") and flag_xmm7560_success_rate == 0 and flag_xmm7560_srvcc_global == 0):
                            ice7560_trial = (function_split1(ice7560[ice7560_min],2,":")) # this is a string
                            ice7560_final.append(ice7560_trial)
                        elif( (ice7560[ice7560_min] != " ") and flag_xmm7560_success_rate == 1 and flag_xmm7560_srvcc_global == 0):
                            ice7560_trial = (function_split1(ice7560[ice7560_min],2,":"))
                            ice7560_trial = (function_split1(ice7560_trial,2,":"))
                            ice7560_final.append(ice7560_trial)
                        elif( (ice7560[ice7560_min] != " ") and flag_xmm7560_srvcc_global == 1):
                            ice7560_trial = (function_split1(ice7560[ice7560_min],2,":"))
                            ice7560_trial_1 = (function_split1(ice7560_trial,2,":"))
                            ice7560_final.append(ice7560_trial_1)
                        else:
                            ice7560_final.append(ice7560[ice7560_min])

                            
                        iphone7p_min = min(i,len(iphone7p)-1)
                        if(iphone7p[iphone7p_min] != " " and flag_iphone7p_new == 0):
                            iphone7p_trial = (function_split1(iphone7p[iphone7p_min],2,":")) # this is a string
                            iphone7p_final.append(iphone7p_trial)
                        elif(iphone7p[iphone7p_min] != " " and flag_iphone7p_new == 1):
                            iphone7p_trial = (function_split1(iphone7p[iphone7p_min],2,":"))
                            iphone7p_trial = (function_split1(iphone7p_trial,2,":"))
                            iphone7p_final.append(iphone7p_trial)
                        else:
                            iphone7p_final.append(iphone7p[iphone7p_min])
                    
                    
                    
                    
                        path_loss_min = min(i,len(path_loss)-1)
                        if(path_loss[path_loss_min]!= " " and flag_path_loss_volte_global == 0):
                            path_loss_final = function_convert_string_to_list(path_loss[path_loss_min])
                            for x in range(0,len(path_loss_final)):
                                path_loss_final[x] = re.sub(r'PL',"",path_loss_final[x])
                        elif(path_loss[path_loss_min]!= " " and flag_path_loss_volte_global == 1):
                            path_loss_trial = (function_split1(path_loss[path_loss_min],2,":"))
                            path_loss_trial = path_loss_trial.strip()
                            #print("path_loss_trial:",path_loss_trial)
                            path_loss_final = function_convert_string_to_list(path_loss_trial)
                            for x in range(0,len(path_loss_final)):
                                path_loss_final[x] = re.sub(r'PL',"",path_loss_final[x])
                        else:
                            path_loss_final.append(path_loss[path_loss_min])

                        #print("Final_path_loss:",path_loss_final)
                        #print("snr_final:",snr_final)
                        #print("snr_final_length:",len(snr_final))
                        #print("dl_throughput_final:",dl_throughput_final)
                        #print("polqa_mos_final:",polqa_mos_final)
                        #print("iphone6s_mos_final:",iphone6s_mos_final)
                        #print("polqa_mos_final_length:",len(polqa_mos_final))
                        #print("polqa_mos_delay_final:",polqa_mos_delay_final)
                        #print("iphone6s_mos_delay_final:",iphone6s_mos_delay_final)
                        #print("below_threshold_final:",below_threshold_final)
                        #print("iphone6s_below_threshold_final:",iphone6s_below_threshold_final)
                        #print("ice7560_final or xmm7560:",ice7560_final)
                        #print("iphone70_final:",iphone7p_final)
                        #print("xmm_rsrp_final:",xmm_rsrp_final)
                        #print("Test_Type:",test_type)
                        
                        min_test_type = min(i,len(test_type)-1)
                        min_tc_group = min(i,len(tc_group)-1)
                        regex_rsrp = re.findall(r'rsrp',test_type[min_test_type],re.I)
                        
                        if(regex_rsrp):
                            for j in range(0,len(xmm_rsrp_final)):
                                #print("Len_xmm_rsrp_final:",len(xmm_rsrp_final))
                                min_rxtx = min(i,len(rxtx)-1)
                                #print("RXTX_0",rxtx[min_rxtx][0])
                                #print("RXTX_0",rxtx[min_rxtx][1])
                                min_infra_place = min(i,len(infra_place)-1)
                                min_test_case_start = min(i,len(test_case_start_final)-1)
                                min_dl = min(j,len(dl_throughput_final)-1)
                                min_ul = min(j,len(ul_throughput_final)-1)
                                min_polqa_mos = min(j,len(polqa_mos_final)-1)
                                min_iphone6s_mos_final = min(j,len(iphone6s_mos_final)-1)
                                min_polqa_mos_delay = min(j,len(polqa_mos_delay_final)-1)
                                min_iphone6s_mos_delay_final = min(j,len(iphone6s_mos_delay_final)-1) 
                                min_below_threshold = min(j,len(below_threshold_final)-1)
                                min_iphone6s_below_threshold_final = min(j,len(iphone6s_below_threshold_final)-1)
                                min_ice7560 = min(j,len(ice7560_final)-1)
                                min_iphone7p = min(j,len(iphone7p_final)-1)
                                min_snr = min(j,len(snr_final)-1)
                                min_path_loss = min(j,len(path_loss_final)-1)
                               
                                list1= [test_case_start_final[min_test_case_start][0],test_case_start_final[min_test_case_start][1],hw_board_version[0],sw_board_version[0],model[0],revision[0],infra_place[min_infra_place],rxtx[min_rxtx][0],rxtx[min_rxtx][1],tc_id[i],tc_group[min_tc_group],test_type[min_test_type],cell1_duplex[0],cell2_duplex[0],cell1_band[0],cell2_band[0],cell1_bandwidth[0],cell2_bandwidth[0],tc_rsrp[i],transfer_type[i],transfer_direction[i],cell1_fading_profile[min(i,len(cell1_fading_profile)-1)],cell2_fading_profile[min(i,len(cell2_fading_profile)-1)],snr_final[min_snr],dl_throughput_final[min_dl],ul_throughput_final[min_ul],xmm_rsrp_final[j],path_loss_final[min_path_loss],polqa_mos_final[min_polqa_mos],polqa_mos_delay_final[min_polqa_mos_delay],below_threshold_final[min_below_threshold],iphone6s_mos_final[min_iphone6s_mos_final],iphone6s_mos_delay_final[min_iphone6s_mos_delay_final],iphone6s_below_threshold_final[min_iphone6s_below_threshold_final],ice7560_final[min_ice7560],iphone7p_final[min_iphone7p],fname_new.encode("utf-8")]
                                writer = cv.writer(output,delimiter=',',lineterminator='\n')
                                writer.writerow(list1) 
                            
                        if not regex_rsrp:   
                            for k in range(0,len(snr_final)):
                                min_rxtx = min(i,len(rxtx)-1)
                                #print("tx:",rxtx[min_rxtx][0])
                                #print("rx:",rxtx[min_rxtx][1])
                                min_infra_place = min(i,len(infra_place)-1)
                                min_test_case_start = min(i,len(test_case_start_final)-1)
                                min_dl = min(k,len(dl_throughput_final)-1)
                                min_ul = min(k,len(ul_throughput_final)-1)
                                min_polqa_mos = min(k,len(polqa_mos_final)-1)
                                min_iphone6s_mos_final = min(k,len(iphone6s_mos_final)-1)
                                min_polqa_mos_delay = min(k,len(polqa_mos_delay_final)-1)
                                min_iphone6s_mos_delay_final = min(k,len(iphone6s_mos_delay_final)-1)
                                min_below_threshold = min(k,len(below_threshold_final)-1)
                                min_iphone6s_below_threshold_final = min(k,len(iphone6s_below_threshold_final)-1)
                                min_ice7560 = min(k,len(ice7560_final)-1)
                                min_iphone7p = min(k,len(iphone7p_final)-1)
                                min_xmm_rsrp = min(k,len(xmm_rsrp_final)-1)
                                min_path_loss = min(k,len(path_loss_final)-1)
                                list1 = [test_case_start_final[min_test_case_start][0],test_case_start_final[min_test_case_start][1],hw_board_version[0],sw_board_version[0],model[0],revision[0],infra_place[min_infra_place],rxtx[min_rxtx][0],rxtx[min_rxtx][1],tc_id[i],tc_group[min_tc_group],test_type[min_test_type],cell1_duplex[0],cell2_duplex[0],cell1_band[0],cell2_band[0],cell1_bandwidth[0],cell2_bandwidth[0],tc_rsrp[i],transfer_type[i],transfer_direction[i],cell1_fading_profile[min(i,len(cell1_fading_profile)-1)],cell2_fading_profile[min(i,len(cell2_fading_profile)-1)],snr_final[k],dl_throughput_final[min_dl],ul_throughput_final[min_ul],xmm_rsrp_final[min_xmm_rsrp],path_loss_final[min_path_loss],polqa_mos_final[min_polqa_mos],polqa_mos_delay_final[min_polqa_mos_delay],below_threshold_final[min_below_threshold],iphone6s_mos_final[min_iphone6s_mos_final],iphone6s_mos_delay_final[min_iphone6s_mos_delay_final],iphone6s_below_threshold_final[min_iphone6s_below_threshold_final],ice7560_final[min_ice7560],iphone7p_final[min_iphone7p],filename_output]
                                writer = cv.writer(output,delimiter=',',lineterminator='\n')
                                writer.writerow(list1)  
                    f_open.close()
                   
                except Exception as e:
                    #files which could not be opened is stored in log_file
                    log_file = open('log_infra.txt', 'a')
                    log_file.write("File failed to open: {0} and Exception : {1}\n".format(str(filename_output),str(e)))
                    log_file.close()
                    
#this will get displayed on jupyter console once all files in  directory have been finished reading                
os.write(1,"File reading finished\n".encode())



    


            

#cell 9


