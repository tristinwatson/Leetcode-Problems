class Solution(object):
    def countDigits(self, num):
        ans = 0
        numL = []
        numL.extend(str(num))

        for i in range(len(numL)):
            if num % int(numL[i]) == 0:
                ans += 1

        return ans