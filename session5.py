# Recursion
# when a function is called within a function


def print_number(number):
    print("number is:", number)
    number += 1
    if number <= 10:
        print_number(number)


print_number(6)
print_number(49)