
#cell 1
import os 
import pandas as pd
import re
import xlsxwriter
import csv as cv
from xlrd import open_workbook


#cell 2
#global variable storage
active_bands = []
bands_with_4L = []


#cell 3
#change the path of file here
smarti_input = r'''C:\Users\shreyatp\Desktop\5G_code\data_file\Smarti_Latest.xlsx'''
mcc_read_file = 'MCC_Bands.txt'
mimo_filter_intermediate_ssim = 'mimo_intermediate_ssim.csv'
mimo_filter_intermediate_msim = 'mimo_intermediate_msim.csv'
mimo_filter_file = 'mimo_filter.csv'
mimo_final_ssim = 'mimo_final_ssim.csv'
mimo_final_msim = 'mimo_final_msim.csv'
list_trial_ssim = ["Parent-Combination","MIMO-INFO","MIMO-FALLBACK","SSIM"]
list_trial_msim = ["Parent-Combination","MIMO-INFO","MIMO-FALLBACK","MSIM"]
list_final_ssim = ["Parent-Combination","MIMO-INFO","SSIM"]
list_final_msim = ["Parent-Combination","MIMO-INFO","MSIM"]
log_file_ssim = 'log_output_ssim.txt'
log_file_msim = 'log_output_msim.txt'

#cell 4
with open(mimo_filter_intermediate_ssim,"w") as output_1,open(mimo_filter_intermediate_msim,"w") as output_2:
    writer_1 = cv.writer(output_1,delimiter=',',lineterminator='\n')
    writer_1.writerow(list_trial_ssim)
    writer_2 = cv.writer(output_2,delimiter=',',lineterminator='\n')
    writer_2.writerow(list_trial_msim)
    
    

#cell 5
with open(mimo_final_ssim,"w") as output_3,open(mimo_final_msim,"w") as output_4:
    writer_1 = cv.writer(output_3,delimiter=',',lineterminator='\n')
    writer_1.writerow(list_final_ssim)
    writer_1 = cv.writer(output_4,delimiter=',',lineterminator='\n')
    writer_1.writerow(list_final_msim)
    

#cell 6
'''Protocol Stack Entries from Smarti Configurator File'''
intra_read = pd.ExcelFile(smarti_input).parse('Protocol Stack Entries')
rx_1_band = intra_read.iloc[4:,4].tolist()
rx_1_bandwidth = intra_read.iloc[4:,5].tolist()
rx_1_mimo =  intra_read.iloc[4:,6].tolist()


rx_2 = intra_read.iloc[4:,7].tolist()
rx_2_bandwidth = intra_read.iloc[4:,8].tolist()
rx_2_mimo = intra_read.iloc[4:,9].tolist()

rx_3 = intra_read.iloc[4:,10].tolist()
rx_3_bandwidth = intra_read.iloc[4:,11].tolist()
rx_3_mimo = intra_read.iloc[4:,12].tolist()

rx_4 = intra_read.iloc[4:,13].tolist()
rx_4_bandwidth = intra_read.iloc[4:,14].tolist()
rx_4_mimo = intra_read.iloc[4:,15].tolist()

rx_5 = intra_read.iloc[4:,16].tolist()
rx_5_bandwidth = intra_read.iloc[4:,17].tolist()
rx_5_mimo = intra_read.iloc[4:,18].tolist()

mimo_fallback = intra_read.iloc[4:,25].tolist()
ssim = intra_read.iloc[4:,26].tolist()
msim = intra_read.iloc[4:,27].tolist()
#print("mimo_fallback:",mimo_fallback)

bcs_smarti_input = intra_read.iloc[4:,30].tolist()
#print("bcs_smarti_input:",bcs_smarti_input) #need to remove zero from here



child_entries_index_to_match = intra_read.iloc[4:,45].tolist()
child_entries_row_to_match = intra_read.iloc[4:,46].tolist()
#print("child_entries_index:",child_entries_index)
#print("child_entries_row:",child_entries_row)


