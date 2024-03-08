class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        toVisit = {i for i in range(0, len(nums) + 1)}
        for i in nums:
            toVisit.remove(i)
        
        return list(toVisit)[0]