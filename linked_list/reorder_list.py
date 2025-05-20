# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Now implement an optimized solution. with space o(1)



        # Hashmap to store nodes and index
        if not head or not head.next:
            return

        ini = head
        link_index = {}
        i = -1
        while head!=None:
            i+=1
            link_index[i] = head

            head = head.next
            
        head = ini
        left = 1
        right = i
        while left<=right:
            head.next = link_index[right]
            head = head.next
            if left!=right:
                head.next = link_index[left]
                head = head.next
            left+=1
            right-=1
        # IMPORTANT to set the last node next to None
        head.next = None

        # Time complexity is o(n) and space o(n)