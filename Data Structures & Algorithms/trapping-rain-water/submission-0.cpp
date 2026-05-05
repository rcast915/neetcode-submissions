#include <vector>
#include <algorithm> // For std::max

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        // Handle the edge case where the map is empty
        if (height.empty()) {
            return 0;
        }

        int result = 0;
        
        // Initialize our two pointers
        int left = 0;
        int right = height.size() - 1;

        // Initialize the max heights seen from both sides
        int lmax = height[left];
        int rmax = height[right];

        // Process the array until the two pointers meet
        while (left < right) {
            // The smaller of the two maxes bottlenecks the water
            if (lmax < rmax) {
                left++; // Move the left pointer inward
                lmax = max(lmax, height[left]); // Update the left max
                result += lmax - height[left];  // Add trapped water
            } else {
                right--; // Move the right pointer inward
                rmax = max(rmax, height[right]); // Update the right max
                result += rmax - height[right];  // Add trapped water
            }
        }

        return result;
    }
};