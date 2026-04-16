class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        z = sorted(zip(position, speed), reverse=True)
        position, speed = zip(*z)
        i = 0
        minimumTime = None
        for i in range(len(position)):
            curTime = (target - position[i])/speed[i]
            if minimumTime is None or curTime > minimumTime:
                minimumTime = curTime
                fleets += 1
        return fleets
        
         