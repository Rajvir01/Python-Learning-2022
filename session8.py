mc_donalds_menu = {
    "burger": 100,
    "fries": 50,
    "coke": 40,
    "icecream": 70,
    "noodles": 150,
    "pizza": 200
}

cart = []

choice = "yes"

while choice == "yes":
    dish_name = input("enter dish name")
    cart.append(mc_donalds_menu[dish_name])

    choice = input("do u wush to continue?")

print("cart")
print(cart)
print("pay \u20b9", sum(cart))