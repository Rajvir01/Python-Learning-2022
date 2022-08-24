#SINGLE VALUE CONAINER
#COPY, CREATE, UPDATE OPERATION

fries_price = 50
coke_price = fries_price
coke_price = 70

print("fries_price:", fries_price, hex(id(fries_price)))
print("coke_price:", coke_price, hex(id(coke_price)))

#MULTIVALUE CONTAINERS (list)
#CREATE, UPDATE , DELETE

dish_price = [20,30,40,50,60]
jons_cafe_dish_price = dish_price

print("dish_price:", dish_price, hex(id(dish_price)))
print("jons_cafe_dish_price:", jons_cafe_dish_price, hex(id(jons_cafe_dish_price)))

dish_price[2] = 34
jons_cafe_dish_price[1] = 56

print("dish_price:", dish_price, hex(id(dish_price)))
print("jons_cafe_dish_price:", jons_cafe_dish_price, hex(id(jons_cafe_dish_price)))

del dish_price[3]
del jons_cafe_dish_price

print("dish_price:", dish_price, hex(id(dish_price)))
print("jons_cafe_dish_price:", jons_cafe_dish_price, hex(id(jons_cafe_dish_price)))


