def find_almost_equal_substring(s: str, pattern: str) -> int:
    pattern_length = len(pattern)
    
    # Iterate through all substrings of s with the length of pattern
    for i in range(len(s) - pattern_length + 1):
        # Extract the substring of s that matches the length of pattern
        substring = s[i:i + pattern_length]
        
        # If the substring matches exactly, return the current index
        if substring == pattern:
            return i

        # Count the number of differing characters
        differences = sum(1 for x, y in zip(substring, pattern) if x != y)
        
        # Check if exactly one character needs to change to match the pattern
        if differences == 1:
            return i
            
    # If no almost-equal substring is found, return -1
    return -1
