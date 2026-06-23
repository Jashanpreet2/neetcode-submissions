class Solution:
    def isHappy(self, n: int) -> bool:
        pastNums = set()
        while n not in pastNums and n != 1:
            pastNums.add(n)
            digits = []
            while n > 0:
                digits.append(n%10)
                n = n // 10
            n = 0
            for digit in digits:
                n += digit * digit
        return n == 1
        