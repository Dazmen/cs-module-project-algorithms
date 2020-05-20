'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    zero_list = []
    int_list = []

    for i in arr:
        if i == 0:
            zero_list.append(i)
        else:
            int_list.append(i)      

    int_list.extend(zero_list)
    return int_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # arr = [0, 3, 1, 0, -2] # test 1
    # arr = [1, 2, 3, 0, 4, 0, 0] # test 2
    arr = [0, 0, 0, 0, 3, 2, 1] # test 5
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")