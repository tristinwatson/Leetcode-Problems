num = 2932
num1 = 4009

class Solution(object):
    def minimumSum(self, num):
        ans1 = ""
        ans2 = ""
        res = 0
        string = str(num)
        list1 = []
        list1.extend(string)

        while True:
            if len(ans2) == 2:
                break
            res = min(list1)
            list1.remove(res)
            if len(ans1) < 2:
                ans1 = ans1 + res
            res = min(list1)
            list1.remove(res)
            if len(ans2) < 2:
                ans2 = ans2 + res

        result = int(ans1) + int(ans2)

        return result
            
ans = Solution().minimumSum(num1)
print(ans)