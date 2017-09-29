# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n<0:
            n = n & 0xffffffff
        while n:
            count+=1
            n = (n-1)&n
        return count

    def NumberOf1II(self,n):
        if n<0:
            s = bin(n& 0xffffffff)
        else:
            s = bin(n)
        return s.count('1')

s = Solution()
print (s.NumberOf1(1))
print (s.NumberOf1II(3))