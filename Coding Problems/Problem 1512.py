nums = [1,2,3,1,1,3]
nums2 = [1,1,1,1]
nums3 = [1,2,3]

class Solution(object):
    def numIdenticalPairs(self, nums):
        i = 0
        j = 1
        count = 0
        
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    count +=1
                j+=1

            i+=1
        return count





ans = Solution().numIdenticalPairs(nums2)
print(ans)