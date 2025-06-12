class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def backtrack(start, end):    
            # Copying sub is O(n) in each backtrack
            result.append(sub[:])
            
            for i in range(start, end):
                # Important to start checking duplicates after first element w/ i>0.
                if i > 0 and nums[i] == nums[i-1] and i-1 >= start:
                    continue
                sub.append(nums[i])
                backtrack(i+1, end)
                sub.pop()

            return

        result = []
        sub = []
        
        backtrack(0, len(nums))
        return result

        # Time complexity is O(n * 2^n) and space is O(n * 2^n)

        # Number of solutions for subsets is 2^n and genereate each sol. is O(n)
        # Time = (Number of solutions) × (Cost to generate each solution)