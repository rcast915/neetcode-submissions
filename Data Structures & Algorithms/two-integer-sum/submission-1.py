from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = defaultdict(list)

        for indx, num in enumerate(nums):
            complement = target - num

            if len(D[complement]) > 0:
                return [D[complement][0], indx]
            else:
                D[num].append(indx)
        
        