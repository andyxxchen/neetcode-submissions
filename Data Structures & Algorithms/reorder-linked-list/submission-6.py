# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy1 = ListNode(next=head)
        slow = fast = dummy1

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        dummy2 = ListNode(next=slow.next)
        slow.next = None

        # reverse dummy2
        # prev cur temp
        # A - B - C
        prev = None
        cur = dummy2.next
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # prev is the head after reversing
        dummy2.next = prev

        p = head
        q = dummy2.next
        #    p tmp 
        # [2,4]
        # [6,8,10]
        while q:
            tmp_p = p.next
            tmp_q = q.next

            p.next = q
            q.next = tmp_p

            p = tmp_p
            q = tmp_q

