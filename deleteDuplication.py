# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead==None or pHead.next==None:
            return pHead
        q = pHead.next
        if pHead.val != q.val:
            pHead.next = self.deleteDuplication(q)
        else:
            while q and pHead.val == q.val:
                q = q.next
            if q:
                pHead = self.deleteDuplication(q)
            else:
                return None
        return pHead

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node4 = ListNode(1)
node5 = ListNode(1)
node6 = ListNode(1)
node7 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
print(s.deleteDuplication(node1))