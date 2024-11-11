def next_greater_element_iv(nums):
    n = len(nums)
    first_greater = [-1] * n
    second_greater = [-1] * n
    stack = []

    # First pass: Find the first greater element for each index using a stack
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            first_greater[i] = stack[-1]
        stack.append(nums[i])
    
    # Second pass: Find the second greater element for each index
    for i in range(n - 1, -1, -1):
        if first_greater[i] != -1:
            # Search for an element greater than first_greater[i]
            found_second = False
            for j in range(i + 1, n):
                if nums[j] > first_greater[i]:
                    second_greater[i] = nums[j]
                    found_second = True
                    break
            if not found_second:
                second_greater[i] = -1
    
    return second_greater