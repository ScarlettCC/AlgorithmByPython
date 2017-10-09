# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        flag = False
        if s==None or len(s)<1:
            return 0
        numstack = []
        dict = {'0': 0, "1": 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for i in s :
            if i in dict.keys():
                numstack.append(dict[i])
            elif '+' == i:
                continue
            elif '-' == i:
                continue
            else:
                return 0
        if 1 == len(s) and '0'==s[0]:
            flag =True
            return 0
        ans = 0
        if 1== len(s) and ('+'==s[0] or '-'==s[0]):
            return 0
        for i in numstack:
            ans = ans*10 + i
        if '-' == s[0]:
            ans = 0-ans
        return ans
s=Solution()
print s.StrToInt('-111')
print s.StrToInt('+')
print s.StrToInt('0')
print s.StrToInt('')

