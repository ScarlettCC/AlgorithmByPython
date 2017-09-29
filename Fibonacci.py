# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        one = 0
        two = 1
        for i in range(2, n + 1):
            fi = one + two
            one = two
            two = fi
        return fi