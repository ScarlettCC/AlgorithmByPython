# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        str = ''
        for c in s:
            if (c==' '):
                str += '%20'
            else :
                str += c
        return str