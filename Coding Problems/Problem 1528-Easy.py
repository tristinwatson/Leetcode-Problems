class Solution(object):
    def restoreString(self, s, indices):
        ans = ""
        ht = {}
        i = 0

        for i in range (len(indices)):
            ht[indices[i]] = s[i]

        for j in range(len(ht)):
            ans += ht[j]

        return ans