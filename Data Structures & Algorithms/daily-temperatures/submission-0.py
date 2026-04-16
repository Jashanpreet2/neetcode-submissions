class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indexes = []
        res = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while len(indexes) > 0 and temperatures[indexes[-1]] < temperature:
                index = indexes.pop()
                res[index] = i - index
            indexes.append(i)
        return res
        