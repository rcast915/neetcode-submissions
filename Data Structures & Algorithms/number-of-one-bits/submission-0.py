class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for i in range(31):

            if (1 << i) & n:
                result += 1
            
        return result