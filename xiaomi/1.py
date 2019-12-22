nums = list("0123456789")
letters = list("abcdefghijklmnopqrstuvwxyz")
letters_up = []
for l in letters:
    letters_up.append(l.upper())
legal_str = nums+letters+letters_up

def str_legal(str_list):
    hefa = []
    buhefa = []
    print(str_list)
    for s in str_list:
        c_len = len(s)
        leg_str = ""
        for c in s:
            length_feifa = 0 # 非法字符长度
            length_hefa = 0 # 合法字符长度
            if c in legal_str:
                length_hefa += 1
                leg_str += c
            else:
                length_feifa += 1
            if length_feifa == c_len:
                buhefa.append(s)
            else:
                hefa.append(leg_str)
    print(hefa)
    print(buhefa)

import sys
if __name__ == '__main__':
    # str = input()
    # str_list = str.strip().split()
    str_list = ['aaaa', 'bbbb', 'sss', 's--=', '===', '--']
    str_legal(str_list)
    # print(str_legal(str_list))


