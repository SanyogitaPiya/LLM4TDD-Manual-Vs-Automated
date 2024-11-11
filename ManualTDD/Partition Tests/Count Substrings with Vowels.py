def count_substrings(word, k):
    vowels = set('aeiou')
    n = len(word)
    
    # Initialize the sliding window and consonant count
    start = 0
    consonant_count = 0
    valid_substrings = 0

    # Iterate with 'end' pointer to expand the window
    for end in range(n):
        # If it's a consonant, increase the consonant count
        if word[end] not in vowels:
            consonant_count += 1
        
        # Shrink the window if the consonant count exceeds k
        while consonant_count > k:
            if word[start] not in vowels:
                consonant_count -= 1
            start += 1
        
        # When the number of consonants in the window is exactly k
        if consonant_count == k:
            # Check if the substring contains only vowels and exactly k consonants
            valid_substrings += 1
    
    return valid_substrings



