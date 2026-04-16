class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
                encoded += str(len(s)) + '#'
                encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            num = ""
            while s[i] != '#':
                num += s[i]
                i += 1
            i += 1
            num = int(num)
            if num == 0:
                out.append("")
            else:
                out.append(s[i:i+num])
            i += num
        return out

