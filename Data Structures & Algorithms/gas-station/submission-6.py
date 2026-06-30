class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, end, tank = len(gas)-1, 0, gas[-1] - cost[-1]
        while start > end:
            if tank >= 0:
                tank += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                tank += gas[start]-cost[start]
        return start if tank >= 0 else -1
    