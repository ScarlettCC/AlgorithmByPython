# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number== 1:
            return 1
        elif number == 2:
            return 2
        one = 1
        two = 2
        for i in range(3,number+1):
            fi = one+two
            one = two
            two = fi
        return fi
    def jumpFloorII(self, number):
        # write code here
        if number== 1:
            return 1
        pre = 1
        for i in range(2,number+1):
            fi = 2*pre
            pre = fi
        return fi