city_flight={
    "Abu Dhabi_F":150,
    "New York_F": 275,
    "Tokyo_F":300,
    "Paris_F":25,
}

city_hotel={
    "Abu Dhabi_H":30,
    "New York_H": 40,
    "Tokyo_H":20,
    "Paris_H":10,
}

city_rental={
    "Abu Dhabi_R":55,
    "New York_R": 45,
    "Tokyo_R":60,
    "Paris_R":35,
}


chosen_city=str(input("""what city are you planning to go to?
choose between:
-Abu Dhabi
-New york
-Tokyo
-Paris
"""))


city_key=("")
hotle_key=("")
car_key=("")

global hotel_price
hotel_price=()
global plane_price
plane_price=()
global car_price
car_price=()
global tot_cost
tot_cost=()


if chosen_city.lower() == ("abu dhabi"):
    city_key=("Abu Dhabi_F")
    hotle_key=("Abu Dhabi_H")
    car_key=("Abu Dhabi_R")
elif chosen_city.lower() == ("new york"):
    city_key=("New York_F")
    hotle_key=("New York_H")
    car_key=("New York_R")
elif chosen_city.lower() == ("tokyo"):
    city_key=("Tokyo_F")
    hotle_key=("Tokyo_H")
    car_key=("Tokyo_R")
elif chosen_city.lower() == ("paris"):
    city_key=("Paris_F")
    hotle_key=("Paris_H")
    car_key=("Paris_R")


num_nights = int(input("how many nights will you be staying? "))
rental_days = int(input("how many days will you be hiring a car for? "))
print ("\n")

def hotel_cost():
    global hotel_price
    hotel_price = num_nights*city_hotel[hotle_key]
    print ("total hotel cost: " + str(hotel_price))
hotel_cost()

def plane_cost():
    global plane_price
    plane_price = city_flight[city_key]
    print ("total flight cost: " + str(plane_price))
plane_cost()

def car_rental():
    global car_price
    car_price = num_nights*city_rental[car_key]
    print ("total rental car cost: " + str(car_price))
car_rental()

def holiday_cost():
    global tot_cost
    tot_cost = hotel_price + plane_price + car_price
    print("the total cost of your trip adds up to: " + str(tot_cost))

holiday_cost()