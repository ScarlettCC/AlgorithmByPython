# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if(n<=0):
            return s
        return s[n:]+s[:n]
s=Solution()
print s.LeftRotateString('12345',2)