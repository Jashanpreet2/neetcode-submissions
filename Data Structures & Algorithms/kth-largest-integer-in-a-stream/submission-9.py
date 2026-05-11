class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        if len(self.minHeap) > 0 and val < self.minHeap[0]:
            return self.minHeap[0]
        if len(self.minHeap) >= self.k:
            heapq.heappushpop(self.minHeap, val)
        else:
            heapq.heappush(self.minHeap, val)
        return self.minHeap[0]
        
