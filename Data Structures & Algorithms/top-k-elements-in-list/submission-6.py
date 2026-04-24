class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [list() for _ in range(len(nums) + 1)]
        counts = dict()
        for num in nums:
            counts[num] = 1 + (counts[num] if num in counts else 0)

        for num in counts:
            buckets[counts[num]].append(num)
        res = []
        for i in range(len(buckets)-1, 0, -1):
            res.extend(buckets[i])
            print(len(res), i)
            if len(res) >= k:
                return res[:k]