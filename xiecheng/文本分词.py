"""
我,要,爱,携程,携程旅行网吧安倍,旅行网,旅行
我爱携程旅行网
"""
def seg_word(d, sen):
    end = len(sen)
    len_l = []
    # # print(d)
    # for c in d:
    #     # print(c)
    #     len_l.append(len(c))
    # max_len = max(len_l)

    # max_len = end-1
    # print(max_len)
    words = []
    while end > 0:
        head = 0
        # head = max(end - max_len, 0)
        for mid in range(head, end - 1):
            word = sen[mid: end]
            if word in d:
                # print(mid, end - 1, word)
                words.append(word)
                end = mid
                break
        else:
            end -= 1
            # print(end, end, sen[end])
            words.append(sen[end])

    # print(words)
    for i in range(len(words)):
        # print(words[i])
        if words[i] not in d:
            print("NO")
            break
        # if words[i] in d:
        #     print(words[i])
        if i == len(words)-1:
            print("YES")
"""
输入两行，第一行描述的是词典W，按逗号分隔
我,要,爱,携程,携程旅行网,旅行网,旅行
我爱携程旅行网
第二行是句子S
"""
import sys
if __name__ == '__main__':
    # d = ['我', '要', '爱', '携程', '携程旅行网', '旅行网', '旅行']
    # sen = '我爱携程旅行网'
    w = input()
    sen = input()
    d = w.split(",")
    # print(d)

    seg_word(d, sen)
