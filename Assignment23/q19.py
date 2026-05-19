'''19) Reverse Number Cross
    5   5
     4 4
      3
     4 4
    5   5'''




for i in range(-2, 3):
    for j in range(-2, 3):
     
        if abs(i) == abs(j):
        
            print(3 + abs(i), end="")
        else:
            
            print(" ", end="")
    print()