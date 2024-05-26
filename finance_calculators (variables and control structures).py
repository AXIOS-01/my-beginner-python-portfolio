import math


def choice():
    decision=(input("""
    
    investment - to calculate the amount of interest you'll earn on your investment
    bond - to calculate the amount you'll have to pay on a home loan

    Enter either 'investment' or 'bond' from the menu above to proceed:
    """))

    if decision.lower() == ("investment"):
     investment()
    elif decision.lower() ==  ("bond"):
     bond()
    else:
     print("please pick one of the options")
     choice()

def investment():
    money=(int(input("how much money will you be investing? ")))
    intrest_rt=(int(input("what is the percentage of interest? ")))
    years=(int(input("how many years are you planning to invest? ")))
    interest=(str(input("do you want a simple or a compound interest? ")))

    if interest.lower() == ("simple"):
        a = money * (1 + (intrest_rt/100)*years)
        print ("The amount of interest you will earn on your investment is: "+ str(a))

    elif interest.lower() == ("compound"):
        a2= money * (math.pow(1+(intrest_rt/100),years))
        print (a2)
    else:
        print ("please pick one of the options")
        investment()

def bond():
    hs_value=(int(input("what is the present value of the house? ")))
    intrest_rt=(int(input("what is the percentage of intrest? ")))
    mounths=(int(input("what is the number of mounths you plan to take to repay the bond? ")))
    repayment = ((intrest_rt/12) * hs_value)/(1 - (1 + (intrest_rt/12))**(-mounths))
    print ("the amount you need to repay every month is: " + str(repayment) )


 
choice()