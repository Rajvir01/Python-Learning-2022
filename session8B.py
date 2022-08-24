"""
    Object Oriented Programming Structure
        Real World:
        1. Object: Anything which exists
        2. Class:  Drawing of an Object
        Computer Science
        1. Object: STORAGE CONTAINER [MULTI VALUE] -> HOMO|HETRO
        2. Class: A program which describes what object will contain
                  or how it will look in memory
        Principle of OOPS:
            1. Think of Object
                An Object is the one which has lot of data associated (attributes) to it
            2. Create its class
                its a programmatical way of defining the object
            3. From the class create Real Object in memory
                class_name()
        Client Requirements:
            Mr. John wants to create a food delivery app
            He want users to login with mobile phone numbers
            and choose dishes from restaurant and add them to cart
            Further place an order which is reflected to the restaurant
            And PickUp Person picks and delivers the order to user
            User can pay by several means
            User is an Object
            name, phone, email, gender, address
            Order is an Object
            id, amount, dishes, user, date, time ......
            Dish
            name, price, description, ratings, category
            Restaurant
            name, phone, email, address, price_per_person, review, operating_hours, dining
            MMT.com
            Object: OneWayFlight
            Attributes: from_location, to_location, departure_date, num_of_travellers, travel_class
            Objects are related to each other
            1. One to One
            2. One to Many
            3. Many to Many
"""


class OneWayFlight:
    pass

flight1 = OneWayFlight()
flight2 = OneWayFlight()
flight3 = flight1

print("flight1 is: ", flight1, flight1.__dict__)
print("flight2 is: ", flight2, flight2.__dict__)
print("flight3 is: ", flight3, flight3.__dict__)

#Operations on class
#add data to object

flight1.from_location = "new delhi"
flight1.to_location = "mumbai"
flight3.departure_date = "30th july, 2022"
flight1.num_of_travelers = 2
flight3.tarvel_class = "economy"

flight2.from_location = "new delhi"
flight2.to_location = "goa"
flight2.departure_date = "15th aug, 2022"
flight2.num_of_travelers = 1
flight2.tarvel_class = "buisness"
flight2.meal_pref = "veg"

print("flight1 is: ", flight1, flight1.__dict__)
print("flight2 is: ", flight2, flight2.__dict__)
print("flight3 is: ", flight3, flight3.__dict__)

# upadate data in object

flight2.departure_date = "13 oct, 2022"
flight2.meal_pref = "italian"

# read operation

print("flight2 is: ", flight2, flight2.__dict__)

# delete data into object

del flight2.tarvel_class

print("flight1 is: ", flight1, flight1.__dict__)
print("flight3 is: ", flight3, flight3.__dict__)

