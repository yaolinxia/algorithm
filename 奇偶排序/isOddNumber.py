"""
思路一：
蛮力法，依次扫描整个数组，每遇到一个偶数，就将该数放到最后
时间复杂度（O^2)， 不符合题目要求
"""
def isOddNumber(num):
    length = len(num)
    i = 0
    while i < length:
        if num[i] % 2 == 0:
            num.append(num[i])
            num.remove(num[i])
            #print(num)
            i += 1
        elif num[i] % 2 == 1:
            i += 1
            continue
    return num

"""
思路二：
设置头尾指针，如果头指针指的是偶数，尾指针指的是奇数，则交换这两个数
"""
def isOddNumber2(num):
    head = 0
    tail = len(num) - 1
    while head < tail:
        if num[head] % 2 == 0 and num[tail] % 2 == 1:
            temp = num[head]
            num[head] = num[tail]
            num[tail] = temp
            head += 1
            tail -= 1
        elif num[head] % 2 == 0 and num[tail] % 2 == 0:
            tail -= 1
        elif num[head] % 2 == 1:
            head += 1
    return num

"""
思路三：
定义一前一后，两个指针进行扫描，first，next
1.如果first是奇数，next也是奇数，继续扫描，next加一
2.如果first是奇数，next是偶数，继续扫描，first,next各自加一
3.如果first是偶数，next是奇数，，交换，然后first,next各自加一
4.如果first是偶数，next是偶数，next加一，first不变
直到，next扫描到数组尾部
"""
def isOddNumber3(num):
    first = 0
    next = 1
    while next < len(num):
        if num[first] % 2 == 1 and num[next] % 2 == 1:
            next += 1
        elif num[first] % 2 == 1 and num[next] % 2 == 0:
            first += 1
            next += 1
        elif num[first] % 2 == 0 and num[next] % 2 == 1:
            temp = num[first]
            num[first] = num[next]
            num[next] = temp
            first += 1
            next += 1
        elif num[first] % 2 == 0 and num[next] % 2 == 0:
            next += 1
    # temp = num[first]
    # num[first] = num[len(num) - 1]
    # num[len(num) - 1] = temp

    return num

if __name__ == "__main__":
    num = [1, 2, 3, 4, 13, 89, 11, 23, 32, 34, 23, 23, 43, 112, 113]
    print(isOddNumber(num))
    print(isOddNumber2(num))
    print(isOddNumber3(num))
