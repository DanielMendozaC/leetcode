# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # When creating the queue, need to create a list
        # LIST
        
        queue = deque([root])
        result = []

        while queue:
            size = len(queue)
            rightmost = None

            for i in range(size):
                sub = queue.popleft()

                # Handling when you get to a None subtree
                if not sub:
                    continue

                queue.append(sub.left)
                queue.append(sub.right)
    
                rightmost= sub

            if rightmost:
                result.append(rightmost.val)

        return result

        # Time complexity is O(n) and space complexity is O(n)