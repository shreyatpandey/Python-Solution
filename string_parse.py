string_input = "1a_2a_3a_4a_5a"
string_list = string_input.split("_")
output_list = []
k = 0
for i in range(0,len(string_list)):
	output_list.append(string_list[i])
	for j in range(i+1,len(string_list)):
		string_insert = output_list[k] + "_" + string_list[j]
        	k += 1
		output_list.append(string_insert)   
	k = len(output_list)

print("Output_list:",output_list)
