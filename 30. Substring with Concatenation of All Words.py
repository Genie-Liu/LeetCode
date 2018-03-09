class Solution:
    # use window slide method to scan all possible
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words or not words[0]:
            return []
        k = len(words[0])
        n = len(words)
        lens = len(s)
        ws = n*k
        base = {}
        ans = []
        if ws > lens: return []
        for w in words:
            if w in base:
                base[w] += 1
            else:
                base[w] = 1
        for i in range(k):
            self._findSub(s, i, i, k, lens, ws, base, ans)
        return ans




    def _findSub(self, s, l, r, k, lens, ws, base, ans):
        curr = {}
        while r + k <= lens:
            w = s[r:r+k]
            r += k
            if w not in base:
                curr.clear()
                l = r
            else:
                if w in curr:
                    curr[w] += 1
                else:
                    curr[w] = 1
                while curr[w] > base[w]:
                    curr[s[l:l+k]] -= 1
                    l += k
                if r-l == ws:
                    ans.append(l)
