class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for indx, a in enumerate(nums):
            if indx > 0 and a == nums[indx - 1]:
                continue
            
            b = indx + 1
            c = len(nums) - 1 

            while b < c:
                sum_abc = a + nums[b] + nums[c]
                if sum_abc == 0:
                    result.append([a, nums[b], nums[c]])
                    # Skip over duplicate elements for b and c
                    while b < c and nums[b] == nums[b + 1]:
                        b += 1
                    while b < c and nums[c] == nums[c - 1]:
                        c -= 1
                    # Move to the next potential pair
                    b += 1
                    c -= 1
                elif sum_abc < 0:
                    b += 1
                else:
                    c -= 1

        return result
        