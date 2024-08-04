# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        length = 0
        
        while curr:
            curr = curr.next
            length += 1
        
        # Special case: removing the head node
        if length == n:
            return head.next
        
        # Find the node just before the one we want to remove
        curr = head
        node_num = length - n
        
        while node_num > 1:
            curr = curr.next
            node_num -= 1
        
        # Remove the n-th node from the end
        curr.next = curr.next.next
        
        return head