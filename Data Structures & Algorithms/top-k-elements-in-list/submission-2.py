class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [None] * len(nums)
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for num in counts:
            if freq[counts[num] - 1] is None:
                freq[counts[num] - 1] = [num]
            else:
                freq[counts[num] - 1].append(num)
        topk = [0] * k
        curr = 0
        i = len(freq) - 1
        while True:
            if i <= -1:
                break
            if curr >= k:
                break
            if freq[i] is None:
                i -= 1
                continue
            for num in freq[i]:
                if curr < k:
                    topk[curr] = num
                    curr += 1
                else:
                    break
            i -= 1
        return topk