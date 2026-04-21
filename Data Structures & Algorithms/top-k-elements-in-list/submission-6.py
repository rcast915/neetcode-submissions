from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        result = []

        # Initialize freq with len(nums) + 1 empty lists
        freq = [[] for i in range(len(nums) + 1)]

        # Count the frequency of each number in nums
        for num in nums:
            count[num] += 1

        # Append numbers to freq based on their frequency
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        # Collect the top k frequent elements
        for i in freq[::-1]:
            for num in i:
                result.append(num)
                if len(result) == k:
                    return result

        return result