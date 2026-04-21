from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        # find tresure chest and water positions
        water = set()
        tresure = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                currval = grid[i][j]

                if currval == -1:
                    water.add((i,j))
                elif currval == 0:
                    tresure.add((i,j))


        def bfs(grid, water, tresure):
            visited = tresure

            q = deque()
            q.extend(visited)

            distance = 0 
            while q:

                for _ in range(len(q)):
                    x, y = q.popleft()

                    grid[x][y] = distance

                    for rx, ry in ((0,1),(0,-1), (1,0), (-1,0)):

                        nx, ny = rx + x, ry + y

                        if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and (nx,ny) not in visited and (nx,ny) not in water:
                            q.append((nx,ny))
                            visited.add((nx,ny))
                    

                distance += 1
            


        bfs(grid,water,tresure)

       


    
        