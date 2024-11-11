def average_value(nums):
    # Filter even numbers that are also divisible by 3
    valid_nums = [num for num in nums if num % 2 == 0 and num % 3 == 0]
    # Calculate the average if there are any valid numbers; otherwise, return 0
    return sum(valid_nums) // len(valid_nums) if valid_nums else 0
