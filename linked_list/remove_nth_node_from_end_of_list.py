# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two pointer approach method
        # fast and slow pointer. fast pointer is n pos ahead of slow
        # meaning that when fast is last(node) + 1, slow is at node[n+1]
        # or if fast is at node when node.next == None, then slow is at node[n]
        # which we have to remove, which we can do by 
        # prev_node.next = current_node.next, then return head.
        # space complexity o(1) and time o(n)




        # Bruce force method by storing the nodes in an array.

        # if just on empty node, return it
        if not head:
            return head

        c = 0
        current = head
        linked_array = []
        # We save the nodes and see how many we have
        while current:
            linked_array.append(current)
            current = current.next
            c-=1

        # n = 1 mean index -1
        # we work with inverse of n for facility
        ni = -n

        # case when we want to remove the first node
        # we just return the head of the 2nd node
        if ni==c:
            next_l = head.next
            return next_l
        # case when need to remove last node.
        # put the 2nd to last node.next to None
        # & return the head of 1st code
        # elif ni==-1:
        #     linked_array[-2].next = None
        #     return head
        # case when node to remove is not on the edges
        else:
            # Remove node at index n
            # Redirect next of the node before this one 
            # linked_array[ni-1].next = linked_array[ni+1]
            linked_array[ni-1].next = linked_array[ni].next
            return head


