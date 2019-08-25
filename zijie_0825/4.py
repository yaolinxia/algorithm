from collections import defaultdict

def _get_gcd(a, b):
    while a%b != 0:
        a, b = b, a % b
    return b > 1

class solution:
    def get_max_sweets(self, sweets):
        n = len(sweets)
        ne = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i!=j:
                    if _get_gcd(sweets[i], sweets[j]):
                        ne[i].append(j)

        self.res = 0
        def dfs(i, path, visited):
            end = True
            for j in ne[i]:
                if j not in visited:
                    end = False
                    visited.add(j)
                    dfs(j, path+[j], visited)
                    visited.remove(j)
            if end:
                self.res = max(self.res, len(path))
        for i in range(n):
            dfs(i, [i], {i})
        return self.res


import sys

N = int(sys.stdin.readline().strip())
# M = []
# for _ in range(N):
line = sys.stdin.readline().strip()
sweets = list(map(int, line.split()))
print(solution().get_max_sweets(sweets))
# print(solution().get_max_sweets([20, 50, 22, 74, 9, 63]))