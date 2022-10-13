# Our aim in this lab was to code based on the input the user would put
# If the input was M then it would print the menu all over again
# If the input was E then we would assign the input to the variable string to the 
# If the input was R then we would look at the varibale string, if it has string assigned from E then we
    # would randomly choose a reandom letter and tell it's postion, otherwise if the string is empty then
    #we would just select a random letter and assign it a random postion.
# If the input was Q then it would Quit the program
# This program will keep asking for inputs until Q is inputed
# Any other choice made would print an error message and ask for the input again



import random
import string

def main(): 
    menu = '''
Thank you for running Lab Assignment 3
Please read carefully as our menu options may have changed:

Please press:
'E' - to enter a different string of text
'R' - to randomly choose a letter from the text
'M' - to repeat this menu again
'Q' - to quit this program

Current string:
012345....10...15...20...25...30...
↓↓↓↓↓↓↓↓↓↓↓    ↓    ↓    ↓    ↓'''
    current_string = "The quick red fox jumps over the lazy brown dog."
    def print_random_letter(current_string):
        i = random.randint(0, len(current_string))
        random_letter = current_string[i]
        if random_letter.isalpha():
            print("Randomly chose the ", random_letter, "at index ", i)
        else:
            print("Error: The string currently has no letters in it.")

    print(menu)
    print(current_string)
    print()
    over = False
    while(not over):
        x = input("Enter your choice: ").upper()
        while (x != 'E') and (x != 'R') and (x != 'M') and (x != 'Q'):
            x = input("You must enter E, C, R, or Q: ").upper()
        if x == 'E':
            current_string = input("Enter the new string: ")
            print("Current string set to: ", current_string)
        elif x == 'R':
            print_random_letter(current_string)
        elif x == 'M':
            print(menu)
            print(current_string)
            print()
        else:
            over = True
            print("Goodbye.")
        
main()
