class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        D = {}

        for i in range(len(numbers)):
            D[numbers[i]] = i + 1
        

        for key in D.keys():
            if target - key in D.keys():
                return [D[key], D[target-key]]
        