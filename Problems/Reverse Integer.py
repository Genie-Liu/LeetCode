import string

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0:
            return 0
        max = 2**31-1
        min = -2**31
        rlt = 0
        i = 0
        sign = 1
        if str[0] == '+':
            sign = 1
            i = 1
        elif str[0] == '-':
            sign = -1
            i = 1
        for s in str[i:]:
            if s in string.digits:
                rlt = rlt*10 + int(s)
            else:
                break
        rlt = rlt*sign
        if rlt > 2**31-1:
            return max
        elif rlt < min:
            return min
        else:
            return rlt


if __name__ == "__main__":
    print(Solution().myAtoi("-0"))

