# Our aim for this Program was as follows:

# Every five of a kind is identified correctly. (All or nothing.)
# Every straight flush is identified correctly. (All or nothing.)
# Every four of a kind is identified correctly. (All or nothing.)
# Every full house is identified correctly. (All or nothing.)
# Every flush is identified correctly. (All or nothing.)
# Every straight is identified correctly. (All or nothing.)
# Every three of a kind is identified correctly. (All or nothing.)
# Every two pair is identified correctly. (All or nothing.)
# Every pair is identified correctly. (All or nothing.)
# Every nothing is identified correctly. (All or nothing.)
# The Python solution is properly commented, easy to understand, high quality and does
    # not contain unnecessary code. (3 points for each type of improvement up to 15 points.)


def get_all_ranks(hand):
    result = []
    for card in hand:
        result.append(card[0])
    return result 

#Defines a hand with 4 cards of the same number and 1 wild card
def five_of_a_kind(hand):
    if(hand[1][0] == hand[2][0] == hand[3][0] == hand[4][0]) and (hand[0][0] == 0): #Since 0 (the value of a joker) is lowest, it will always be the 0th entry in the list
        return True
    
    else:
        return False

#Defines a hand of numerically consecutive cards that have the same suit
def straight_flush(hand):
    if (hand [0][0] == hand[1][0] - 1 == hand[2][0] - 2 == hand[3][0] - 3 == hand[4][0] - 4):
        if (hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]):
            return True
        
        else:
            return False

#Defines a hand of numerically consecutive cards   
def straight(hand):
    if(hand [0][0] == hand[1][0] - 1 == hand[2][0] - 2 == hand[3][0] - 3 == hand[4][0] - 4):
            return True
        
    else:
        return False
    
#Defines a hand of four cards with the same number    
def four_of_a_kind(hand):
    if (hand[0][0] != hand[1][0] == hand[2][0] == hand[3][0] == hand[4][0] ) or (hand[0][0] == hand[1][0] == hand[2][0] == hand[3][0] != hand[4][0]):                                                        
            return True
        
    else:
        return False
    
#Defines a hand of 3 cards of one number and 2 cards of a second number
def full_house(hand):
    if (hand[0][0] == hand[1][0] == hand[2][0] != hand[3][0] == hand[4][0] ) or (hand[0][0] == hand[1][0] != hand[2][0] == hand[3][0] == hand[4][0]):
        return True
    
    else:
        return False
    
#Defines a hand of 5 cards with the same suit
def flush(hand):
    if (hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]):
        return True
    
    else:
        return False
    
#Defines a hand of 3 cards of the same number with two other cards of different numbers   
def three_of_a_kind(hand):
    if (hand[0][0] == hand[1][0] == hand[2][0] != hand[3][0] != hand[4][0] ) or (hand[0][0] != hand[1][0] == hand[2][0] == hand[3][0] != hand[4][0] ) or (hand[0][0] == hand[1][0] == hand[2][0] != hand[3][0] != hand[4][0]):
        return True
    
    else:
        return False
    
#Defines a hand with 2 cards of one number, 2 cards of a second number, and one card with a third number    
def two_pair(hand):
    if(hand[0][0] == hand[1][0] != hand[2][0] == hand[3][0] != hand[4][0]) or(hand[0][0] != hand[1][0] == hand[2][0] != hand[3][0] == hand[4][0]) or (hand[0][0] == hand[1][0] != hand[2][0] != hand[3][0] == hand[4][0]):
        return True
    
    else:
        return False
    
#Defines a hand containing two cards of the same number and 3 cards of different numbers    
def pair(hand):
    if (hand[0][0] == hand[1][0] != hand[2][0] != hand[3][0] != hand[4][0]) or (hand[0][0] != hand[1][0] == hand[2][0] != hand[3][0] != hand[4][0]) or (hand[0][0] != hand[1][0] != hand[2][0] == hand[3][0] != hand[4][0]) or (hand[0][0] != hand[1][0] != hand[2][0] != hand[3][0] == hand[4][0]):
        return True
    
    else:
        return False
    
# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+

def evaluate(poker_hand):
    poker_hand.sort() 
    print(poker_hand, "Poker Hand: ", end="")
    if five_of_a_kind(poker_hand):
        print("Five of a Kind")
    elif straight_flush(poker_hand):
        print("Straight Flush")
    elif four_of_a_kind(poker_hand):
        print("Four of a Kind")
    elif full_house(poker_hand):
        print("Full House")
    elif flush(poker_hand):
        print("Flush")
    elif straight(poker_hand):
        print("Straight")
    elif three_of_a_kind(poker_hand):
        print("Three of a Kind")
    elif two_pair(poker_hand):
        print("Two Pair")
    elif pair(poker_hand):
        print("One Pair")
    else:
        print("Nothing") # Can only beat another hand with nothing. (High card wins)
		
# -----------------------------------------+

def main():
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14 
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    evaluate([[2, "♠"], [7, "♣"], [8, "♦"], [A, "♦"], [Q, "♥"]])    # High card
    evaluate([[T, "♠"], [Q, "♣"], [6, "♦"], [9, "♦"], [Q, "♥"]])    # One pair
    evaluate([[T, "♠"], [9, "♣"], [6, "♦"], [9, "♦"], [6, "♥"]])    # Two pair
    evaluate([[K, "♦"], [7, "♣"], [7, "♥"], [8, "♣"], [7, "♠"]])    # Three of a kind
    evaluate([[T, "♣"], [9, "♣"], [6, "♣"], [7, "♣"], [8, "♠"]])    # Straight
    evaluate([[2, "♥"], [9, "♥"], [3, "♥"], [6, "♥"], [T, "♥"]])    # Flush
    evaluate([[8, "♦"], [7, "♣"], [8, "♥"], [8, "♣"], [7, "♠"]])    # Full house
    evaluate([[2, "♦"], [7, "♣"], [2, "♥"], [2, "♣"], [2, "♠"]])    # Four of a kind
    evaluate([[T, "♣"], [9, "♣"], [6, "♣"], [7, "♣"], [8, "♣"]])    # Straight flush    
    evaluate([[7, "♥"], [0, "?"], [7, "♦"], [7, "♣"], [7, "♠"]])    # 5 of a kind ([0, "?"] is the Joker)



main()
