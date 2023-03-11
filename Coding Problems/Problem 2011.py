operations = ["--X","X++","X++"]
operations2 = ["++X","++X","X++"]

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        i = 0
        ans = 0
        while i != len(operations):
            if operations[i] == "++X" or operations[i] == "X++":
                ans+=1
            elif operations[i] == "--X" or operations[i] == "X--":
                ans-=1
            i+=1

        return ans

ans = Solution().finalValueAfterOperations(operations2)
print(ans)