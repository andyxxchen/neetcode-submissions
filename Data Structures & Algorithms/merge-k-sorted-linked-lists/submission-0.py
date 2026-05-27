# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        # devide and conquer, will be merged into the head_p
        def merge_two_sorted(head_p, head_q) -> ListNode:
            # we want to merge the second head_q into the first list head_p
            dummy = ListNode()

            k = dummy
            p = head_p
            q = head_q

            while p and q:
                if p.val <= q.val:
                    k.next = p
                    p = p.next
                else:
                    k.next = q
                    q = q.next
                k = k.next

            if p:
                k.next = p
            else:
                k.next = q

            return dummy.next

        # divide & conquer
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None

                merged_lists.append(
                    merge_two_sorted(l1, l2)
                )

            lists = merged_lists

        return lists[0]
        


            