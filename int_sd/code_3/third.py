#cell 1
import os
import pandas as pd
import itertools
import csv as cv
import re
import glob
import xlwt
from xlrd import open_workbook

#cell 2
'''NR File and MCC_Read_File Path'''
nr_file_input = r'''C:\Users\shreyatp\Desktop\5G_code\5G_Files\latest.xls'''
mcc_read_file = 'MCC_Bands.txt'
trial_output_file = 'band_combination_trial.csv'
input_list = ['Band-Combination']

#cell 3
with open(trial_output_file,"w") as output:
    writer_1 = cv.writer(output,delimiter=',',lineterminator='\n')
    writer_1.writerow(input_list)

#cell 4
'''Extracting Band Combination Parameter:ActiveBands + Class'''
nr_read = pd.ExcelFile(nr_file_input).parse('NRF_PS_NR_MRDC_BAND_COMBINATION')
nr_read_list = []
for i in range(0,len(nr_read)):
    nr_read_list.append(nr_read.iloc[i,:].tolist())
column_names_sheet_1 = list(nr_read)
'''Total of 7 Bands'''
band_1 = nr_read.iloc[0:,5].tolist()
nr_check_1 = nr_read.iloc[0:,6].tolist()
bandclass_1 = nr_read.iloc[0:,7].tolist()
band_2 = nr_read.iloc[0:,8].tolist()
nr_check_2 = nr_read.iloc[0:,9].tolist()
bandclass_2 = nr_read.iloc[0:,10].tolist()

band_3 = nr_read.iloc[0:,11].tolist()
nr_check_3 = nr_read.iloc[0:,12].tolist()
bandclass_3 = nr_read.iloc[0:,13].tolist()

band_4 = nr_read.iloc[0:,14].tolist()
nr_check_4 = nr_read.iloc[0:,15].tolist()
bandclass_4 = nr_read.iloc[0:,16].tolist()

band_5 = nr_read.iloc[0:,17].tolist()
nr_check_5 = nr_read.iloc[0:,18].tolist()
bandclass_5 = nr_read.iloc[0:,19].tolist()

band_6 = nr_read.iloc[0:,20].tolist()
nr_check_6 = nr_read.iloc[0:,21].tolist()
bandclass_6 = nr_read.iloc[0:,22].tolist()

band_7 = nr_read.iloc[0:,23].tolist()
nr_check_7 = nr_read.iloc[0:,24].tolist()
bandclass_7 = nr_read.iloc[0:,25].tolist()

#cell 5
'''Combination_Index'''
nrf_3gpp_feature_set_combination_index = nr_read.iloc[0:,32].tolist()
nrf_3gpp_feature_set_combination_count = nr_read.iloc[0:,33].tolist()


'''NRF_PS_NR_FEATURE_SET_COMBINATI'''
nrf_ps_nr_feature_set_combinati = pd.ExcelFile(nr_file_input).parse('NRF_PS_NR_FEATURE_SET_COMBINATI')
nrf_nr_feature_set_per_band_index =  nrf_ps_nr_feature_set_combinati.iloc[0:,1].tolist()
column_names_nr_combinati = list(nrf_ps_nr_feature_set_combinati)


'''NRF_PS_MRDC_FEATURE_SET_COMBINA'''
nrf_ps_mrdc_feature_set_combina = pd.ExcelFile(nr_file_input).parse('NRF_PS_MRDC_FEATURE_SET_COMBINA')
nrf_mrdc_feature_set_per_band_index =  nrf_ps_mrdc_feature_set_combina.iloc[0:,1].tolist()


'''NRF_PS_NR_FEATURE_SETS_PER_BAND'''
nrf_ps_nr_feature_sets_per_band = pd.ExcelFile(nr_file_input).parse('NRF_PS_NR_FEATURE_SETS_PER_BAND')
nrf_ps_nr_feature_sets_per_band_list = []
for i in range(0,len(nrf_ps_nr_feature_sets_per_band)):
    nrf_ps_nr_feature_sets_per_band_list.append(nrf_ps_nr_feature_sets_per_band.iloc[i,:].tolist())
column_names_nr_per_band = list(nrf_ps_nr_feature_sets_per_band)

'''NRF_PS_MRDC_FEATURE_SETS_PER_BAND'''
nrf_ps_mrdc_feature_sets_per_band = pd.ExcelFile(nr_file_input).parse('NRF_PS_MRDC_FEATURE_SETS_PER_BA')

