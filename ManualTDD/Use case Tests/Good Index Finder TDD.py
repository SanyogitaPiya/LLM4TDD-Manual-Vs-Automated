def find_good_indices(nums, k):
    n = len(nums)
    result = []

    # Early exit if k is too large to have valid indices
    if n < 2 * k + 1:
        return result

    # Arrays to track the longest non-increasing and non-decreasing subarrays
    left_non_increasing = [0] * n
    right_non_decreasing = [0] * n

    # Fill left_non_increasing: counts length of non-increasing subarray ending at each index
    for i in range(1, n):
        if nums[i] <= nums[i - 1]:
            left_non_increasing[i] = left_non_increasing[i - 1] + 1
        else:
            left_non_increasing[i] = 0

    # Fill right_non_decreasing: counts length of non-decreasing subarray starting at each index
    for i in range(n - 2, -1, -1):
        if nums[i] <= nums[i + 1]:
            right_non_decreasing[i] = right_non_decreasing[i + 1] + 1
        else:
            right_non_decreasing[i] = 0

    # Check each potential "good index"
    for i in range(k, n - k):
        if left_non_increasing[i - 1] >= k - 1 and right_non_decreasing[i + 1] >= k - 1:
            result.append(i)

    return result
