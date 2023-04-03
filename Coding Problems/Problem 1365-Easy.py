class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans = []

        for i in range(len(nums)):
            sum = 0

            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    sum += 1
                
            ans.append(sum)
        
        return ans