# Check if the lengths of both strings are different
    if len(s) != len(t):
        return False
    
    # Create two dictionaries to store character mappings
    mapping_s_to_t = {}
    mapping_t_to_s = {}
    
    for char1, char2 in zip(s, t):
        # Check mapping from s to t
        if char1 in mapping_s_to_t:
            if mapping_s_to_t[char1] != char2:
                return False
        else:
            mapping_s_to_t[char1] = char2
        
        # Check mapping from t to s
        if char2 in mapping_t_to_s:
            if mapping_t_to_s[char2] != char1:
                return False
        else:
            mapping_t_to_s[char2] = char1

    return True