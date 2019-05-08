import re
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
    print("parent_superset:",superset)
            
    
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
    print("child_bcs_0:",superset_child)
    
    flag = 0
    for j in range(0,len(superset_child)):
        if any(superset_child[j] in s for s in superset) == False:
            flag = 1
    
    if(flag == 1):
        return False
    else:
        return True
#list_input = ['-/-/5/10/15/20\n-/-/5/10/15/20\n-/-/5/10/-/-']
#child_input = ['-/-/5/10/15/20\n-/3/5/10/15/20']
list_input_2 = ['-/-/5/10/15/20\n-/-/5/10/15/20\n-/-/5/10/15/20\n-/-/5/10/15/20\n-/-/5/10/-/-']
child_input_2 = ['-/-/5/10/15/20\n-/-/5/10/15/20\n-/-/5/10/15/20\n-/-/5/10/15/20']

string_result = combination_input(list_input_2[0],child_input_2[0])
if string_result == False:
    print("Combination Error")
