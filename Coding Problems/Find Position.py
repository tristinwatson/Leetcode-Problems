query = 4
List = [1, 3, 4, 6, 7, 8, 10]
List2 = [40, 30, 26, 14, 11, 10, 5]
List3 = []

# this is a linear O(N) solution to find positions
def card_position(cards, query):
    # sets position to 0 for index
    position = 0
    # checks empty list
    if not cards:
        return "empty list"
    # compares list of position index to query
    while cards[position] != query:
        position+=1

        # card not found
        if len(cards) == position:
            return "card not in list"

    return position

results = card_position(List, query)
print(results)