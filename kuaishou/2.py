class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 每一个字典表示一行的元素出现次数

        dic_row = [{}, {}, {}, {}, {}, {}, {}, {}, {}]  # 每行的元素以一个字典储存，key是数字，value统一为1.
        dic_col = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        dic_box = [{}, {}, {}, {}, {}, {}, {}, {}, {}]

        # 只遍历一遍整个棋盘
        # 这里比较强大的地方在于它可以通过i,j来推断这个点在哪个3*3网格内
        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == "X":
                    continue
                if num not in dic_row[i] and num not in dic_col[j] and num not in dic_box[3 * (i // 3) + (j // 3)]:
                    dic_row[i][num] = 1
                    dic_col[j][num] = 1
                    dic_box[3 * (i // 3) + (j // 3)][num] = 1  # 利用地板除，向下取余。巧妙地将矩阵划分为九块
                else:
                    return False

        return True



import sys
if __name__ == '__main__':
    # l = [1, 2, 3, 4, 3, 3,1,1]
    # N = int(sys.stdin.readline().strip('\n'))
    l = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    #
    # l = []
    # for i in range(9):
    #
    #     line = sys.stdin.readline().strip()
    #     li = list(line)
    #     l.append(li)
    # # li = list(line)
    # # print(li)

    # print(l)

    print(Solution().isValidSudoku(l))
    # li = []
    # for i in range(N):
    #     s = int(sys.stdin.readline().strip('\n'))
    #     li.append(s)
    # s = "2??"