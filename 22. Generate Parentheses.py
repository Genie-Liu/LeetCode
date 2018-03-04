class Solution:
    def dsp(self, left, right, base, rlt):
        if left == 0 and right == 0:
            rlt.append(base)
        else:
            if left >= right and left > 0:
                self.dsp(left-1, right, base+"(", rlt)
            else:
                if left > 0:
                    self.dsp(left-1, right, base+"(", rlt)
                if right > 0:
                    self.dsp(left, right-1, base+")", rlt)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rlt = []
        self.dsp(n, n, "", rlt)
        return rlt
