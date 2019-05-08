
#cell 1
import pandas as pd
import itertools
import os
import re
import xlsxwriter
import xlrd
import csv as cv
import math

#cell 2
#Change the path of the file here
smarti_input = r'''C:\Users\shreyatp\Desktop\5G_code\data_file\smarti_file.xlsx'''
input_file_excel =  r'''C:\Users\shreyatp\Desktop\5G_code\data_file\Latest_UMTS_LTE_NR_RF-band_overview_201902.xlsx'''
csvoutput_file = r'''Band_Combination_Intermediate.csv'''
csvoutput_file_2 = r'''Band_Combination_Validation.csv'''
list_write = ["Parent-Combination","Parent-Bandwidth-Reference","Child-Combination","Child-Bandwidth-Reference","Parent-Band-Combination-Set","Child-Band-Combination-Set","Reason"]
list_write_2 = ["Parent-Combination","Parent-Smarti-BCS","Parent-BCS-List","Parent-Bandwidth-Reference-Superset","Child-Combination","Child-Bandwidth-Reference","Reason"]
reference_not_found = 'reference_not_found_4.txt'

#cell 3
with open(csvoutput_file, "w") as output,open(csvoutput_file_1, "w") as output_1,open(csvoutput_file_2, "w") as output_2:
    writer = cv.writer(output,delimiter=',',lineterminator='\n')
    writer.writerow(list_write)
    writer_1 = cv.writer(output_1,delimiter=',',lineterminator='\n')
    writer_1.writerow(list_write)
    writer_2 = cv.writer(output_2,delimiter=',',lineterminator='\n')
    writer_2.writerow(list_write_2)

#cell 4
'''Read Excel File and Store it in List'''
def read_excel(input_file_read,string_sheet_type):
    if(string_sheet_type == 'LTE Intra-band CA'):
        band_class = input_file_read.iloc[3:,0].tolist()
        bandwidth_combination_set = input_file_read.iloc[3:,12].tolist()
        band_combination = input_file_read.iloc[3:,13].tolist()
        nan_found = 0
        for i in range(0,len(band_class)):
            if str(band_class[i]) == 'nan':
                nan_found = i
                break;
        del band_class[nan_found:len(band_class)]
        del bandwidth_combination_set[nan_found:len(bandwidth_combination_set)]
        del band_combination[nan_found:len(band_combination)]
        return band_class,band_combination,bandwidth_combination_set
    else: #working-tested
        band_class = input_file_read.iloc[3:,0].tolist()
        band_combination = input_file_read.iloc[3:,7].tolist()
        bandwidth_combination_set = input_file_read.iloc[3:,12].tolist()
        nan_found = 0
        for i in range(0,len(band_class)):
            if str(band_class[i]) == 'nan':
                nan_found = i
                break;
        del band_class[nan_found:len(band_class)]
        del bandwidth_combination_set[nan_found:len(bandwidth_combination_set)]
        del band_combination[nan_found:len(band_combination)]
        return band_class,band_combination,bandwidth_combination_set
    

#cell 5
#Intra-Band
intra_read = pd.ExcelFile(input_file_excel).parse('LTE Intra-band CA')
intra_band_class,intra_band_combination,intra_band_combination_set = read_excel(intra_read,'LTE Intra-band CA')

#LTE 2 Bands
lte_bands_2_read = pd.ExcelFile(input_file_excel).parse('LTE 2 bands CA')
band_2_class, band_2_combination,band_2_combination_set = read_excel(lte_bands_2_read,'LTE 2 bands CA')


#LTE 2 Bands with DL
lte_bands_2_dl_read = pd.ExcelFile(input_file_excel).parse('LTE 2 bands DL with xUL')
band_2_class_dl, band_2_combination_dl,band_2_combination_set_dl = read_excel(lte_bands_2_dl_read,'LTE 2 bands DL with xUL')

#LTE 3 Bands
lte_bands_3_read = pd.ExcelFile(input_file_excel).parse('LTE 3 bands CA')
band_3_class, band_3_combination,band_3_combination_set = read_excel(lte_bands_3_read,'LTE 3 bands CA')

