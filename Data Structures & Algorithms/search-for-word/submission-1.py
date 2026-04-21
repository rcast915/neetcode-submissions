class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def bfs(board, i, j, word):
            visited = set()
            q = collections.deque()

            visited.add((i,j))
            q.append((i,j,word[0]))

            while q:
                x,y,curr = q.popleft()

                if len(curr) == len(word) and curr == word:
                    return True
                
                for rx, ry in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx, ny = rx + x, ry + y

                    if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[0]) and ((nx,ny)) not in visited and (curr+board[nx][ny]) == word[:len(curr)+1]:
                        q.append((nx,ny, curr + board[nx][ny]))
                        visited.add((nx,ny))
            


            return False




        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    val = bfs(board, x,y, word)

                    if val:
                        return True
        return False
                

                    
                


        