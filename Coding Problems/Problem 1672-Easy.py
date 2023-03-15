accounts = [[1,2,3],[3,2,1]]
accounts2 = [[1,5],[7,3],[3,5]]
accounts3 = [[2,8,7],[7,1,3],[1,9,5]]

class Solution(object):
    def maximumWealth(self, accounts):
        ans = 0
        for i in range((len(accounts))):
            add = 0
            for j in range((len(accounts[i]))):
                add += accounts[i][j]
                if add > ans:
                    ans = add

        return ans

ans = Solution().maximumWealth(accounts)
print(ans)