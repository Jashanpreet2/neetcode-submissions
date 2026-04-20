class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        numbers = dict()
        candidates = sorted(candidates)
        for i in range(len(candidates)):
            if candidates[i] in numbers.keys():
                numbers[candidates[i]]["last_index"] = i
            else:
                numbers[candidates[i]] = {"last_index": i, "found": False}
        res = []
        def backtrack(cur: List[int], total: int, i: int):
            j = i
            added = False
            if i >= len(candidates):
                return
            total += candidates[i]
            cur.append(candidates[i])
            if total == target:
                res.append(cur.copy())
                cur.pop()
                return
            i += 1
            while i < len(candidates):
                if total + candidates[i] <= target and (candidates[i] != candidates[i-1] or j == i - 1):
                    backtrack(cur, total, i)
                i += 1
            num = cur.pop()
        for i in range(len(candidates)):
            ls = list()
            if candidates[i] <= target and (i == 0 or candidates[i] != candidates[i-1]):
                backtrack(ls, 0, i)
        return res
