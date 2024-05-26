menu=["coffee", "cake", "sandwich","tea"]

stock={
    "coffee":100,
    "cake":10,
    "sandwich":100,
    "tea":200,
    }
price={
    "coffee":5,
    "cake":3,
    "sandwich":5,
    "tea":3,
    }

val=0
tot_val=0

for i in menu:
    val = stock[i] * price[i]
    tot_val = tot_val + val


print ("Total stock value: £" + str(tot_val))