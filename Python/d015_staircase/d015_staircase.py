
import math

def memoizer(calculate_function):

    class calculation_memoizer(object):

        def __init__(self, calculate_function):
            self.calculate_function = calculate_function
            self.calculations_cache = {}

        def __call__(self, *args):
            if args in self.calculations_cache:
                return self.calculations_cache[args]
            else:
                self.calculations_cache[args] = self.calculate_function(*args)
                return self.calculations_cache[args]

    return calculation_memoizer(calculate_function)

@memoizer
def calculate(remaining_bricks, last_step):
    options = 0
    if remaining_bricks/float((last_step + 1)) <= 2:
        print("{0} : {1}".format(remaining_bricks, last_step))
        return 1
    else:
        options += 1
    limit = int(math.ceil(remaining_bricks/2.0))
    for i in range(last_step + 1, limit):

        options += calculate(remaining_bricks - i, i)
    return options

def answer(n):
    return calculate(n, 0) - 1

number = int(input("Enter number of bricks: "))
staircase_options = answer(number)
print(staircase_options)