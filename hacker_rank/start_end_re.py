import re
string_main = input()
string_compare = input()
index_string_compare = 0

if re.search(string_compare,string_main):
    while index_string_compare + len(string_compare) < len(string_main) :
        string_result= re.search(string_compare,string_main[index_string_compare:])
        print("({0},{1})\n".format(index_string_compare+string_result.start(),index_string_compare+string_result.end()-1))
        index_string_compare += string_result.start() + 1
else:
    print("1,-1")