#cell 7
#here need to extract bandwidth_combination_set as well from Smarti-Input + MIMO VARIANT
global string_input
string_input = []
i=0
output_file = "string_debug_2.txt"
input_file_write = open(output_file,'a')
bcs_smarti_input_wz = [] #need to remove zero from here
mimo_info = []
mimo_fallback_final = []
ssim_final = []
msim_final = []
for i in range(0,len(rx_1_band)):
    if rx_1_band[i] == 0:
        continue;     
    string_first = str(rx_1_band[i]) + str(rx_1_bandwidth[i])
    string_mimo_first = str(rx_1_mimo[i])
    bcs_smarti_input_wz.append(bcs_smarti_input[i])
    
    string_two = ""
    string_two_mimo = ""
    if rx_2[i] == 0:
        string_two = string_first
        string_two_mimo = string_mimo_first
    if rx_2[i] != 0:
        string_two = string_first + "-" + str(rx_2[i]) + str(rx_2_bandwidth[i])
        string_two_mimo = string_mimo_first + "-" + str(rx_2_mimo[i]) 

    
    string_three = ""
    string_three_mimo = ""
    if rx_3[i] == 0:
        string_three = string_two
        string_three_mimo = string_two_mimo
    if rx_3[i] != 0:
        string_three = string_two + "-" + str(rx_3[i]) + str(rx_3_bandwidth[i])
        string_three_mimo = string_two_mimo + "-" + str(rx_3_mimo[i])
   
    
    string_four = ""
    string_four_mimo = ""
    if rx_4[i] == 0 :
        string_four = string_three
        string_four_mimo = string_three_mimo
    if rx_4[i] != 0:
        string_four = string_three + "-" +  str(rx_4[i]) + str(rx_4_bandwidth[i])
        string_four_mimo = string_three_mimo + "-" + str(rx_4_mimo[i])
    
    
    string_five = ""
    string_five_mimo = ""
    if rx_5[i] == 0:
        string_five = string_four
        string_five_mimo = string_four_mimo
    if rx_5[i] != 0:
        string_five = string_four + "-" + str(rx_5[i]) + str(rx_5_bandwidth[i])
        string_five_mimo = string_four_mimo + "-" + str(rx_5_mimo[i])
    
    string_input.append(string_five)
    mimo_info.append(string_five_mimo)
    mimo_fallback_final.append(mimo_fallback[i])
    ssim_final.append(ssim[i])
    msim_final.append(msim[i])




#cell 8
def split_line_from_file_store(line_read):
    line_read_split_store = line_read.split(":")
    string_split_return = line_read_split_store[1]
    return string_split_return

#cell 9
def read_mcc_band_text(input_mcc_read):
    read_mcc_input = open(input_mcc_read,'r').read().split("\n")
    for line in read_mcc_input:
        if (re.findall(r'Active',line)):
            string_from_split_function = split_line_from_file_store(line)
            active_bands.append(string_from_split_function)
        
        if(re.findall(r'Bands with',line)):
            string_from_split_function = split_line_from_file_store(line)
            bands_with_4L.append(string_from_split_function)
    
    return active_bands,bands_with_4L

            
   

    

#cell 10
active_bands_main,bands_with_4L_main = read_mcc_band_text(mcc_read_file)
#print(active_bands_main,bands_with_4L_main)
bands_with_4L_main_list = bands_with_4L_main[0].split(',')
#print("bands_with_4L_main_list:",bands_with_4L_main_list)


#cell 11
'''
with open(mimo_trial, "a",encoding ='utf-8' ) as output:
    for i in range(0,len(string_input)):
        list_1 = [string_input[i],mimo_info[i],mimo_fallback_final[i]]
        writer = cv.writer(output,delimiter=',',lineterminator='\n')
        writer.writerow(list_1)
'''

