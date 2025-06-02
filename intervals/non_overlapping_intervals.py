class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)<=1:
            return 0

        intervals.sort(key=lambda x: x[1])

        last = intervals[0]
        count = 1

        for current in intervals[1:]:
            if current[0]>=last[1]:
                last = current
                count+=1

        return len(intervals) - count

        # Time complexity is O(n log(n)) and space complexity is O(1)
        