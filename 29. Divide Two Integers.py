class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if divisor == 0 or (dividend == -2**31 and divisor == -1):
            return 2**31-1
        if dividend == 0: return 0
        sign = (dividend > 0) is (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        ret = 0
        for i in range(31, -1, -1):
            if dividend >> i >= divisor:
                ret |= 0x01 << i
                dividend -= divisor << i
        if not sign:
            ret = 0 - ret
        return ret

