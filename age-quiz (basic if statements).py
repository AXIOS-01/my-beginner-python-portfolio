user_age=int(input("What is your age? "))

if user_age > 100:
    print ("sorry, your dead")
elif user_age >= 65:
    print ("Enjoy you're retirement!")
elif user_age >= 40:
    print ("you're over the hill.")
elif user_age == 21:
    print ("Congrats on your 21!")
elif user_age < 13:
    print ("you qualify for the kiddie discount")
else:
    print ("age is just a number")