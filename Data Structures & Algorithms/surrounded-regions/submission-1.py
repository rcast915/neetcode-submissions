class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board or not board[0]:
            return

        def bfs(board, edges):
            q = deque(edges)
            
            while q:
                x, y = q.popleft()
                board[x][y] = 'E'  # Mark as escape

                for rx, ry in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nx, ny = x + rx, y + ry

                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 'O' and (nx,ny) not in edges:
                        q.append((nx, ny))
                        board[nx][ny] = 'E'  # Mark as escape
                        edges.add((nx,ny))

        edges = set()
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and board[i][j] == 'O':
                    edges.add((i, j))

        bfs(board, edges)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
