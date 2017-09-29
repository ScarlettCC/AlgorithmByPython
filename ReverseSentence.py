# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if(len(s)==0):
            return s
        str1 = s[::-1]
        print str1
        str2 = []
        for x in str1.split(' '):
            str2 .append(x[::-1])
        return ' '.join(str2)
    def ReverseSentence2(self, s):
        if(len(s)==0):
            return s
        l = s.split(' ')
        print l
        return ' '.join(l[::-1])
s=Solution()
print s.ReverseSentence('I am a student.')
print s.ReverseSentence2('I am a student.')