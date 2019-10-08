# 给你一个字符串，长度为n，要你找出字符串中出现次数最多的字符

"""
思路：
1. dict存储， key: 字符，value: 次数
2.
"""

def find_maxS(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    new_d = {v: k for k, v in d.items()}
    print(new_d[max(d.values())])

if __name__ == '__main__':
    find_maxS(s="aaaaabbbbbbb                   cccc")