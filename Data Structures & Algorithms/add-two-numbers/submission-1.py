# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = cur = prev = ListNode()
        while l1 or l2 or carry:
            temp = carry
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val  
                l2 = l2.next
            cur.val = temp % 10
            carry = temp // 10
            cur.next = ListNode()
            prev = cur
            cur = cur.next
        if cur.val == 0:
            prev.next = None
        return head