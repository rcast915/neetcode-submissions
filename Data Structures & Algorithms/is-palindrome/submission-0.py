class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None: return True
        if len(s) == 0:
            return True
        
        if len(s) == 1:
            return True

        s = s.lower()

        if s[0].isalnum() == False:
            return self.isPalindrome(s[1:])
        
        if s[-1].isalnum() == False:
            return self.isPalindrome(s[:-1])
        

        if s[0] == s[-1]:
            return self.isPalindrome(s[1:-1])
        else: return False
            

        





        