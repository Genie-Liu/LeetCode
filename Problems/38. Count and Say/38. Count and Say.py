class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        init = "1"
        if n <= 1: return init
        for i in range(n-1):
            init = self.nextN(init)
        return init

    def nextN(self, pre):
        rlt = ""
        start = 0
        while start < len(pre):
            curr = pre[start]
            count = 0
            while start < len(pre) and pre[start] == curr:
                count += 1
                start += 1
            rlt += str(count) + str(curr)
        return rlt

