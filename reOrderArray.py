# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if len(array) == 0:
            return []
        if len(array)==1:
            return array
        i = 0
        p = -1
        while i<len(array):
            if (array[i]&1) ==1:
                p += 1
                if i > p:
                    q = i
                    temp = array[i]
                    while q > p:
                        array[q] = array[q-1]
                        q -= 1
                    array[p] = temp
            i += 1
        return array
    def reOrderArray2(self,array):
        a =[]
        b = []
        for num in array:
            if num&1 ==0:
                b.append(num)
            else:
                a.append(num)
        return a+b
    def reOrderArray3(self,array):
        left = [x for x in array if x&1]
        right = [x for x in array if not x&1]
        return left+right
s=Solution()
print(s.reOrderArray([1, 2, 3, 4, 5, 6, 7]))
print(s.reOrderArray2([4, 5, 6, 7, 8, 9, 10]))
print(s.reOrderArray3([4, 5, 6, 7, 8, 9, 10]))