#LTE 4 Bands
lte_bands_4_read = pd.ExcelFile(input_file_excel).parse('LTE 4 bands CA')
band_4_class, band_4_combination,band_4_combination_set = read_excel(lte_bands_4_read,'LTE 4 bands CA')

#LTE 5 Bands
lte_bands_5_read = pd.ExcelFile(input_file_excel).parse('LTE 5 bands CA')
band_5_class, band_5_combination,band_5_combination_set = read_excel(lte_bands_4_read,'LTE 5 bands CA')



#cell 6
'''Protocol Stack Entries, Child and Parent Entries from Smarti-Input'''
intra_read = pd.ExcelFile(smarti_input).parse('Protocol Stack Entries')
rx_1_band = intra_read.iloc[4:,4].tolist()
rx_1_bandwidth = intra_read.iloc[4:,5].tolist()

rx_2 = intra_read.iloc[4:,7].tolist()
rx_2_bandwidth = intra_read.iloc[4:,8].tolist()

rx_3 = intra_read.iloc[4:,10].tolist()
rx_3_bandwidth = intra_read.iloc[4:,11].tolist()

rx_4 = intra_read.iloc[4:,13].tolist()
rx_4_bandwidth = intra_read.iloc[4:,14].tolist()


rx_5 = intra_read.iloc[4:,16].tolist()
rx_5_bandwidth = intra_read.iloc[4:,17].tolist()

bcs_smarti_input = intra_read.iloc[4:,30].tolist()


child_entries_index_to_match = intra_read.iloc[4:,45].tolist()
child_entries_row_to_match = intra_read.iloc[4:,46].tolist()



#cell 7
intra_read_one = pd.ExcelFile(smarti_input).parse('Child Entries')
child_entries_index = intra_read_one.iloc[3:,0].tolist()
child_entries_row = intra_read_one.iloc[3:,1].tolist()


#cell 8
'''Band-Combination String Generation and Bandwidth-Combination Set'''
global string_input
string_input = []
i=0
output_file = "string_debug_2.txt"
input_file_write = open(output_file,'a')
bcs_smarti_input_wz = [] #need to remove zero from here
for i in range(0,len(rx_1_band)):
    if rx_1_band[i] == 0:
        continue;     
    string_first = str(rx_1_band[i]) + str(rx_1_bandwidth[i])
    bcs_smarti_input_wz.append(bcs_smarti_input[i])
    
    
    string_two = ""
    if rx_2[i] == 0:
        string_two = string_first
    if rx_2[i] != 0:
        string_two = string_first + "-" + str(rx_2[i]) + str(rx_2_bandwidth[i])
    
    string_three = ""
    if rx_3[i] == 0:
        string_three = string_two
    if rx_3[i] != 0:
        string_three = string_two + "-" + str(rx_3[i]) + str(rx_3_bandwidth[i]) 
   
    
    string_four = ""
    if rx_4[i] == 0 :
        string_four = string_three
    if rx_4[i] != 0:
        string_four = string_three + "-" +  str(rx_4[i]) + str(rx_4_bandwidth[i])
    
    
    string_five = ""
    if rx_5[i] == 0:
        string_five = string_four
    if rx_5[i] != 0:
        string_five = string_four + "-" + str(rx_5[i]) + str(rx_5_bandwidth[i])
    
    input_file_write.write("string_five: {0}\n".format(string_five))
    string_input.append(string_five)




#cell 9
#removing duplicates from above list
string_input_wd = []
child_entries_index_to_match_wd = []
child_entries_row_to_match_wd = []
bcs_smarti_input_wzd = []
for i in range(0,len(string_input)):
    if string_input[i] not in string_input_wd:
        string_input_wd.append(string_input[i])
        child_entries_index_to_match_wd.append(child_entries_index_to_match[i])
        child_entries_row_to_match_wd.append(child_entries_row_to_match[i])
        bcs_smarti_input_wzd.append(bcs_smarti_input_wz[i])

