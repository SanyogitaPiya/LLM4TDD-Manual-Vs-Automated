def sort_people(names, heights):
    # Combine the names and heights into a list of tuples
    combined = list(zip(names, heights))
    
    # Sort the combined list based on the heights (second item in the tuple), in descending order
    sorted_combined = sorted(combined, key=lambda x: x[1], reverse=True)
    
    # Extract the sorted names from the sorted list
    sorted_names = [name for name, _ in sorted_combined]
    
    return sorted_names

# Test
def test_names_sorted_ascending_by_height():
    names = ["Alice", "Bob", "Emma"]
    heights = [150, 170, 180]
    assert sort_people(names, heights) == ["Emma", "Bob", "Alice"], f"Expected ['Emma', 'Bob', 'Alice'], got {sort_people(names, heights)}"

# Running the test
test_names_sorted_ascending_by_height()
