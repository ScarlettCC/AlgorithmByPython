# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        if matrix == None:
            return
        rows = len(matrix)
        colums = len(matrix[0])
        left = 0
        right = colums -1
        top = 0
        bottom = rows-1
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            for i in range(top+1,bottom+1):
                result.append(matrix[i][right])
            if top<bottom:
                for i in range(right-1,left-1,-1):
                    result.append(matrix[bottom][i])
            if left<right:
                for i in range(bottom-1,top,-1):
                    result.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return result
def printresult(result):
    for x in result:
        print x
    print '\n'
matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix2 = [[1],[2],[3],[4],[5]]
matrix3 = [[1,2],
           [3,4],
           [5,6],
           [7,8],
           [9,10]]
S = Solution()
result1 = S.printMatrix(matrix)
result2 = S.printMatrix(matrix2)
result3 = S.printMatrix(matrix3)
printresult(result1)
printresult(result2)
printresult(result3)