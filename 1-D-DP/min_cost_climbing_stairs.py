class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        result = [0] * (n+1)

        result[0] = cost[0]
        if n>1:
            result[1] = cost[1]

        for i in range(2,n):
            result[i] = cost[i]
            result[i] += min(result[i-1], result[i-2])

        result[n] = min(result[n-1], result[n-2])
        
        return result[-1]

        # Time complexity is o(n) and space o(n)
        


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp[i] = minimum cost to reach position i
        # Position 0 and 1 are starting points (free)
        # Position n is the "top" destination
        dp = [0] * (n + 1)
        
        # Fill positions 2 through n
        for i in range(2, n + 1):
            # To reach position i, we can come from:
            # - Position i-1 (pay cost[i-1] to step on step i-1)
            # - Position i-2 (pay cost[i-2] to step on step i-2)
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])
        
        # Return cost to reach the top
        return dp[n]