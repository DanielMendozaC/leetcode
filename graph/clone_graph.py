
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # dfs
        if not node:
            return node
        mapping = {}

        def dfs(node):
            if node in mapping:
                return

            cloned_node = Node(node.val)
            mapping[node] = cloned_node

            for i, nod in enumerate(node.neighbors):
                dfs(nod)
                cloned_node.neighbors.append(mapping[nod]) 

        dfs(node)
        cloned_node = mapping[node]

        return cloned_node
        
        # Time complexity is O(N + E) and space complexity is o(n)


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]  # Return already cloned node

            copy = Node(node.val)
            oldToNew[node] = copy  # Cache immediately to handle cycles
            
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))  # Recursively clone neighbors
            return copy

        return dfs(node) if node else None
        
        # Time: O(N + E), Space: O(N)