input_trial_list = string_input_wd.copy()

#cell 10
'''From Smati-Input File as Reference Extracting Relevant Information from 3GPP Reference File'''
def band_combination_generator(final_result):
    intra_found_list = []
    band_2_found_list = []
    band_3_found_list = []
    band_4_found_list = []
    band_5_found_list = []
    
    intra_found_bcs = []
    band_2_found_bcs = []
    band_3_found_bcs = []
    band_4_found_bcs = []
    band_5_found_bcs = []
    
    for i in range(0,len(intra_band_class)):
        if re.match(final_result,intra_band_class[i]) and len(final_result) == len(intra_band_class[i]):    
            intra_band_combination_found = intra_band_combination[i]
            intra_found_list.append(intra_band_combination_found)
            intra_found_bcs.append(intra_band_combination_set[i])
        
    if len(intra_found_list) !=0 :
        return intra_found_list,intra_found_bcs
        
    for i in range(0,len(band_2_class)):
        if re.match(final_result,band_2_class[i]) and len(final_result) == len(band_2_class[i]):
            band_2_class_combination_found = band_2_combination[i]
            band_2_found_list.append(band_2_class_combination_found)
            band_2_found_bcs.append(band_2_combination_set[i])
        
    if len(band_2_found_list) !=0 :
        return band_2_found_list,band_2_found_bcs
    
    for i in range(0,len(band_3_class)):
         if re.match(final_result,band_3_class[i]) and len(final_result) == len(band_3_class[i]):
            band_3_class_combination_found = band_3_combination[i]  
            band_3_found_list.append(band_3_class_combination_found)
            band_3_found_bcs.append(band_3_combination_set[i])
    
    if len(band_3_found_list) !=0 :
        return band_3_found_list,band_3_found_bcs
    
    for i in range(0,len(band_4_class)):
         if re.match(final_result,band_4_class[i]) and len(final_result) == len(band_4_class[i]):
            band_4_class_combination_found = band_4_combination[i]
            band_4_found_list.append(band_4_class_combination_found)
            band_4_found_bcs.append(band_4_combination_set[i])
    
    if len(band_4_found_list) != 0 :
        return band_4_found_list,band_4_found_bcs
    
    for i in range(0,len(band_5_class)):
        if re.match(final_result,band_5_class[i]) and len(final_result) == len(band_5_class[i]):
            band_5_class_combination_found = band_5_combination[i]
            band_5_found_list.append(band_5_class_combination_found)
            band_5_found_bcs.append(band_5_combination_set[i])

    if len(band_5_found_list) != 0 :
        return band_5_found_list,band_5_found_bcs

    
    if len(intra_found_list) == 0 and len(band_2_found_list) == 0 and len(band_3_found_list) == 0 and len(band_4_found_list) == 0 and len(band_5_found_list) == 0:
        return (None,None)

#cell 11
'''String-Splitting Function'''
def split_further(string_input_split_further):
    input_match_store = []
    string_list_space = string_input_split_further.split("\n")
    flag_colon = 0
    for j in range(0,len(string_list_space)):
        if ":" in string_list_space[j]:
            flag_colon = 1
            loop_split = string_list_space[j].split(":")
            input_match_store.append(loop_split[1])
    if(flag_colon == 1):
        for l in range(0,len(input_match_store)):
            string_store = ','.join(input_match_store) #just replaced ',' with '\n'
        return string_store
    if(flag_colon == 0):
        for l in range(0,len(string_list_space)):
            string_input_no_change = ','.join(string_list_space) #just replaced ',' with '\n'
        return string_input_no_change

#cell 12
def combo_split(string_input_split_further):
    input_match_store = []
    string_list_space = string_input_split_further.split("\n")
    flag_colon = 0
    for j in range(0,len(string_list_space)):
        if ":" in string_list_space[j]:
            flag_colon = 1
            loop_split = string_list_space[j].split(":")
            input_match_store.append(loop_split[1])
    if(flag_colon == 1):
        return input_match_store
    if(flag_colon == 0):
        return string_list_space

