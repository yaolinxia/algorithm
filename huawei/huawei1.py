import sys


# 初始化输入
def input_init():
    string_list = []
    while True:
        line = sys.stdin.readline().rstrip('\n')  # 逐行读入，并去除行末的换行符
        if 0 == len(line):  # 输入以空行结束,break语句较强应放在 continue语句前，不然会陷入死循环
            break
        if len(line) > 64:  # 每个字符串长度不超过64
            continue
        if len(string_list) > 100 - 1:  # 输入字符串个数不超过100
            continue
        if (line.startswith(' ')) & (0 != len(line)):  # 输入字符串不能以空格开始
            continue
        temp_str = line.split()  # split()，默认分割(删除)所有的空字符,包括空格、换行(\n)、制表符(\t)等
        string_list.append(' '.join(temp_str))  # 输入的连续空字符串（空格/制表符/回车/换行符）作为一个空格处理
        return string_list


# 保存合法字符串
def get_legal_string(string_list: list):
    number_ls = list("0123456789")


    letter_ls = list("abcdefghijklmnopqrstuvwxyz")
    up_letter_ls = []
    for letter in letter_ls:
        up_letter_ls.append(letter.upper())

    flag = int(0)
    legal_str = []

    for index in range(0, len(string_list)):
        temp_str = string_list[index]
        for ix in range(0, len(temp_str)):
            x = temp_str[ix]
            if (x in number_ls) | (x in letter_ls) | (x in up_letter_ls):
                # 合法字符串
                flag = 1
            else:
                flag = 0
                break
        if flag:
            legal_str.append(temp_str)
    return legal_str


# 去除列表中重复的字符串
def remove_repeat_string(string_list: list):
    remove_repeated_str = string_list.copy()


    ix = 0
    while True:
        temp_str = remove_repeated_str[ix]
        count = remove_repeated_str.count(temp_str)  # 统计重复字符串个数
        if ix == len(remove_repeated_str) - 1:
            break
        if count == 1:
            ix = ix + 1
            continue
        while count > 1:  # for循环不能动态改变数组长度，因此用while
            count = count - 1
            j = 1
            while True:
                need_remove = remove_repeated_str[-j]  # 反序遍历
                if temp_str == need_remove:
                    # remove_repeated_str.remove(need_remove) # 因为remove()只能移除列表中第一个匹配的元素
                    pop_index = len(remove_repeated_str) - j
                    remove_repeated_str.pop(pop_index)  # 删除指定索引位置元素(反序)
                    break
                else:
                    j = j + 1
    return remove_repeated_str


# 保存非法字符串
def get_non_legal_string(raw_string_list: list, legal_string: list):
    non_legal_str = []
    for i in raw_string_list:
        if i in legal_string:
            continue
            non_legal_str.append(i)
            return non_legal_str


# 左移10次字符 10%len(str)
def shift_string(string_list: list):
    shift_string = []


    for shift_str in string_list:
        start = 10 % len(shift_str)
    shift_temp = ""
    shift_temp += shift_str[start:]
    shift_temp += shift_str[:start]
    shift_string.append(shift_temp)
    return shift_string


# 输出字符串结果
def output_string(string_list: list):
    output = ""


    for str_ in string_list:
        output += str_ + " "
    print(output)


def main():


    # 原始输入
    str_list = input_init()
    # 保存合法字符串
    legal_str = get_legal_string(str_list)
    # 保存非法字符串
    non_legal_str = get_non_legal_string(raw_string_list=str_list, legal_string=legal_str)
    # 保存合法字符串_去重
    remove_repeated_string = remove_repeat_string(legal_str)
    # 1.输出去重合法字符串
    output_string(remove_repeated_string)
    # 2.输出未去重的非法字符串
    output_string(non_legal_str)
    # 3.输出去重合法字符串左移10次后的结果
    shift_legal_str = shift_string(remove_repeated_string)
    output_string(shift_legal_str)
    # 4.输出对合法字符串字符串左移后排序，按ASCII表字符从小到大顺序排序
    shift_legal_str = sorted(shift_legal_str)
    output_string(shift_legal_str)

if __name__ == '__main__':
    main()