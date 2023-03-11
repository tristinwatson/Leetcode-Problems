celsius = 122.11

class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        ans = []
        ans.append(round(celsius + 273.15, 5))
        ans.append(round(celsius * 1.80 + 32.00, 5))

        return ans


ans = Solution().convertTemperature(celsius)
print(ans)