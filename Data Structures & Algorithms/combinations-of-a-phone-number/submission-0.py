class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        maps = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        def backtrack(cur, i):
            cur.append('.')
            for c in maps[digits[i]]:
                cur[-1] = c
                if len(cur) == len(digits):
                    res.append(''.join(cur))
                elif i < len(digits) - 1:
                    backtrack(cur, i + 1)
            cur.pop()
        backtrack([], 0)
        return res