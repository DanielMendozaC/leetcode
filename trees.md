# Trees Pattern Cheatsheet

## 1. Pattern Overview
**What it is:** Hierarchical data structure with nodes connected by edges, where each node has at most one parent and zero or more children.

**When to recognize/use this pattern:**
- Problem mentions "binary tree", "BST", "root", "leaf", "parent/child"
- Need to traverse or search hierarchical data
- Asked about "depth", "height", "level", "ancestor", "descendant"
- Problem involves "path" from root to leaf or between nodes
- [Keyword triggers: "tree", "binary", "root", "leaf", "depth", "level", "ancestor", "path"]

## 2. Core Template/Algorithm Steps

### General Algorithm Steps:
1. **Setup:** Check if root is null (base case)
2. **Main Logic:** Choose DFS (recursive/stack) or BFS (queue)
3. **Process:** Handle current node, then recurse/iterate on children
4. **Termination:** When null node reached or target found
5. **Return:** Result from recursive calls or accumulated value

### Code Template:
```python
def tree_dfs_template(root):
    # Step 1: Base case - handle null node
    if not root:
        return base_case_value
    
    # Step 2: Process current node
    current_result = process(root.val)
    
    # Step 3: Recurse on children
    left_result = tree_dfs_template(root.left)
    right_result = tree_dfs_template(root.right)
    
    # Step 4: Combine results
    return combine(current_result, left_result, right_result)

def tree_bfs_template(root):
    if not root:
        return base_case_value
    
    queue = [root]
    result = []
    
    while queue:
        node = queue.pop(0)
        result.append(process(node.val))
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result
```

## 3. Common Variations
- **DFS Traversals:** Preorder (root→left→right), Inorder (left→root→right), Postorder (left→right→root) - Use for different processing orders
- **BFS/Level Order:** Process nodes level by level - Use when need level-wise information
- **BST Operations:** Search, insert, delete - Use when tree has BST property (left < root < right)
- **Advanced:** Path sum, tree construction from traversals, tree modification, LCA problems

## 4. Key Insights
- **Core insight 1:** Recursion naturally maps to tree structure - solve for subtrees and combine
- **Core insight 2:** Most tree problems can be broken into: process current node + solve for left subtree + solve for right subtree
- **Optimization insight:** DFS uses O(h) space vs BFS uses O(w) space, where h=height, w=max width
- **Trade-off insight:** Recursion is cleaner but may cause stack overflow; iteration with explicit stack is safer for deep trees

## 5. Complexity Analysis
**Time Complexity:**
- Best case: O(1) - finding root value
- Average case: O(n) - visiting all nodes
- Worst case: O(n) - must visit all nodes

**Space Complexity:**
- O(h) for DFS - call stack depth equals tree height
- O(w) for BFS - queue size equals maximum width of tree
- Best case O(log n) for balanced tree, worst case O(n) for skewed tree

**When is this optimal:** When you need to visit nodes in specific order or when tree structure naturally fits the problem

## 6. Edge Cases Checklist
□ **Empty input:** root is None - return appropriate default value
□ **Single element:** root with no children - handle base case properly
□ **Two elements:** root with one child - ensure both left/right are checked
□ **All same elements:** tree with identical values - logic should still work
□ **Boundary conditions:** Very deep tree (stack overflow), very wide tree (memory)
□ **Pattern-specific edges:** Invalid BST, cycles in tree (shouldn't exist), unbalanced tree
□ **Invalid input:** null pointers, negative values when not expected

## 7. Problem Examples
**Easy Level:**
- Maximum Depth of Binary Tree - Simple DFS recursion
- Same Tree - Compare two trees recursively
- Invert Binary Tree - Swap left and right subtrees

**Medium Level:**
- Validate Binary Search Tree - Check BST property with bounds
- Binary Tree Level Order Traversal - BFS implementation
- Path Sum II - DFS with backtracking to find all paths
- Lowest Common Ancestor of Binary Tree - Find LCA using recursion
- Construct Binary Tree from Preorder and Inorder - Tree reconstruction

**Hard Level:**
- Binary Tree Maximum Path Sum - DFS with global maximum tracking
- Serialize and Deserialize Binary Tree - Convert tree to/from string

## 8. Common Pitfalls & Mistakes
**Coding Mistakes:**
- [Forgetting null checks]: Always check if node is None before accessing properties
- [Wrong traversal order]: Confusing preorder/inorder/postorder - draw small examples
- [Incorrect return values]: Not returning proper values from recursive calls

**Logic Mistakes:**
- [Confusing node vs subtree]: Remember if you're processing single node or entire subtree
- [Global vs local state]: Mixing up when to use global variables vs return values
- [BST property violations]: For BST problems, remember left < root < right for ALL ancestors

## 9. Interview Tips
**Recognition:**
- Look for hierarchical relationships or tree-like data
- Ask: "Is this a binary tree, BST, or general tree?"
- Clarify: "Can there be cycles?" (usually no for trees)

**Implementation:**
- Start with base case (null node)
- Choose DFS for most problems unless level-order is specifically needed
- Code recursively first, then optimize to iterative if needed

**Communication:**
- Explain your traversal choice (DFS vs BFS, which DFS order)
- Walk through a small tree example
- Mention space complexity trade-offs

**Follow-up Questions:**
- "What if tree is very deep?" (iterative solution)
- "What if tree is a BST?" (optimization opportunities)
- "What about n-ary trees?" (extend to multiple children)

## 10. Quick Reference
**Pattern Triggers:** Hierarchical data, mentions of root/leaf/parent/child, tree terminology
**Template Summary:** Check null → Process current → Recurse on children → Combine results
**Complexity:** Time O(n), Space O(h) for DFS or O(w) for BFS
**Key Insight:** Break tree problems into current node + left subtree + right subtree

---

## Notes Section
- Remember TreeNode definition: class TreeNode: def __init__(self, val=0, left=None, right=None)
- For BST problems, inorder traversal gives sorted order
- DFS generally easier to code, BFS needed for level-specific problems
- Practice tree drawing for complex problems