#cell 13
def split_further_1(string_input_split_further):
    input_match_store = []
    string_list_space = string_input_split_further.split("\n")
    flag_colon = 0
    for j in range(0,len(string_list_space)):
        if ":" in string_list_space[j]:
            flag_colon = 1
            loop_split = string_list_space[j].split(":")
            input_match_store.append(loop_split[1])

    if(flag_colon == 1):
        return input_match_store

    if(flag_colon == 0):
        return string_list_space

#cell 14
def combination_input(main_parent_band,child_band):
    main_parent_list = combo_split(main_parent_band)
    child_band_list = combo_split(child_band)
    
    parent_one = re.findall(r'\d+\.*\d*',str(main_parent_list[0]))
    parent_two = re.findall(r'\d+\.*\d*',str(main_parent_list[1]))
    
    #parent-combination-generaion
    #first-two and store in superset_list
    superset = []
    for i in range(0,len(parent_one)):
        for j in range(0,len(parent_two)):
            comb_str = str(parent_one[i]) + "-" + str(parent_two[j])
            superset.append(comb_str)
    if(len(main_parent_list)>2):
        for k in range(2,len(main_parent_list)):
            parent_loop = re.findall(r'\d+\.*\d*',str(main_parent_list[k]))
            for m in range(0,len(superset)):
                for n in range(0,len(parent_loop)):
                    superset.append(superset[m] + "-" + str(parent_loop[n]))
            
                        
    found_index = 0
    for l in range(0,len(superset)):
        if superset[l].count('-') == len(main_parent_list)-1:
            found_index = l
            break
   
    del superset[:found_index]
    #print("parent_superset:",superset)
            
    
    #child-combination-generation
    child_one = re.findall(r'\d+\.*\d*',str(child_band_list[0]))
    child_two = re.findall(r'\d+\.*\d*',str(child_band_list[1]))
    
    superset_child = []
    
    for i in range(0,len(child_one)):
        for j in range(0,len(child_two)):
            comb_str = str(child_one[i]) + "-" + str(child_two[j])
            superset_child.append(comb_str)
    if(len(child_band_list)>2):
        for k in range(2,len(child_band_list)):
            child_loop = re.findall(r'\d+\.*\d*',str(child_band_list[k]))
            for m in range(0,len(superset_child)):
                for n in range(0,len(child_loop)):
                    superset_child.append(superset_child[m] + "-" + str(child_loop[n]))
            
                        
    found_index = 0
    child_list_return = []
    for l in range(0,len(superset_child)):
        if superset_child[l].count('-') == len(child_band_list)-1:
            found_index = l
            break
    

    del superset_child[0:found_index]
    #print("child_bcs_0:",superset_child)
    
    flag = 0
    for j in range(0,len(superset_child)):
        if any(superset_child[j] in s for s in superset) == False:
            flag = 1
    
    if(flag == 1):
        return False
    else:
        return True
            
                
    
    
   

#cell 15
'''Super-Set BCS and Band Combination Validatin Testing'''

