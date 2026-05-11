class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            largest = heapq.heappop_max(stones)
            if largest == stones[0]:
                heapq.heappop_max(stones)
            else:
                secondlargest = heapq.heappop_max(stones)
                heapq.heappush_max(stones, abs(largest-secondlargest))
        return stones[0] if len(stones) > 0 else 0
        