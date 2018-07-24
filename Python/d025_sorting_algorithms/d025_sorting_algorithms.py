import time

def bubble(items):
    result = items[:]
    for limit in range(len(result) - 1, 0, -1):  # Starts at end of list and goes down
        for num in range(limit):                # Goes from start of list up to end
            if result[num + 1] < result[num]:     
                temporary_holder = result[num]
                result[num] = result[num + 1]
                result[num + 1] = temporary_holder

    return result

if __name__=="__main__":
    test_list = [5, 6, 1, 2, 7, 8, 11, 3, 20, 3, 1, 50, 1, 5, 6, 1, 3, 4, 8, 40, 5] * 1000
    start = time.time()
    print(bubble(test_list))
    total = time.time() - start
    print(f"Bubble sort on list of length {len(test_list)} took {total} seconds")