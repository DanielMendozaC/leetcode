# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Classes dont use parenthesis ()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge cases
        if not list1:
            return list2
        elif not list2:
            return list1

        # Create a dummy node to start building our result
        merged = ListNode()
        res = merged

        # Process while both lists have nodes
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next
        
        # Attach any remaining nodes
        if list1:
            merged.next = list1
        else:
            merged.next = list2
        
        # Return the actual start of our merged list (skip the dummy)
        return res.next