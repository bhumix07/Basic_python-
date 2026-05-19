'''14) Spiral Number Square
     1   2   3   4
    12  13  14   5
    11  16  15   6
    10   9   8   7'
    
    n = 4
matrix = [[0] * n for _ in range(n)]

num = 1
row, col = 0, 0

# Loop until all 16 numbers are filled
while num <= n * n:
    # 1. Move Right
    while col < n and matrix[row][col] == 0:
        matrix[row][col] = num
        num += 1
        col += 1
    col -= 1  # Step back inside the grid
    row += 1  # Move down to the next row

    # 2. Move Down
    while row < n and matrix[row][col] == 0:
        matrix[row][col] = num
        num += 1
        row += 1
    row -= 1  # Step back inside the grid
    col -= 1  # Move left to the next column


    while col >= 0 and matrix[row][col] == 0:
        matrix[row][col] = num
        num += 1
        col -= 1
    col += 1  
    row -= 1  


    while row >= 0 and matrix[row][col] == 0:
        matrix[row][col] = num
        num += 1
        row -= 1
    row += 1  
    col += 1  

for r in matrix:
    for val in r:
        print(f"{val:3d}", end="")
    print()