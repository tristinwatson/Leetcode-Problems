class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = ""
        i = 0
        length = word1 + word2

        while len(ans) < len(length):
            if len(word1) > 0:
                ans += word1[i]
                word1 = word1[1:]
            
            if len(word2) > 0:
                ans += word2[i]
                word2 = word2[1:]

        return ans