'''NRF_PS_NR_FEATURE_SET_UL_TABLE'''
nrf_ps_nr_feature_set_ul_table = pd.ExcelFile(nr_file_input).parse('NRF_PS_NR_FEATURE_SET_UL_TABLE')
nrf_ps_nr_feature_set_ul_table_list = []
column_names_nr_ul_table = list(nrf_ps_nr_feature_set_ul_table)
for i in range(0,len(nrf_ps_nr_feature_set_ul_table)):
    nrf_ps_nr_feature_set_ul_table_list.append(nrf_ps_nr_feature_set_ul_table.iloc[i,:].tolist())

'''NRF_PS_NR_FEATURE_SET_DL_TABLE'''
nrf_ps_nr_feature_set_dl_table = pd.ExcelFile(nr_file_input).parse('NRF_PS_NR_FEATURE_SET_DL_TABLE')
nrf_ps_nr_feature_set_dl_table_list = []
column_names_nr_dl_table = list(nrf_ps_nr_feature_set_dl_table)
for i in range(0,len(nrf_ps_nr_feature_set_dl_table)):
    nrf_ps_nr_feature_set_dl_table_list.append(nrf_ps_nr_feature_set_dl_table.iloc[i,:].tolist())

'''NRF_PS_NR_FEATURE_SETS_UL_PER_CC'''
nrf_ps_nr_feature_sets_ul_per_cc = pd.ExcelFile(nr_file_input).parse('NRF_PS_NR_FEATURE_SETS_UL_PER_C')
nrf_ps_nr_feature_sets_ul_per_cc_list = []
column_names_nr_ul_per_cc = list(nrf_ps_nr_feature_sets_ul_per_cc)
for i in range(0,len(nrf_ps_nr_feature_sets_ul_per_cc)):
    nrf_ps_nr_feature_sets_ul_per_cc_list.append(nrf_ps_nr_feature_sets_ul_per_cc.iloc[i,:].tolist())
print('nrf_ps_nr_feature_sets_ul_per_cc_list',nrf_ps_nr_feature_sets_ul_per_cc_list)

'''NRF_PS_NR_FEATURE_SETS_DL_PER_CC'''
nrf_ps_nr_feature_sets_dl_per_cc = pd.ExcelFile(nr_file_input).parse('NRF_PS_NR_FEATURE_SETS_DL_PER_C')
nrf_ps_nr_feature_sets_dl_per_cc_list = []
column_names_nr_dl_per_cc = list(nrf_ps_nr_feature_sets_dl_per_cc)
for i in range(0,len(nrf_ps_nr_feature_sets_dl_per_cc)):
    nrf_ps_nr_feature_sets_dl_per_cc_list.append(nrf_ps_nr_feature_sets_dl_per_cc.iloc[i,:].tolist())
print('nrf_ps_nr_feature_sets_dl_per_cc_list',nrf_ps_nr_feature_sets_dl_per_cc_list)


'''NRF_PS_LTE_FEATURE_SET_UL_TABLE'''
nrf_ps_lte_feature_set_ul_table = pd.ExcelFile(nr_file_input).parse('NRF_PS_LTE_FEATURE_SET_UL_TABLE')

'''NRF_PS_LTE_FEATURE_SET_DL_TABLE'''
nrf_ps_lte_feature_set_dl_table = pd.ExcelFile(nr_file_input).parse('NRF_PS_LTE_FEATURE_SET_DL_TABLE')






