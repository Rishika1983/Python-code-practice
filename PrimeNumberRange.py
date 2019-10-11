# This is a Python Program to print prime numbers in a range using Sieve of Eratosthenes.
# means removing the multiple of the numbers from set.


n = int(input("Enter upper limit of range: "))
sieve = set(range(2, n + 1))
while sieve:
    prime = min(sieve)
    print(prime, end="\t")
    # In this step remove the multiple of varible prime
    sieve -= set(range(prime, n + 1, prime))

print()

