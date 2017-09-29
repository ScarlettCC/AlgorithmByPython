# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        exp = exponent
        if exponent < 0:
            exp = -exponent
        result = 1.0
        while exp:
            if exp & 1:
                result *= base
            base *= base
            exp >> 1
        if exponent<0:
            result = 1/result
        return result