#cell 6
band_combination_list = []
for i in range(0,len(band_1)):
    string_band = ""
    if band_1[i] != 0 :
        if nr_check_1[i] == 1:
            string_band = 'n'+ str(band_1[i]) + 'A' 
        else:
            string_band = string_band + str(band_1[i]) + 'A'
        
        string_two = ""
        if band_2[i] == 0:
            string_two = string_band
        else:
            if nr_check_2[i] == 1:
                string_two = string_band + "-"+ "n"+ str(band_2[i]) + 'A'
            else:
                string_two = string_band + "-" + str(band_2[i]) + 'A' 
        
        string_three = ""
        if band_3[i] == 0:
            string_three = string_two
        else:
            if nr_check_3[i] == 1:
                string_three = string_two + "-" + "n"+ str(band_3[i]) + 'A'
            else:
                string_three = string_two + "-" + str(band_3[i]) + 'A'
        
        string_four = ""
        if band_4[i] == 0:
            string_four = string_three
        else:
            if nr_check_4[i] == 1:
                string_four = string_three + "-" + "n"+ str(band_4[i]) + 'A'
            else:
                string_four = string_three + "-" + str(band_4[i]) + 'A'
        
        string_five = ""
        if band_5[i] == 0:
            string_five = string_four
        else:
            if nr_check_5[i] == 1:
                string_five = string_four + "-"+ "n"+ str(band_5[i]) + 'A'
            else:
                string_five = string_four + "-" + str(band_5[i]) + 'A'
        
        string_six = ""
        if band_6[i] == 0:
            string_six = string_five
        else:
            if nr_check_6[i] == 1:
                string_six = string_five + "-"+ "n" + str(band_6[i]) + 'A'
            else:
                string_six = string_five + "-" + str(band_6[i]) + 'A'
        
        string_seven = ""
        if band_7[i] == 0:
            string_seven = string_six
        else:
            if nr_check_7[i] == 1:
                string_seven = string_six + "-"+ "n"+ str(band_7[i]) + 'A'
            else:
                string_seven = string_six + "-" + str(band_7[i]) + 'A'
        
        
        band_combination_list.append(string_seven)


        
        
        

#cell 7
active_bands = []
bands_with_4L = []
sub_carrier_spacing_dl = []
sub_carrier_spacing_ul = []

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
        
        if(re.findall(r'Sub Carrier Spacing DL',line)):
            string_from_split_function = split_line_from_file_store(line)
            sub_carrier_spacing_dl.append(string_from_split_function)
        
        if(re.findall(r'Sub Carrier Spacing UL',line)):
            string_from_split_function = split_line_from_file_store(line)
            sub_carrier_spacing_ul.append(string_from_split_function)

    return active_bands,bands_with_4L,sub_carrier_spacing_dl,sub_carrier_spacing_ul

            

#cell 10
active_bands_main = []
bands_with_4L_main = []
sub_carrier_spacing_dl_main = []
sub_carrier_spacing_ul_main = []
active_bands_main,bands_with_4L_main,sub_carrier_spacing_dl_main,sub_carrier_spacing_ul_main = read_mcc_band_text(mcc_read_file)
bands_with_4L_main_list = bands_with_4L_main[0].split(',')
#print("sub_carrier_spacing_dl_main:",sub_carrier_spacing_dl_main)
#print("sub_carrier_spacing_ul_main:",sub_carrier_spacing_ul_main)

#cell 11
'''filtering-band-combination'''
nr_mrdc_band_combination = 'nrf_ps_nr_mrdc.csv'
nr_feature_set_combinati = 'nrf_ps_combinati.csv'
nr_feature_set_per_band = 'nrf_ps_nr_per_band.csv'
nr_feature_set_ul_table = 'nrf_ps_nr_ul_table.csv'
nr_feature_set_dl_table = 'nrf_ps_nr_dl_table.csv'
nr_feature_set_ul_per_cc = 'nrf_ps_nr_ul_per_cc.csv'
nr_feature_set_dl_per_cc = 'nrf_ps_nr_dl_per_cc.csv'
band_combination_final = []
#sub_carrier_spacing_list = re.findall(r'\d+\.*\d*',str(sub_carrier_spacing_main[0]))

