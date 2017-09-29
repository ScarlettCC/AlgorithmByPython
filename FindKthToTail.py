# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        p = head
        q = head
        if head ==None or k<=0:
            return
        while q and (k > 0):
            q = q.next
            k -= 1
            if q== None and k>0:
                return
        while q:
            p = p.next
            q = q.next
        return p

p = ListNode(1)
q = ListNode(2)
r = ListNode(3)
m = ListNode(4)
n = ListNode(5)
p.next = q
q.next = r
r.next = m
m.next = n
s=Solution()
l= s.FindKthToTail(p, 6)
print l.val
