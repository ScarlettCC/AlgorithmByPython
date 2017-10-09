# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        p = 0
        q = len(rotateArray)-1
        while q-p>1 :
            mid = (p+q)/2
            if rotateArray[mid]>=rotateArray[p]:
                p=mid
            elif rotateArray[mid]<=rotateArray[p]:
                q=mid
        return rotateArray[q]
