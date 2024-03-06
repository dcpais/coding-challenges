class Solution:
    def rob(self, nums: List[int]) -> int:
        lookup = [0 for i in range(len(nums) + 2)]

        for i in range(len(nums) - 1, -1, -1):
            lookup[i] = max(nums[i] + lookup[i + 2], lookup[i + 1])

        return max(lookup[0], lookup[1])