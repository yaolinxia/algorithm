#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def paiban(num, string):
    l_s = string.strip().split(" ")
    len_s = len(string)
    len_ls = len(l_s)
    print(l_s)
    print(len_s)
    line_num = (len_s+2)//num+1
    print(line_num)
    i = 0
    total = []
    for s in l_s:
        if i == 0:
            sen0="  "
            if len(sen0)<num:
                sen0 = sen0 + s + ' '
            else:
                sen0 = sen0[:-1]
                total.append(sen0)
                i +=1
        elif i < line_num-1:
            sen0 = ''
            if len(sen0) <num:
                sen0 = sen0 + s + ' '
                print(sen0)
            else:
                sen0 = sen0[:-1]
                total.append(sen0)
                i+=1
        elif i == line_num-1:
            sen0 = ''
            if len(sen0) < num:
                sen0 = sen0 + s + ' '
            else:
                sen0 = sen0[:-1]
                total.append(sen0+'\n')
                i += 1
    print(total)
    return total
    print("  I have a")
    print("dream Martin")
    print("Luther King")

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