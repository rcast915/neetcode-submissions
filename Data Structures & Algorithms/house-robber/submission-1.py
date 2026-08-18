class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0   # Max money if we robbed the previous house
        prev2 = 0  # Max money if we robbed the house before the previous

        for num in nums:
            # Calculate the max we can rob up to the current house
            current_max = max(prev, prev2 + num)
            
            # Shift our variables forward for the next iteration
            prev2 = prev
            prev = current_max
        
        return current_max



            
