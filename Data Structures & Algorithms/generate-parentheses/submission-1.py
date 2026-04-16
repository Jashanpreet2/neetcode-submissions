class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            elif openN < n:
                if closedN < openN:
                    stack.append(")")
                    backtrack(openN, closedN+1)
                    stack.pop()
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
            else:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()

        backtrack(0, 0)
        
        return res
            
        