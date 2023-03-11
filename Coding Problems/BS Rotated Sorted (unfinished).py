nums = [6, 7, 8, 4, 5]
nums2 = [1, 2, 3, 4, 5, 6]
nums3 = [7, 8, 9, 1, 3, 4, 6]
nums4 = [2, 3, 4, 5, 6, 7, 8, 1]
nums5 = []

def bs_rotations(num):
    # empty list
    if not num:
        return "empty list"
    
    low = 0
    hi = len(num - 1)


    while low <= hi:
        mid = (hi + low) // 2
        mid_number = num[mid]

        if mid > 0 and num[mid_number] < num[mid_number - 1]:
            return mid
        elif num[mid_number] < num[mid_number - 1]:
            hi = mid - 1
        else:
            low = mid + 1
     
    return "not rotated"

rotations = bs_rotations(nums3)
print(rotations)