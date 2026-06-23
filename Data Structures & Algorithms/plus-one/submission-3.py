class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] + 1 < 10:
            digits[-1] += 1
            return digits
        i = len(digits)-2
        while digits[i+1]+1 == 10:
            if i == -1:
                digits[0] = 0
                digits.insert(0, 1)
                return digits
            digits[i+1]=0
            i-=1
        digits[i+1] += 1
        return digits
        