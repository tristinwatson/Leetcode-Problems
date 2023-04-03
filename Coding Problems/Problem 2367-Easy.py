class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        count = 0

        for i in range(len(nums)):
            if nums[i] - diff in nums and nums[i] - diff - diff in nums:
                count += 1
        
        return count