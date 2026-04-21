from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxarea = 0
        visited = set()

        def bfs(visited, x, y, grid):
            q = deque()
            q.append((x,y))
            visited.add((x,y))
            size = 0

            while q:
                x,y = q.popleft()
                size += 1

                for rx, ry in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx, ny = rx + x, ry + y

                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and ((nx,ny)) not in visited and grid[nx][ny] == 1:
                        visited.add((nx,ny))
                        q.append((nx,ny))
                
            return size



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    maxarea = max(bfs(visited, i, j, grid), maxarea)
        

        return maxarea
        