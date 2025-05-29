# Graph Pattern Cheatsheet

## 1. Pattern Overview
**What it is:** Traversing and analyzing nodes connected by edges using DFS/BFS to solve connectivity, path, and relationship problems.

**When to recognize/use this pattern:**
- **Connected components:** "How many islands/groups/clusters are there?"
- **Path existence:** "Is there a path from A to B?" or "Can you reach target?"
- **Shortest path:** "What's the minimum steps/distance to reach target?"
- **Cycle detection:** "Is there a cycle?" or "Can you finish all courses?"
- **Level-by-level processing:** "Process nodes level by level" or "minimum steps"
- **Dependency relationships:** "Prerequisites", "topological order", "can finish"
- **Keyword triggers:** "connected", "island", "path", "graph", "tree", "neighbors", "adjacent", "reachable"

## 2. Core Template/Algorithm Steps

### General Algorithm Steps:
1. **Setup:** Initialize visited set/array, queue/stack, result variables
2. **Main Logic:** For each unvisited node, start DFS/BFS
3. **Process:** Visit current node, mark as visited, explore neighbors
4. **Termination:** When no more unvisited neighbors or target found
5. **Return:** Count, path, boolean result, or modified structure

### Code Template:
```python
# DFS Template (Most Common)
def dfs_template(graph, start):
    visited = set()  # or boolean array
    result = []
    
    def dfs(node):
        visited.add(node)  # Mark as visited immediately
        result.append(node)  # Process current node
        
        for neighbor in graph[node]:
            if neighbor not in visited:  # Only check here
                dfs(neighbor)
    
    dfs(start)
    return result

# BFS Template (For shortest path/level processing)
def bfs_template(graph, start):
    from collections import deque
    queue = deque([start])
    visited = set([start])
    level = 0
    
    while queue:
        size = len(queue)
        for i in range(size):  # Process current level
            node = queue.popleft()
            # Process current node
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        level += 1
    
    return level - 1  # or other result

# Union-Find Template (For connectivity/components)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True
```

## 3. Common Variations
- **Grid DFS/BFS:** 2D array with 4-directional movement (islands, shortest path in grid)
- **Topological Sort:** DFS with post-order or BFS with in-degree (course schedule, alien dictionary)
- **Cycle Detection:** DFS with three colors (white/gray/black) or Union-Find
- **Bipartite Check:** DFS/BFS with 2-coloring
- **Shortest Path:** BFS for unweighted, Dijkstra for weighted
- **All Paths:** DFS with backtracking to find all possible paths
- **Advanced:** Tarjan's (strongly connected components), articulation points

## 4. Key Insights
- **DFS insight:** Goes deep first, good for path existence, cycle detection, and connected components
- **BFS insight:** Level-by-level exploration guarantees shortest path in unweighted graphs
- **Union-Find insight:** Efficiently tracks connectivity without explicit traversal, O(α(n)) per operation
- **Visited tracking insight:** Prevents infinite loops and ensures O(V+E) complexity
- **Graph representation insight:** Adjacency list is usually better than matrix for sparse graphs

## 5. Complexity Analysis
**Time Complexity:**
- DFS/BFS: O(V + E) where V = vertices, E = edges
- Union-Find: O(E × α(V)) where α is inverse Ackermann (nearly constant)
- Grid problems: O(m × n) where m, n are grid dimensions

**Space Complexity:**
- DFS: O(V) for visited set + O(V) for recursion stack = O(V)
- BFS: O(V) for visited set + O(V) for queue = O(V)
- Union-Find: O(V) for parent and rank arrays

**When is this optimal:** Graph algorithms are usually optimal when you need to visit most/all nodes or edges

## 6. Edge Cases Checklist
□ **Empty graph:** Handle null/empty input gracefully
□ **Single node:** Graph with one node, no edges
□ **Disconnected components:** Multiple separate components
□ **Self-loops:** Node pointing to itself
□ **Duplicate edges:** Multiple edges between same nodes
□ **Directed vs undirected:** Different neighbor relationships
□ **Unreachable nodes:** Not all nodes accessible from start
□ **Grid boundaries:** Out of bounds access in 2D grids
□ **Negative cycles:** In weighted graphs (for shortest path)

## 7. Problem Examples
**Easy Level:**
- **Flood Fill** - Basic DFS on 2D grid with color change
- **Number of Islands** - Count connected components using DFS/BFS
- **Find if Path Exists in Graph** - Simple DFS/BFS path existence

**Medium Level:**
- **Course Schedule** - Cycle detection in directed graph using DFS or topological sort
- **Number of Provinces** - Connected components in adjacency matrix
- **Rotting Oranges** - Multi-source BFS with level tracking
- **Clone Graph** - DFS/BFS with node cloning and visited map
- **Pacific Atlantic Water Flow** - DFS from boundaries, intersection of reachable sets

**Hard Level:**
- **Word Ladder** - BFS shortest path with string transformations
- **Alien Dictionary** - Topological sort to determine character ordering
- **Critical Connections** - Tarjan's algorithm for bridges/articulation points

## 8. Common Pitfalls & Mistakes
**Coding Mistakes:**
- **Forgetting visited check:** Leads to infinite loops and TLE
- **Grid boundary errors:** Not checking if indices are within bounds
- **Wrong graph representation:** Using adjacency matrix when list is better
- **Modifying during iteration:** Changing graph structure while traversing

**Logic Mistakes:**
- **DFS vs BFS confusion:** Using DFS when BFS needed for shortest path
- **Directed vs undirected:** Not handling edge directionality correctly
- **Starting point errors:** Not considering all possible starting points for disconnected graphs
- **Early termination:** Stopping search too early before exploring all necessary paths

## 9. Interview Tips
**Recognition:**
- Look for keywords: "connected", "path", "reachable", "components", "islands"
- Ask: "Is this asking about connectivity, shortest path, or counting components?"
- Clarify: "Is the graph directed or undirected? Weighted or unweighted?"

**Implementation:**
- Start with graph representation (adjacency list usually best)
- Choose DFS for simplicity, BFS for shortest path
- Always implement visited tracking first
- Handle edge cases (empty graph, disconnected components)

**Communication:**
- Explain why you chose DFS vs BFS
- Walk through visited tracking to prevent cycles
- Mention time/space complexity: O(V + E)
- Discuss how you handle the graph representation

**Follow-up Questions:**
- "What if the graph is weighted?" → Dijkstra's algorithm
- "What if we need all shortest paths?" → Modified BFS or Floyd-Warshall
- "What if the graph is very large?" → Consider memory optimization or streaming
- "Can you detect cycles?" → Add colors or use Union-Find

## 10. Quick Reference
**Pattern Triggers:** Connected components, path existence, level-by-level processing, dependency relationships
**Template Summary:** 
```python
visited = set()
def dfs(node):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)
```
**Complexity:** O(V + E) time, O(V) space
**Key Insight:** Track visited nodes to avoid cycles, choose DFS for simplicity or BFS for shortest path

---

## Notes Section
- **Grid problems:** Remember to check bounds and use directions array: `[(0,1), (1,0), (0,-1), (-1,0)]`
- **Topological sort:** Use DFS post-order or BFS with in-degree counting
- **Union-Find optimization:** Path compression + union by rank gives nearly O(1) operations
- **Multi-source BFS:** Add all starting points to queue initially (like rotting oranges)
- **Backtracking in graphs:** Remove from visited set when backtracking for "all paths" problems