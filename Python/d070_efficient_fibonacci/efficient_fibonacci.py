import numpy as np
import timeit

MATRIX = np.array([[1, 1],
                   [1, 0]])

def log_fibonacci(num):
    result = np.copy(MATRIX)

    # We create a stack, floor dividing by 2 each time. 
    # The length of the stack determines how many matrix multiplications to do
    stack = [num]
    while stack[len(stack) - 1] != 1:
        last_ele = stack[len(stack) - 1]
        stack.append(last_ele // 2 )

    # The last element, which will be one, does not provide any useful info.
    stack.pop()

    while len(stack) != 0:
        result = np.matmul(result, result)

        # If smallest integer is odd, then we multiply by MATRIX once more
        # to match the necessary power on result
        if stack.pop() % 2 == 1:
        # Do one final multiplication in this cycle if we have an odd number
            result = np.matmul(result, MATRIX)

    return result[0][1]

def linear_fibonacci(num):
    # The matrix above to the nth power will have the nth fibonacci
    # number in its second and third entries.
    result = np.copy(MATRIX)

    for _ in range(num - 1):
        result = np.matmul(result, MATRIX)

    # Could've used: 'return result[1][0]'
    return result[0][1]

def main():
    print('Input a number to find that numbered entry in the Fibonacci sequence!')
    num = int(input())
    fib = linear_fibonacci(num)
    print(f'Fibonacci number {num} is {fib}')
    log_fig = log_fibonacci(num)
    print(f'Log(n) time fibonacci number {num} is {log_fig}')

if __name__ == '__main__':
    main()