def test_happy_number():
    assert isHappy(1), "Test Case 1 Failed"

def test_another_happy_number():
    assert isHappy(7), "Test Case 2 Failed"

def test_non_happy_numbers():
    assert not isHappy(2), "Test Case 3 Failed"
    assert not isHappy(3), "Test Case 4 Failed"
    assert not isHappy(4), "Test Case 5 Failed"

def test_edge_cases():
    assert not isHappy(5), "Test Case 6 Failed"
    assert not isHappy(6), "Test Case 7 Failed"
    assert isHappy(10), "Test Case 8 Failed"

def test_large_happy_number():
    assert isHappy(19), "Test Case 9 Failed"