def combination_here(parent_string_here,child_string_here,bcs_smarti_here):
    try:
        main_parent_band,main_parent_set = band_combination_generator(parent_string_here)
        if main_parent_band is None:
            input_file_write.write("{0}:Reference not found\n".format(parent_string_here))

        if main_parent_band is not None:
            band_combination_result,band_bcs = band_combination_generator(child_string_here)
            if band_combination_result is None:
                input_file_write.write("{0}:Reference not found\n".format(child_string_here))

            if band_combination_result is not None:
                #Need to add another loop for combination- main_superset
                
                if bcs_smarti_here == 1: #no superset required
                    flag = True # for good combination it would be required
                    bcs_set_check = [0]
                    flag_value = []
                    main_parent_string = split_further(main_parent_band[0])
                    main_parent_string = "0:"+ main_parent_string
                    for k in range(0,len(band_combination_result)):
                        band_combination_split = split_further(band_combination_result[k])
                        flag = combination_input(main_parent_band[0],band_combination_result[k])
                        if(flag == False):
                            #print("flag_value:",flag)
                            list_1 =[parent_string_here,bcs_smarti_here,bcs_set_check[0],main_parent_string,child_string_here,band_combination_split,"Child with BCS"+str(band_bcs[k])+"Not found in Superset"]
                            writer = cv.writer(output_2,delimiter=',',lineterminator='\n')
                            writer.writerow(list_1)  
                

                
                if bcs_smarti_here == 3:
                    #print("main_parent_string:",parent_string_here)
                    #print("child_string_here:",child_string_here)
                    bcs_set_check = ['0','1']
                    bcs_string = "0,1"
                    #definition_to_get_superset
                    flag_value = []
                    main_string_store = []
                    for i in range(0,len(bcs_set_check)):
                        parent_string = split_further(main_parent_band[i])
                        main_string_store.append(parent_string)
                    main_parent_string =" "
                    for i in range(0,len(main_string_store)):
                        if(i!=len(main_string_store)-1):
                            main_parent_string = main_parent_string + str(bcs_set_check[i]) + ":" + main_string_store[i] + "|"
                        else:
                            main_parent_string = main_parent_string + str(bcs_set_check[i]) + ":" + main_string_store[i]
                    for i in range(0,len(bcs_set_check)):  
                        for k in range(0,len(band_combination_result)):
                            band_combination_split = split_further(band_combination_result[k])
                            flag = combination_input(main_parent_band[i],band_combination_result[k])
                            flag_value.append(flag)
                    if len(set(flag_value)) <= 1 :
                        print("here")
                        list_1 =[parent_string_here,bcs_smarti_here,bcs_string,main_parent_string,child_string_here,band_combination_split,"Child with BCS"+str(band_bcs[k])+"Not found in Superset"]
                        writer = cv.writer(output_2,delimiter=',',lineterminator='\n')
                        writer.writerow(list_1)
                
                
                if bcs_smarti_here == 7:
                    bcs_set_check = ['0','1','2']
                    bcs_string = "0,1,2"
                    flag_value = []
                    main_string_store = []
                    for i in range(0,len(bcs_set_check)):
                        parent_string = split_further(main_parent_band[i])
                        main_string_store.append(parent_string)
                    main_parent_string =" "
                    for i in range(0,len(main_string_store)):
                        if(i!=len(main_string_store)-1):
                            main_parent_string = main_parent_string + str(bcs_set_check[i]) + ":" + main_string_store[i] + "|"
                        else:
                            main_parent_string = main_parent_string + str(bcs_set_check[i]) + ":" + main_string_store[i]
                    for i in range(0,len(bcs_set_check)):  
                        for k in range(0,len(band_combination_result)):
                            band_combination_split = split_further(band_combination_result[k])
                            flag = combination_input(main_parent_band[i],band_combination_result[k])
                            flag_value.append(flag)
                    if len(set(flag_value)) <= 1 :
                        print("here")
                        list_1 =[parent_string_here,bcs_smarti_here,bcs_string,main_parent_string,child_string_here,band_combination_split,"Child with BCS"+str(band_bcs[k])+"Not found in Superset"]
                        writer = cv.writer(output_2,delimiter=',',lineterminator='\n')
                        writer.writerow(list_1)
                
                
                if bcs_smarti_here == 15:
                    #print("parent_string:",parent_string_here)
                    #print("child_string:",child_string_here)
                    bcs_set_check = ['0','1','2','3']
                    bcs_string = "0,1,2,3"
                    flag_value = []
                    main_string_store = []
                    for i in range(0,len(bcs_set_check)):
                        parent_string = split_further(main_parent_band[i])
                        main_string_store.append(parent_string)
                    main_parent_string =" "
                    for i in range(0,len(main_string_store)):
                        if(i!=len(main_string_store)-1):
                            main_parent_string = main_parent_string + str(bcs_set_check[i]) + ":" + main_string_store[i] + "|"
                        else:
                            main_parent_string = main_parent_string + str(bcs_set_check[i]) + ":" + main_string_store[i]
                    for i in range(0,len(bcs_set_check)):  
                        for k in range(0,len(band_combination_result)):
                            band_combination_split = split_further(band_combination_result[k])
                            flag = combination_input(main_parent_band[i],band_combination_result[k])
                            flag_value.append(flag)
                    if len(set(flag_value)) <= 1 :
                        print("here")
                        list_1 =[parent_string_here,bcs_smarti_here,bcs_string,main_parent_string,child_string_here,band_combination_split,"Child with BCS"+str(band_bcs[k])+"Not found in Superset"]
                        writer = cv.writer(output_2,delimiter=',',lineterminator='\n')
                        writer.writerow(list_1)
                
                
                
                if bcs_smarti_here == 63:
                    #print("parent_string:",parent_string_here)
                    #print("child_string:",child_string_here)
                    bcs_set_check = ['0','1','2','3','4']
                    bcs_string = "0,1,2,3,4"
                    flag_value = []
                    main_string_store = []
                    for i in range(0,len(bcs_set_check)):
                        parent_string = split_further(main_parent_band[i])
                        main_string_store.append(parent_string)
                    main_parent_string =" "
                    for i in range(0,len(main_string_store)):
                        if(i!=len(main_string_store)-1):
                            main_parent_string = main_parent_string + str(bcs_set_check[i]) + ":" + main_string_store[i] + "|"
                        else:
                            main_parent_string = main_parent_string + str(bcs_set_check[i]) + ":" + main_string_store[i]
                    for i in range(0,len(bcs_set_check)):  
                        for k in range(0,len(band_combination_result)):
                            band_combination_split = split_further(band_combination_result[k])
                            flag = combination_input(main_parent_band[i],band_combination_result[k])
                            flag_value.append(flag)
                    if len(set(flag_value)) <= 1 :
                        list_1 =[parent_string_here,bcs_smarti_here,bcs_string,main_parent_string,child_string_here,band_combination_split,"Child with BCS"+str(band_bcs[k])+"Not found in Superset"]
                        writer = cv.writer(output_2,delimiter=',',lineterminator='\n')
                        writer.writerow(list_1)
                    

    except Exception as e:
        log_file = open('reference_bcs_not_found.txt', 'a')
        log_file.write("Exception:{0} ,parent_combination:{1} and child_combination:{2}\n".format(str(e),str(parent_string_here),str(child_string_here)))
        log_file.close()



            
            

