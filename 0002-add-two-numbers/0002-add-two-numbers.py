# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        leftover = 0
        ft = False
        value = l1.val+l2.val
        if value >= 10:
            value = value - 10
            leftover += 1
        head = ListNode(val=value)
        l1 = l1.next
        l2 = l2.next
        curr = head
        while l1 or l2:
            value = leftover
            leftover = 0
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            if value >= 10:
                value = value - 10
                leftover += 1
            curr.next = ListNode(val=value)
            curr = curr.next
        if leftover != 0:
            curr.next = ListNode(val=leftover)
        return head