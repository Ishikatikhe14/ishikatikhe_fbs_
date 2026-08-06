#Sum of all prime numbers between 1 to n

def sum_of_primes(n):
    total = 0
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            total += num
    return total
n= int(input("Enter the value of n: "))
print("Sum of all prime numbers between 1 to n:", sum_of_primes(n))