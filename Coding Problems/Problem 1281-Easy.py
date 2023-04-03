class Solution(object):
    def subtractProductAndSum(self, n):
        prod = 1
        sum = 0
        lst = []
        lst.extend(str(n))

        for i in range(len(lst)):
            prod = prod * int(lst[i])
            sum = sum + int(lst[i])
            
        ans = prod - sum

        return ans