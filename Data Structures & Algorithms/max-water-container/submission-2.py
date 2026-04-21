class Solution:
    def maxArea(self, heights: List[int]) -> int:

        if not heights:
            return 0
        
        currmax = 0

        start = 0
        stop = len(heights)-1
        currlen = len(heights)-1

        while start < stop:
            volume = min(heights[start],heights[stop]) * currlen

            currmax = max(volume,currmax) 
 
            if heights[start] <= heights[stop]:
                start += 1
            else:
                stop -= 1
            
            currlen -= 1
        return currmax
        