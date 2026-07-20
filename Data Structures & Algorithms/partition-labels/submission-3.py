class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = dict()
        res = []
        for i, c in enumerate(s):
            last[c] = i
        remaining = set()
        length = 0
        for i, c in enumerate(s):
            remaining.add(c)
            length += 1
            if i == last[c]:
                remaining.remove(c)
            if len(remaining)==0:
                res.append(length)
                length = 0
        return res



            

        