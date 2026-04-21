class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        def getmax(D):
            currmax = float('-inf')

            for value, count in D.items():
                if count > 0:
                    currmax = max(currmax, value)
            return currmax

      
        if k <= 1:
            return nums
        if k > len(nums):
            return max(nums)


        D = collections.defaultdict(int)
        currmax = float('-inf')

        for num in nums[:k]:
            D[num] += 1
            currmax = max(num,currmax)
        
        result = []
        left = 0
        right = k-1

        while right < len(nums):
            D[nums[right]] += 1
            if nums[right] > currmax:
                currmax = nums[right]
            elif D[currmax] == 0: 
                currmax = getmax(D)
            
            result.append(currmax)  

            D[nums[left]] -= 1  
            left += 1
            right += 1
           
        
        return result
            






        