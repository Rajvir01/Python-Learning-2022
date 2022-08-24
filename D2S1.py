#Copy operation

johns_age = 20
rias_age = johns_age

print("johns_age hashcode: ", hex(id(johns_age)))
print("rias_age hashcode: ", hex(id(rias_age)))


#UPdate operation

rias_age = 30
print("upd rias_age hashcode:", hex(id(rias_age)))

del johns_age
print(johns_age)