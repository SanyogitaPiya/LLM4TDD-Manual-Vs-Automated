class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeQueries(root, queries):
    # Step 1: Compute the height of each subtree rooted at each node
    heights = {}
    
    def calculate_height(node):
        if not node:
            return 0
        left_height = calculate_height(node.left)
        right_height = calculate_height(node.right)
        heights[node.val] = 1 + max(left_height, right_height)
        return heights[node.val]
    
    calculate_height(root)

    # Step 2: Process each query
    result = []
    def get_height_excluding_subtree(node, excluding_val):
        if not node or node.val == excluding_val:
            return 0
        left_height = get_height_excluding_subtree(node.left, excluding_val)
        right_height = get_height_excluding_subtree(node.right, excluding_val)
        return 1 + max(left_height, right_height)
    
    for query in queries:
        result.append(get_height_excluding_subtree(root, query) - 1)
        
    return result

# Code to satisfy the test
