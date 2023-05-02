class Solution(object):
    def countAsterisks(self, s):
        ans, count = 0, 0

        for i in range(len(s)):
            if s[i] == "|":
                count += 1
            if s[i] == "*" and count % 2 == 0:
                ans += 1
        
        return ans