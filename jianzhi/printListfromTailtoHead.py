# -*- coding:utf-8 -*-
'''
输入一个链表，从尾到头打印链表每个节点的值
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode == None:
            return
        l = []
        head=listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

singleNode = ListNode(12)
test = ListNode()

S = Solution()
print(S.printListFromTailToHead(node1))
print(S.printListFromTailToHead(singleNode))
print(S.printListFromTailToHead(test))
