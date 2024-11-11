def maxSum(grid):
    max_sum = float('-inf')  # Initialize to the smallest possible value
    rows = len(grid)
    cols = len(grid[0])
    
    # Iterate over possible hourglass centers (the middle point of each hourglass)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Compute the sum of the current hourglass
            top = grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1]
            middle = grid[i][j]
            bottom = grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]
            hourglass_sum = top + middle + bottom
            
            # Update max_sum if the current hourglass sum is larger
            max_sum = max(max_sum, hourglass_sum)
    
    return max_sum
