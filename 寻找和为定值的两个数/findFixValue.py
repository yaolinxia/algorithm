class Solution(object):
    """
    1, 用sum减去li列表中各元素的值，存放到li2中
    2, 设置两个指针，指向头和尾
    """
    def findFixV(self, li, Sum):
        l2 = []
        for i in range(0, len(li)):
            l2.append(Sum - li[i])
            #print(c)

        for i in range(0, len(li)):
            for j in range(len(l2)-1, -1, -1):
                if li[i] == l2[j]:
                    print(li[i])
                    print(l2[j])
                    break

        # for t in l2:
        #     print(t)

        # for j in range(len(l2)-1, -1, -1):
        #     print(l2[j])

        # for t2 in li:
        #     print(t2)
    """
    使用hash表进行存储
    1，针对给定的数组构造hash表
    2，直接查找sum-元素值是否等于hash函数中的某个数
    """
    def findFixV2(self, li, Sum):
        D = {}
        length = len(li)
        for i in range(0,length):
            D[i] = li[i]
        #     print(D[i])
        # print(D.keys())
        # print(D.values())
        print(D)
        for j in range(0, length):
            #print(D[j])
            s = Sum - D[j]

            if s in D.values():
                print(D[j])
                #print(Sum - D[j])
            else:
                continue
    """
    1，先进行排序
    2，然后分别设置两个指针，指向头和尾
    3，如果某一刻a[i]+a[j] > sum，则要想办法让sum的值减小，所以此刻i不动，j--；
       如果某一刻a[i]+a[j] < sum，则要想办法让sum的值增大，所以此刻i++，j不动。
    """
    def findFixV3(self, li, Sum):
        li = sorted(li)
        print(li)
        head = 0
        tail = len(li) - 1
        temp = []
        while head < tail:
            if li[head] + li[tail] > Sum:
                tail -= 1
            elif li[head] + li[tail] < Sum:
                head += 1
            elif li[head] + li[tail] == Sum:
                temp.append(li[head])
                temp.append(li[tail])
                break
        print(temp)

    # time: 2019_0116
    # 存在问题：复杂度高于O(n),为O(n^2)
    def findFixV4(self, li, Sum):
        for i in li:
            if Sum-i in li:
                print(li.index(Sum-i))

    # time: 2019_0116
    # 使用额外的空间存储差值
    def findFixV5(self, li, Sum):
        sub_list = []
        for i in li:
            sub_list.append(Sum-i)
        print(sub_list)
        head = 0
        tail = len(li) - 1
        while head < len(li) & tail >= 0:
            if li[head] == sub_list[tail]:
                # print(li[head], sub_list[tail])
                print("------------")
            else:

                head += 1
                tail -= 1

if __name__ == "__main__":
    li = [15, 1, 2, 4, 7, 11]
    value = 15
    Solution().findFixV5(li, value)