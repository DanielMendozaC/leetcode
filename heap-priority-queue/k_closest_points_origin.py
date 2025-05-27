class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        values = []
        for x,y in points:
            distance = x**2 + y**2
            values.append((distance, (x,y)))

        heapq.heapify(values)

        result=[]
        for i in range(k):
            d, point = heapq.heappop(values)
            result.append(point)
        
        return result

        # Time complexity O(n + k log n), which is O(n log n) in the worst case when k approaches n and space is o(n)
