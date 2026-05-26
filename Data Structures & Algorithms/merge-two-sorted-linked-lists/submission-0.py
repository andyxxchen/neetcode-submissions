# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = list1
        q = list2 
        dummy = ListNode()
        cur = dummy

        # if p < q -> p
        # else     -> q
        while p and q: 
            if p.val < q.val:
                cur.next = p
                p = p.next
            else: 
                cur.next = q
                q = q.next
            cur = cur.next
        
        if p:
            cur.next = p
        else:
            cur.next = q

        return dummy.next