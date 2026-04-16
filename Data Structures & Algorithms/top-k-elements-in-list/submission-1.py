class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        unique_nums = set()
        for num in nums:
            unique_nums.add(num)
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        sortable_list = list(unique_nums)
        sortable_list.sort(reverse=True, key=lambda num : frequencies[num])
        return sortable_list[:k]
