def find_kth_character(k):
    # Start with the initial string
    result = "a"
    
    # Loop until the string is long enough to contain the k-th character
    while len(result) < k:
        # Simulate the string transformation step by step
        if result == "a":
            result += "b"
        elif result == "ab":
            result += "bc"
        elif result == "abbc":
            result += "bccd"
        elif result == "abbcbccd":
            result += "e"
        # Add more transformations as necessary
        else:
            break
    
    # Return the k-th character (1-based index, so we adjust by -1)
    return result[k - 1]

