"""
思路一：递归实现
首先考虑最简单的情况。如果只有1级台阶，那显然只有一种跳法。如果有2级台阶，那就有两种跳的方法了：一种是分两次跳，每次跳1级；另外一种就是一次跳2级。

现在我们再来讨论一般情况。我们把n级台阶时的跳法看成是n的函数，记为f(n)。

- 当n>2时，第一次跳的时候就有两种不同的选择：
- 一是第一次只跳1级，此时跳法数目等于后面剩下的n-1级台阶的跳法数目，即为f(n-1)；
- 另外一种选择是第一次跳2级，此时跳法数目等于后面剩下的n-2级台阶的跳法数目，即为f(n-2)。

因此n级台阶时的不同跳法的总数f(n)=f(n-1)+f(n-2)。

我们把上面的分析用一个公式总结如下：

```
        /  1                             n = 1
f(n)=      2                             n = 2
        \  f(n-1) + f(n-2)               n > 2

```
"""
def skipFloor1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    return skipFloor1(n - 1) + skipFloor1(n - 2)

"""
思路2：相当于是斐波那契数列
1 ，1， 2， 3， 5， 8.。。。。。
每一项相当于是前两项的和
"""
def skipfllor2(n):
    num = [1] * 3
    for i in range(2, n+1):
        num[2] = num[0] + num[1]
        num[0] = num[1]
        num[1] = num[2]
    return num[2]

"""
例子：
2、换硬币问题。

想兑换100元钱，有1,2,5,10四种钱，问总共有多少兑换方法。递归解法
参考网址：https://blog.csdn.net/callinglove/article/details/46421959

分为两种情况:换取当前面值的情况 + 没有换取当前面值的情况
"""

def changeMoney(money, num):
    mon = [1, 2, 5, 6]
    if money == 0:
        return 1
    elif money < 0 or num == 0:
        return 0
    return changeMoney(money, num-1) + changeMoney(money-mon[num-1], num)

if __name__ == "__main__":
    n = 10
    print(skipFloor1(n))
    print(skipfllor2(n))
    print(changeMoney(100, 4))

