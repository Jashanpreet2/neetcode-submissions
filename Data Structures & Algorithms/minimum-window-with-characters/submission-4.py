class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = dict()
        for c in t:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1
        
        total = len(t)
        shorti = shortj = i = j = 0
        
        while j < len(s) and total > 0:
            c = s[j]
            if c in d.keys():
                if d[c] > 0:
                    total -= 1
                d[c] -= 1
            if total <= 0:
                shortj = j
                break
            j += 1
        
        if total > 0:
            return ""
       
        ret = ""
        while True:
            if i < len(s) and i < j and (s[i] not in d.keys() or d[s[i]] < 0):
                if s[i] in d.keys():
                    d[s[i]] += 1
                i += 1
                continue
            ret += f"{j-i}, {shortj-shorti}"
            if j - i <= shortj - shorti:
                shorti = i
                shortj = j
            j += 1
            if j >= len(s):
                break
            if s[j] in d.keys():
                d[s[j]] -= 1
        
        return s[shorti: shortj+1]
            
                                
        