nums = [6, 7, 8, 4, 5]
nums2 = [1, 2, 3, 4, 5, 6]
nums3 = [7, 8, 9, 10, 11, 1, 3, 4, 6]
nums4 = [2, 3, 4, 5, 6, 7, 8, 1]
nums5 = []

# this is a linear O(N) solution to rotation counting
def rotated(numList):
    # set rotations equal to 0 for index
    rotations = 0
    # empty list
    if not numList:
        return "empty list"

    # while loop to check rotation to lenth of list
    while rotations < len(numList):
        # compares list index to index - 1
        if rotations > 0 and numList[rotations] < numList[rotations - 1]:
            return rotations
        
        rotations+=1

    return "not rotated"

rotations = rotated(nums4)
print(rotations)