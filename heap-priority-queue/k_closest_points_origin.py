class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heaplist = []
        for x, y in points:
            distance = x**2 + y**2
            heaplist.append((distance, [x, y]))

        heapq.heapify(heaplist)
        result = []

        for i in range(k):
            point = heapq.heappop(heaplist)
            # heappop is O(log n)
            # heappush is O(log n) too
            result.append(point[1])

        return result
        # Time complexity is O(n + k log(n))



class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res



        # values = []
        # for x,y in points:
        #     distance = x**2 + y**2
        #     values.append((distance, (x,y)))

        # heapq.heapify(values)

        # result=[]
        # for i in range(k):
        #     d, point = heapq.heappop(values)
        #     result.append(point)
        
        # return result

        # # Time complexity O(n + k log n), which is O(n log n) in the worst case when k approaches n and space is o(n)
