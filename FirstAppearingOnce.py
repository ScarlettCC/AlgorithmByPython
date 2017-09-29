# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.adict = {}
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.adict[i] == 1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.s += char
        if char in self.adict:
            self.adict[char] += 1
        else:
            self.adict[char] = 1


