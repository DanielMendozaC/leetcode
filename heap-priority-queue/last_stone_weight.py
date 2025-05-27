import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create max-heap by negating values (heapq is min-heap by default)
        heapl = [-v for v in stones]
        heapq.heapify(heapl)  # O(n) - efficient heap construction

        # Simulate stone collisions until 0 or 1 stone remains
        while len(heapl) > 1:
            # Get two heaviest stones (most negative values = largest original values)
            heaviest = heapq.heappop(heapl)          # O(log n)
            second_heaviest = heapq.heappop(heapl)   # O(log n)

            # If stones have different weights, add the difference back
            # Math works: -8 - (-5) = -3, representing remaining stone of weight 3
            if heaviest != second_heaviest: 
                heaviest = heaviest - second_heaviest
                heapq.heappush(heapl, heaviest)      # O(log n)
            # If equal weights, both stones destroy each other (do nothing)

        # Return final result
        if heapl:
            return -heapq.heappop(heapl)  # Convert back to positive
        else: 
            return 0  # No stones remaining

    """
    TIME COMPLEXITY ANALYSIS:
    
    • Initialization: 
      - List comprehension: O(n)
      - heapify(): O(n) 
      - Total initialization: O(n)
    
    • While loop:
      - Runs at most (n-1) times (each iteration removes at least 1 stone)
      - Each iteration: 2 × heappop() + maybe 1 × heappush()
      - Each heap operation: O(log n)
      - Total loop: O(n × log n)
    
    • Final result: O(log n) or O(1)
    
    OVERALL TIME COMPLEXITY: O(n) + O(n log n) = O(n log n)
    
    SPACE COMPLEXITY: O(n) - heap stores all stones initially
    
    Why O(n log n) and not O(n)?
    The heapify() is O(n), but the while loop dominates with O(n log n) 
    because we potentially do n iterations of O(log n) heap operations.
    """