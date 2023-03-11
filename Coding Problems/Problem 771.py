jewels, stones= "z", "ZZ"
jewels1, stones1 = "aA", "aAAbbbb"

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        i = 0
        ans = 0
        jewelList = []
        for jewel in jewels:
            jewelList.append(jewel)
        while i < len(stones):
            if stones[i] in jewelList:
                ans+=1
            i+=1

        return ans

ans = Solution().numJewelsInStones(jewels, stones)
print(ans)