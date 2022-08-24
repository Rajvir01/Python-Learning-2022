#TUPLES
#immutable
#cannot be updated

prices = (100, 200, 300, 40, 50)
print(prices, hex(id(prices)))

new_price = prices
print(new_price, hex(id(new_price)))

all_prices = (100, 200, 300, 40, 50)
print(all_prices, hex(id(all_prices)))

print(type(prices), type(new_price), type(all_prices))

del prices


