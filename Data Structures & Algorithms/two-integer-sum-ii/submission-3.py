class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers: return []

        start = 0
        stop = len(numbers)-1

        while start < stop:
            currsum = numbers[start] + numbers[stop]

            if currsum == target:
                return [start + 1, stop +1]
            elif currsum > target:
                stop -= 1
            else:
                start += 1


        return []