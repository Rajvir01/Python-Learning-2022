# break and continue
"""
employees = ["john", "kia", "fig", "lian"]
employ_to_find = input("enter name: ")

for idx in range(0, len(employees)):
    print("checking employ with", employees[idx])

    if employees[idx] == employ_to_find:
        print("emp found")
        break

my_floor = 5
for floor_number in range(1, 11):
    print("Elevator Arrived at Floor #", floor_number)

    if floor_number == my_floor:
        print("My Floor Arrived:", my_floor)
        break
"""
"""
for idx in range(1,11):
    if idx >=5:
        print(idx)
    continue
"""

emp_salaries = [40000, 30000, 50000, 60000, 70000]
for idx in range(0, len(emp_salaries)):
    if emp_salaries[idx]>=50000:
        print(emp_salaries[idx])
        continue
    emp_salaries[idx] += 5000
    emp_salaries[idx] += (idx+1)*500

print(emp_salaries)
