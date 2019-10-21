# 给定一个字符串，转化为列表
"""
2,3,4,1
['2', '3', '4', '1']
[2, 3, 4, 1]
"""
def str2list(s="[2,3,4,1]"):
    s_cut = s[1:-1]
    print(s_cut)
    s_l = s_cut.strip().split(',')
    print(s_l)
    l = []
    for c in s_l:
        l.append(int(c))
    print(l)

# 字典里面基于字进行排序
def sorted_dict(d={"a":3, "f":5, "b":6}):
    s_d = sorted(d, key=lambda i:d[i])
    print(s_d)
# 按照字符串的第一个字母进行对整个字符串对排序
def sorted_s(l=["delphi" ,"Delphi" ,"python" ,"Python" ,"c++" ,"C++" ,"c" ,"C" ,"golang" ,"Golang"]):
    l.sort(key=lambda s: s[0])
    print(l)

def test():
    from functools import reduce
    def fn(m,n):
        return m*10+n
    print(reduce(fn, [8,9,5,6,3,2]))


if __name__ == '__main__':
    # str2list()
    # sorted_dict()
    test()