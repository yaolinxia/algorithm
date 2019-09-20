def sort_nums(b):

    # n = eval(input())
    n = b[0]
    a = []
    for i  in range(1, len(b)):
        a.append(b[i])

    # a = list(map(int, input().split()))

    b = sorted(a)
    count = 0
    for i in range(n):
        if a[i] != b[i]:
            count += 1
    print(count)
    return count

if __name__ == '__main__':
    arr=[1, 3, 4, 1]
    sort_nums(arr)