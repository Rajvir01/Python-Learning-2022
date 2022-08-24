mc_donald_menu = [
    {
        "name": "burger",
        "price": 100,
        "quantity": 0
    },
    {
        "name": "fries",
        "price": 70,
        "quantity": 0
    },
    {
        "name": "coke",
        "price": 50,
        "quantity": 0
    },
    {
        "name": "pizza",
        "price": 300,
        "quantity": 0
    },
    {
        "name": "noodles",
        "price": 200,
        "quantity": 0
    }
]

def shopping_cart():
#shopping cart

    cart = []
    total_dishes = 0
    total_amount = 0

    choice = "yes"
    while choice == "yes":
        dish_name = input("enter dish name:")

        for idx in range(len(mc_donald_menu)):
            if mc_donald_menu[idx]["name"] == dish_name:
                quantity = int(input("enter quantity for "+dish_name+":"))
                mc_donald_menu[idx]["quantity"] = quantity
                total_dishes += quantity
                total_amount += quantity * mc_donald_menu[idx]["price"]
                cart.append(mc_donald_menu[idx])
                break

        choice = input("do u wish to continue:")

    print("cart")
    print(cart)
    print("total dishes = ", total_dishes)
    print("pay:", total_amount )

    return total_amount


result = shopping_cart()
