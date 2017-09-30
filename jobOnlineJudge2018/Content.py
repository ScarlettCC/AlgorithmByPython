# -*- coding:utf-8 -*-
'''
n个人排队站，每个人可能面向左L或面向右R
如果两个人是面对面站立，他们会发生争吵，后悔退出一个人
同一个时刻只能有一个争吵发生
问发生一系列争吵后这个队伍最少剩下多少人

输入：LR组成的字符串
输出：最少剩下的人数
'''
import sys
class Solution():

    def afterContent(self,s): #未通过
        if s==None or len(s)<0:
            return None
        if len(s)== 0:
            return 0
        if len(s) == 1:
            return 1
        number = len(s)
        for i in range(len(s)-1):
            if s[i] == 'R' and s[i+1] == 'L':
                number1, number2 = len(s), len(s)
                if (i > 0 and s[i-1] == 'R') or (i < len(s)-2 and s[i+2] == 'L'):
                    if i > 0 and s[i-1] == 'R':
                        number1 = self.afterContent(s[:i]+s[i+1:])
                    elif i < len(s)-2 and s[i+2] == 'L':
                        number2 = self.afterContent(s[:i+1]+s[i+2:])
                else:
                    number1 = self.afterContent(s[:i] + s[i + 1:])
                    number2 = self.afterContent(s[:i + 1] + s[i + 2:])
                if number1 < number and number1 <= number2:
                    number = number1
                elif number2 < number and number2 <= number1:
                    number = number2
        return number

    def afterContent2(self,state):
        i = 0
        result = 0
        if state==None:
            return None
        if len(state) == 0:
            return 0
        if len(state) == 1:
            return 1
        while i < len(state) and state[i] == 'L':
            i += 1
            result += 1
        j = len(state)-1
        while j >= 0 and state[j] == 'R':
            j -= 1
            result += 1
        if i < j:
            result += 1
        return result

    def Content3(self,state):
        state_new = state.lstrip('L').rstrip('R')
        return len(state)-len(state_new)+min(len(state_new), 1)

    def Content4(self, state):
        if state.find('RL') == -1:
            print (len(state))
        else:
            import re
            t = re.findall('R+L+', state)
            print (len(state)-len(''.join(t))+1)

'''if __name__ == "__main__":
    state = sys.stdin.readline().strip()
    s = Solution()
    print s.afterContent2(state)'''

s=Solution()
print s.afterContent('RRR')
print s.afterContent('LLL')
print s.afterContent('RL')
print s.afterContent('RRRLLL')
print s.afterContent('R')
print s.afterContent('L')
print s.afterContent('LRLLLRRRL')

print s.afterContent2('RRR')
print s.afterContent2('LLL')
print s.afterContent2('RL')
print s.afterContent2('RRRLLL')
print s.afterContent2('R')
print s.afterContent2('L')
print s.afterContent2('LRLLLRRRL')

print s.Content3('RRR')
print s.Content3('LLL')
print s.Content3('RL')
print s.Content3('RRRLLL')
print s.Content3('R')
print s.Content3('L')
print s.Content3('LRLLLRRRL')