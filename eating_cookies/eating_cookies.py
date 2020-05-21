'''
Input: an integer
Returns: an integer
'''

# awnser should be awnsered with recursion
def eating_cookies(n, cache):
    # Your code here
    if n < 0:
        return 0

    elif n == 0:
        return 1

    elif cache and cache[n] > 0:
        return cache[n]

    else:
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
### Fibanacii sequence