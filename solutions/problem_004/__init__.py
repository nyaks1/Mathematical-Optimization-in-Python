def largest_palindrome_product() -> int:
    """
    Finds the largest palindrome made from the product of two 3-digit numbers.
    
    Time Complexity: O(n^2) where n is the range of 3-digit numbers.
    Space Complexity: O(1)
    """
    max_palindrome = 0

    for a in range(999, 99, -1):
        # Optimization: b doesn't need to check numbers greater than a.
        # This cuts our search space completely in half (avoids checking 999*998 AND 998*999).
        for b in range(a, 99, -1):
            product = a * b
            
            # Optimization Shortcut: If the product is already smaller than the 
            # largest palindrome we've found, breaking out of the inner loop saves cycles.
            if product <= max_palindrome:
                break
                
            # Cast to string and verify mirror symmetry
            product_str = str(product)
            if product_str == product_str[::-1]:
                max_palindrome = product


    return max_palindrome

if __name__ == "__main__":
    result = largest_palindrome_product()
    print(f"The largest palindrome product of two 3-digit numbers is: {result}")