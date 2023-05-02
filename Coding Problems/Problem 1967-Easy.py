class Solution(objecT):
    def numOfStrings(self, patterns, word):
        ans = 0

        for i in patterns:
            if i in word:
                ans += 1

        return ans