swim_time= (int(input("what was your time for the swimming event in minutes? ")))
run_time= (int(input("what was your time for the running event in minutes? ")))
cycle_time= (int(input("waht was your time for the cycling event in minutes? ")))
tot_time=(swim_time + run_time + cycle_time)

print()

print ("your total time was: " + str(tot_time))

if tot_time <= 100:
    print("you have been awarded the Provincial Colours. ")
elif tot_time > 100 and tot_time < 106 :
    print ("you have been awarded the Provincial Half Colours. ")
elif tot_time >= 106 and tot_time < 111:
    print ("you have been awarded the Provincial Scroll. ")
else:
    print ("unfortunatly you dont receive an award. ")

print("""
Time needed for Provincial Colours : 0-100 minutes
Time needed for Provincial Half Colours : 101 - 105 minutes
Time needed for Provincial Scroll :  106 - 110 minutes
No award : 111+ minutes
""")