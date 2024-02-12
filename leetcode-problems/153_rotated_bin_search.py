class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        res = nums[0]

        while lo <= hi:
            if nums[lo] < nums[hi]:
                res = min(res, nums[lo])
                break

            m = (lo + hi) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[lo]:
                lo = m + 1
            else:
                hi = m - 1

        return res


