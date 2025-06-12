class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        def helper(nums):
            n = len(nums)
            if n == 0:
                return 0
            elif n == 1:
                return nums[0] 

            dp = [0] * (n)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])  
            return dp[-1]

        # Rob first house, dont rob last house
        rob1 = helper(nums[:-1])
        # Rob last house, don't rob first
        rob2 = helper(nums[1:])

        return max(rob1, rob2)

        # Time complexity is O(n) and space complexity is O(n)

# Case 1: helper(nums[:-1])  → processes n-1 elements → O(n)
# Case 2: helper(nums[1:])   → processes n-1 elements → O(n)
# Total: O(n) + O(n) = O(2n) = O(n)