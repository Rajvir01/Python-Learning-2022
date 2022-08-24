"""idx = 1
while idx<10:
    idx+=1
    print(idx)

for idx in range(1,11):
    print(idx)

for row in range(1, 9):
    print("\u25A1", end=" ")"""

"""print("coord1:")
coord1 = int(input())
print("coord2:")
coord2 = int(input())"""


for row in range(1, 9):
    for column in range(1, 9):
        if(row+column) % 2 == 0:
            print("\u25A0", end=" ")
        else:
            print("\u2B1C", end=" ")
    print()


