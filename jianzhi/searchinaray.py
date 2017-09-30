# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array == []:
            return False

        colnum = len(array)
        rawnum = len(array[0])
        i = 0
        j = colnum - 1
        while i < colnum and j > -1:
            if array[i][j] == target:
                return True
            elif array[i][j] < target :
                i += 1
            else:
                j -= 1
        return False