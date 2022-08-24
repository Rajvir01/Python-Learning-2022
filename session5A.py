# max of numbers using recursion
"""
def get_max(numbers, length):
    if length == 1:
        return numbers[0]
    else:
        number = get_max(numbers, length-1)
        if number > numbers[length-1]:
            return number
        else:
            return numbers[length - 1]


data = [2, 30, 4]
max = get_max(data, len(data))
print(max)
"""


# Factorial of a number using recursion
"""
def fact_num(number):
    if number == 0 or number == 1:
        return 1
    else:
        result = number*fact_num(number-1)
        return result


print(fact_num(2))
"""


#Print your name in reverse using recursion


"""
def rev_name(name):
    if len(name) == 0:
        return name
    else:
        return rev_name(name[1:]) + name[0]


print(rev_name("rajvir"))
"""


#Fibonacci series using recursion

def fib_ser(num):
    if num <= 1:
        return num
    else:
        return (fib_ser(num-1)+fib_ser(num-2))


print(fib_ser(7))




















