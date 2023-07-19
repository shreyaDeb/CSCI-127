import random

class Wordle:
    

    def __init__(self, letters_in_word, file_of_words):
        self.num_letters = letters_in_word
        self.word_list = open(file_of_words, 'r').read().upper().splitlines()
        self.answer = self.word_list[random.randint(0, len(self.word_list)-1)]
        self.cheat_code = "?"
        self.test_code = "!"
        self.turn_num = 0
        

    def change_answer(self, new_answer):
        self.answer = new_answer.upper()
        
#--------------------<>--------------------#

    def get_player_guess(self):
        
        self.turn_num += 1
        user_word = input("Enter your " + str(self.num_letters) + " letter guess: ").upper()
        
        
        if(user_word == self.cheat_code):
            self.turn_num -= 1
            print("\tPsst. Answer is", self.answer)
            user_word = self.get_player_guess()
            
            
        if(user_word == self.test_code):
            self.turn_num -= 1
            new_answer = input("\tOkay. Enter the new answer: ").upper()
            while new_answer not in self.word_list:
                new_answer = input("\tEnter a valid " + str(self.num_letters) + " letter word: ").upper()
            self.change_answer(new_answer)
            print("\tAnswer set to " + new_answer.upper())
            user_word = self.get_player_guess()
      
            
        if user_word not in self.word_list:
            self.turn_num -= 1
            user_word = '     '     #So that a guess not contained in the word list will not be displayed
            print('\nERROR: The word you entered is not in the word list')
            print('Please enter a valid word')
    
    
        if len(user_word) == self.num_letters:  #If word is correct length then continue
            return user_word
   
        elif len(user_word) <= self.num_letters:    #If word is too short display message and discount attempt
            self.turn_num -= 1
            print('ERROR: Your guess contains too few characters')
            
        elif len(user_word) >= self.num_letters:    #If word is too short display message and discount attempt
            self.turn_num -= 1
            print('ERROR: Your guess contains too many characters')
        
        
        return (user_word.upper())
  
#--------------------<>--------------------#

    def generate_hint(self, guess):
        print('\n\t' + guess)
        hint = ""
        
        
        if(guess == self.answer): #Ends game if word is guessed
            return guess 
        
        
        if len(guess) == len(self.answer):
            if guess in self.word_list:
                for x in range(self.num_letters):
                    
                    if guess[x] == self.answer[x]:  #Displays a letter in the correct position
                        hint += guess[x].upper()
                
                    elif guess[x] in self.answer:   #Displays a letter in incorrect position but still in word
                        hint += guess[x].lower()
                
                    elif guess[x] not in self.answer:   #Displays a dash if letter is not in word
                        hint += '-'
 
    
        return(hint)
    
#--------------------<>--------------------#

def main(file):
    
    game = Wordle(5, file)
    print("\nWelcome to WORDLE!\n")
    guess = ""
    while(guess != game.answer and game.turn_num < 6 ):
        print(game.turn_num +1, end='. ')
        guess = game.get_player_guess()
        print('\t'+ game.generate_hint(guess) + '\n')
        
        
        if guess == game.answer:    #Displays messages based on number of attempts
        
            if game.turn_num == 1:
                print("Wow! You're either very lucky, or you got some insider information.")
                
            elif 1 < game.turn_num < 6:
                print("GREAT! You got it in " + str(game.turn_num) + " tries.")
                
            elif game.turn_num == 6:
                print("Phew! You got it on the last try!")
                
                
        if guess != game.answer and game.turn_num == 6:
            x = input('Game over. Reveal answer? y/n: ').lower()
        
            if x == 'y':    #Prints answer if user chooses
                print('\nAnswer was: ' + game.answer + '\n')
        

    print("\nThanks for playing!\n")
    
#--------------------<>--------------------#
    
if __name__ == "__main__":
    main("knuth5letterwords.csv")
