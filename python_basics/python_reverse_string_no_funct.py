class Solution:
    def reverse_method_1(self,string):
        string_output = ""
        for i in string:
            string_output = i + string_output
        return string_output
    def reverse_method_2(self,string):
        string_output = ""
        count = 0;
        for i in string:
            count +=1
        for j in range(0,count):
            string_output = string_output+string[count-j-1]
        return string_output

if __name__ == "__main__":
    s = Solution()
    display_result_1 = s.reverse_method_1("hi all")
    display_result_2 = s.reverse_method_2("hi all")
    print("Reverse_Method_1:",display_result_1)
    print("Reverse_Methdo_2:",display_result_2)
