# -*- coding:utf-8 -*-
import sys
class Solution():
    '''
    数组添加元素构成回文数组并使数组的和最小，输出构造好的回文数组的和，
    如[1,2,3,1,2] 可添加2个元素 变为回文 [1,2,1,3,1,2,1], 输出11。
    '''
    def structHuiwen(self, number, n):
        if (number is None) or ( len(number) != int(n)):
            return None
        number_reverse = number[::-1]
        dp = [[] for i in range(n)]
        for i in range(len(number)):
            for j in range(len(number_reverse)):
                if number[i] == number_reverse[j]:
                    dp[i].append(dp[i-1][j-1]+1)
                else:
                    dp[i].append(max(dp[i-1][j], dp[i][j-1]))
        return dp

if __name__ == "__main__":
    n = sys.stdin.readline().strip()
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    ans = [[0 for i in range(n)] for j in range(n)]
    for i in range(1,n+1):
        for j in range(n-i+1):
            if i == 1:
                ans[j][j+i-1] = values[j]
                continue
            else:
                if values[j] == values[j+i-1]:
                    if i>2:
                        ans[j][j+i-1] = 2*values[j] + ans[j+1][j+i-2]
                    else:
                        ans[j][j + i - 1] = 2 * values[j]
                else:
                    ans[j][j + i - 1] = min(2*values[j]+ans[j+1][j+i-1], 2*values[j+i-1]+ans[j][j+i-2])
    print(ans[0][n-1])

if __name__ == "__main__":
    n = sys.stdin.readline().strip()
    number_array = sys.stdin.readline().strip().split(' ')
    number = ''.join(number_array)
    s=Solution()
    print s.structHuiwen(number, int(n))