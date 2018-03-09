class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: stra
        :rtype: int
        """
        openp = 0
        maxp = 0
        dp = [0] * (len(s) + 1)
        for i in range(len(s)):
            if s[i] == '(':
                openp += 1
            else:
                if openp > 0:
                    if s[i - 1] == '(':
                        dp[i+1] = dp[i - 1] + 2
                    else:
                        dp[i+1] = dp[i] + 2 + dp[i - dp[i] - 1]
                    openp -= 1
                    maxp = max(maxp, dp[i+1])
        return maxp

