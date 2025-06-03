class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return True

        furthest = 0
        for i in range(len(nums)-1):
            if furthest<i:
                return False

            furthest = max(furthest, i + nums[i])
            # print(furthest)

            if furthest>=len(nums)-1:
                return True

        return False
        # Time complecity is O(n) and space is O(1)