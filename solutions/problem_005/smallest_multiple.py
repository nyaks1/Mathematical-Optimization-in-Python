def smallest_multiple(limit):
    """
    Finds the smallest positive number evenly divisible
    by all numbers from 1 to limit
    """
    num = limit  # smallest sensible starting point

    while True:
        if all(num % i == 0 for i in range(1, limit + 1)):
            return num
        num += limit  # jump in steps of limit

if __name__ == "__main__":
    result = smallest_multiple(20)
    print(f"Smallest number divisible by 1 to 20: {result}")