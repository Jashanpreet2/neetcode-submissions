class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        largest = nums[0]
        for _ in range(k):
            largest = heapq.heappop_max(nums)
        return largest