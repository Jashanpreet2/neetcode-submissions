class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or self.store[key][0][0] > timestamp:
            return  ""
        beg = 0
        end = len(self.store[key]) - 1
        mid = (beg + end) // 2
        ret = (beg + end) // 2
        eligible = mid
        while beg <= end:
            if self.store[key][mid][0] == timestamp:
                return self.store[key][mid][1]
            elif self.store[key][mid][0] > timestamp:
                end = mid - 1
            else:
                eligible = mid
                beg = mid + 1
            if beg > end:
                break
            mid = (beg + end) // 2

        return self.store[key][eligible][1]
    
        
