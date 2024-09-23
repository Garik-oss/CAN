# Input from the user
N = int(input("Enter a number N: "))

primes = []
for num in range(2, N):
    isPrime = True
    if num <= 1:
        isPrime = False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            isPrime = False
    if isPrime:
        primes.append(num)

print(f"Prime numbers less than {N}: {primes}")
