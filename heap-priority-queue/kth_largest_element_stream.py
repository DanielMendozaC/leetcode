import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heapk = []
        # heapq.heapify(self.heapk)
        self.k = k

        for num in nums:
           heapq.heappush(self.heapk, num) 

           if len(self.heapk) > self.k:
                heapq.heappop(self.heapk)


    def add(self, val: int) -> int:
        heapq.heappush(self.heapk, val)
        
        # while len(self.heapk) > self.k:
        # Just need to pop one element if exceed the len
        if len(self.heapk) > self.k:
            heapq.heappop(self.heapk)

        return self.heapk[0]

        # Time complexity is o(n) and space o(k)

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)



# Other solution

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]