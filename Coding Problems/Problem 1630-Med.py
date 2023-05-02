class Solution(objecT):
    def checkArithmeticSubarrays(self, nums, l, r):
        ans, sub = [], []

        for i in range(len(l)):
            sub = sorted(nums[l[i]:r[i]+1])

            lr = abs(sub[0] -sub[1])

            for j in range(len(sub) - 1):
                if sub[j] + lr != sub[j+1]:
                    ans.append(False)
                if j == len(sub) - 2:
                    ans.append(True)
            
        return ans