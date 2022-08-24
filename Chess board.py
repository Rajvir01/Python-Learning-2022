#TASK 1 CHESS BOARD
"""
for row in range(1, 9):
    for column in range(1, 9):
        if(row+column) % 2 == 0:
            print("\u25A0", end="")
        else:
            print("\u2B1C", end="")
    print()

"""
#TASK 2
#PLACE QUEEN ON GIVEN COORDINATES


row_queen1 = int(input("enter coordinates for queen1:"))
column_queen1 = int(input("enter coordinates for queen1:"))

row_queen2 = int(input("enter coordinates for queen2:"))
column_queen2 = int(input("enter coordinates for queen2:"))

if row_queen1 == row_queen2 and column_queen1 == column_queen2:
    print("2 queens cannot be on same row or same column")

else:
    for row in range(1,9):
        for column in range(1,9):
            if row == row_queen1 and column == column_queen1:
                print("\u2655", end="")
            elif row == row_queen2 and column == column_queen2:
                print("\u2658", end="")
            else:
                if (row + column) % 2 ==0:
                    print("\u2b1c", end="")
                else:
                    print("\u2b1b", end="")
        print()