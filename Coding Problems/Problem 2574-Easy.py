class Solution(object):
    def leftRigthDifference(self, nums):
        ans = []

        for i in range(len(nums)):
            left, right = 0, 0

            for j in range(len(nums)):
                if j < i:
                    left += nums[j]
                elif j > i:
                    right += nums[j]

        return ans

