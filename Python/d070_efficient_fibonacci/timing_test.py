import timeit

def make_setup_string(num):
    string = "import efficient_fibonacci as fib\n"
    string += f"num = {num}"

    return string

def main():
    file = open('results.txt', 'w')
    file.write('Linear\n')

    print("\nLinear testing started")

    for num in range(15, 91, 15):
        comp_time = timeit.timeit('fib.linear_fibonacci(num)', 
                                  setup=make_setup_string(num))
        print(f'\nLinear fibonacci calculation for n={num} took {comp_time} seconds')
        file.write(f'{comp_time}\n')

    file.write('Logarithmic\n')
    print("\nLogarithmic testing started")

    for num in range(15, 91, 15):
        comp_time = timeit.timeit('fib.log_fibonacci(num)', 
                                  setup=make_setup_string(num))
        print(f'\nLogarithmic fibonacci calculation for n={num} took {comp_time} seconds')
        file.write(f'{comp_time}\n')

    print()

    file.close()

if __name__ == '__main__':
    main()