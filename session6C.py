# Bubble sort
# Pass  y reference

numbers = [6,5,8,1,4]
print("numbers before:", numbers)

def sort(numbers):

    n = len(numbers)
    for idx in range(0,len(numbers)):
        for idx2 in range(0, n-idx-1):
            if numbers[idx2] > numbers[idx2+1]:
                numbers[idx2],numbers[idx2+1] = numbers[idx2+1],numbers[idx2]


sort(numbers)
print("numbers after:", numbers)
