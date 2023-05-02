class Solution(object):
    def countConsistentStrings(self, allowed, words):
        ans = 0
        lst = set(allowed)

        for i in words:
            for j in i:
                if j not in lst:
                    ans += 1
                    break
                
        return len(words) - ans