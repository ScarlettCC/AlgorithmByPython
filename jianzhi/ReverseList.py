# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead==None:
            return None
        p=None
        q=pHead
        while q!=None:
            r=q.next
            q.next=p
            p = q
            q = r
        return p
    def ReverseList2(self, phead):
        if not phead or not phead.next:
            return phead
        pReversedHead=self.ReverseList(phead.next)
        phead.next.next=phead
        phead.next=None
        return pReversedHead
def printlist(p):
    while p != None:
        print p.val
        p = p.next
p = ListNode(1)
q = ListNode(2)
r = ListNode(3)
p.next = q
q.next = r
s = Solution()
x1 = s.ReverseList(p)
x2 = s.ReverseList2(p)
printlist(x1)
printlist(x2)