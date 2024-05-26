names=[]
dates=[]

with open('DOB.txt', 'r+') as file: # opens the text file containing the names and dates of birth of the individules.
    for line in file:               # for every line in the text file,
        splits=line.split()         # split every the text by every line.
        names+=splits[0:2]          # stores the first two words of the line in this list.
        dates+=splits[2:5]          # stores the last three words of the line in this list.
        
count=0
print ("Names:")      
while count != 1:                    
    print (" ".join(names[0:2]))    # it joins the first two names on the list and adds a space between the selected names and prints them.
    names.pop(0)                    # removes the name at the begining of the list that has been used.
    names.pop(0)                    # removes the second name that as been used.
    if len(names) == 0:             # when the length of the list has is equal to 0 then increment the count, which will end the loop.
        count = count + 1           

print ("\n")

count=0
print ("Dates of birth:")
while count != 1:
    print (" ".join(dates[0:3]))    # repeats the same process as the one listed above for the dates of birth.
    dates.pop(0)
    dates.pop(0)
    dates.pop(0)
    if len(dates) == 0:
        count = count + 1