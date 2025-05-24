class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort to group duplicates together for easier skipping
        candidates.sort()
        result = []
        
        def backtrack(start, path):
            # Make a copy of current path
            new = path[:]
            
            # Base case: found valid combination
            if sum(path) == target:
                result.append(new)
                return
            
            # Pruning: stop if sum exceeds target
            elif sum(path) > target:
                return
            
            # Try each candidate from start position onwards
            for i in range(start, len(candidates)):
                # Skip duplicates: if current number equals previous number
                # and we're not at the first position of current iteration
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Choose: add current number to path
                path.append(candidates[i])
                
                # Recurse: explore with next position (i+1 prevents reusing same element)
                backtrack(i + 1, path)
                
                # Backtrack: remove current number to try next option
                path.pop()
        
        backtrack(0, [])
        return result

# Time Complexity: O(2^n) - in worst case, explore all possible subsets
# Space Complexity: O(target/min(candidates)) - maximum recursion depth
# where n is length of candidates array


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, path):
            new = path[:]
            if sum(path)==target:
                result.append(new)
                return
            elif sum(path)>target:
                return

            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return result