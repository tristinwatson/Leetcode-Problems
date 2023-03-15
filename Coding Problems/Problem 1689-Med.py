n = "27346209830709182346"

class Solution(object):
    def minPartitions(self, n):
        i = 0
        ans = 0
        while i < len(n):
            if ans < int(n[i]):
                ans = int(n[i])
            if ans == 9:
                return ans
            i+=1
        return ans
        
    
ans = Solution().minPartitions(n)
print(ans)