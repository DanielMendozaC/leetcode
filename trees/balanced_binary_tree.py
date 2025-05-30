# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            depth = max(left_depth, right_depth)
            if abs(left_depth-right_depth)>1:
                res = False

            return 1 + depth
    
        dfs(root)
        return res
        # Time complexity is O(n) and space complexity is O(n)
        

# Othe solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]