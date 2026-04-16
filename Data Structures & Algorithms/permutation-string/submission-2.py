class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = dict()
        for c in s1:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1
        copy = d.copy()
        
    
        i = 0
        j = 0
        total = len(s1)
        while total > 0 and j < len(s2):
            cend = s2[j]
            if cend in d.keys():
                d[cend] -= 1
                total -= 1
                if d[cend] < 0:
                    while True:
                        if s2[i] in d.keys():
                            d[s2[i]] += 1
                            total += 1
                        if s2[i] == cend:
                            i+= 1
                            break
                        i += 1
            else:
                i = j
                d = copy.copy()
                total = len(s1)
            if total == 0:
                return True
            j += 1

        return False
                


        