class Solution(object):
    def countKDifference(self, nums, k):
        ans = 0

        for i in range(len(nums)):
            j = 1
            for j in range(len(nums)):
                if i < j and abs(num[i] - nums[j]) == k:
                    ans += 1

        return ans