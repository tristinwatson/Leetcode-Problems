rectangle = [[1,2,1],[4,3,4],[3,2,1],[1,1,1]]
row1, col1, row2, col2, newValue = 1,1,2,2,100
row, col = 0,0
row1, col1 = 2,2
rectangle1= [[1,1,1],[2,2,2],[3,3,3]]

class SubrectangleQueries(object):
    def __init__(self, rectangle):
        self.rectangle = rectangle
        

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        r = row1
        while r <= row2:
            c = col1
            while c <= col2:
                self.rectangle[r][c] = newValue

                c+=1
            r+=1

        return self.rectangle

    def getValue(self, row, col):
        return self.rectangle[row][col]

# Your SubrectangleQueries object will be instantiated and called as such:
obj = SubrectangleQueries(rectangle1)
obj.updateSubrectangle(row1,col1,row2,col2,newValue)
param_2 = obj.getValue(row,col)
param_3 = obj.getValue(row1,col1)
print(param_2)
print(param_3)