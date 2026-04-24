class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = dict()
        for num in nums:
            if num in a:
                a[num] += 1
            else:
                a[num] = 1
        a = dict(sorted(a.items(), key=lambda el: el[1], reverse=True))
        return list(a.keys())[:k]