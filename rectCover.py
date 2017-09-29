# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number ==0:
            return 0
        elif number==1:
            return 1
        elif number ==2:
            return 2
        one =1
        two =2
        for i in range(3,number+1):
            fi = one+two
            one = two
            two =fi
        return fi
