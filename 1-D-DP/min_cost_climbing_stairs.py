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
        