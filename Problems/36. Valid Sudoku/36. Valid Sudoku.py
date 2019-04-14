class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            if not self._isValidRow(board, i):
                return False
            if not self._isValidCol(board, i):
                return False
        rows = [0, 3, 6]
        cols = [0, 3, 6]
        for i in rows:
            for j in cols:
                if not self._isValid(board, i, j):
                    return False
        return True

    def _isValidRow(self, board, row):
        marked = [False] * 10
        for i in range(9):
            s = board[row][i]
            if s != '.':
                if marked[int(s)]:
                    return False
                else:
                    marked[int(s)] = True
        return True

    def _isValidCol(self, board, col):
        marked = [False] * 10
        for i in range(9):
            s = board[i][col]
            if s != '.':
                if marked[int(s)]:
                    return False
                else:
                    marked[int(s)] = True
        return True

    def _isValid(self, board, i, j):
        marked = [False]*10
        for k in range(3):
            for l in range(3):
                s = board[i+k][j+l]
                if s != '.':
                    if marked[int(s)]:
                        return False
                    else:
                        marked[int(s)] = True
        return True

