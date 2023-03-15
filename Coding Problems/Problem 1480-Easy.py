class Solution(object):
    def runningSum(self, nums):
        ans = []
        sum = 0
        for num in range(len(nums)):
            sum = sum + nums[num]
            ans.append(sum)
        
        return ans