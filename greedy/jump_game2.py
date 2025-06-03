class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0
        pos = len(nums)-1
        jump = 0

        while pos>0:
            for i in range(pos):
                if i+nums[i] >= pos:
                    jump += 1
                    pos = i
                    break

        return jump

        # Time complexity is O(n^2) and space is O(1)

        
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
        # Time complexity is O(n) and space is O(1)
