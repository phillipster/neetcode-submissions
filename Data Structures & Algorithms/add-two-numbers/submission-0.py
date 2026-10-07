# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = cur = prev = ListNode()
        while l1 and l2:
            temp = l1.val + l2.val + carry
            cur.val = temp % 10
            carry = temp // 10
            cur.next = ListNode()
            prev = cur
            cur = cur.next
            l1, l2 = l1.next, l2.next
        while l1:
            temp = l1.val + carry
            cur.val = temp % 10
            carry = temp // 10
            prev = cur
            cur.next = ListNode()
            cur, l1 = cur.next, l1.next
        while l2:
            temp = l2.val + carry
            cur.val = temp % 10
            carry = temp // 10
            prev = cur
            cur.next = ListNode()
            cur, l2 = cur.next, l2.next
        if carry:
            cur.val = carry
        if cur.val == 0:
            prev.next = None
        return head