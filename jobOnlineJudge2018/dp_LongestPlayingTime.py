# -*- coding:utf-8 -*-
'''
小明去游乐园玩耍，他的票一共可以玩t分钟。
游乐场一共有n个项目，编号1到n，第i个项目需要a[i]的时间。
游乐场规定，在票没有到期前，拥有者都可以入场，无论完成项目出场时该票是否已经过期。
小明可以任意决定玩项目的顺序，但是每个项目他只想玩一次。问小明最长可以玩多久？
'''
import sys

class Solution():
    def LogestPlayingTime(self, number, maxtime, tickettime):
        '''
        将最大时间的项目取出，对剩下的01背包
        :param number: 项目总数
        :param maxtime: 最大可玩时间
        :param tickettime: 每个项目需要时间
        :return:LogestPlayingTime:最大玩耍时间
        '''
        tickettime = sorted(tickettime)
        dp = [[0 for j in range(maxtime)] for i in range(number)]
        #dp =[[0] * maxtime] * number   浅拷贝，不可用
        for i in range(1, number):
            for j in range(1, maxtime):
                if tickettime[i-1] <= j:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-tickettime[i-1]]+tickettime[i-1])
                else:
                    dp[i][j] = dp[i-1][j]
        print dp[number-1][maxtime-1]
        print tickettime[number-1]
        dp[number-1][maxtime-1] += tickettime[number-1]
        # if dp[number-1][maxtime-1] < maxtime:
        #     for i in range(number-1, 0, -1):
        #         dp[number-1][maxtime-1] += tickettime[i]
        #         if dp[number-1][maxtime-1] >= maxtime:
        #             break
        return dp[number-1][maxtime-1]
if __name__ == "__main__":
    n = sys.stdin.readline().strip().split()
    tickettime = sys.stdin.readline().strip().split()
    tickettime = map(int, tickettime)
    #tickettime = ''.join(str)
    number = int(n[0])
    maxtime = int(n[1])
    s = Solution()
    print s.LogestPlayingTime(number, maxtime, tickettime)

'''
测试用例：
输入： 4 12        4 5       4 4       4 8
      5 5 5 5     1 2 2 3   1 2 2 3   1 2 2 3
输出： 15          7         5         8
'''
