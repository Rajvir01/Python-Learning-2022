# Functions
# f(x) = y | y = x*x + 1
# f(1) -> 1*1 + 1 -> 2

# def -> define i.e. create a function in memory
# f -> name of function, which can be any name of your choice
# after the : wih tab space, we have instructions which a function will execute in a sequence

"""
def f(x):
    y = x*x + 1
    print(y)
f(3)
f(4)
"""

ac_power = False

def ac_check():
    global ac_power

    if ac_power:
        print("ac is on ")
        ac_power = False

    else:
        print("ac is off")
        ac_power = True

ac_check()
ac_check()