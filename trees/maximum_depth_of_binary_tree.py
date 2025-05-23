# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # End of tree, no node, return 0
        if not root:
            return 0

        len_left = self.maxDepth(root.left)
        len_right = self.maxDepth(root.right)

        # Check max between depth of left and right subtree
        # Add 1 for the current node
        len_result = 1 + max(len_left, len_right)
        return len_result

        # space complexity is o(n) and time complex o(n)
