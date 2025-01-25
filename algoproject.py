def wildlife_monitoring(V, movements):
    # Initialize the adjacency list for the graph
    adjacency_list = {}

    # Add vertices (locations) to the dictionary
    for i in range(V):
        adjacency_list[i] = []

    # Add edges (movements) to the dictionary
    for start, end in movements:
        adjacency_list[start].append(end)

    # Set to keep track of visited nodes and nodes currently in the recursion stack
    visited = set()
    recursion_stack = set()

    # Helper function to perform DFS for cycle detection
    def dfs(node):
        if node in recursion_stack:  # Cycle detected
            return True
        if node in visited:
            return False

        # Mark the node as visited and add it to the recursion stack
        visited.add(node)
        recursion_stack.add(node)

        # Visit all neighbors
        for neighbor in adjacency_list.get(node, []):
            if dfs(neighbor):
                return True

        # Remove the node from the recursion stack after exploring
        recursion_stack.remove(node)
        return False

    # Check each node for a cycle
    for node in adjacency_list:
        if node not in visited:
            if dfs(node):
                return "Loop detected"

    return "No loop detected"

# Test cases for the wildlife monitoring project
V1 = 7  # Number of unique locations
movements1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 2), (4, 6)]
print(wildlife_monitoring(V1, movements1))  # Output: Loop detected

V2 = 5  # Number of unique locations
movements2 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(wildlife_monitoring(V2, movements2))  # Output: No loop detected
