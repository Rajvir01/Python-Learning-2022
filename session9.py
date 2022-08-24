class OneWayFlight:

    #constructor

    """
    def __init__(self):
        print("self is: ", self, "type is ", type(self))
        self.from_location = "new delhi"
        self.to_location = "mumbai"
        self.departure_date = "30th july, 2022"
        self.num_of_travellers = 2
        self.travel_class = "economy"
    """
# Now, the previous constructor is no more available to be used
# Further, we do not have Constructor or Function Overloading in Python OOPS

    def __init__(self, from_location = "new delhi", to_location = "mumbai", departue_date = "26th july, 2022", num_of_travellers = 1, travel_class = "economy"):
        print("self is : ", self, "type is ", type(self))
        self.from_location = from_location
        self.to_loaction = to_location
        self.departure_date = departue_date
        self.num_of_travellers = num_of_travellers
        self.travel_class = travel_class

print("class dictionary")
print(OneWayFlight.__dict__)

flight1 = OneWayFlight() #OneWayFlight() -> executes __init__
# flight1.from_location = "New Delhi"
# flight1.to_location = "Bangalore"

flight2 = OneWayFlight()
print("flight2 is ", flight2, "type is: ", type(flight2))

flight3 = OneWayFlight()
flight4 = OneWayFlight()

print("flight1 is: ", flight1, flight1.__dict__)
print("flight2 is: ", flight2, flight2.__dict__)
print("flight3 is: ", flight3, flight3.__dict__)
print("flight4 is: ", flight4, flight4.__dict__)
