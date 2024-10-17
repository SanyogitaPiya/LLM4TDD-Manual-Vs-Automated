def test_different_lengths():
    assert not isomorph("ab", "abc"), "Test Case 1 Failed"

def test_identical_mapping():
    assert isomorph("egg", "add"), "Test Case 2 Failed"
    assert isomorph("foo", "app"), "Test Case 3 Failed"

def test_repeated_characters_valid_mapping():
    assert isomorph("paper", "title"), "Test Case 4 Failed"

def test_invalid_mapping():
    assert not isomorph("foo", "bar"), "Test Case 5 Failed"

def test_non_repeating_characters():
    assert isomorph("abc", "def"), "Test Case 6 Failed"
    assert not isomorph("abc", "dee"), "Test Case 7 Failed"

def test_same_characters_different_order():
    assert not isomorph("abc", "bca"), "Test Case 8 Failed"

def test_single_character():
    assert isomorph("a", "b"), "Test Case 9 Failed"
    assert isomorph("a", "a"), "Test Case 10 Failed"

def test_empty_strings():
    assert isomorph("", ""), "Test Case 11 Failed"

def test_large_input_valid():
    s = "abcdefghijklmnopqrstuvwxyz" * 4000
    t = "zyxwvutsrqponmlkjihgfedcba" * 4000
    assert isomorph(s, t), "Test Case 12 Failed"

def test_large_input_invalid():
    s = "abcdefghijklmnopqrstuvwxyz" * 4000
    t = "zyxwvutsrqponmlkjihgfedcba" * 3999 + "a"
    assert not isomorph(s, t), "Test Case 13 Failed"