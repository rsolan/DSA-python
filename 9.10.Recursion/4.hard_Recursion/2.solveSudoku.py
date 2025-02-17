https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # m1 - recursion - TLE
        n = len(board)
        def isvalid(board,r,c,char):
            for i in range(9):
                if board[r][i] == char:
                    return False

                if board[i][c] == char:
                    return False

                row = 3*(r//3) + (i//3)
                col = 3*(c//3) + (i%3)
                if board[row][col] == char:
                    return False

            return True

            
        def solve(board):
            for r in range(n):
                for c in range(n):

                    if board[r][c] == '.':
                        for char in "123456789": #- string

                            if isvalid(board,r,c,char):
                                board[r][c] = char

                                # next rec cal
                                if solve(board):
                                    return True
                                else:
                                    board[r][c] ='.'  #earlier was wrong choice

                        return False #- not able to place any char-- outside fo rloop impppppp

            return True #- when no empty cell so didnt go in if statement




        solve(board)

