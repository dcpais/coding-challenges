class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        // Using Kadane's Algorithm 
        // Ensure that at the end of each loop
        // We are keeping track of the current
        // max sum sub array
        int current = nums[0];
        int best = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            current = max(nums[i], current + nums[i]);
            if (current > best) {
                best = current;
            }
        }
        return best;
    }
};