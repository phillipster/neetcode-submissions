# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # simplified version that creates a single empty node to start
        result = cursor = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cursor.next = list1
                list1 = list1.next
                cursor = cursor.next
            else:
                cursor.next = list2
                list2 = list2.next
                cursor = cursor.next
        if list1:
            cursor.next = list1
        elif list2:
            cursor.next = list2
        return result.next
