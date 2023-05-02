class Solution(object):
    def lastStoneWeight(self, stones):
        stones.sort(reverse=True)

        if len(stones) == 1:
            return stones[0]
        
        while len(stones) > 1:
            sub = stones.pop(0)
            if sub - stones[0] == 0:
                stones.pop(0)
            else:
                curr = sub - stones[0]
                stones.pop(0)
                stones.append(curr)

            stones.sort(reverse=True)
        
        if len(stones) == 0:
            return 0
        
        return stones[0]
