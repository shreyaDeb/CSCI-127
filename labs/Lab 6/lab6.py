# Our aim in this lab was as the following:

# First function: get_list_from_file
# opening census_data file for reading, and assigning the file to a variable
# looping through each line in the file...
# splitting name and population into a list (ie: a state), and adding that state to the list of states

# Second function: get_listing_in_range
# the count variable is correct integer
# the listing variable contains the correct data
# order is correct: states are printed from lowest population to highest
# string formatting is correct: (-- see transcript, and also hints below)
    # tab character,
    # state left justified on a field of 20 characters,
    # population of state, 
    # newline character
    # float rounding is correct (population given as a number of millions rounded to 2 decimal places -- see transcript), 
# the function is pure

# Third function: validate_input
# that function should collect the user input rather than the capturing it directly in main. The function should:
# verify that the lower bound is less than the upper bound:
# return a list [lower, upper] if the input is valid (or -1 point)
# print "Invalid input: Swapping upper and lower bounds." if the input is not valid, and return [upper, lower] (or -1 point)
# use the result from validate_input to initialize the lo and hi variables (or -1 point)


def get_list_from_file(census_data):
    file = open(census_data, 'r')       
    states = [] 
    for line in file:                   
        state = line.split()            
        states += [state]               
    file.close()
    return states

def get_listing_in_range(lower, upper, state_list):
    listing = ""
    count = 0
    all_states = state_list[:]
    all_states.reverse()
    for state in all_states:
        population = int(state[1])/1000000
        if (lower < population < upper):
            count += 1
            listing += '\t' + state[0].ljust(20) + str(round(population, 2)) + '\n'
    print('\n', count, "States have a population between", lower, "and", upper, "million.")
    return listing

def validate_input():
    lower = float(input("Enter lower bound: "))
    upper = float(input("Enter upper bound: "))
    if lower > upper:
        print("Invalid input: Swapping upper and lower bounds.")
        return [upper, lower]
    else:
        return [lower, upper]
    
def main():
    states = get_list_from_file("census2020.txt")
    print("\n ***first state in list:", states[0][0], '*** \n')

    print("The least populous U.S. state: Wyoming with just over 0.5 million")
    print("The most populous U.S. state: California with almost 40 million")
    print("Enter two numbers between 0.5 and 40 to list states in that range.")
    result = validate_input() ;
    lo = result[0]
    hi = result[1]
    
    listing = get_listing_in_range(lo, hi, states)
    print(listing)
    print("\n ***first state in list:", states[0][0], '*** \n')

main()
