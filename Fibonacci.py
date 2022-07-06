#              Author : Melvin M. Flores
#        Date Created : 06 July 2022
#        Program Name : Fibonacci.py
# Program Description : 1. Get the nth number in the fibonacci sequence given n.
#                       2. Alternatively given a number F, print out whether it's a fibonacci number
#                          and what the closest index n in the fibonacci sequence is.
#          Input File : none
#         Output File : none
# Program Features    : 1. This application allows user to get the nth number in the fibonacci sequence.
#                     : 2. This application allows user to determine number F if it is a fibonacci number and its closest index.
# Program Assumption  : 1. The fibonacci sequence starts at zero followed by 1 then 1 then 3 then 5 and so on... (0, 1, 1, 2, 3, 5, ...)
#                     : 2. The fibonacci index starts at 1, and not 0.
# Program Limitation  : 1. If the user enters a character as input either for 'n' or 'F', the program crashes. User must enter an integer as input.
#                     : 2. Maximum value for 'n' is around 511. The program crashes if it exceeds this maximum value.
#                     : 3. If the identified closest index is exactly halfway between two indices, then the lower index is considered as the closest index



#imported for function tools
from functools import lru_cache

# Imported for determining execution time
import time

# Determine start of execution time
start_time = time.time()

@lru_cache(maxsize = 1000)
# Find the closest index
def find_closest_index(number_F, idx):
    lower_index_value = fibonacci_nth_number (idx-1)
    upper_index_value = fibonacci_nth_number (idx)
    lower_difference = number_F - lower_index_value
    upper_difference = upper_index_value - number_F
    if (lower_difference <= upper_difference): 
        return idx-1
    else:
        return idx
    
@lru_cache(maxsize = 1000)
# Compare the number F
def fibonacci_number_F (F):   
    first_term = 0
    second_term = 1
    if F == 0:
        print ("The closest index is '1'")
        return True

    if F == 1:
        print ("The closest index is '2'")
        return True

    third_term = first_term + second_term

    index = 3
    while (third_term < F ):

        #Swap and save values
        first_term = second_term
        second_term = third_term
        third_term = first_term + second_term
        index = index + 1

    if  third_term == F:
        print ("The exact index is '", index, "'")
        return True
    else:
        print ("The closest index is '", find_closest_index(F, index), "'")
        return False
        

@lru_cache(maxsize = 1000)
# Calculate the nth number
def fibonacci_nth_number(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_nth_number(n-1) + fibonacci_nth_number(n-2)        

# Get the nth number in the fibonacci sequence given n
def get_nth_number():
    valid_number = False
    
    while (valid_number == False  ):
        
        nth_number_choice = int(input("Enter nth number: "))

        if  nth_number_choice < 1:
            valid_number = False
            print('Number must be a positive integer. Please try again.\n')
            
        else:
            valid_number = True
            print ("The nth number '", nth_number_choice, "' in the fibonacci sequence is '", fibonacci_nth_number (nth_number_choice), "'")

    quit_program()
                   
# Determine number F, if it is a fibonacci number and get its closest index
def determine_number_F():
    valid_number = False
    
    while (valid_number == False  ):
        
        number_F_choice = int(input("Enter a number F: "))

        if  number_F_choice < 0:
            valid_number = False
            print('Number must either be zero or a positive integer. Please try again.\n')
            
        else:
            valid_number = True
            if fibonacci_number_F (number_F_choice) == True:
                print ("The number F '", number_F_choice, "' IS A fibonacci number.")
            else:
                print ("The number F '", number_F_choice, "' IS NOT A fibonacci number.")


    quit_program()


# List of menu options 
def menu_options():
    print("\n-----------------------------------------------------")
    print("------ Welcome to the Fibonnaci Program -------------")
    print("-----------------------------------------------------")
    print("Main Menu - please select an option:")
    print("1.)	Get the nth number in the fibonacci sequence given n")
    print("2.)	Determine number F, if it is a fibonacci number and get its closest index")
    print("3.)	Quit          ")



# Menu Function
def menu():
   
    global user_input
    quit_switch  = False

    while (quit_switch == False):

        menu_options()
        user_input = input("Enter choice (1, 2, or 3): ")
    
        if user_input == '1':
            get_nth_number()
            quit_switch = True
            break

        elif user_input == '2':
            determine_number_F()
            quit_switch  = True
            break
            
        elif user_input == '3':
            quit_program()
            quit_switch = True
            break
        
        else:
            print('Unknown option-please try again.\n')


# Quit function 
def quit_program():
    print("\nThanks for using the Fibonnaci Program!")

    
# Calling of the main menu
menu()

# Determine end of execution time
end_time = time.time()

# Calculate execution time
exec_time = end_time-start_time

# Displays the program limitation and execution time
print("\nExecution time : {:.2f} minutes".format(exec_time/60))


