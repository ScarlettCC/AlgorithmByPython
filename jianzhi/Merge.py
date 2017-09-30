# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        pMerge = None
        if pHead2.val<=pHead1.val:
            pMerge =pHead2
            pMerge.next=self.Merge(pHead1,pHead2.next)
        elif pHead1.val<=pHead2.val:
            pMerge=pHead1
            pMerge.next=self.Merge(pHead1.next,pHead2)
        return pMerge


node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

S=Solution()
X=S.Merge(node1,node4)
while X!=None:
    print X.val
    X=X.next