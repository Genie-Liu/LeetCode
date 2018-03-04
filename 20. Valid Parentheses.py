class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        st = []
        for c in s:
            if not st and (c == ")" or c == "}" or c == "]"):
                return False
            if (c == ")" and st[-1] == "(") or (c == "]" and st[-1] == "[") or (c == "}" and st[-1] == "{"):
                st.pop()
            else:
                st.append(c)
        return not st
