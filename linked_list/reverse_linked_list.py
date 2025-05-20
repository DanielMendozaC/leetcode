from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers
        current = head  # Start from the head node
        prev = None     # Previous node starts as None
        
        # Iterate through the list
        while current is not None:
            # Save next node before we overwrite the pointer
            save_next = current.next
            
            # Reverse the pointer (this is the key step)
            current.next = prev
            
            # Move both pointers forward
            prev = current
            current = save_next
        
        # At this point, current is None and prev is the new head
        return prev
    
    # Time complexity is O(n) where n is the number of nodes in the list
    # Space complexity is O(1) since we only use a constant amount of extra space