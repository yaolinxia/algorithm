def calculate(n, W, w_people):
    if n == 2:
        if w_people[0] + w_people[1] > W:
            return 2
        else:
            return 1
    if n == 1:
        return 1
    w_people.sort()
    if w_people[0] + w_people[n-1] <= W:
        w_people[n-1] += w_people[0]
        return calculate(n-1, W, w_people[1:]) + 1
    else:
        return calculate(n-1, W, w_people[:n-2]) + 1

if __name__ == '__main__':
    n, W = (int(x) for x in input().split())
    w_people = []
    for i in range(n):
        w_people.append(int(input()))

    print(calculate(n, W, w_people))