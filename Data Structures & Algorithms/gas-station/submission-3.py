class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        extraNeeded = [0] * len(gas)
        if len(gas) == 1:
            return 0 if gas[0] >= cost[0] else -1
        def getIdx(i):
            if i < 0:
                return len(gas)+i
            return i % len(cost)
        left, right, curGas = 0, 0, gas[0]-cost[0] 
        while True:
            while curGas >= 0:
                print(left, right)
                right = getIdx(right+1)
                if right == left:
                    return left
                curGas += gas[right] - cost[right]
            while curGas < 0:
                left = getIdx(left-1)
                if left == right:
                    return -1
                curGas += gas[left] - cost[left]
            if left == right:
                break
        return -1
    
