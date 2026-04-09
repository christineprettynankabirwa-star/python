N = int(input("Enter any positive integer: "))

# numbers <= 1 are not prime
if N <= 1:
    print(f"{N} is not a prime number.")

else:
    is_prime = True

    # check divisibility from 2 to N-1
    for i in range(2, N):
        if N % i == 0:
            is_prime = False
            break 

    # for i in range(2, int(N**0.5) + 1):
    #     if N % i == 0:
    #         is_prime = False
    #         break 

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")