# -*- coding:utf-8 -*-
import re
class Solution:
    # s字符串
    def isNumeric2(self,s):
        pa = r'^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$'
        pattern= re.compile(pa)
        if re.match(pattern,s)!=None:
            return True
        else:
            return False
    def isNumeric3(self, s):
        try:
            float(s)
            print s
            if s[0:2]!='-+' and s[0:2]!='+-':
                return True
            else:
                return False
        except:
            return False

    def isNumeric(self, s):
        # write code here
        if s == None or len(s) <= 0:
            return False
        i = 0
        digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if s[0] == '+' or s [0] == '-':
            i += 1
            if i >= len(s):
                return False
        if self.findonly0(s[i:]):
            return False
        dig = self.scanDigit(s[i:])
        i += dig
        if i < len(s):
            if s[i] == '.':
                i += 1
                dig = self.scanDigit(s[i:])
                i += dig
        else:
            return True
        if i < len(s):
            if s[i] == 'e' or s[i] == 'E':
                i += 1
                if i >= len(s):
                    return False
                if s[i] == '+' or s[i] == '-':
                    i += 1
                    if self.findonly0(s[i:]):
                        return False
                    else:
                        dig = self.scanDigit(s[i:])
                        if dig == 0:
                            return False
                        else:
                            i += dig
                else:
                    dig = self.scanDigit(s[i:])
                    i += dig
        else:
            return True
        return i == len(s)

    def scanDigit(self, s):
        i = 0
        if s == None or len(s) == 0:
            return 0
        digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        while i<len(s) and (s[i] in digit):
            i += 1
        return i
    def findonly0(self,s):
        if s==None or len(s) == 0:
            return False
        if len(s)==1 and s[0] == '0':
            return True
        digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if s[0] == '0' and s[1] in digit:
            return True
        else:
            return False
s=Solution()
print s.isNumeric3('+100')  #True
print s.isNumeric3('5e2')   #True
print s.isNumeric3('-123')  #True
print s.isNumeric3('3.1415')    #True
print s.isNumeric3('-1e-16')    #True
print s.isNumeric3('12E')   #False
print s.isNumeric3('1a3.14')    #False
print s.isNumeric3('123.45') #True
print s.isNumeric3('123.45e')   #False
print s.isNumeric3('-.123')   #True
print s.isNumeric3('123.45e+6') #True
