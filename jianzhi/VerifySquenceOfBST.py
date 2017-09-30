# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == []:
            return False
        if len(sequence) == 1:
            return True
        if min(sequence) >= sequence[-1] or max(sequence) <= sequence[-1]:
            return True
        index = 0
        for i in range(len(sequence)-1):
            index=i
            if sequence[i] > sequence[-1]:
                break
        for i in range(index,len(sequence)-1):
            if sequence[i] < sequence[-1]:
                return False
        left = self.VerifySquenceOfBST(sequence[:index])
        right = self.VerifySquenceOfBST(sequence[index:len(sequence)-1])
        return left and right

array = [5, 7, 6, 9, 11, 10, 8]
array2 = [4, 6, 7, 5]
array3 = [1, 2, 3, 4, 5]
S = Solution()
print(S.VerifySquenceOfBST(array))
print(S.VerifySquenceOfBST(array2))
print(S.VerifySquenceOfBST(array3))