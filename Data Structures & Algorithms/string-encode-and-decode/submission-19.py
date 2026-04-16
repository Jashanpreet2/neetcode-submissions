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
            j = i
            while s[j] != '#':
                num += s[j]
                j += 1
            num = int(num)
            num_len = len(str(num))
            if num == 0:
                out.append("")
            else:
                print(num, num_len)
                out.append(s[i + num_len + 1:i + num + num_len + 1])
            i += num + num_len + 1
        return out

