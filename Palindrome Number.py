class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        y = 0
        tmp = x
        while tmp > 0:
            tail = tmp % 10
            y = y*10 + tmp % 10
            tmp = (tmp-tail) / 10
        if x == y:
            return True
        else:
            return False

