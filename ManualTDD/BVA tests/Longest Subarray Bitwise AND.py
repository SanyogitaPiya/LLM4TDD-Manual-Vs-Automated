def longest_subarray_with_max_bitwise_and(nums):
    # Find the maximum value in the array
    max_and = max(nums)
    
    # Initialize variables to track the longest subarray of the max_and value
    max_length = 0
    current_length = 0
    
    # Loop through the array to find the longest subarray that contains only max_and
    for num in nums:
        if num == max_and:
            current_length += 1  # Increase the length of the current subarray
            max_length = max(max_length, current_length)  # Update the max length if needed
        else:
            current_length = 0  # Reset the length if the current number is not max_and
    
    return max_length
