nums = list("0123456789")
letters = list("abcdefghijklmnopqrstuvwxyz")
letters_up = []
for l in letters:
    letters_up.append(l.upper())
legal_str = nums+letters+letters_up
# print(legal_str)

def str_legal(str_list):
    hefa = []
    buhefa = []
    for s in str_list:
        c_len = len(s)
        leg_str = ""
        length_feifa = 0  # 非法字符长度
        length_hefa = 0  # 合法字符长度
        for c in s:
            if c in legal_str:
                length_hefa += 1
                leg_str += c
            else:
                length_feifa += 1
                # print("s:", length_feifa)
        if length_feifa == c_len:
            buhefa.append(s)
        else:
            if leg_str not in hefa:
                hefa.append(leg_str)
    # print(hefa)
    # print(buhefa)
    return hefa, buhefa

import sys
if __name__ == '__main__':
    # str = input()
    # str_list = str.strip().split()
    str_list = ['aaa=a', 'ABC¥%%', 'aaa)()a', 'sss', 's--=', '===', '--']
    hefa, buhefa = str_legal(str_list)
    hefa1 = ''
    buhefa1 = ''
    for c in hefa:
        hefa1 = hefa1 + c + " "
    for c in buhefa:
        buhefa1 = buhefa1 + c + " "
    print(hefa1[:-1])
    print(buhefa1[:-1])
