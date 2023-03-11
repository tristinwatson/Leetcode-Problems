address = "255.100.50.0"

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ans = address.replace('.', '[.]')

        return ans



ans = Solution().defangIPaddr(address)
print(ans)