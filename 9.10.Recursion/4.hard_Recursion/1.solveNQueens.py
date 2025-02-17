https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def issafe(row,col,board):
            # preserve row and col first
            r = row
            c = col
            # check only backward dir - n onee to check forwards
            # 1. left up diagonal
            while row>=0 and col>=0:
                if board[row][col]=='Q':return False
                row-=1
                col-=1

            row  = r
            col = c
            # 2. left staright
            while col>=0:
                if board[row][col]=='Q':return False
                col-=1

            row  = r
            col = c
            # 3. left down daignon
            while row<n and col>=0:  #-- row moves towards n
                if board[row][col]=='Q':return False
                row+=1
                col-=1

            return True #-- if all passed
            
        def rec(col,board,ans):
            if col ==n:
                ans.append(list(board))
                return

            for row in range(n):
                if issafe(row,col,board):
                    board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                    rec(col+1, board, ans)
                    board[row] = board[row][:col] + '.' + board[row][col+1:]

        ans=[]
        # board =[['.' for _ in range(n)] for _ in range(n)]
        # print(board)
        board = ['.'*n for _ in range(n)]
        print(board)

        rec(0,board,ans)
        return ans
