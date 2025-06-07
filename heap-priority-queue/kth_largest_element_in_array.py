class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify(list)
        # heapq.heappush(heaplist, val)
        # heapq.heappop(heaplist)
        heaplist = [-v for v in nums]
        heapq.heapify(heaplist)

        for i in range(k-1):
            heapq.heappop(heaplist)
            # heappop is just O(1)...?
            # No, this is O(log n)
        
        return -heapq.heappop(heaplist)

        # Time complexity is O(n + k log(n)) and space complexity is O(n)

class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
        # O(nlogk)