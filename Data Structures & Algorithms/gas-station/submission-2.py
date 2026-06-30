class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1:
            return 0 if gas[0] >= cost[0] else -1
        def getIdx(i):
            if i < 0:
                return len(gas)-i
            return i % len(cost)
        for i in range(len(gas)):
            curGas = gas[i]-cost[i]
            j = 1
            while curGas >= 0 and getIdx(i+j) != i:
                idx = getIdx(i+j)
                curGas += gas[idx]-cost[idx]
                if curGas >= 0:
                    j += 1
            if getIdx(i+j) == i:
                return i
        return -1
    
