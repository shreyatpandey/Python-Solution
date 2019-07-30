import re
def month_name_extraction(string_input):
    month_date = {'January':31,'Febuary':28,'March':31}
    for key,values in month_date.items():
        regex_match = re.search(string_input,key,re.I)
        if regex_match:
            return key,values
        else:
            return 0,0

string_result = month_name_extraction("mar")
print(string_result)
