# -*- coding:utf-8 -*-
class Solution:
    def powerOf2(self,number):
        if number&(number-1)==0:
            return True
        else:
            return False

s=Solution()
print(s.powerOf2(3))