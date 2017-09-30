# -*- coding:utf-8 -*-
import sys
class Solution():
    '''
    大学足球赛
    1，参赛队伍n支
    2，进入前1/2的才有资格进入淘汰赛
    3，队伍按积分排名：胜一场积3分，平一场积1分，负一场0分

    输入：
    第一行整数n(1<=n<=50),球队数
    随后n行为球队的名字，不超过30个的大写拉丁字母,不重名
    随后n*(n-1)行为赛事开展情况，格式为：
            name1-name2 num1:num2   0<=num1,num2<=100
    输出：
    n/2行，按字母序排列的进入淘汰赛的n/2支队伍的名单

    示例输入：
    4
    A
    B
    C
    D
    A-B 1：1
    A-C 2：2
    A-D 1：0
    B-C 1：0
    B-D 0：3
    C-D 0：3
    2
    a
    A
    a-A 2:1
    输出：
    A
    D
    a
    '''
    def FootbalGame(self,name,state):
        for i in range(len(state)):
            print state

if __name__ == "__main__":
    n= int(sys.stdin.readline())
    for i in range(n):
        name = sys.stdin.readline().strip()
    state = []
    for i in sys.stdin.readline().strip():
         state.append(i)
    s = Solution()
    print s.FootbalGame(name,state)