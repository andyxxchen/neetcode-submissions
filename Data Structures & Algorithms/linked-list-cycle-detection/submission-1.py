# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 0
        dummy = ListNode(next=head)
        slow = fast = dummy

        while fast.next and fast.next.next:
            if slow == fast != dummy: 
                return True
            slow = slow.next
            fast = fast.next.next

        return False
