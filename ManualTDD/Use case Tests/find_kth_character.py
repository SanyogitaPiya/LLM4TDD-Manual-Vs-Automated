def find_kth_character(k, operations):
    # Initial setup: sequence is just 'a'
    base_character = "a"
    current_length = 1  # Starting length of the sequence (just "a")

    # Apply operations to compute the final length and character state
    for op in operations:
        if op == 0:
            current_length *= 2  # Doubling the sequence length
        elif op == 1:
            # Shift character to next letter in the alphabet
            base_character = chr(((ord(base_character) - ord("a") + 1) % 26) + ord("a"))
        
        # If the length exceeds k, stop expanding further
        if current_length >= k:
            break

    # Backtrack through the operations to find the character at the k-th position
    for op in reversed(operations):
        if current_length == 1:
            break  # Reached the original string of just "a"

        if op == 0:
            # Undo the doubling: if k is in the second half, adjust its position
            current_length //= 2
            if k > current_length:
                k -= current_length  # Adjust k to the first half equivalent position

        elif op == 1:
            # Undo the transformation: revert the character to its previous state
            base_character = chr(((ord(base_character) - ord("a") - 1) % 26) + ord("a"))

    # Return the final character after applying the operations
    return base_character

# Test case to check the debugging
def test_case_6():
    k = 20
    operations = [0, 1, 0, 0, 1]
    assert find_kth_character(k, operations) == "c"  # Expected 'c'
    print("Test case passed")

test_case_6()
