class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i, s in enumerate(strs):
            if s == "":
                encoded += "<empty>"
            else:
                encoded += s
            if i != len(strs) - 1:
                encoded += "<separator>"
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        strs = s.split("<separator>")
        out = []
        for i in range(len(strs)):
            if strs[i] == "<empty>":
                out.append("")
            else:
                out.append(strs[i])
        return out

