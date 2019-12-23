'''
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')* i for i in range(amount+1)]
        dp[0] = 0
        for change in range(1,amount+1):
            for coin in range(0,len(coins)):
                if coins[coin]<= change :
                    dp[change] = min(dp[change],dp[change-coins[coin]]+1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
                    
        
