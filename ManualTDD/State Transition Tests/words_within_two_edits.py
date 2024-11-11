def words_within_two_edits(queries, dictionary):
    def is_within_two_edits(word1, word2):
        # If words are of different lengths, they cannot be within two edits if the difference is greater than 2.
        if abs(len(word1) - len(word2)) > 2:
            return False
        
        # Check if they are within two edits apart (either insertion, deletion, or substitution)
        edits = 0
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            if word1[i] != word2[j]:
                edits += 1
                if edits > 2:
                    return False
                # Move to the next character in the longer word.
                if len(word1) > len(word2):
                    i += 1
                elif len(word1) < len(word2):
                    j += 1
                else:
                    i += 1
                    j += 1
            else:
                i += 1
                j += 1
        if i < len(word1) or j < len(word2):
            edits += 1
        
        return edits <= 2
    
    result = []
    for query in queries:
        matched_words = [word for word in dictionary if is_within_two_edits(query, word)]
        if matched_words:
            result.append(query)
    
    return result
