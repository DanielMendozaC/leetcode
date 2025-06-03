class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # max_sum = -inf
        # for i in range(len(nums)):
        #     subsum = nums[i]
        #     max_sum = max(max_sum, subsum)

        #     for j in range(i+1, len(nums)):
        #         subsum += nums[j]
        #         max_sum = max(max_sum, subsum)

        # return max_sum


        # Kadane's Algorithm - at each position, decide to extend or start fresh
        max_sum = nums[0]        # Global maximum seen so far
        current_sum = nums[0]    # Current subarray sum
        
        for i in range(1, len(nums)):
            # Greedy choice: extend current subarray OR start new one
            current_sum = max(nums[i], nums[i] + current_sum)
            max_sum = max(current_sum, max_sum)

        return max_sum
        # Time complexity: O(n), Space complexity: O(1)


