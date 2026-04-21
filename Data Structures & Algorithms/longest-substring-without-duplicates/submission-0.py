class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        charset = set()
        l = 0
        currmax = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1

            charset.add(s[r])
            currmax = max(r - l + 1, currmax)

        return currmax
