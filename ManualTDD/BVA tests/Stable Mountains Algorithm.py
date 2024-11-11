def find_stable_mountains(height, threshold):
    stable_mountains = []
    
    # Start from index 1, because there is no previous mountain to compare at index 0
    for i in range(1, len(height)):
        # Check if current mountain height is >= previous mountain height
        if height[i-1] >= threshold:
            stable_mountains.append(i)  # Append the 1-based index
    
    return stable_mountains
