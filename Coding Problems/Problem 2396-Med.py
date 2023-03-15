n = 9
n1 = 2

class Solution(object):
    def isStrictlyPalindromic(self, n):
        def checkPali(n, base):
            string = ""
            while n:
                string += str(n % base)
                n = n // base

            return string
        
        for base in range(2, n - 1):
            string = checkPali(n, base)
            if string != string[::-1]:
                return False
            
        return True

ans = Solution().isStrictlyPalindromic(n)
print(ans)