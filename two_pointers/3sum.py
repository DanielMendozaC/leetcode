class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list
        # fix k pointer, use a for loop.
        # left and right pointer with while left<right
        # initialization of left and right, checking the condition
        # handling duplicates

        nums.sort()
        result = []

        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            left = k+1
            right = len(nums)-1
            while left<right:
                csum = nums[left]+nums[right]+nums[k]
                if csum == 0:
                    result.append([nums[k],nums[left],nums[right]])
                    # NEED TO MOVE THE POINTERS
                    left+=1
                    right-=1
                    while left<right and nums[left-1]==nums[left] :
                        left+=1
                    while left<right and nums[right+1]==nums[right]:
                        right-=1
                
                elif csum<0:
                    left+=1

                else:
                    right-=1
        return result


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()

#         for i, a in enumerate(nums):
#             if a > 0:
#                 break

#             if i > 0 and a == nums[i - 1]:
#                 continue

#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 threeSum = a + nums[l] + nums[r]
#                 if threeSum > 0:
#                     r -= 1
#                 elif threeSum < 0:
#                     l += 1
#                 else:
#                     res.append([a, nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1
                        
#         return res

