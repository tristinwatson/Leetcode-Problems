class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans = []
        for i in range(len(candies)):
            hi = candies[i] + extraCandies
            sum = 0
            for j in range(len(candies)):
                if hi >= candies[j]:
                    sum+=1

            if sum == len(candies):
                ans.append(True)
            else:
                ans.append(False)
        
        return ans