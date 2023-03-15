list = [[1, 1, 0], [1], [2], [3], [1]]
big, medium, small = list[0][0], list[0][1], list[0][2]
carType = list[1][0]

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType):
        if carType == 1 and self.big >= 1:
            self.big = self.big - 1
            return True
        elif carType == 2 and self.medium >= 1:
            self.medium = self.medium - 1
            return True
        elif carType == 3 and self.small >= 1:
            self.small = self.small - 1
            return True
        else:
            return False
        


obj = ParkingSystem(big, medium, small)
param_1 = obj.addCar(carType)
print(param_1)