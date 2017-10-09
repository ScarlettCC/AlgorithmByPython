# -*- coding:utf-8 -*-
class Solution:
    def Print1ToMaxOfNDigits(self,n):
        if n <=0 :
            return None
        while n:
            for i in range(0,10):
                if i!= 0:
                    print i
                self.Print1ToMaxOfNDigits(n-1)
s= Solution()
s.Print1ToMaxOfNDigits(2)