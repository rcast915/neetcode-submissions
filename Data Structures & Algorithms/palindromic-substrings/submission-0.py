class Solution:
    def countSubstrings(self, s: str) -> int:

        def helper(s,left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            return count 

        result = 0

        for index in range(len(s)):
            result += helper(s, index, index)
            result += helper(s, index, index + 1)

        return result

  