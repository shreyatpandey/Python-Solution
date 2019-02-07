def split_further(string_input_split_further):
    input_match_store = []
    string_list_space = string_input_split_further.split("\n")
    print("string_list_space:",string_list_space)
    flag_colon = 0
    for j in range(0,len(string_list_space)):
        if ":" in string_list_space[j]:
            print("colon detected")
            flag_colon = 1
            loop_split = string_list_space[j].split(":")
            #input_2 = re.findall(r'\d+',loop_split[1])
            input_match_store.append(loop_split[1])
    print("input_match_store:",input_match_store)
    if(flag_colon == 1):
        for l in range(0,len(input_match_store)):
            string_store = ','.join(input_match_store)
        print("string_store:",string_store)
        return string_store
    if(flag_colon == 0):
        for l in range(0,len(string_list_space)):
            string_input_no_change = ','.join(string_list_space)
        print("string_input_no_change:",string_input_no_change)
        return string_input_no_change

import re
list_trial = ['2: -/-/5/10/15/20\n2: -/-/5/10/15/20']
list_trial_input = split_further(list_trial[0])
#if split_child in split_main:
    #print("Doomed")


string_one = '-/-/5/10'
string_two = '-/-/-/10'
#input_one = re.findall(r'\d+\.*\d*',split_main)
#input_two = re.findall(r'\d+\.*\d*',split_child)
#print("input_one:",input_one)
#print("input_two:",input_two)
#if set(input_two).issubset(input_one):
    #print("yes")
