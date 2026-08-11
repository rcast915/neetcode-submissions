from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        return self.helper(0,0,m,n)

    @cache
    def helper(self, currx, curry, m, n) -> int:
        
        if currx == m - 1 and curry == n - 1:
            return 1
        
        elif currx >= m or curry >= n:
            return 0
        
        # Fixed typo and added 'self.'
        else:
            return self.helper(currx, curry + 1, m, n) + self.helper(currx + 1, curry, m, n)