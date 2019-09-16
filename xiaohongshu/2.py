#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def paiban(num, string):
    l_s = string.strip().split(" ")
    len_s = len(string)
    len_ls = len(l_s)
    # print(l_s)
    # print(len_s)
    line_num = (len_s+2)//num+1
    # print(line_num)
    i = 0
    total = [""]*line_num
    total[0] = "  "
    for s in l_s:
        if len(total[i]+s)<num:
            total[i] = total[i] + s + ' '
        else:
            # total[i] = total[i][:-1]
            i += 1
            total[i] = total[i] + s + ' '
        # print(total)
    for i in range(line_num):
        if i == line_num-1:
            print(total[i][:-1]+'\n')
        else:
            print(total[i][:-1])

def s(input, limit):
    localStr = ''
    lines = []
    currentStr = ''
    for c in input:
        if c == ' ':
            if len(currentStr + localStr) <= limit:
                lines.append(currentStr + localStr)
                currentStr = ''
                localStr = ''
            else:
                lines.append(currentStr)
                currentStr = localStr
                localStr = ''
        else:
            localStr += c
    for i in lines:
        print(i)


import sys

if __name__ == '__main__':
    # s = "I have a dream Martin Luther King"
    # num = 13
    num = int(sys.stdin.readline().strip('\n'))
    s = sys.stdin.readline().strip('\n')

    paiban(num, s)