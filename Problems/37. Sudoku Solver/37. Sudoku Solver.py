class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        # initialization
        row = [[False for i in range(10)] for j in range(10)]
        col = [[False for i in range(10)] for j in range(10)]
        block = [[False for i in range(10)] for j in range(10)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    n = int(board[i][j])
                    bn = 3 * int(i / 3) + int(j / 3)
                    row[i][n] = True
                    col[j][n] = True
                    block[bn][n] = True
        flag = [False]
        self.dfs(board, 0, 0, flag, row, col, block)

    def dfs(self, board, i, j, flag, row, col, block):
        if flag[0]: return
        if i >= 9:
            flag[0] = True
            return
        if board[i][j] != '.':
            if j < 8:
                self.dfs(board, i, j + 1, flag, row, col, block)
            else:
                self.dfs(board, i + 1, 0, flag, row, col, block)
            if flag[0]: return
        else:
            bn = 3 * int(i / 3) + int(j / 3)
            for num in range(1, 10):
                if not (row[i][num] or col[j][num] or block[bn][num]):
                    board[i][j] = str(num)
                    row[i][num] = col[j][num] = block[bn][num] = True
                    if j < 8:
                        self.dfs(board, i, j + 1, flag, row, col, block)
                    else:
                        self.dfs(board, i + 1, 0, flag, row, col, block)
                    if flag[0]: return

                    row[i][num] = col[j][num] = block[bn][num] = False
                    board[i][j] = '.'
