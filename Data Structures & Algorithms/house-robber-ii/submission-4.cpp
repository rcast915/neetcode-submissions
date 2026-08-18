#include <vector>
#include <algorithm>

class Solution {
public:
    int rob(std::vector<int>& nums) {
        // Edge case for a single house
        if (nums.size() == 1) return nums[0];

        // Call our private helper function
        return std::max(helper(nums, 0, nums.size() - 2), 
                        helper(nums, 1, nums.size() - 1));
    }

private:
    // Helper function moved outside of rob()
    int helper(const std::vector<int>& nums, int start, int end) {
        int prev = 0;
        int prev2 = 0;
        int currentmax = 0;

        // Fixed loop syntax and boundary
        for (int i = start; i <= end; i++) {
            currentmax = std::max(prev, prev2 + nums[i]);
            prev2 = prev;
            prev = currentmax;
        }
        
        return currentmax;
    }
};