#cell 16
'''Writing into Final Output CSV File'''
with open(csvoutput_file, "a",encoding ='utf-8' ) as output,open(csvoutput_file_1,"a",encoding = 'utf-8') as output_1, open(csvoutput_file_2, "a",encoding ='utf-8' ) as output_2,open(reference_not_found,"a") as input_file_write:
    for i in range(0,len(input_trial_list)):
        value_1 = child_entries_index_to_match_wd[i]
        value_2 = child_entries_row_to_match_wd[i]
        sum_total = value_1 + value_2-1
        for j in range(value_1,sum_total):
            protocol_stack_index = child_entries_row[j]
            required_child_index = string_input[protocol_stack_index] 
            combination_here(input_trial_list[i],required_child_index,bcs_smarti_input_wzd[i])
            

#cell 17
'''Removal of Duplicaties'''
rows = open(csvoutput_file_2).read().split("\n")
newrows = []
for row in rows:
    if row not in newrows:
         newrows.append(row)

writer = open('Band_Combination_Validation_Final.csv', 'w')
for line in newrows:
    writer.write(line + "\n")
writer.close()

rows = open(reference_not_found).read().split('\n')
newrows = []
for row in rows:
    if row not in newrows:
         newrows.append(row)

writer = open('reference_bc_not_found.txt', 'w')
for line in newrows:
    writer.write(line + "\n")
writer.close()


#cell 18


