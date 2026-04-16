import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        nums = []
        for token in tokens:
            try:
                nums.append(int(token))
            except:
                num = nums.pop()
                match token:
                    case '+':
                        nums[-1] += num
                    case '-':
                        nums[-1] -= num
                    case '*':
                        nums[-1] *= num                        
                    case '/':
                        nums[-1] = math.trunc(nums[-1] / num)
        
        return nums.pop()
        