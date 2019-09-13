class solution:

    def main(self, AB, k):
        for a, b in AB:
            print(self.get_sol_num(a, b, k))

    def get_sol_num(self, a, b, k):
        res_range = list(range(a, b + 1))
        self.count = 0

        #        self.paths = []

        def dfs(path):
            lp = len(path)
            if lp > b:
                return
            if lp in res_range:
                #                self.paths.append(path)
                self.count += 1
            dfs(path + '红')
            dfs(path + k * '白')

        dfs('')
        return int(self.count%(1e9+7))  # , self.paths


# print(solution().get_sol_num(1,3,2))
# print(solution().get_sol_num(2,3,2))
# print(solution().get_sol_num(4,4,2))

import sys

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    t, k = list(map(int, line.split()))
    AB = []
    for _ in range(t):
        line = sys.stdin.readline().strip()
        a, b = list(map(int, line.split()))
        AB.append((a, b))
    solution().main(AB, k)