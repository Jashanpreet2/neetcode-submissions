class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_combinations = []
        def backtrack(stack, openN, closedN):
            if openN == closedN == n:
                all_combinations.append("".join(stack))
                return
            elif openN < n:
                if closedN < openN:
                    copy = stack.copy()
                    copy.append(")")
                    backtrack(copy, openN, closedN+1)
                stack.append("(")
                backtrack(stack, openN+1, closedN)
                
            else:
                stack.append(")")
                backtrack(stack, openN, closedN+1)

        backtrack([], 0, 0)
        
        return all_combinations
            
        