with open(nr_mrdc_band_combination,"w",encoding = 'utf-8') as output,open(nr_feature_set_ul_per_cc,"w",encoding = 'utf-8') as ulp_cc,open(nr_feature_set_dl_per_cc,"w",encoding = 'utf-8') as dlp_cc,open(nr_feature_set_combinati,"w",encoding = 'utf-8') as out_combi,open(nr_feature_set_per_band,"w",encoding = 'utf-8') as out_per_band,open(nr_feature_set_ul_table,"w",encoding = 'utf-8') as out_1,open(nr_feature_set_dl_table,"w",encoding = 'utf-8') as out_2:
    writer = cv.writer(output,delimiter=',',lineterminator='\n')
    writer.writerow(column_names_sheet_1)
    writer_combinati = cv.writer(out_combi,delimiter=',',lineterminator='\n')
    writer_combinati.writerow(column_names_nr_combinati)
    writer_per_band = cv.writer(out_per_band,delimiter=',',lineterminator='\n')
    writer_per_band.writerow(column_names_nr_per_band)
    writer_ul = cv.writer(out_1,delimiter=',',lineterminator='\n')
    writer_ul.writerow(column_names_nr_ul_table)
    writer_dl = cv.writer(out_2,delimiter=',',lineterminator='\n')
    writer_dl.writerow(column_names_nr_dl_table)
    writer_ul_cc = cv.writer(ulp_cc,delimiter=',',lineterminator='\n')
    writer_ul_cc.writerow(column_names_nr_ul_per_cc)
    writer_dl_cc = cv.writer(dlp_cc,delimiter=',',lineterminator='\n')
    writer_dl_cc.writerow(column_names_nr_dl_per_cc)
    
    for i in range(0,len(band_combination_list)):
        number_regex = re.findall(r'\d+\.*\d*',str(band_combination_list[i]))
        active_list = re.findall(r'\d+\.*\d*',str(active_bands_main[0]))
        if (set(number_regex).issubset(active_list)) == True:
            print("band_combination_list:",band_combination_list[i])
            band_combination_final.append(band_combination_list[i])
            writer.writerow(nr_read_list[i])
            value_1 = nrf_3gpp_feature_set_combination_index[i]
            value_2 = nrf_3gpp_feature_set_combination_count[i]
            if str(band_combination_list[i]).find("-") != -1:
                string_split = str(band_combination_list[i]).split("-")
                for j in range(0,len(string_split)):
                    for k in range(value_1,value_1+value_2):
                        flag_dl = 0
                        flag_ul = 0
                        ul_value = 0
                        dl_value = 0
                        nrf_nr_feature_set_per_band_index_hold = nrf_nr_feature_set_per_band_index[k]
                        #print("nrf_feature_set_per_band_index_hold:", nrf_nr_feature_set_per_band_index_hold)
                        m = 5 + (2*j)
                        nrf_ps_nr_feature_sets_per_band_ul = nrf_ps_nr_feature_sets_per_band.iloc[0:,m].tolist()
                        nrf_ps_nr_feature_sets_per_band_dl = nrf_ps_nr_feature_sets_per_band.iloc[0:,m+1].tolist()
                        '''DL_PER_CC and UL_PER_CC'''
                        if (nrf_ps_nr_feature_sets_per_band_ul[nrf_nr_feature_set_per_band_index_hold] != 1023 and nrf_ps_nr_feature_sets_per_band_dl[nrf_nr_feature_set_per_band_index_hold] != 1023):
                            #writer_ul.writerow(nrf_ps_nr_feature_set_ul_table_list[nrf_ps_nr_feature_sets_per_band_ul[nrf_nr_feature_set_per_band_index_hold]])
                            for l in range(0,len(nrf_ps_nr_feature_sets_dl_per_cc_list)):
                                if (str(nrf_ps_nr_feature_sets_dl_per_cc_list[l][2]) in sub_carrier_spacing_dl_main[0]):
                                    flag_dl = 1
                                    dl_value = l
                                    break;
                            for p in range(0,len(nrf_ps_nr_feature_sets_ul_per_cc_list)):
                                if (str(nrf_ps_nr_feature_sets_ul_per_cc_list[p][2]) in sub_carrier_spacing_ul_main[0]):
                                    flag_ul = 1
                                    ul_value = p
                                    break;
                            if(flag_ul == 1 and flag_dl == 1):
                                #print("band_combination_list_satisfying:",band_combination_list[i])
                                writer_dl.writerow(nrf_ps_nr_feature_set_dl_table_list[nrf_ps_nr_feature_sets_per_band_dl[nrf_nr_feature_set_per_band_index_hold]])
                                writer_ul.writerow(nrf_ps_nr_feature_set_ul_table_list[nrf_ps_nr_feature_sets_per_band_ul[nrf_nr_feature_set_per_band_index_hold]])
                                list_combinati = [k,nrf_nr_feature_set_per_band_index_hold]
                                writer_combinati.writerow(list_combinati)
                                writer_per_band.writerow(nrf_ps_nr_feature_sets_per_band_list[nrf_nr_feature_set_per_band_index_hold])    
                                writer_ul_cc.writerow(nrf_ps_nr_feature_sets_ul_per_cc_list[ul_value])
                                writer_dl_cc.writerow(nrf_ps_nr_feature_sets_dl_per_cc_list[dl_value])
                            
            else:
                '''go to NRF_PS_NR_FEATURE_SET_COMBINATI'''
                for k in range(value_1,value_1+value_2):
                    flag_dl = 0
                    flag_ul = 0
                    dl_value = 0
                    ul_value = 0
                    nrf_nr_feature_set_per_band_index_hold = nrf_nr_feature_set_per_band_index[k]
                    nrf_ps_nr_feature_sets_per_band_ul = nrf_ps_nr_feature_sets_per_band.iloc[0:,5].tolist()
                    nrf_ps_nr_feature_sets_per_band_dl = nrf_ps_nr_feature_sets_per_band.iloc[0:,6].tolist()
                   #print("nrf_ps_nr_feature_sets_per_band_ul:",nrf_ps_nr_feature_sets_per_band_ul[nrf_nr_feature_set_per_band_index_hold])
                   #print("ul_table_list:",nrf_ps_nr_feature_set_ul_table_list[nrf_ps_nr_feature_sets_per_band_ul[nrf_nr_feature_set_per_band_index_hold]])
                   #print("dl_table_list:",nrf_ps_nr_feature_set_dl_table_list[nrf_ps_nr_feature_sets_per_band_dl[nrf_nr_feature_set_per_band_index_hold]])
                    if (nrf_ps_nr_feature_sets_per_band_ul[nrf_nr_feature_set_per_band_index_hold] != 1023 and nrf_ps_nr_feature_sets_per_band_dl[nrf_nr_feature_set_per_band_index_hold] != 1023):
                            for l in range(0,len(nrf_ps_nr_feature_sets_dl_per_cc_list)):
                                if (str(nrf_ps_nr_feature_sets_dl_per_cc_list[l][2]) in sub_carrier_spacing_dl_main[0]):
                                    flag_dl = 1
                                    dl_value = l
                                    break;
                            for p in range(0,len(nrf_ps_nr_feature_sets_ul_per_cc_list)):
                                if (str(nrf_ps_nr_feature_sets_ul_per_cc_list[p][2]) in sub_carrier_spacing_ul_main[0]):
                                    flag_ul = 1
                                    ul_value = p
                                    break;
                            if(flag_ul == 1 and flag_dl == 1):
                                #print("band_combination_list_satisfying:",band_combination_list[i])
                                writer_dl.writerow(nrf_ps_nr_feature_set_dl_table_list[nrf_ps_nr_feature_sets_per_band_dl[nrf_nr_feature_set_per_band_index_hold]])
                                writer_ul.writerow(nrf_ps_nr_feature_set_ul_table_list[nrf_ps_nr_feature_sets_per_band_ul[nrf_nr_feature_set_per_band_index_hold]])
                                list_combinati = [k,nrf_nr_feature_set_per_band_index_hold]
                                writer_combinati.writerow(list_combinati)
                                writer_per_band.writerow(nrf_ps_nr_feature_sets_per_band_list[nrf_nr_feature_set_per_band_index_hold])    
                                writer_ul_cc.writerow(nrf_ps_nr_feature_sets_ul_per_cc_list[ul_value])
                                writer_dl_cc.writerow(nrf_ps_nr_feature_sets_dl_per_cc_list[dl_value])
                
            
            
        