#cell 12
string_filter_ssim =[]
string_filter_msim = []
mimo_filter_ssim = []
mimo_filter_msim = []
mimo_fallback_ssim = []
mimo_fallback_msim = []
with open(mimo_filter_intermediate_ssim,"a",encoding='utf-8') as output,open(mimo_filter_intermediate_msim,"a",encoding='utf-8') as output_1:
    for i in range(0,len(string_input)):
        number_regex = re.findall(r'\d+\.*\d*',str(string_input[i]))
        active_list = re.findall(r'\d+\.*\d*',str(active_bands_main[0]))
        mimo_regex = mimo_info[i].split("-")
        if (set(number_regex).issubset(active_list)) == True:
            #print("string:",string_input[i])
            for j in range(0,len(number_regex)):
                if number_regex[j] in bands_with_4L_main_list and ssim[i] == 1:
                    '''
                    print("mimo_info:",mimo_info[i])
                    print("mimo_fallback_final:",mimo_fallback_final[i])
                    print("ssim:",ssim[i])
                    '''
                    list_ssim = [string_input[i],mimo_info[i],mimo_fallback_final[i],ssim[i]]
                    writer = cv.writer(output,delimiter=',',lineterminator='\n')
                    writer.writerow(list_ssim)
                    #if "4*" in mimo_regex[j]:
                    #print("string_here:",string_input[i])
                    string_filter_ssim.append(string_input[i])
                    mimo_filter_ssim.append(mimo_info[i])
                    mimo_fallback_ssim.append(mimo_fallback_final[i])    
                    
                    break;
                
                if number_regex[j] in bands_with_4L_main_list and msim[i] == 1:
                    '''
                    print("mimo_info:",mimo_info[i])
                    print("mimo_fallback_final:",mimo_fallback_final[i])
                    print("msim:",msim[i])
                    '''
                    list_msim = [string_input[i],mimo_info[i],mimo_fallback_final[i],msim[i]]
                    writer = cv.writer(output_1,delimiter=',',lineterminator='\n')
                    writer.writerow(list_msim)
                
                    #if "4*" in mimo_regex[j]:
                    #print("string_here:",string_input[i])
                    string_filter_msim.append(string_input[i])
                    mimo_filter_msim.append(mimo_info[i])
                    mimo_fallback_msim.append(mimo_fallback_final[i])
                    break;


                    
                
'''              
print("string_filter:",string_filter)
with open(mimo_filter_file,"a",encoding='utf-8' ) as output:
    for i in range(0,len(string_filter)):
        list_1 = [string_filter[i],mimo_filter[i],mimo_fallback_filter[i]]
        writer = cv.writer(output,delimiter=',',lineterminator='\n')
        writer.writerow(list_1)  
'''


    

#cell 13
def superset(string_input):
    remove_element=[]
    for i in range(0,len(string_input)-1):
        for j in range(i+1,len(string_input)):
            max_value = max(int(string_input[i],2),int(string_input[j],2))
            min_value = min(int(string_input[i],2),int(string_input[j],2))
            exor_value = (int(string_input[i],2))^(int(string_input[j],2))
            if exor_value > max_value:
                continue;
            if exor_value <= max_value:
                exor_or_exor = (exor_value|min_value)^(max_value)
                if exor_or_exor == 0:
                    min_value = min(string_input[i],string_input[j])
                    if min_value not in remove_element:
                        remove_element.append(min_value)
    '''to remove elements from string_input=>first find index and then remove it'''
    for i in range(0,len(remove_element)):
        index_remove = string_input.index(remove_element[i])
        del string_input[index_remove]
    
    return string_input
    
            

#cell 14
def getKeysByValue(dictOfElements, valueToFind):
    #listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            #listOfKeys.append(item[0])
            return  item[0]

#cell 15
'''
ssim:output
'''
#print("mimo_fallback_ssim:",mimo_fallback_ssim)
flag_ssim = 0
index_monitor_one = 0
index_monitor_zero = 0

