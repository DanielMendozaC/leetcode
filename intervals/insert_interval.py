class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result=[]

        # - Phase 1: Add intervals ending before new interval
        i = 0
        while i<len(intervals) and intervals[i][1]<newInterval[0]:
            result.append(intervals[i])
            i+=1

        # - Phase 2: Merge overlapping intervals with new interval  
        while i<len(intervals) and newInterval[1]>=intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1

        result.append(newInterval)

        # - Phase 3: Add remaining intervals
        while i<len(intervals):
            result.append(intervals[i])
            i+=1

        return result
        # Time complexity is O(n) and space complexity is O(n)
        