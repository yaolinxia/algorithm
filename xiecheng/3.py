def kmp(s,t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if j == -1 or s[i] ==t[j]:
            i+=1
            j+=1
        else:
            j = next(j)
    if j == len(t):
        return "true"
    else:
        return "false"

def k(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    l = []
    for i in d.values():
        l.append(i)
    if len(set(l)) == 1:
        print("True")
    else:
        print("False")

while True:
    s = input()
    k(s)
