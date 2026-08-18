class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums,start,end):
            prev = 0
            prev2 = 0

            currentmax = 0
            for i in range(start, end + 1):
                currentmax = max(prev, prev2 + nums[i])

                prev2 = prev
                prev = currentmax

            return currentmax

        return max(helper(nums,0,len(nums)-2), helper(nums,1,len(nums)-1))
