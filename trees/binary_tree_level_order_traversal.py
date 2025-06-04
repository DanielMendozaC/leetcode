# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        result = []

        while queue:
            vals = []

            for i in range(len(queue)):
                valnode = queue.popleft()
                if not valnode:
                    continue

                queue.append(valnode.left)
                queue.append(valnode.right)
                vals.append(valnode.val)
            if vals:
                result.append(vals)
        return result

        # Time complexity is O(n) and space is O(n)