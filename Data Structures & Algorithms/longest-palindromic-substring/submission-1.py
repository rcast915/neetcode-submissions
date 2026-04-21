class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        curr = ""

        for index in range(len(s)):
            # odd
            left = index 
            right = index 

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left:right+1]) > len(curr):
                    curr = s[left:right+1]
                
                left -= 1
                right += 1
            # even
            left = index
            right = index + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left:right+1]) > len(curr):
                    curr = s[left:right+1]
                
                left -= 1
                right += 1

        return curr