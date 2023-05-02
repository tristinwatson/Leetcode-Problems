class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        w, x, y, z = nums[0], nums[1], nums[-1], nums[-2]
        ans = (y * z) - (w * x)

        return ans