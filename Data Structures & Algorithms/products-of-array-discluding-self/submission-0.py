class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [0 for i in nums]
        sufix = [0 for i in nums]

        prefixsum = 0

        for index, number in enumerate(nums):
            if index == 0:
                prefix[index] = 1
                prefixsum += number
            else:
                prefix[index] = prefixsum
                prefixsum *= number
        

        sufixsum = 0
        for index, number in reversed(list(enumerate(nums))):
            if index == len(nums) - 1:
                sufix[index] = 1
                sufixsum += number
            else:
                sufix[index] = sufixsum
                sufixsum *= number
        

        for index in range(len(nums)):
            nums[index] = prefix[index] * sufix[index]
        
        return nums

        
                
        