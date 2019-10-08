# 给出已排序整数数组，请写一个函数快速找出“k”在第几位。
"""
思路：
1. 蛮力法
2，二分查找
3. dict存储，k:index, v:num
"""
def find_k(l, k):
    d = {}
    for i, j in enumerate(l):
        d[i] = j
    new_d = {v:k for k,v in d.items()}
    if k in new_d:
        print(new_d[k]+1)
    else:
        print("k不存在！")

if __name__ == '__main__':
    l = [1, 2, 5, 6, 9]
    k = 10
    find_k(l, k)
