# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a1, a2 = [], []
        tmp = l1
        while tmp != None:
            a1.append(tmp.val)
            tmp = tmp.next
        tmp = l2
        while tmp != None:
            a2.append(tmp.val)
            tmp = tmp.next

        answer = (list(str(int("".join(str(num) for num in a1[::-1])) + int("".join(str(num) for num in a2[::-1])))))[::-1]

        def insert2(root, item):
            temp = ListNode(item)
            if root == None:
                root = temp
            else:
                ptr = root
                while ptr.next != None:
                    ptr = ptr.next
                ptr.next = temp

            return root

        root = None
        for i in range(0, len(answer), 1):
            root = insert2(root, answer[i])

        return root
