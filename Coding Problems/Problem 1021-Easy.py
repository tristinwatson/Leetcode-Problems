class Solution(object):
    def removeOuterParentheses(self, s):
        ans = ""
        count, j, k = 0, 0, 1

        for i in range(len(s)):
            if s[i] == '(':
                count += 1
                j += 1
            elif s[i] == ')':
                count -= 1
                j += 1
            if count == 0:
                ans += s[k:j-1]
                k = j + 1

        return ans
