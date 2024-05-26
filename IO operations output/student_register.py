num_of_student = int(input("how many student are going to be registering? ")) # stores an interger value for the number of times the proceding loop will run

with open('reg_form.txt', 'w') as f:                                          # opens the text file and alows up to write to it
    f.write("\n")                                                              
    for i in range (num_of_student):                                          # ensures the following process happens for the amount of students in the class
        id_num=input("Enter your id number: ")                                # allows student to enter the id number 
        f.write(id_num + "....................." + "\n")                      # writes the id number and adds a dotted line after the number
        f.write("\n")                                                         # adds a new line for less clutter
