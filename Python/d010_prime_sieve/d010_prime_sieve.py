import math

number = int(input("Enter a number, and all primes below it shall be found: "))

numbers = list(range(2, number))

for i in range(2, math.floor(math.sqrt(number))):
    for num in range(i**2, number, i):
        if num in numbers:
            numbers.remove(num)

print(numbers)
