import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        mid = (high + low) // 2
        k = mid
        while low <= high:
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile/mid)
            if totalHours <= h:
                k = mid
                high = mid - 1
            else:
                low = mid + 1
            
            mid = (low + high) // 2
        return k