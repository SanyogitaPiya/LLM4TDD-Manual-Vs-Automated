def bitwiseXOROfAllPairings(nums1, nums2):
    # Initialize the result to 0
    result = 0
    n, m = len(nums1), len(nums2)
    
    # Loop over each bit position (0 to 31)
    for bit in range(32):
        # Count how many numbers in nums1 have the current bit set to 1
        count1 = sum((num >> bit) & 1 for num in nums1)
        # Count how many numbers in nums2 have the current bit set to 1
        count2 = sum((num >> bit) & 1 for num in nums2)
        
        # Calculate the number of pairs where the bit positions are different
        # A pair contributes to this bit if one number has the bit set and the other doesn't
        count_pairs = count1 * (m - count2) + (n - count1) * count2
        
        # Each differing pair contributes 2^bit to the final result
        result |= (count_pairs % 2) << bit
    
    return result
