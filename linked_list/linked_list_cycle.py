# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
        slow = head  # Tortoise - moves one step at a time
        fast = head  # Hare - moves two steps at a time
        
        # Continue until fast reaches end of list
        # We need to check both fast and fast.next before accessing fast.next.next
        while fast and fast.next:
            slow = slow.next        # Move tortoise one step
            fast = fast.next.next   # Move hare two steps
            
            # If tortoise and hare meet, a cycle exists
            if slow == fast:
                return True
                
        # If we reach here, fast pointer reached the end, so no cycle
        return False
        # Time complexity is O(n) and space O(1)


        # Alternative solution using a hash set
        node_set = set()  # Track nodes we've already seen
        current = head
        
        while current != None:
            # If we see a node twice, we've found a cycle
            if current in node_set:
                return True
            
            # Add current node to our set of seen nodes
            node_set.add(current)
            current = current.next

        # If we reached the end (None), there's no cycle
        return False
        # Time complexity O(n) and space O(n)