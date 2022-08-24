# Conditional Operators
# ==, !=, >=, <=, >, <

# Logical Operators
# and or

# Membership Testing Operators
# is, is not

cab_fare = 500
e_wallet = 200

e_wallet += 500

print("can i book a cab:", (e_wallet >= cab_fare))

result = False
print(result)

email = input("enter ur email: ").strip()
password = input("enter ur password: ")

print("Login status: ", (email == "john@example.com" and password == "john123"))

otp = 4281
user_otp = int(input("enter otp: "))

print("otp check: ", (user_otp == otp))

johns_age = 10
fionnas_age = 10
daves_age = 30
# print(johns_age == fionnas_age)
print(johns_age is fionnas_age)
# print(daves_age != fionnas_age)
print(daves_age is not fionnas_age)

# Assignment1: Explore difference between == and is + != vs is not