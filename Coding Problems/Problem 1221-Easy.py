class Solution(object):
    def balanceStringSplit(self, s):
        ans, count = 0, 0

        for i in s:
            if i == "L":
                count += 1
            else:
                count -= 1

            if count == 0:
                ans += 1

        return ans