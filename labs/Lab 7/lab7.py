# Our aim for this lab was as follows:
#The program prompts the user again if they input a string that is not in a key in
    # the drinks dictionary
# Support upper/lower case input
# Add the drink to the order and add the price to the total
# Get out of the while loop if the user writes 'no' when prompted for whether they'd like another drink (see transcript)
# Print the drink order and total price to the console window (see transcript)
# Print the price with exactly 2 decimal places
# If the customer orders an extra shot, ask how many and sum the correct total to the bill (or -1)

def main():
    menu = '''
    ***** MENU *****
    Brewed     $2.75
    Americano   3.25
    Cappuccino  3.50
    Latte       4.00
    Extra shot  0.75
    *****************
    '''
    drinks = { 'brewed':2.75, 'americano':3.25, 'cappuccino':3.50, 'latte':4.00, 'extra shot':0.75 }
    print(menu)
    
    order = []
    x = 0.00
    total = 0.00
    coffee = (input("What would you like to order? ")).lower()
    while coffee != "no":
        if coffee in drinks:
            x = drinks.get(coffee)
            total = total + x
            order.append(coffee)
        else:
            coffee = (input("That is not a drink to order, what would you like to order? ")).lower()
        coffee = (input("Would you like to order anything else? ")).lower()
            
    print("Great! Your order is::")
    ord = 1
    for i in order:
        print(ord, " - ", i, '\t' , x)
        ord += 1
    print("Your total is: ", '\t', "$",(format(total, ".2f")))

main()
