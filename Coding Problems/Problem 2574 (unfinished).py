nums = [10,4,8,3]
nums2 = [1]

class Solution(object):
    def leftRigthDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        i = 0
        leftSum = 0
        rightSum = 0
        while len(answer) != len(nums):
            if i == 0:
                leftSum = 0
            elif i == (len(nums) - 1):
                rightSum = 0
            for ele in range(0, len(nums)):
                if i > 0:
                    leftSum = leftSum + nums[ele - i]
                    print(f'leftSum {leftSum}')
                if i < len(nums):
                    rightSum = rightSum + nums[ele]
                    print(f'rightSum {rightSum}')
            i+=1
            answer.append(abs(leftSum - rightSum))

        return answer


answer = Solution().leftRigthDifference(nums2)
print(answer)