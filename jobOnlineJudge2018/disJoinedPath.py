# -*- coding:utf-8 -*-
'''
城市由n个片区组成，片区与片区之间由n-1条道路相连。
任意两个片区之间，都存在一条简单路径可以到达。
现在有两个人，在城中旅游。
需要制定出完美的计划，满足这两个人的旅行路径不相交的目标。
当然，这两个人的旅行路径都是从一个地方旅行到另外一个地方，且他们的路线一定是最短的路线。
问，能够构造出多少种不同的计划呢？

第一行一个整数n，表示快乐之城由n条片区组成。
接下来n-1行，每行两个整数x,y，表示片区x与片区y相连。
满足
1<=n<=30000
1<=x,y<=n
'''
import sys