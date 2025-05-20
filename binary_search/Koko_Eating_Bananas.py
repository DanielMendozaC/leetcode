import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Koko Eating Bananas - LeetCode 875
        
        Problem:
        - Koko can eat at most k bananas per hour
        - Guards return in h hours
        - Find minimum integer k so Koko can eat all bananas before guards return
        
        Approach: Binary Search
        - Search for minimum valid k between 1 and max(piles)
        - For each potential k, calculate total hours needed
        - If hours ≤ h, try a smaller k (search left half)
        - If hours > h, try a larger k (search right half)
        """
        
        # Find maximum pile size (upper bound for k)
        max_k = max(piles)
        
        # Binary search to find minimum valid k
        left = 1 
        right = max_k
        smallest_k = max_k
        
        while left <= right:
            # Try middle value of current range
            mid_k = (left + right) // 2
            
            # Calculate total hours needed at speed mid_k
            total_h = 0
            for pile in piles:
                # Ceiling division: if pile = 10, k = 3, we need 4 hours (⌈10/3⌉ = 4)
                total_h += math.ceil(pile / mid_k)
                # Alternative method:
                # total_h += (pile // mid_k) + (1 if pile % mid_k != 0 else 0)
            
            if total_h <= h:
                # This speed works - save it and search for smaller valid k
                smallest_k = mid_k
                right = mid_k - 1
            else:
                # This speed is too slow - search for larger k
                left = mid_k + 1
                
        return smallest_k
        
        # Time complexity: O(n*log(m)) where n = number of piles, m = max pile size
        # Space complexity: O(1)
        
        """
        # Brute Force Solution - O(n*m) time complexity
        smallest_k = float('inf')
        for k in range(1, max_k + 1):
            total_h = 0
            for pile in piles:
                total_h += (pile // k) + (1 if pile % k != 0 else 0)
            if total_h <= h and k < smallest_k:
                smallest_k = k
        return smallest_k
        """