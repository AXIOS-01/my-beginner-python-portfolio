average = 0                                                                         # creating a variable to store the average in later
count = 0                                                                           # creating a variable to count the number of times the loop is used and therefore the amount of numbers entered 
numbers = 0                                                                         # creating a variavble for the sum of all numbers entered
user_input = 0                                                                      # stores the users input
                                                                                  
while user_input != -1:                                                             # while the answer is not correct
    user_input=int(input("Enter a number until you find the right number: "))       # ask the user to enter a number
    count = count + 1                                                               # increment count by 1
    numbers = numbers + user_input                                                  # store the users input in the numbers variable
                                                                                    # once the number has been entered the program will break from the the while loop 
count = count - 1                                                                   # remove the last count as the -1 is not involved in the average equasion
numbers += +1                                                                       # +1 to remove the -1 from the average equasion
average=numbers/count                                                               # calculate the average 
print (average)                                                                     # print the average