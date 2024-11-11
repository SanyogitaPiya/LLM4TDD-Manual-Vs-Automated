class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def number_of_good_paths(vals, edges):
    n = len(vals)
    uf = UnionFind(n)

    # Sort edges by the maximum value of the nodes they connect
    edges.sort(key=lambda edge: max(vals[edge[0]], vals[edge[1]]))

    # Process each edge, connecting nodes with the same value
    for u, v in edges:
        if vals[u] == vals[v]:
            uf.union(u, v)

    # Counting good paths
    good_paths = 0
    component_sizes = {}

    # Group nodes by their root (representative of their connected component)
    for i in range(n):
        root = uf.find(i)
        if root not in component_sizes:
            component_sizes[root] = []
        component_sizes[root].append(i)

    # Count single-node good paths (each node is a good path by itself)
    for nodes in component_sizes.values():
        good_paths += len(nodes)

    # Count multi-node good paths: paths between nodes with the same value
    for root, nodes in component_sizes.items():
        # Find all nodes that have the same value
        value_groups = {}
        for node in nodes:
            value = vals[node]
            if value not in value_groups:
                value_groups[value] = []
            value_groups[value].append(node)
        
        # For each group of nodes with the same value, calculate how many good paths can be formed
        for value_group in value_groups.values():
            # Add combination of pairs of nodes in the group (choose 2)
            good_paths += len(value_group) * (len(value_group) - 1) // 2  # Combination of 2 nodes
    
    return good_paths
