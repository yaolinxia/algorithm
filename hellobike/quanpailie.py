def permute(l, begin, end):
    if begin>=end:
        print(l)
    else:
        i = begin
        for num in range(begin, end):
            l[num], l[i] = l[i], l[num]
            permute(l, begin+1, end)
            l[num], l[i] = l[i], l[num]


l = [1, 2, 3, 4]
permute(l, 0, len(l))


