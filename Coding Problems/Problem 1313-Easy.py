class Solution(object):
    def decompressRLElist(self, nums):
        ans = []

        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            for j in range(freq):
                ans.append(val)

        return ans