# CSC 1024 Programming Project
# On-Screen Version of a Master Mind Computer Game
# Written by: Tan Jia Ying (17099516)

# ------------------------------------------------------------------------------------------

# Function 1: Check if user's guess is valid
def guess_validation(guess):

    # List of possible colours
    colours = ['R', 'O', 'Y', 'G', 'B', 'P']

    # Check validity of user's guess
    valid = False
    while valid != True:

        # Check if user's guess is a string
        if guess.isalpha() == False:
            print()
            print('Invalid guess: Your guess must all be letters.')
            valid = False

        else: 
            guess = guess.upper() # Convert user's guess to uppercase

            # Check if user's guess contains 4 letters
            if len(guess) != 4:
                print()
                print('Invalid guess: Your guess must have exactly four letters.')
                valid = False
            # Check if user's guess is in the list of possible colours
            else:
                # Convert user's guess from string to list 
                check_guess = [guess[0], guess[1], guess[2], guess[3]]
                for i in check_guess:
                    if (i not in colours):
                        valid = False
                        print()
                        print('Invalid guess: Your guess must only contain R, O, Y, G, B or P.')
                        break
                    else:
                        valid = True         

        if not valid:
            guess = input('Please try again: ')

    # Return the valid guess to Function 3              
    return check_guess
    
# ------------------------------------------------------------------------------------------

# Function 2: Check how many colours are correct and in the correct position
#           : and how many colours are correct but in the wrong position

def check_colour(guess, code):
    correct_correct = 0 # No. of colours that are correct and in the correct position
    correct_wrong = 0 # No. of colours that are correct but in the wrong position

    # Make a copy of code for manipulation
    code_copy = []
    for i in code:
        code_copy.append(i)

    # Check how many colours are correct and in the correct position
    for j in range(4):
        if guess[j] == code[j]:
            correct_correct += 1
            
    # Check how many colours are correct but in the wrong position
    for k in range(4):
        if guess[k] in code_copy:
            code_copy.remove(guess[k])
    # Total number of letters
    # - No. of colours that are correct and in the correct position
    # - No. of colours in code but not present in guess 
    correct_wrong = 4 - correct_correct - len(code_copy)
         
    # Return feedback to Function 3
    feedback = (correct_correct, correct_wrong)
    return feedback

# ------------------------------------------------------------------------------------------

# Function 3: Start game
def start_game():
    
    # Import the 'random' library to allow computer to generate 4-colour code randomly
    import random

    # Allow user to play again using while loop 
    repeat = 'Y'

    while repeat == 'Y' or repeat == 'y':
        # Inform user that the game has begun  
        print()
        print('        ================================')
        print('                   Game Begins ')
        print('        ================================')
        print()

        # Display list of possible colours to user
        print('List of possible colours:')
        print('R = Red, O = Orange, Y = Yellow, G = Green, B = Blue, P = Purple')
        print()

        # Create list of possible colours
        colours = ['R', 'O', 'Y', 'G', 'B', 'P']

        # Create random 4-colour code
        code = random.choices(colours, k = 4)
        # print(code)

        # Inform user format of code 
        print('Try to guess the 4-colour code.')
        print('Example: RRGB')
        print()
        print('============================================================================')
        print()

        # Prompt user to guess the code
        print('[ Guess No.1 ]')
        guess = input('Enter your guess: ')

        # Call Function 1 to check if guess is valid 
        valid_guess = guess_validation(guess)

        # Check if guess matches 4-colour code
        number = 1 # Initialise number of guesses
        correct = False

        # Save every guess in a list 
        guess_list = []
        correct_correct_list = [] # No. of colours that are correct and in the correct position
        correct_wrong_list = [] # No. of colours that are correct but in the wrong position
            
        while correct != True:
            # If code is guessed correctly
            if valid_guess == code:
                # Convert code from list to string
                code_string = ""
                for i in code:
                    code_string +=  i
                print()
                print('4-colour code: ' + code_string) 
                print("Congratulations! You've managed to guess the 4-colour code! :D")
                print('You took ' + str(number) + ' guess(es).')
            
                # Inform user that game is over
                print()
                print('        ================================')
                print('                   Game Over ')
                print('        ================================')
                print()
                correct = True # break out of while loop
            
            # If guess is incorrect 
            else:
                number += 1
                # Call Functiom 2 to check colour 
                feedback = check_colour(valid_guess, code)
                        
                # Convert guess from list to string
                guess = ""
                for j in valid_guess:
                    guess +=  j
                    
                # Provide feedback to user
                guess_list.append(guess)
                correct_correct_list.append(feedback[0])
                correct_wrong_list.append(feedback[1])
                print()
                print('                       | Correct Colour,   | Correct Colour,  |')
                print('                       | Correct Position  | Wrong Position   |')
                print('---------------------------------------------------------------')
                length = len(guess_list)
                for k in range(length):
                    print('Your guess: ' + str(guess_list[k]) + '       |         ' + str(correct_correct_list[k]) + '         |         ' + str(correct_wrong_list[k]) + '        |')
                    print('---------------------------------------------------------------')
                
                  
                # Prompt user to enter next guess
                print()
                print('============================================================================')
                print()
                print('[ Guess No.' + str(number) + ' ]')
                print('List of possible colours:')
                print('R = Red, O = Orange, Y = Yellow, G = Green, B = Blue, P = Purple')
                new_guess = input('Enter your next guess: ')
                
                # Call Function 1 to check if guess is valid 
                valid_guess = guess_validation(new_guess)

        # Ask user if they want to play again
        print()
        repeat = input('Do you want to play again? [Y/N]: ')

    # If user chooses to not play again
    print()
    print('        ================================')
    print('                 End of Program ')
    print('        ================================')
    
# ------------------------------------------------------------------------------------------

# Function 4: Display instructions to user 
def view_instructions():
    print()
    print('        ================================')
    print('                  Instructions ')
    print('        ================================')
    print()
    print('1) The computer will generate a 4-colour code from a list of possible colours.')
    print('2) List of possible colours: ')
    print('   - R = Red, O = Orange, Y = Yellow, G = Green, B = Blue, P = Purple')
    print('3) Your task is to guess the 4-colour code.')
    print('4) Enter a 4-colour code from the colours listed above, using only the first letter.')
    print('   - Example: RGBP')
    print('5) Colours may also be repeated.')
    print('   - Example: RGBB')
    print('6) After each guess, two feedbacks will be given by the computer.')
    print('   - How many colours are correct and in the correct position')
    print('   - How many colours are correct but in the wrong position')
    print('7) To win the game, your have to enter the 4-color code exactly.')
    print('8) At the end of the game, the computer will tell you how many guesses you took.')
    print('Good luck breaking the code! :)')
    print()

    # Prompt user to start the game
    start = input("Enter 's' to start the game: ")
    
    # Check if user entered 's'
    while start != 's':
        start = input("Incorrect input, enter 's' to start the game: ")

    # Call Function 3 to start the game 
    start_game()

# ------------------------------------------------------------------------------------------

# Main Program

# Display welcome message to user
print()
print('       |================================|')
print('       |     Welcome to MASTER MIND     |')
print('       |================================|')
print('            *** A Computer Game ***')
print()

# Allow user to view instructions or start playing right away 
print('[1] Instructions')
print('[2] Start Game')
selection = input('Enter 1 or 2: ')

# Check if selection is a valid input
valid = False
while valid != True:
    if selection == '1':
        view_instructions()
        valid = True # break out of while loop 
    elif selection == '2':
        start_game()
        valid = True # break out of while loop 
    else:
        print()
        selection = input('Invalid selection, please enter 1 or 2: ')
    


