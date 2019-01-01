from math import sqrt, floor

# 10^8
LIMIT = 1_00_000_000
square_limit = floor(sqrt(LIMIT))

''' 
We can loop through all integers up to the square root limit.
The square root limit is such that if we square the integer one after it, we will be
over the limit.

1^2 will give us an eligible number.

I don't know any math tricks so I'll brute force this.
'''
results = []

def palindrome(num):
    str_num = str(num)
    if str_num == str_num[::-1]:
        return True
    return False

for start_int in range(1, square_limit):
    # Square the integer
    temp_sum = start_int ** 2

    for j in range(start_int + 1, square_limit):
        # Add the next consecutive number squared to the temp sum
        temp_sum += j ** 2
        # If we've broken the limit, maybe with the sum of squares of very large numbers, then break
        if temp_sum >= LIMIT:
            break

        if temp_sum not in results and palindrome(temp_sum):
            results.append(temp_sum)

print(f'Final sum: {sum(results)}')