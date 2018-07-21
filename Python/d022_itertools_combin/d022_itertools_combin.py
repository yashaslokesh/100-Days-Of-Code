import itertools # Use itertools for combinations

def answer(num_buns, num_required):
    
    # result = []
    # Create the result list with as many inner lists as there are bunnies 
    result = [[] for _ in range(num_buns)]

    # The required number of copies of each key can be expressed this way.
    # I got this formula using the examples of (3, 2), (4, 4), (5, 3), (2, 1), and (8, 9)
    copies_of_each_key = 1 + num_buns - num_required

    """
        Creates an itertools combinations object. num_buns choose copies_of_each_key
        gives all possible combinations for the placement of each key among each of the bunnies
    """
    combinations_list = itertools.combinations(range(num_buns), copies_of_each_key)

    """
        In example of 5 choose 3, we have 10 possible combinations. The "key" value will go
        through the range of keys needed, hence through all combinations. Each tuple combination, 
        named key_assignments, lists each of the bunnies that should receive a copy of the 
        corresponding key, the index of that tuple. enumerate(combinations_list) returns
        a sorted iterable of the combinations. We can then loop through each of the tuples inside,
        added a key assignment to each bunny in turn.
    """
    for key, key_assignments in enumerate(combinations_list):
        # print(key)
        # print(key_assignments)
        for bunny in key_assignments:
            result[bunny].append(key)

    return result