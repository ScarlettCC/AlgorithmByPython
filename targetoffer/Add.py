# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            sum = num1 ^ num2
            carry = num1 & num2
            num1 = sum
            num2 = carry << 1
        return num1
    def Swap(self, num1, num2):
        num1 += num2
        num2 = num1 - num2
        num1 -= num2
        print num1
        print num2
    def Swap2(self, num1, num2):
        num1 ^= num2
        num2 = num1 ^ num2
        num1 ^= num2
        print num1
        print num2
s = Solution()
print s.Add(6, 7)
s.Swap(6, 7)
s.Swap2(6, 7)