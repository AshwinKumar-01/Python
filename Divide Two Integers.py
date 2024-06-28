class Solution:
    def divide(self, dividend,divisor):
        sign=-1 if (dividend<0 or divisor<0) else 1
        dividend,divisor=abs(dividend),abs(divisor)
        result=len(range(0,dividend-divisor+1,divisor))
        if sign==-1:
            result=-result
        plus=(2**31)-1
        minus=(-2**31)
        return min(max(result,minus),plus)
