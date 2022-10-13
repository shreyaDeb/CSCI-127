# Our aim in the lab was to take in user inputs
# Convert those inputs into a list of integers
# Then writing a make_int_list() function that would take in 3 arguments namely the original
    # list from the user, an upper bounds, and lower bounds and then returning a list which
    # only has the integers in the upper and lower bounds inputed.
    # Also the make_int_list() had to be a pure function
                                                         
def main():
    numbers = input("Enter some integers: ").split(" ")
    lowBound = int(input("Lower bound: "))
    highBound = int(input("Upper bound: "))

    print("Original list: " + str(numbers))
    print("Filtered list: " + str(make_int_list(numbers, lowBound, highBound)))



def make_int_list(numbers, lowBound, highBound):
    numbersFiltered = []
    for i in range(len(numbers)):
        if (int(numbers[i]) >= lowBound and int(numbers[i]) <= highBound):
            numbersFiltered.append(numbers[i])
    return numbersFiltered

main()
