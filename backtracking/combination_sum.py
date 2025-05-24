class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start, path):
            if sum(path) == target:
                result.append(path[:])
                return
            elif sum(path) > target:
                return  # Pruning - stop exploring this branch
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path)      # Use 'i' to allow reusing same number
                path.pop()              # Backtrack
        
        backtrack(0, [])

        return result