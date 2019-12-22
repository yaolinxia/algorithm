# coding=utf-8
# 求数组全部的子集，123=1,2,3,12，23，123
def find_subSet(s=[1, 2, 3]):
    # l: 存放全部的子集
    l = []
    len_l = len(s)
    win = 1
    # 子集为单独的
    for i in range(len_l):
        l.append(s[i])
    while win <= len_l:
        for i in range(len_l):
            temp = ""
            if i+win < len_l:
                for j in range(i, i+win+1):
                    temp += str(s[j])
                l.append(int(temp))
        win += 1
    print(l)

def find_subSet2(s):
    l = []
    ss = str(s)[1:-1]
    print(ss)
    win = 0  # 窗口大小
    while win < len(s):
        for i in range(len(s)):
            sub_s = ss[i:win]
            l.append(s)

if __name__ == '__main__':
    s = [1,2,3,4]
    find_subSet(s)

