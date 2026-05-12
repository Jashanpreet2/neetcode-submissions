class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for num in nums:
            if len(res) == k:
                heapq.heappushpop(res, num)
            else:
                heapq.heappush(res, num)

        return res[0]