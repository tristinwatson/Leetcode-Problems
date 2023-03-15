nums = [0,2,1,5,3,4]

class Solution(object):
    def buildArray(self, nums):
        self.nums = nums
        ans = []
        i = 0
        while i < len(nums):
            addTo = nums[nums[i]]
            ans.append(addTo)
            i+=1
        return ans


ans = Solution().buildArray(nums)
print(ans)