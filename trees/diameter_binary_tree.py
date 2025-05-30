# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth_func(root):
            if not root:
                return 0, 0

            left_depth, max_diaml = depth_func(root.left)
            right_depth, max_diamr = depth_func(root.right)

            depth = max(left_depth, right_depth)
            subtree_diam = left_depth + right_depth

            # max_diam = max(max_diaml, max_diamr)

            # if subtree_diam>max_diam:
            #     max_diam=subtree_diam
            max_diam = max(max_diaml, max_diamr, subtree_diam)

            return 1 + depth, max_diam

        max_depth, max_diameter = depth_func(root)

        return max_diameter

        # Time complexity is O(n) and space complexity is O(n)

# Cleaner solution

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res