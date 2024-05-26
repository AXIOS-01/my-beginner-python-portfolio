#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~created a function to alternate words in a sentance~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def alternate_words():
    new_sen=""                                            # created a variable that will store the alternated sentance
    sen=str(input("enter a sentenece: "))                 # asks user to enter a sentance
    [sen_list]=[sen.split()]                              # formats the sentance into a list spliting it up between words
    sen_list_len=len(sen_list)                            # gets the length of the sentance list in other words the amount of words in the sentance (starting from 0)
    global user_input                                     # defines a global variable called user input to be used for making the sentace out of alternating letters and words of the same input as the first and can keep it global as its only going to be used in either splitting words or the letters and then in the W_and_L function after.
    user_input=sen                                        # takes the input of the user and stores it in the global variable user_input
    for i in range (sen_list_len):                        # loops through the number of words in the list starting at 0
      if i % 2 == 0:                                      # this if statment allows me to go through the list of words making one uppercase and the next lower case
        new_sen = new_sen + sen_list[i].upper() + (" ")   # adds the upper case word to the empty variable
      else:                                               #
        new_sen = new_sen + sen_list[i].lower() + (" ")   # adds the lower case to the empty variable
    print (new_sen)                                       # prints the new sentance
    W_and_L()                                             # runs words and letters function

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~creates a function to alternate letters~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def alternate_letters():                                                    
    new_word=""                                           # created a variable that will store the alternated sentance
    word=str(input("enter a sentance: "))                 # asks user to enter a sentance
    word_len=len(word)                                    # gets the length of the sentance
    global user_input                                     # global variable from earlier
    user_input = word                                     # stores the sentance in the global variable
    for i in range (word_len):                            # for every letter in the sentance
      if i % 2 == 0:                                      # 
          new_word = new_word + word[i].upper()           # make it upper case
      else:                                               # 
         new_word = new_word + word[i].lower()            # make it lower case
    print (new_word)                                      # print the new sentance
    W_and_L()                                             # run the W_and_L function


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~this fucntion allows you to choose if you want to alternate letters or words by running the relavant function~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def decision():                                                  
    choice=input("do you want to alternate letters or words? answer with letters or words: ")
    print("\n")
    if choice.lower() == ("letters"):
        alternate_letters()
    elif choice.lower() == ("words"):
        alternate_words()
    else:
        print("that is not an option")
        decision()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~this function alternates letters and words and is run reguardless of the choice previous of the user~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def W_and_L():
    global user_input 
    user_input=str(user_input)                                            # takes the users previous input
    [user_split]=[user_input.split()]                                     # splits it up by the words into a list
    user_len=len(user_split)                                              # stores the lenght of the list into a variable
    alt_word=""                                                           # creates an empty varibale for the alternating letters
    new_word2=""                                                          # creates an empty variale for the final letter
    for i in range (user_len):                                            # for every word in the list
        if i % 2 == 0:                                                    # alternarte between the words
            new_word2=new_word2+user_split[i].lower() + (" ")             # make selected word forced lower case
        else:                                                             # to the next word
            alt_word = user_split[i]                                      # store the next word in this variable
            new_alt_word=""                                               # empty variable for the alternating version of the word
            alt_len=len(alt_word)                                         # get the length of the word
            for x in range (alt_len):                                     # for every letter in the word
                if x % 2 == 0:                                            # alternate between them
                    new_alt_word=new_alt_word+alt_word[x].upper()         # make one uppercase and save it to the empty variable 
                else:
                    new_alt_word=new_alt_word+alt_word[x].lower()         # make the next one lower case and save it to the empty variable
            new_word2 = new_word2 + new_alt_word + (" ")                  # add the alternated letter word to the variable holding the whole sentance
    print ("\n") 
    print("this is your sentance with alternating letters and words: ")
    print (new_word2)                                                     # print the final sentance


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Finally run the program that starts it all~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
decision()