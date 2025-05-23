# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Maybe using a stack?
        # going over a subtree, if we dont find the nodes, return False
        if not root:
            return 

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # elif p.val >= root.val and q.val <= root.val:
        #     return root
        # elif q.val >= root.val and p.val <= root.val:
        #     return root

        else:
            return root

        # Time complexity is o(n) and space complexity is o(1)
        # No, is o(n) (worst case), o(log(n)) (best case), n or h for time compelxity? 
        # and o(h) h:depth of the tree,     
        # recursive stack


# ITERATIVE SOL. More space optimal O(1)
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # Start from the root and move down the tree
    while root:
        # If both p and q are greater than current node
        # LCA must be in the right subtree
        if p.val > root.val and q.val > root.val:
            root = root.right  # Move to right child
            
        # If both p and q are less than current node  
        # LCA must be in the left subtree
        elif p.val < root.val and q.val < root.val:
            root = root.left   # Move to left child
            
        # If p and q are on different sides of root
        # OR one of them equals root
        # Then current root IS the LCA
        else:
            return root
            
    # This line should never be reached given problem constraints
    return None

# Time Complexity: O(h) where h is height of tree
#   - Best case: O(log n) for balanced BST
#   - Worst case: O(n) for skewed tree
# Space Complexity: O(1) - only using a few variables, no recursion stack!