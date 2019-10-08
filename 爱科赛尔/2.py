# 给你一个整数，如何判断它是否是一个7的n次方？
# //不是7的n次方，返回-1；是7的n次方，返回n


"""
思路：
1. 枚举看看最后一位[1, 7, 9, 3，1，7。。。。。 ]
2. 对7进行取摸，不停取(7的20次方后不好使，数据位数太大)
"""


def if_7(num):
    # 定义一个temp, 存放每次取模后的结果
    temp = num
    n = 1 # 7的n次方
    while(temp):
        if temp == 7:
            print(n)
            break
        elif temp%7 == 0: # 说明能整除，继续除7
            temp = temp/7
            n += 1
        else:
            print(-1)
            break


if __name__ == '__main__':
    num = 7**19
    if_7(num)