#cell 12
'''Writing into csv output file'''
with open(trial_output_file,"a",encoding='utf-8') as output:
    for j in range(0,len(band_combination_final)):
        band_combination = [band_combination_final[j]]
        writer = cv.writer(output,delimiter=',',lineterminator='\n')
        writer.writerow(band_combination)
    


#cell 13
'''removing the duplicates in the file'''
import fileinput
def file_reduce(file_name):
    seen = set()
    for line in fileinput.FileInput(file_name, inplace=1):
        if line in seen: 
            continue
        seen.add(line)
        print(line,end="")

#cell 14
file_reduce(nr_feature_set_combinati)
file_reduce(nr_feature_set_per_band)
file_reduce(nr_feature_set_ul_table)
file_reduce(nr_feature_set_dl_table)
file_reduce(nr_feature_set_ul_per_cc)
file_reduce(nr_feature_set_dl_per_cc)


    

#cell 15
'''combining all .csv file into one excel sheet: output.xls'''
wb = xlwt.Workbook()
for csvfile in glob.glob(os.path.join('.', '*.csv')):
    fpath = csvfile.split("\\", 1)
    #fname = fpath[1].split(".", 1) ## fname[0] should be our worksheet name

    ws = wb.add_sheet(fpath[1])
    with open(csvfile, 'r') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                ws.write(r, c, col)
    wb.save('output.xls')
    os.remove(csvfile)

#cell 16


