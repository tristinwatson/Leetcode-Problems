nums = [1,2,1]

class Solution(object):
    def getConcatenation(self, nums):
        i = 0
        n = 0
        ans = []

        while len(ans) != (2 * len(nums)):
            if len(ans) < len(nums):
                ans.append(nums[i])
                i+=1
            elif len(ans) >= len(nums):
                ans.append(nums[n])
                n+=1

        return ans

ans = Solution().getConcatenation(nums)
print(ans)