class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        digit_1 = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        digit_10 = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        digit_100 = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]

        roman_num = ""

        if num >= 1000:
            roman_num = roman_num + int(num / 1000) * "M"
            num = num % 1000
        if num >= 100:
            roman_num = roman_num + digit_100[int(num / 100) - 1]
            num = num % 100
        if num >= 10:
            roman_num = roman_num + digit_10[int(num / 10) - 1]
            num = num % 10
        if num != 0:
            roman_num = roman_num + digit_1[num - 1]

        return roman_num
