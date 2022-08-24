#PRINT NAME IN NATIVE LANGUAGE
#print("my name is : Rajvir -> \u0A30\u0A06\u0A1C\u0A35\u0A08\u0A30")

message = """
    Welcome to zomato
    Apply promo code
    ---------------
        TRYNEW
    ---------------
    Get 30% OFF up to ₹75
    Valid on total value of items worth ₹149 or more.
    _______________
    ZOMATO
    _______________
    FLAT 100 OFF
    Valid on total value of items worth ₹249 or more.
    """

print(message)

amount = int(input("Enter amount:"))
promo_code = input("Enter promocode:")

print("amount: \u20b9", amount)
print("prom code:", promo_code)


if amount>149:
    print("u can apply promccode")
else:
    print("ad items worth ", 149-amount, "more")


if promo_code == "TRYNEW" and amount >= 149:
    discount = 0.3 * amount
    print("u can get discount: ", discount)
    amount -= discount
    print("u have to pay \u20b9", amount)
else:
    print("either promocode or amount is invalid")


if promo_code =="TRYNEW" :
    if amount >=149:
        discount = 0.3 * amount
        print("u can get discount: ", discount)
        amount -= discount
        print("u have to pay \u20b9", amount)
    else:
        print("add items worth ", 149-amount, "more bc")
else:
    print("pcode is invalid")
    print("pay asap", amount)


if promo_code == "TRYNEW":
    if amount >= 149:
        discount = 0.30 * amount
        if discount > 75:
            discount = 75
        print("Discount is: \u20b9", discount)
        amount -= discount
        print("Please Pay: \u20b9", amount)
    else:
        print("Add items worth", (149-amount), "more")
else:
    print("Promo Code is Invalid")
    print("Please Pay: \u20b9", amount)




