def checkXMatrix(grid):
    n = len(grid)
    for i in range(n):
        if grid[i][i] == 0 or  grid[i][((n-1)-i)] == 0:
            return False
    for i in range(n):
        for j in range(n):
            if i != j and j != n-1-i and grid[i][j] != 0:
                return False
    return True


print(checkXMatrix([[5,0,0,1],[0,4,1,5],[0,5,2,0],[4,1,0,2]]))

[[5,0,0,1]
,[0,4,1,5]
,[0,5,2,0]
,[4,1,0,2]]