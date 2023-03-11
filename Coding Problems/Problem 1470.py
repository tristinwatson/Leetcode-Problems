nums = [1,2,3,4,4,3,2,1]
n = 4

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans = []
        i = 0
        n = int(len(nums) / 2)
        while len(ans) != len(nums):
            ans.append(nums[i])
            ans.append(nums[n])
            i+=1
            n+=1
        return ans


ans = Solution().shuffle(nums, n)
print(ans)