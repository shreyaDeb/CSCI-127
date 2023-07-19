import string

#--------------------<>--------------------#

class President:
    
    def __init__(self, first, last, number, start_in, term, occupations):
        self.name = str(first) + ' ' + str(last)
        self.num = number
        self.year = start_in
        self.term = term
        self.jobs = occupations
    
    def get_name(self): #Returns president's name
        return self.name.lower()
    
    def get_number(self): #Returns president's number
        return str(self.num)
    
    def get_job(self):  #Returns president's jobs
        return self.jobs
      
    def get_time_in_office(self):  #returns president's term length
        return self.term
    
    def __str__(self):  #Prints president's information in a nice format
        
        if self.num <= 9:
            return ('No. ' + str(self.num) + '  (' + str (self.year) #Adds an extra space if number is a single digit (for alignment)
                    + ') ' + str(self.name))
        else:
            return ('No. ' + str(self.num) + ' (' + str (self.year) 
                    + ') ' + str(self.name))
        
#--------------------<>--------------------#

def print_by_name(listing, name):
    '''Lists all presidents whose name contains the given substring'''
    
    count = 0

    if len(name) < 3:
        print('\nYou must enter at least 3 characters to use this option')

    else:
        print('\n')
        for president in listing:

        
            if name.lower() in president.get_name():
                count += 1
                print(president)
            
        if count == 0:
            print("No president's name contains '" + name + "'")
 

#--------------------<>--------------------#

def print_by_number(listing, number):
   '''Prints president that corresponds to the given number'''
   
   for n in listing:
        if str(number) == n.get_number():
            print('\n' + str(n))
            
   if number < 1 or number > 46:
        print('\nPresident number must be between 1 and 46')
   

#--------------------<>--------------------#

def count_by_occupation(listing, job):
    '''prints the number of presidents who had given occupation and their names'''
    
    count = 0
    presidents = ''
    tracker = []    #Placeholder to keep track of names that have already been added
    
    for work in listing:
       if job in work.get_job():
           if work.get_name() not in tracker:   #So a president won't be counted more than once 
               
               tracker.append(work.get_name())
               presidents += str(work.get_name().title()) + ', '
               count += 1
        
    presidents = presidents[:-2]    #Takes off the last comma and space
    print('\n' + str(count) + ' ' + str(job) + ' presidents: ' + presidents)

#--------------------<>--------------------#

def average_term_length(listing):
    '''Calculates and printsthe average term length'''
    
    bottom = len(listing)
    top = 0
    
    for n in listing:
        x = n.get_time_in_office()
        top += x
        
    average = top/bottom
    round_ave = round(average, 1)
    print('Average term length, about', round_ave, 'years' )
    
#--------------------<>--------------------#    
#--------------------<>--------------------#
#--------------------<>--------------------#

def print_menu():
    print ("""
1. Print all presidents
2. Print president by name
3. Print president by number
4. Count presidents with occupation
5. Print average term length
6. Quit
    """)
# ---------------------------------------

def print_all_presidents(pres_listing):
    
    for president in pres_listing:
        print(president)
    
# ---------------------------------------

def create_pres_listing(filename):
    
    pres_listing = []
    file = open(filename, "r")
    
    for president in file:
        presilist = president.strip().split(",")
        number = int(presilist[0])               # number
        last = presilist[1]                      # last name
        first = presilist[2]                     # first name
        start_in = int(presilist[3])             # first year in office
        term = float(presilist[4])               # years in office
        occupations = []
        
        for position in range(5, len(presilist)):
            occupations += [presilist[position]] # occupation
            
        pres_listing += [President(first, last, number, start_in, term, occupations)]

    file.close()
    return pres_listing

# ---------------------------------------

def get_choice(low, high, message):
    
    legal_choice = False
    answer = input(message)
    
    while answer == "":
        answer = input(message)
        
    for char in answer:
        
        if char not in string.digits:
            print('ERROR: ', answer, "is not a number")
            return 0
        
    answer = int(answer)
    
    if (low > answer) or (answer > high):
        
        print('ERROR: ', answer, "is not a choice")
        return 0

    return answer

# ---------------------------------------

def main():
    
    pres_listing = create_pres_listing("pres_listing.txt")
    choice = 0
    
    while choice != 6:
        
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        
        if choice == 1:    
            print_all_presidents(pres_listing)
            
        elif choice == 2:
            name = input("Enter a president name: ").lower()
            print_by_name(pres_listing, name)
            
        elif choice == 3:
            number = get_choice(1, 46, "Enter a president number: ")
            print_by_number(pres_listing, number)
            
        elif choice == 4:
            occupation = input("Enter a president occupation: ").lower()
            count_by_occupation(pres_listing, occupation)
            
        elif choice == 5:
            average_term_length(pres_listing)
            
        elif choice == 6:
            print("Thank you.  Goodbye!")

# ---------------------------------------

main()
