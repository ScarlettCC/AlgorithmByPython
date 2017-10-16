#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/11 9:30
# @Author  : Lelsey
# @Site    : 
# @File    : LCS.py
# @Software: PyCharm Community Edition
# @Description: 最长公共子序列 AC
import sys
def find_lcseque(s1, s2):
    m = [[0 for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]
    d = [[None for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]

    for p1 in range(len(s1)):
        for p2 in range(len(s2)):
            if s1[p1] == s2[p2]:
                m[p1 + 1][p2 + 1] = m[p1][p2] + 1
                d[p1 + 1][p2 + 1] = 'ok'
            elif m[p1 + 1][p2] > m[p1][p2 + 1]:
                m[p1 + 1][p2 + 1] = m[p1 + 1][p2]
                d[p1 + 1][p2 + 1] = 'left'
            else:
                m[p1 + 1][p2 + 1] = m[p1][p2 + 1]
                d[p1 + 1][p2 + 1] = 'up'
    (p1, p2) = (len(s1), len(s2))
    s = []
    while m[p1][p2]:
        c = d[p1][p2]
        if c == 'ok':
            s.append(s1[p1 - 1])
            p1 -= 1
            p2 -= 1
        if c == 'left':
            p2 -= 1
        if c == 'up':
            p1 -= 1
    s.reverse()
    return len(''.join(s))
def ReverseSentence(s): #逆序
    if(len(s)==0):
        return s
    l = s.split(' ')
    return ' '.join(l[::-1])
if __name__ == "__main__":
    strs = sys.stdin.readline().strip()
    reverstr = ReverseSentence(strs)
    print find_lcseque(strs, reverstr)