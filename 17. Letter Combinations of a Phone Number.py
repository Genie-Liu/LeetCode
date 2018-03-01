from collections import deque


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ret = deque()
        ret.append("")
        mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if not digits:
            return []
        for i, d in enumerate(digits):
            s = mapping[int(d)]
            while len(ret[0]) == i:
                p = ret.popleft()
                for c in s:
                    ret.append(p + c)
        return list(ret)

