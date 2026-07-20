class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = dict()
        res = []
        for i, c in enumerate(s):
            last[c] = i
        length = 0
        lastPos = 0
        for i, c in enumerate(s):
            length += 1
            lastPos = max(last[c], lastPos)
            if lastPos == i:
                res.append(length)
                length = 0
        return res



            

        