class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string has 1 way
        dp[1] = 1  # First character (we already checked it's not '0')
        
        for i in range(2, n + 1):
            # Single digit decode
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # Two digit decode  
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]


# class Solution:
#     def numDecodings(self, s: str) -> int:
#         n = len(s)
#         if n == 0 or int(s[0]) == 0:
#             return 0
#         elif n == 1:
#             return 1

#         dp = [0] * (n)

#         dp[0] = 1
#         dp[1] = 2 if (10 < int(s[:2]) <= 26 and int(s[:2]) != 20) else 1

#         for i in range(2, n):
#             # Ways to decode the current element:
#             if 10 < int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1]) != 20: 
#                 dp[i] = 1 + dp[i-1]
#             elif int(s[i]) == 0 and int(s[i-1:i+1]) not in [10,20]:
#                 return 0
#             else:
#                 dp[i] = dp[i-1]

#         print(dp)
        
#         return dp[-1]