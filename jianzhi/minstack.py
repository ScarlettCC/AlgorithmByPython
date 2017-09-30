# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.datastack = []
        self.minstack = []
    def push(self, node):
        # write code here
        self.datastack.append(node)
        if not self.minstack or node<self.min():
            self.minstack.append(node)
        else:
            self.minstack.append(self.min())
    def pop(self):
        # write code here
        self.datastack.pop()
        self.minstack.pop()
    def top(self):
        # write code here
        return self.datastack[-1]
    def min(self):
        # write code here
        return self.minstack[-1]
S=Solution()
S.push(3)
S.push(4)
S.push(2)
S.push(1)
print(S.min())
S.pop()
print(S.min())
S.pop()
print(S.min())