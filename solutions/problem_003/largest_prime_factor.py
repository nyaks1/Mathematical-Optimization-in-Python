def largest_prime_factor(n):
    """
    Finds the largest prime factor of the number
    """
    # Step 1: Strip out all factors of 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # Step 2: Check odd numbers up to sqrt(n)
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            largest_factor = divisor
            n //= divisor  # Aggressively shrinks n
        divisor += 2       # Skip even numbers entirely

    # Step 3: If n is still greater than 1, the remaining n is prime
    if n > 1:
        largest_factor = n

    return largest_factor

if __name__ == "__main__":
    # Project Euler Problem 3 Benchmark Challenge
    target = 600851475143
    result = largest_prime_factor(target)
    print(f"The largest prime factor of {target} is: {result}")
