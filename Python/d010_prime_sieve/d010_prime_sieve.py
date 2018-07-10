import math
import time

number = int(input("Enter a number, and all primes below it shall be found: "))

numbers = list(range(2, number))

start = time.time()
for i in range(2, math.floor(math.sqrt(number))):
    for num in range(i**2, number, i):
        if num in numbers:
            numbers.remove(num)
end = time.time()

print(numbers)
print(f"\nNumber of primes below {number}: {len(numbers)}")
print(f"The primes were calculated in {end - start} seconds")
