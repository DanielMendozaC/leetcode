# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # More structure and cleaner code:
        # Cleaner approach using dummy node (alternative solution):
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        for i in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


        # Two pointer approach method
        # fast and slow pointer. fast pointer is n pos ahead of slow
        # meaning that when fast is last(node), slow is at node[n]
        # or if fast is at node when node.next == None, then slow is at node[n]
        # which we have to remove, which we can do by 
        # prev_node.next = current_node.next, then return head.
        # space complexity o(1) and time o(n)

        # Two-pointer approach: O(1) space, O(n) time
        # Strategy: Move fast pointer n steps ahead, then move both until fast reaches end
        # When fast reaches end, slow will be at the node to remove


        slow = head
        fast = head
        c = 0  # Counter to track total list length
        
        # Move fast pointer n steps ahead
        for i in range(n):
            fast = fast.next
            c += 1
        
        # Move both pointers until fast reaches the end
        # prev tracks the node before slow (needed for removal)
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
            c += 1
        
        # Edge case: removing the head node (when n equals list length)
        if c - n == 0:
            return head.next
        # Edge case: single node list  
        elif c == 1:
            return None  # Fixed: was return []
        # Normal case: remove middle/end node
        else:
            prev.next = slow.next
            return head




        # # Bruce force method by storing the nodes in an array.

        # # if just on empty node, return it
        # if not head:
        #     return head

        # c = 0
        # current = head
        # linked_array = []
        # # We save the nodes and see how many we have
        # while current:
        #     linked_array.append(current)
        #     current = current.next
        #     c-=1

        # # n = 1 mean index -1
        # # we work with inverse of n for facility
        # ni = -n

        # # case when we want to remove the first node
        # # we just return the head of the 2nd node
        # if ni==c:
        #     next_l = head.next
        #     return next_l
        # # case when need to remove last node.
        # # put the 2nd to last node.next to None
        # # & return the head of 1st code
        # # elif ni==-1:
        # #     linked_array[-2].next = None
        # #     return head
        # # case when node to remove is not on the edges
        # else:
        #     # Remove node at index n
        #     # Redirect next of the node before this one 
        #     # linked_array[ni-1].next = linked_array[ni+1]
        #     linked_array[ni-1].next = linked_array[ni].next
        #     return head


