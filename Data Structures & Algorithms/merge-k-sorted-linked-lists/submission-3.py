# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        def mergeTwo(l1, l2):
            head = ListNode()
            dummy = head
            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            dummy.next = l1 if l1 else l2
            return head.next

        interval = 1
        k = len(lists)

        while interval < k:
            for i in range(0, k - interval, interval * 2):
                lists[i] = mergeTwo(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]
        


            