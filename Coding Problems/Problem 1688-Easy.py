class Solution(object):
    def numberOfMatches(self, n):
        ans = 0

        while n != 1:
            if n % 2 == 0:
                n /= 2
                ans += n
            elif n % 2 == 1:
                n = (n - 1) / 2 + 1
                ans += n - 1

        return ans
    
        #return n - 1