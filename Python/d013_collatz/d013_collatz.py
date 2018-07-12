
def collatz(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        count += 1
    return count

if __name__ == "__main__":
    n = int(input("Enter the number for which you'd like to calculate the collatz steps: "))
    steps = collatz(n)
    print(f"The number {n} takes {steps} steps to finish the collatz sequence")