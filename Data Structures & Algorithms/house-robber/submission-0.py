class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for val in nums:
            # find the current max
            temp = max(val + rob1, rob2)

            # update
            rob1 = rob2
            rob2 = temp
        

        return rob2