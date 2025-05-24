class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return result
    # Time Complexity: O(n * 2^n) and space o(n) and O(2^n)?


def backtrack(start, path):
    result.append(path[:])  # Add current subset
    for i in range(start, len(nums)):
        path.append(nums[i])    # Include nums[i]
        backtrack(i+1, path)    # Recurse
        path.pop()              # Backtrack