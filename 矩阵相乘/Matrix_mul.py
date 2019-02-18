"""
input: 两个矩阵，用二维列表来定义
output: 一个数，两个矩阵相乘的结果
"""

import numpy as np
#　思路１：直接用numpy的矩阵相乘
def Matrix_mul(m1, m2):
    print(m1)
    print(m2)
    # print(m1[0])
    mul = m1 * m2
    print(int(mul))

# 思路2 :Strassen算法
if __name__ == '__main__':
    m1 = np.matrix('1 0 2')
    m2 = np.matrix('1; 1; 1')
    Matrix_mul(m1, m2)