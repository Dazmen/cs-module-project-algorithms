'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # declaring the set (used for searching efficiency)
    values = set()

    # looping through the list, adding a value to the set if it is not present and removing it if it is present (this will elimate duplicates from the set)
    for i in arr:
        if i in values:
            values.discard(i)
        elif i not in values:
            values.add(i)

    # set.pop() removes and returns an arbitrary set element, at this point the single number should be the only number left in the set and thus be the only possible number to be popped
    return values.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")