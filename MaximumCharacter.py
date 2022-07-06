#              Author : Melvin M. Flores
#        Date Created : 06 July 2022
#        Program Name : MaximumCharacter.py
# Program Description : Write a solution to find the character that has the highest number of occurrences within a certain string, ignoring case.
#                       If there is more than one character with equal highest occurrences, return the character that appeared first within the string.
#          Input File : none
#         Output File : none
# Program Features    : This application allows user to get the character that has the highest number of occurrences within a certain string


# imported for the string functions
import string

# Imported for determining execution time
import time

# Determine start of execution time
start_time = time.time()


# Get the character that has the highest number of occurrences within a certain string
def get_max_char():

    user_string = input("Enter string: ").lower()
    character_dictionary = {}
    for each in user_string:
        if each in character_dictionary.keys():
            character_dictionary[each] = character_dictionary[each] + 1
        else:
            character_dictionary[each] = 1

    print ("Character that has the highest number of occurrences in the string is '", max (character_dictionary, key=character_dictionary.get), "'")

    quit_program()
                   


# List of menu options 
def menu_options():
    print("\n------------------------------------------------------------")
    print("------ Welcome to the MaximumCharacter Program -------------")
    print("------------------------------------------------------------")
    print("Main Menu - please select an option:")
    print("1.)	Get the character that has the highest number of occurrences within a certain string")
    print("2.)	Quit          ")



# Menu Function
def menu():
   
    global user_input
    quit_switch  = False

    while (quit_switch == False):

        menu_options()
        user_input = input("Enter choice (1, or 2): ")
    
        if user_input == '1':
            get_max_char()
            quit_switch = True
            break

        elif user_input == '2':
            quit_program()
            quit_switch = True
            break
        
        else:
            print('Unknown option-please try again.\n')


# Quit function 
def quit_program():
    print("Thanks for using the MaximumCharacter Program!")

    
# Calling of the main menu
menu()

# Determine end of execution time
end_time = time.time()

# Calculate execution time
exec_time = end_time-start_time

# Displays the program limitation and execution time
print("\nExecution time : {:.2f} minutes".format(exec_time/60))


