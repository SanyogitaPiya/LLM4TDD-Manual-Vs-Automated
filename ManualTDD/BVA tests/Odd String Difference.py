def odd_string_difference(words):
    def get_difference_array(word):
        return [ord(word[i+1]) - ord(word[i]) for i in range(len(word) - 1)]

    # Get the difference arrays for each word
    difference_arrays = [get_difference_array(word) for word in words]
    
    # Find the difference array that is unique
    for i in range(len(difference_arrays)):
        # Count how many times each difference array appears
        if difference_arrays.count(difference_arrays[i]) == 1:
            return words[i]
    
    return None  # Return None if all arrays are the same (though the test case suggests this won't happen)
