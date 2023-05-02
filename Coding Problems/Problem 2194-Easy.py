class Solution(object):
    def cellsInRange(self, s):
        ans = []
        l1, l2 = ord(s[0]), ord(s[3])

        for i in range(l1, l2+1):
            for j in range(int(s[1]), int(s[4])+1):
                hold = chr(i) + str(j)
                ans.append(hold)

        return ans