with open(mimo_final_ssim,"a",encoding='utf-8') as output,open(log_file_ssim,"a") as log_file_writer:
    for j in range(0,len(string_filter_ssim)-1):
        if mimo_fallback_ssim[j] == 1 and mimo_fallback_ssim[j+1] !=0 :
            list_ssim = [string_filter_ssim[j],mimo_filter_ssim[j],'1']
            writer = cv.writer(output,delimiter=',',lineterminator='\n')
            writer.writerow(list_ssim)

        if mimo_fallback_ssim[j] == 1:
            if flag_ssim == 1:
                string_binary = []
                flag_ssim = 0
                string_band = []
                mimo_list = []
                string_value_dict = {}
                for k in range(index_monitor_one,index_monitor_zero+1):
                    #print("string_monitor_one:",string_filter_ssim[k])
                    string_band.append(string_filter_ssim[k])
                    number_regex = re.findall(r'\d+\.*\d*',str(string_filter_ssim[k]))
                    split_list = mimo_filter_ssim[k].split('-')
                    mimo_list.append(mimo_filter_ssim[k])
                    for l in range(0,len(number_regex)):
                        if number_regex[l] not in bands_with_4L_main_list and ('4*' in split_list[l]):
                            #print("string:",string_filter_ssim[k],split_list[l])
                            #Downgrade
                            split_list[l] = '2x2'
                    #print("split_list:",split_list)
                    string_int = ""
                    string_split = string_filter_ssim[k].split('-')
                    for m in range(0,len(split_list)):
                        if 'A' in string_split[m] :
                            if '2x2' in split_list[m]:
                                string_int = string_int + '0'
                            if '4*' in split_list[m]:
                                string_int = string_int + '1'               

                        if 'B' in string_split[m] or 'C' in string_split[m]:
                            if '2x2' in split_list[m]:
                                string_int = string_int + '00'
                            if '4*' == split_list[m]:
                                string_int = string_int + '10'
                            if '44*' == split_list[m]:
                                string_int = string_int + '11'             

                        if 'D' in string_split[m]:
                            if '2x2' in split_list[m]:
                                string_int = string_int + '000'
                            if '4*' == split_list[m]:
                                string_int = string_int + '100'
                            if '44*' == split_list[m]:
                                string_int = string_int + '110'
                            if '444*' == split_list[m]:
                                string_int = string_int + '111'


                        if 'E' in string_split[m]:
                            if '2x2' in split_list[m]:
                                string_int = string_int + '0000'
                            if '4*' == split_list[m]:
                                string_int = string_int + '1000'
                            if '44*' == split_list[m]:
                                string_int = string_int + '1100'
                            if '444*' == split_list[m]:
                                string_int = string_int + '1110'
                            if '4444*' == split_list[m]:
                                string_int = string_int + '1111'

                        if 'F' in string_split[m]:
                            if '2x2' in split_list[m]:
                                string_int = string_int + '00000'
                            if '4*' == split_list[m]:
                                string_int = string_int + '10000'
                            if '44*' == split_list[m]:
                                string_int = string_int + '11000'
                            if '444*' == split_list[m]:
                                string_int = string_int + '11100'
                            if '4444*' == split_list[m]:
                                string_int = string_int + '11110'
                            if '44444*' == split_list[m]:
                                string_int = string_int + '11111'
                    string_binary.append(string_int)
                    integer = int(string_int,2)
                
                string_binary_without_duplicates = []
                for n in range(0,len(string_binary)):
                    if string_binary[n] not in string_binary_without_duplicates:
                        string_binary_without_duplicates.append(string_binary[n])
                string_value_dict = dict(zip(mimo_list,string_binary))
                #print("dict:",string_value_dict)
                log_file_writer.write("Band_Combination:{0}\n".format(string_band[0]))
                log_file_writer.write("Mimo_Variant-Binary_String:{0}\n".format(string_value_dict))
                log_file_writer.write("Binary_String_Only:{0}\n".format(string_binary))
                #print("string_binary:",string_binary)
                exor_result_hold = superset(string_binary_without_duplicates)
                #print("superset:",exor_result_hold)
                log_file_writer.write("Superset:{0}\n".format(exor_result_hold))
                final_to_csv = []
                for m in range(0,len(exor_result_hold)):
                    value_dict_compare = getKeysByValue(string_value_dict,exor_result_hold[m])
                    final_to_csv.append(value_dict_compare)     
                
                #print("value_to_csv:",final_to_csv)
                for p in range(0,len(final_to_csv)):
                    list_ssim = [string_band[0],final_to_csv[p],'1']
                    writer = cv.writer(output,delimiter=',',lineterminator='\n')
                    writer.writerow(list_ssim)
        
        if mimo_fallback_ssim[j] == 1 and mimo_fallback_ssim[j+1] == 0:
                #print("string_1:",string_filter_ssim[j])
                flag_ssim = 1
                index_monitor_one = j
        
        if mimo_fallback_ssim[j] == 0:
            index_monitor_zero = j




#cell 16
'''
msim 
'''
flag_msim = 0
index_monitor_one = 0
index_monitor_zero = 0

