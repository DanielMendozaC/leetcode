# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        # if root.val == subRoot.val:
        #     sametree = self.isSametree(root, subRoot)
        #     if sametree == True:
        #         return True

        # Cleaner: isSametree checks whether the root is the same in O(1)
        # So we can call the function in every node

        sametree = self.isSametree(root, subRoot)
        if sametree:
            return True

        leftnode = self.isSubtree(root.left, subRoot)
        rightnode = self.isSubtree(root.right, subRoot)

        return leftnode or rightnode

    def isSametree(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        elif root.val != subRoot.val:
            return False
        
        left = self.isSametree(root.left, subRoot.left)
        right = self.isSametree(root.right, subRoot.right)

        return left and right