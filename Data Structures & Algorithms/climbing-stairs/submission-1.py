class Solution:
    def climbStairs(self, n: int) -> int:
        
        prev1, prev2 = 1, 0
       

        for _ in range(n):
            currval = prev1 + prev2

            prev2 = prev1
            prev1 = currval
        

        return prev1


