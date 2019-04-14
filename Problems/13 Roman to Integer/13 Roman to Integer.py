class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        sum = 0
        for i in range(len(s)):
            if s[i] == "C" and (s.find("D", i) >= 0 or s.find("M", i) >= 0):
                sum -= dic[s[i]]
            elif s[i] == "X" and (s.find("L", i) >= 0 or s.find("C", i) >= 0):
                sum -= dic[s[i]]
            elif s[i] == "I" and (s.find("V", i) >= 0 or s.find("X", i) >= 0):
                sum -= dic[s[i]]
            else:
                sum += dic[s[i]]
        return sum
