from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        from collections import deque
        """
        BFS from all 'O's around the border, and save nodes that are visited. 
        Then, change all 'O's to 'X' that are not visited.
        """
        if not board: return
        m, n = len(board), len(board[0])
        for (i,j) in [*[(0,j) for j in range(n-1)], *[(i,0) for i in range(1,m-1)], *[(m-1,j) for j in range(n-1)], *[(i,n-1) for i in range(m)]]:
            if board[i][j] == 'O':
                # BFS
                q = deque([(i,j)])
                while q:
                    i, j = q.popleft()
                    if board[i][j] != 'O': continue
                    board[i][j] = '#'
                    for (di,dj) in [(1,0), (-1,0), (0,1), (0,-1)]:
                        if 0<=i+di<m and 0<=j+dj<n and board[i+di][j+dj] == 'O':
                            q.append((i+di,j+dj))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == '#': board[i][j] = 'O'
        
s = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s.solve(board)
print(board)
board = [["X"]]
s.solve(board)
print(board)

