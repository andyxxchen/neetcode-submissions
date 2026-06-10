# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
 
    fast 从 groupPrev 开始走 k 步，确认够 k 个节点。
    如果不够，直接返回。
    如果够，记录 groupNext = kth.next。
    然后从 groupPrev.next 开始反转，直到 cur == groupNext。
    最后把 groupPrev 接到 kth，把 groupPrev 移到原来的组头。
'''

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = groupPrev

            # move k steps to find kth node
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next

            # reverse current group
            prev = groupNext
            cur = groupPrev.next

            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            # reconnect
            oldGroupHead = groupPrev.next
            groupPrev.next = kth
            groupPrev = oldGroupHead