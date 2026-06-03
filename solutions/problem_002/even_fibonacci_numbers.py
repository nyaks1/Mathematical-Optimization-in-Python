def even_fibonacci_number(n):
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
    find the sum of the even-valued terms.
    """
    if n < 0:
        raise ValueError("n cannot be negative")
    
    total_sum = 0
    a, b = 0, 1

    while a <= n:
        if a % 2 ==0:
            total_sum += a

        a,b = b, a + b

    return print(total_sum)

even_fibonacci_number(4000000)

