class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i, s in enumerate(strs):
            if s == "":
                encoded += '0#'
            else:
                encoded += str(len(s)) + '#'
                encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            num = "0"
            for j in range(i, len(s)):
                if s[j] != "#":
                    num += s[j]
                else:
                    break
            if num == 0:
                out.append("")
            else:
                out.append(s[i + len(num):i + int(num) + len(num)])
            i += int(num) + len(num)
        return out

