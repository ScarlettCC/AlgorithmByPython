# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None :
            return False
        temp = []
        p = pHead
        while p:
            if p in temp:
                return p
            else:
                temp.append(p)
            p = p.next
        return False