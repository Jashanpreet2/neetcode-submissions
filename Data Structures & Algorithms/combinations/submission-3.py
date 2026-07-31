class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def recurse(cur):
            if len(cur) == k:
                res.append(cur.copy())
                return
            for i in range(1 if len(cur)==0 else cur[-1]+1 , n-k+1+len(cur)+1):
                cur.append(i)
                recurse(cur)
                cur.pop()
        recurse(list())
        return res


        