word_dict = {}
file_read = open("input_read.txt",'r')
for line in file_read:
    line_split = line.split(" ") 
    for i in range(len(line_split)):
        if line_split[i] in word_dict:
            word_dict[line_split[i]]  += 1
        else:
            word_dict[line_split[i]] = 1
for key,values in word_dict.items():
    print(str(key)+"-"+str(values))
