N = int(input("Enter any positive integer: "))

# numbers <= 1 are not prime
if N <= 1:
    print(f"{N} is not a prime number.")

else:
    is_prime = True

    # check divisibility from 2 to N-1
    for i in range(2, N):
