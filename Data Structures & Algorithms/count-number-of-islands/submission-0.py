from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None: return 0

        def bfs(i, j, grid: List[List[str]], visited: set()):
            q = deque()

            visited.add((i,j))
            q.append((i,j))

            while q:
                x,y = q.popleft()

                for rx, ry in [(1,0),(-1,0),(0,-1),(0,1)]:
                    nx = x + rx
                    ny = ry + y

                    if nx >= 0 and nx < len(grid) and  ny >= 0 and ny < len(grid[0]) and (nx,ny) not in visited and grid[nx][ny] == "1":
                        visited.add((nx,ny))
                        q.append((nx,ny))
            return
        
        
        
        
        
        
        count = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j, grid,visited)
                    count += 1
        return count
                       