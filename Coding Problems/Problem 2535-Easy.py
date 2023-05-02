class Solution(object):
    def differenceOfSum(self, nums):
        diff, sum1, sum2 = 0, 0, 0

        for i in range(len(nums)):
            sum1 += nums[i]

            if len(str(nums[i])) > 1:
                tokens = []
                tokens.extend(str(nums[i]))

            for j in range(len(tokens)):
                sum2 += int(tokens[j])

            else:
                sum2 += nums[i]

        diff = abs(sum1 - sum2)

        return diff
            

