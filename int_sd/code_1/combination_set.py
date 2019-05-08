combinations = []
def combine(terms, accum):
    last = (len(terms) == 1)
    n = len(terms[0])
    for i in range(n):
        item = ""
        item = str(accum + terms[0][i]) + item
        if last:
            combinations.append(item)
        else:
            combine(terms[1:], item)
 
list_input_2 = ['-/1.4/5/10/15/20\n-/-/5/10/-/-\n-/-/-/10/15/20']
main_parent_list = list_input_2[0].split("\n")
main_parent_setup = []
for i in range(0,len(main_parent_list)):
    main_parent_loop = re.findall(r'\d+\.*\d*',str(main_parent_list[i]))
    main_parent_setup.append(main_parent_loop)

child_input_2 = ['1.4/3/5/10/15/20\n-/-/5/10/15/20']

combine(main_parent_setup,'')
print("combi:",combinations)
string_hold =combinations[0]
for i in range(1,len(combinations)):
    if(i != len(combinations)-1):
        string_hold = string_hold + "," + (combinations[i])
    else:
        string_hold = string_hold + combinations[i]
print("string_hold:",string_hold)
#list_two = ['1.4-5-10-,1.4-20-20-']
string_one = "1.420"
if string_one in string_hold:
    print("Yes")

print("set:",set(list_two[0]))
print("result:",set(list_two[0]).issubset(combinations[0]))
