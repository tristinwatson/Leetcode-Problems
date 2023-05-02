class Solution(object):
    def maxDepth(self, s):
        ans, count = 0, 0

        for i in range(len(s)):
            if s[i] == '(':
                count += 1
                if ans < count:
                    ans = count
            elif s[i] == ')':
                count -= 1

        return ans