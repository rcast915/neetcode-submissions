class Solution {
public:
    int rob(vector<int>& nums) {
        int prev = 0;
        int prev2 = 0;
        int current_max = 0;

        for (int num: nums){
            current_max = std::max(prev, prev2 + num);

            prev2 = prev;
            prev = current_max;
        }

        return current_max;
        
    }
};
