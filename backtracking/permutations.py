class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, end):
            if len(perm) == len(nums):
                result.append(perm[:])
                return

            for i in range(start, end):
                if i not in used_idx:
                    # LIST .APPEND
                    # SET .ADD
                    used_idx.add(i)
                    perm.append(nums[i])
                    backtrack(0, end)
                    perm.pop()
                    used_idx.remove(i)

        used_idx = set()
        perm = []
        backtrack(0, len(nums))
        return result
    
    # Time complexity is O(n! x n) and space is o(n! x n)


    """
    Time Complexity: O(n! × n) (not just O(n!))

There are n! total permutations to generate
For each permutation, we do O(n) work to build it (the loop runs n times per level)
So it's n! × n

Space Complexity: O(n! × n) (not just O(n))

Auxiliary space: O(n) for recursion stack + used_idx set + perm list
Output space: O(n! × n) to store all n! permutations, each of length n
Total: O(n! × n)
    """

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                perm.pop()
                pick[i] = False


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], idx: int):
        if idx == len(nums):
            self.res.append(nums[:])
            return
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]