# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

    # prev    cur.    temp
# dummy -> head -> node1 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur 
            cur = temp

        return prev