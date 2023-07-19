# -*- coding: utf-8 -*-

import numpy as np
import random

class Die:

    def __init__(self, sides):
        """A constructor method to create a die with given number of sides"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

# -------------------------------------------------

class Farkle:

    def __init__(self, sides):
        """A constructor method that can record 6 dice rolls"""
        
        self.rolls = np.zeros(6, dtype=np.int16)
        self.sides = sides
        
    def roll_dice(self):
        """A general method that rolls 6 dice"""
        
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(self.sides).roll()
            

    def count_outcomes(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        
        counts = np.zeros(self.sides + 1, dtype=np.int16)
        for roll in self.rolls:
            counts[roll] += 1
        return counts
        
#--------------------------------------------------

    def is_it_four_of_a_kind(self):
        '''Method to count occurences of rolling a four of a kind'''
        
        count = 0
        x = np.sort(self.rolls) #Sorts dice within roll
        
        if x[0] == x[1] == x[2] == x[3] != x[4]:
            count += 1
            
        elif x[0] != x[1] == x[2] == x[3] == x[4] != x[5]:  
            count += 1
            
        elif x[1] != x[2] == x[3] == x[4] == x[5]:
            count += 1
       
        return count
       
#--------------------<>--------------------#

    def is_it_straight(self):
        '''Method to count occurences of rolling a straight'''
        
        count = 0
        x = np.sort(self.rolls) #Sorts dice within roll
        
        if  x[0] == x[1] - 1 == x[2] - 2 == x[3] - 3 == x[4] - 4 == x[5] - 5:
            count += 1
            
        return count
    
#--------------------<>--------------------#
    
    def is_it_two_triplets(self):
        '''Method to count occurences of rolling two triplets'''
        
        count = 0
        x = np.sort(self.rolls) #Sorts dice within roll
        
        if x[0] == x[1] == x[2] != x[3] == x[4] == x[5]:
            count += 1
            
        return count 
    
# -------------------------------------------------
        
def main(how_many):

    four_of_a_kind = 0
    straight = 0
    two_triplets = 0
    game = Farkle(6)

    for i in range(how_many):
        game.roll_dice()
        
        if game.is_it_four_of_a_kind():
            four_of_a_kind += 1
            
        elif game.is_it_straight():
            straight += 1
            
        elif game.is_it_two_triplets():
            two_triplets += 1

    four_percent = four_of_a_kind/how_many
    straight_percent = straight/how_many
    triplets_percent = two_triplets/how_many
    

    print("Number of Rolls:", how_many)
    print("---------------------")
    
    if four_of_a_kind == 0:
        print("No Four of a Kinds were rolled\n")
        
    else:
        print("Number of Four of a Kinds:", four_of_a_kind)
        print("Apparent Probability: 1 in {:.2f}\n".format(how_many/four_of_a_kind), '(' + str(four_percent) + '%)\n' )
        
    if straight == 0:
        print("No Straights were rolled\n")
        
    else: 
        print("Number of Straights:", straight)
        print("Apparent Probability: 1 in {:.2f}\n".format(how_many/straight), '(' + str(straight_percent) + '%)\n')
    
    if two_triplets == 0:
        print("No Two Triplets were rolled\n")
    
    else:
        print("Number of Two Triplets:", two_triplets)
        print("Apparent Probability: 1 in {:.2f}\n".format(how_many/two_triplets), '(' + str(triplets_percent) + '%)\n')

# -------------------------------------------------

if __name__ == "__main__":
    main(1000)
    main(10000)
    main(20000)
    
    
        
