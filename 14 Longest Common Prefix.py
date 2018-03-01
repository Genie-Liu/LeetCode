class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        min_s = min(strs, key=len)
        for i, ch in enumerate(min_s):
            for o in strs:
                if o[i] != ch:
                    return min_s[:i]
        return min_s