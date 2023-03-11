num1, num2 = 12, 5
num3, num4 = -10, 4

class Solution(object):
    def sum(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        ans = num1 + num2 
        return ans


ans = Solution().sum(num1, num2)
print(ans)