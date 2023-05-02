class Solution(object):
    def minOperations(self, boxes):
        ans = []

        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    count += abs(i - j)

            ans.append(count)
        
        return ans