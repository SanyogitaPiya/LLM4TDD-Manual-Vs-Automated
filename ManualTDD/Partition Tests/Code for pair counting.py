def numberOfPairs(nums1, nums2, diff):
    # Initialize a counter for valid pairs
    count = 0
    
    # Iterate through all pairs (i, j) where i < j
    n = len(nums1)
    for i in range(n):
        for j in range(i + 1, n):
            if nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff:
                count += 1

    return count
