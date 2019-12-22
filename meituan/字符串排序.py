"""
作者：tttsq
链接：https://www.nowcoder.com/discuss/261885?type=1
来源：牛客网

题目描述：生活中经常有需要将多个字符串进行排序的需要，比如将美团点评的部分业务名称（外卖，打车、旅游、丽人、美食、结婚、旅游景点、教培、门票、酒店），
用拼音表示之后按字母逆序排列，字母逆序指从z到a排列，比如对两个字符串排序时，先比较第一个字母按字母逆序排z在a的前面，当第一个字母一样时再比较第二个字母按字母逆序排，
以此类推。特殊情况（1）空字符串需排在最前面；（2）若一个短字符串是另一个长字符串的前缀则短字符串排在前面。请自行实现代码进行排序，直接调用sort等排序方法将不得分且视为作弊。
输入：
输入为一行，由多个字符串以英文逗号拼接而成，最多不超过128个字符串且可能有重复，每个字符串由小写字母a-z组成，可以为空，最长不超过128个字符。
输出：
对于每个测试实例，要求将输入中被拼接为一行的多个字符串，按字母序逆序排序后，仍以逗号拼接成一行输出。
样例输入：
waimai,dache,lvyou,liren,meishi,jieun,lvyoujingdian,jiaopei,menpiao,jiudian
样例输出：
waimai,menpiao,meishi,lvyou,lvyoujingdian,liren,jiudia,jiehun,jiaopei,dache
提示：
对输入进行切分得到字符串数组，首先按第一个字母进行排序和分区，再对同一区内字符串按第二个字母进行排序和分区，以此类推递归实现，直到对所有字符串排序结束，最后拼接并输出。
"""
def sort_str():
    l =["delphi" ,"Delphi" ,"python" ,"Python" ,"c++" ,"C++" ,"c" ,"C" ,"golang" ,"Golang"]
    l.sort()  # 按字典顺序升序排列
    print("升序:" ,l)

    l.sort(reverse=True)  # 按降序排列
    print("降序:" ,l)

# 对字符串进行从小到大排序
def sored_maopao(l_sub):

    for i in range(len(l_sub)):
        for j in range(i+1, len(l_sub)):
            if l_sub[i] < l_sub[j]:
                temp = l_sub[i]
                l_sub[j] = l_sub[i]
                l_sub[i] = temp
    print(l_sub)

# l: 存放数据库
def sort_str1(l):
    l_len = len(l)
    for i in range(l_len):
        # l = sorted(l, key=l[i][0])
        print(l[i][0])
    l.sort(key=lambda s:s[0])
    print(l)


"""
waimai,dache,lvyou,liren,meishi,jiehun,lvyoujingdian,jiaopei,menpiao,jiudian
"""
import sys
if __name__ == '__main__':
    # nums = [[1, 2, 3, 5], [4, 5, 6, 9], [7, 8, 9,11]]
    # # m = 3
    # # n = 3
    # line1 = sys.stdin.readline().strip()
    # l = list(map(int, line1.split()))
    # m = l[0] #行
    # n = l[1] #列
    # temp = []
    # for i in range(m):
    #     lines = sys.stdin.readline().strip()
    #     # print(8)
    #     ls = list(map(int, lines.split()))
    #     temp.append(ls)
    # s = sys.stdin.readline().strip()
    # l = list(map(str, s.split(",")))
    # l.sort(reverse=True)
    # sorted(l,reverse=True)
    # print(l)
    """  
    pre = 0
    next = 1
    while next< len(l):
        # min_s = min(len(l[pre]), len(l[next]))
        # print(min_s)
        if len(l[pre])>len(l[next]):
            # print(l[next], l[pre][:len(l[next])])
            if l[next] == l[pre][:len(l[next])]:
                # print(l[next],l[pre][:len(l[next])])
                temp = l[pre]
                l[pre] = l[next]
                l[next] = temp
        next+=1
        pre+=1
        # for i in range(1, min_s+1):
        #     if l[pre][:i] == l[next][:i]:
        #         continue
    s_total = ""
    for c in l:
        s_total=s_total+c+','
    print(s_total[:-1])

    # print(str(l)[1:-1])
    # sort_str()
    """
    s = "waimai,dache,lvyou,liren,meishi,jiehun,lvyoujingdian,jiaopei,menpiao,jiudian"
    l = s.split(',')
    # l = ["delphi" ,"Delphi" ,"python" ,"Python" ,"c++" ,"C++" ,"c" ,"C" ,"golang" ,"Golang"]
    sort_str1(l)