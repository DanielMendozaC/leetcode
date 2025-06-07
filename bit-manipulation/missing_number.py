class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        freq = set(nums)
        for i in range(n+1):
            if i not in freq:
                return i
        

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n  
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr