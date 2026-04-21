class Solution {
#include <algorithm>

public:
    int maxProduct(vector<int>& nums) {
        int globalmax = nums[0];

        int currentmax = nums[0];
        int currentmin = nums[0];

        for (int i = 1; i < nums.size(); i++){
            // if the number we are looking at is negative we have to flip
            int number = nums[i];

            if (nums[i] < 0){
                swap(currentmin, currentmax);
            }

            currentmin = min(number, number * currentmin);
            currentmax = max(number, number * currentmax);

            globalmax = max(globalmax, currentmax);

        }
        return globalmax;
    }
};
