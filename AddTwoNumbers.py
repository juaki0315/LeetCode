# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def to_list(self, node):
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        return arr

    def to_linkedlist(self, arr):
        dummy = ListNode(0)
        curr = dummy
        for x in arr:
            curr.next = ListNode(x)
            curr = curr.next
        return dummy.next

    def addTwoNumbers(self, l1, l2):
        a = self.to_list(l1)
        b = self.to_list(l2)

        if len(a) < len(b):
            a = [0] * (len(b) - len(a)) + a
        elif len(b) < len(a):
            b = [0] * (len(a) - len(b)) + b
        # a[::-1]
        # b[::-1]
        carry = 0
        res = []

        for i in range(len(a)):
            s = a[i] + b[i] + carry
            res.append(s % 10)
            carry = s // 10

        if carry:
            res.append(carry)

        return self.to_linkedlist(res)
    
