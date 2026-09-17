# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ll = 0
        cursor = head
        while cursor:
            ll += 1
            cursor = cursor.next
        
        # short-execute logic: if index is out of bounds
        index = ll - n
        if index < 0 or index > ll:
            return head
        
        if n == ll:
            return head.next

        cursor = head
        for i in range(ll):
            if i == index-1:
                if not cursor.next:
                    return head
                cursor.next = cursor.next.next
                break
            cursor = cursor.next
        return head
                    