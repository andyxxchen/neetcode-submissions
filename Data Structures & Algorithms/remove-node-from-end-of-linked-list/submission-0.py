# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

  
# 0 -> 1 -> 2 -> 3
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = fast = dummy

        # move fast pointer n times
        k = n
        while k > 0 and fast:
            fast = fast.next
            k -= 1
        
        # now fast is Nth faster than slow
        while fast.next:
            fast = fast.next
            slow = slow.next 

        # now slow will be at 1 element ahead of the deleting cadidate
        slow.next = slow.next.next

        return dummy.next