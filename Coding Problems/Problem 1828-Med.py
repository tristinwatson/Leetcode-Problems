class Solution(object):
    def countPoints(self, points, queries):
        ans = []
        for i in range(len(queries)):
            count = 0
            x1 = queries[i][0]
            y1 = queries[i][1]
            width = queries[i][2]
            tangent = tan(1)
            for j in range(len(points)):
                x2 = points[j][0]
                y2 = points[j][1]
                if (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) <= width * width:
                    count += 1
                else:
                    continue
                    
            ans.append(count)
            
        return ans