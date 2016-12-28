def find_empty(grid): #JUST FIND AN EMPTY COORDINATE
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == -1:
                return (r,c)

def returnaSquare(grid,r,c):
    answer = []
    for i in range(r,r+3):
        for j in range(c,c+3):
            answer.append(grid[i][j])
    return answer

def getLittleSquare(grid,r,c):
    if c <= 2:
        if r <= 2:
            return returnaSquare(grid,0,0)
        if r > 2 and r <=5:
            return returnaSquare(grid,3,0)
        if r > 5 and r <= 8:
            return returnaSquare(grid,6,0)
    if c > 2 and c <= 5:
        if r <= 2:
            return returnaSquare(grid,0,3)
        if r > 2 and r <=5:
            return returnaSquare(grid,3,3)
        if r > 5 and r <= 8:
            return returnaSquare(grid,6,3)
    if c > 5:
        if r <= 2:
            return returnaSquare(grid,0,6)
        if r > 2 and r <=5:
            return returnaSquare(grid,3,6)
        if r > 5 and r <= 8:
            return returnaSquare(grid,6,6)
    else:
        return "SACMALIK"

def isPassable(grid,r,c,value):
    column = getCols(grid)[c]
    row = grid[r]
    if value not in row and value not in column and value not in getLittleSquare(grid,r,c): 
        return True
    return False

def getCols(grid):
    acc = []
    for c in range(len(grid[0])):
        acc.append([grid[r][c] for r in range(len(grid))])
    return acc

def solveSudoku(grid):
    target = find_empty(grid)
    if not target:
        return grid
    (r,c) = target
    for i in range(1,10):
        if isPassable(grid,r,c,i): #WRITE A NICE CONSTRAINT CHECKER FUNCTION
            grid[r][c] = i
            if solveSudoku(grid): #RECURSE IF SO 
                return grid 
        grid[r][c] = -1 #IF DID NOT WORK! 

    return False

#-----MY SAMPLE TEST CASE ------#

grid = [[8,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,3 ,6,-1,-1,-1,-1,-1],
        [-1,7,-1 ,-1,9,-1,2,-1,-1],
        [-1,5,-1,-1,-1,7,-1,-1,-1],
        [-1,-1,-1,-1,4,5,7,-1,-1],
        [-1,-1,-1,1,-1,-1,-1,3,-1],
        [-1,-1,1,-1,-1,-1,-1,6,8],
        [-1,-1,8,5,-1,-1,-1,1,-1],
        [-1,9,-1,-1,-1,-1,4,-1,-1]]

#1 = [[1, 4, 8, 2, 3, 5, 6, 9, 7], [3, 2, 1, 4, 5, 6, 7, 8, 9], [2, 1, 3, 5, 4, 7, 9, 6, 8], [4, 3, 2, 1, 6, 9, 8, 7, 5], [5, 6, 4, 7, 9, 8, 1, 2, 3], [6, 5, 7, 9, 8, 1, 2, 3, 4], [7, 8, 9, 3, 1, 2, 4, 5, 6], [8, 9, 5, 6, 7, 4, 3, 1, 2], [9, 7, 6, 8, 2, 3, 5, 4, 1]]



x = solveSudoku(grid)
for row in x:
    print row
