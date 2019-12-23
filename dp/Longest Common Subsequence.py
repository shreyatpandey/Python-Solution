

#Recursive solution | Overlapping Subproblems | TLE
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        def longestcommonsubsequence(text1,text2,lengthtext1,lengthtext2):
            if lengthtext1 == 0 or lengthtext2 == 0: 
                return 0; 
            elif text1[lengthtext1-1] == text2[lengthtext2-1]: 
                return 1 + longestcommonsubsequence(text1, text2,lengthtext1-1, lengthtext2-1); 
            else: 
                return max(longestcommonsubsequence(text1, text2, lengthtext1,lengthtext2-1), longestcommonsubsequence(text1, text2, lengthtext1-1, lengthtext2)) 

        return longestcommonsubsequence(text1,text2,len(text1),len(text2))
        
   
