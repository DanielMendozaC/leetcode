class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        # Sort by start time to process overlaps in order
        # This is O(n log(n))
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for current in intervals[1:]:
            last = result[-1]

            # Check if current interval overlaps with the last merged interval
            if current[0] <= last[1]:
                # Merge by extending the end time
                last[1] = max(last[1], current[1])
            else:
                # No overlap, add as separate interval
                result.append(current)

        return result
        
        # Time: O(n log n) - sorting dominates
        # Space: O(n) - result array