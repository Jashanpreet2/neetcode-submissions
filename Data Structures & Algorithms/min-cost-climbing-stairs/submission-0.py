class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = dict()
        def recurse(i):
            if i >= len(cost):
                return 0
            if i in d:
                return d[i]
            d[i] = cost[i] + min(recurse(i+1), recurse(i+2))
            return d[i]

        return min(recurse(0), recurse(1))