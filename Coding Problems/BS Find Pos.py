query = 4
List = [10, 7, 5, 4, 3, 2, 1]
List2 = [40, 30, 26, 14, 11, 10, 5]
List3 = []
List4 = [9, 9, 9, 7, 6, 5, 5, 5, 4, 4, 4, 1]

# this is an O(log(N)) Binary Search for finding position
def check_multi(cards, query, position):
    # states the mid number of the search so far
    mid = cards[position]
    
    # compares mid number to query number
    if mid == query:
        # checks if position is not 0 and if the index of list 
        # with (position - 1) equals query
        if position - 1 >= 0 and cards[position - 1] == query:
            return 'left'
        # if mid == query and above if statement is not true
        # return 'found'
        else:
            return 'found'
        # checks if position is less than query return 'left' 
        # else return 'right'
    elif position < query:
        return 'left'
    else:
        return 'right'
    

def binary_search(cards, query):
    if not cards:
        return "empty list"
    
    # sets hi to the max list index
    # sets low to index 0
    hi = len(cards) - 1 
    low = 0

    #compares low and hi
    while low <= hi:
        # creates a middle position by adding (low and hi) // 2
        position = (low + hi) // 2
        # calls check_multi method with specified arguments
        result = check_multi(cards, query, position)

        # results of check_multi
        if result == 'found':
            return position
        elif result == 'left':
            hi = position - 1
        elif result == 'right':
            low = position + 1
        
    return "card not in list"

results = binary_search(List4, query)
print(results)