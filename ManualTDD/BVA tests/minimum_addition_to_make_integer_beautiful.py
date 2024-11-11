def sum_of_digits(num):
    """Helper function to calculate sum of digits of a number."""
    return sum(int(digit) for digit in str(num))

def minimum_addition_to_make_integer_beautiful(n, target):
    """Function to calculate minimum addition to make the sum of digits of n <= target."""
    
    # Step 1: Calculate the sum of digits of n
    current_digit_sum = sum_of_digits(n)
    
    # If the sum of digits is already <= target, no addition is needed
    if current_digit_sum <= target:
        return 0
    
    addition = 0
    while current_digit_sum > target:
        # Step 2: We increment n in a way that reduces the sum of digits
        # We can add large enough values to cause the carry and reduce the sum
        # We calculate the next nearest value that will drop the sum below the target
        n += 1
        current_digit_sum = sum_of_digits(n)
        addition += 1
        
    return addition

