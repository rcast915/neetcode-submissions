#include <limits>
class Solution {

public:
    int maxSubArray(vector<int>& nums) {

        double current = 0;
        double max = numeric_limits<int>::lowest();

        for (auto &num : nums){
            current += num;

            if (current > max) max = current;
            if (current < 0) current = 0;

        }

        return max;
    }
};