with open(mimo_final_msim,"a",encoding='utf-8') as output,open(log_file_msim,"a") as log_file_writer:
    for j in range(0,len(string_filter_msim)-1):
        if mimo_fallback_msim[j] == 1 and mimo_fallback_msim[j+1] !=0 :
            list_msim = [string_filter_msim[j],mimo_filter_msim[j],'1']
            writer = cv.writer(output,delimiter=',',lineterminator='\n')
            writer.writerow(list_msim)

        if mimo_fallback_msim[j] == 1:
            if flag_msim == 1:
                string_binary = []
                flag_msim = 0
                string_band = []
                mimo_list = []
                string_value_dict = {}
                for k in range(index_monitor_one,index_monitor_zero+1):
                    #print("string_monitor_one:",string_filter_msim[k])
                    string_band.append(string_filter_msim[k])
                    number_regex = re.findall(r'\d+\.*\d*',str(string_filter_msim[k]))
                    split_list = mimo_filter_msim[k].split('-')
                    mimo_list.append(mimo_filter_msim[k])
                    for l in range(0,len(number_regex)):
                        if number_regex[l] not in bands_with_4L_main_list and ('4*' in split_list[l]):
                            print("string:",string_filter_msim[k],split_list[l])
                            #Downgrade
                            split_list[l] = '2x2'
                    #print("split_list:",split_list)
                    string_int = ""
                    string_split = string_filter_msim[k].split('-')
                    for m in range(0,len(split_list)):
                        if 'A' in string_split[m] :
                            if '2x2' in split_list[m]:
                                string_int = string_int + '0'
                            if '4*' in split_list[m]:
                                string_int = string_int + '1'               

                        if 'B' in string_split[m] or 'C' in string_split[m]:
                            if '2x2' in split_list[m]:
                                string_int = string_int + '00'
                            if '4*' == split_list[m]:
                                string_int = string_int + '10'
                            if '44*' == split_list[m]:
                                string_int = string_int + '11'             

                        if 'D' in string_split[m]:
                            if '2x2' in split_list[m]:
                                string_int = string_int + '000'
                            if '4*' == split_list[m]:
                                string_int = string_int + '100'
                            if '44*' == split_list[m]:
                                string_int = string_int + '110'
                            if '444*' == split_list[m]:
                                string_int = string_int + '111'


                        if 'E' in string_split[m]:
                            if '2x2' in split_list[m]:
                                string_int = string_int + '0000'
                            if '4*' == split_list[m]:
                                string_int = string_int + '1000'
                            if '44*' == split_list[m]:
                                string_int = string_int + '1100'
                            if '444*' == split_list[m]:
                                string_int = string_int + '1110'
                            if '4444*' == split_list[m]:
                                string_int = string_int + '1111'

                        if 'F' in string_split[m]:
                            if '2x2' in split_list[m]:
                                string_int = string_int + '00000'
                            if '4*' == split_list[m]:
                                string_int = string_int + '10000'
                            if '44*' == split_list[m]:
                                string_int = string_int + '11000'
                            if '444*' == split_list[m]:
                                string_int = string_int + '11100'
                            if '4444*' == split_list[m]:
                                string_int = string_int + '11110'
                            if '44444*' == split_list[m]:
                                string_int = string_int + '11111'
                    string_binary.append(string_int)
                    integer = int(string_int,2)
                
                string_binary_without_duplicates = []
                for n in range(0,len(string_binary)):
                    if string_binary[n] not in string_binary_without_duplicates:
                        string_binary_without_duplicates.append(string_binary[n])
                string_value_dict = dict(zip(mimo_list,string_binary))
                #print("dict:",string_value_dict)
                log_file_writer.write("Band_Combination:{0}\n".format(string_band[0]))
                log_file_writer.write("Mimo_Variant-Binary_String:{0}\n".format(string_value_dict))
                log_file_writer.write("Binary_String_Only:{0}\n".format(string_binary))
                #print("string_binary:",string_binary)
                exor_result_hold = superset(string_binary_without_duplicates)
                #print("superset:",exor_result_hold)
                log_file_writer.write("Superset:{0}\n".format(exor_result_hold))
                final_to_csv = []
                for m in range(0,len(exor_result_hold)):
                    value_dict_compare = getKeysByValue(string_value_dict,exor_result_hold[m])
                    final_to_csv.append(value_dict_compare)     
                
                #print("value_to_csv:",final_to_csv)
                for p in range(0,len(final_to_csv)):
                    list_msim = [string_band[0],final_to_csv[p],'1']
                    writer = cv.writer(output,delimiter=',',lineterminator='\n')
                    writer.writerow(list_msim)
        
        if mimo_fallback_msim[j] == 1 and mimo_fallback_msim[j+1] == 0:
                #print("string_1:",string_filter_msim[j])
                flag_msim = 1
                index_monitor_one = j
        
        if mimo_fallback_msim[j] == 0:
            index_monitor_zero = j




#cell 17


