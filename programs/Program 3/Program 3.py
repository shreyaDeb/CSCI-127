def list_sectors(file):
    print('GICS Sectors in the S&P 500'.center(60, '-'))
    sp500 = open(file, 'r', errors = 'ignore')
    sp500.readline()
    sectors = []
    num = 1

    for line in sp500:
        listing = line.split(',')
        
        if listing[2] not in sectors:
            sectors.append(listing[2])

    sp500.close()
    sectors.sort() 
    for sector in sectors:  #Creates numbered list of sectors
        print(str(num) + '. ' + sector)
        num += 1

    print(''.center(60, '-'))
    return sectors

#--------------------<>--------------------#

def get_user_choices(sector):
    num = int(input("Please enter a number: "))
    
    if 0 < num < 12:    #Pulls the corresponding sector from sectors
        return sector[num - 1]
    
    else:
        while num < 0 or num > 11:  #Promtps user for a valid number
            num = int(input("Please enter a valid number (1-11): "))
            
        return sector[num-1]

#--------------------<>--------------------#

def get_securities_in_sector(file, sector):
    f = open(file, 'r', errors = 'ignore')
    book = f.readlines()
    x = len(book)
    info = []
    lists = []
    
    for entry in range(0, x):   #Creates list of the categories
        seperated = book[entry].split(',')
        info.append(seperated)

    
    for entry in info:
        
        if entry[2] == sector:  #Adds information to each tuple
            lists.append(entry[0])
            lists.append(entry[1])
            lists.append(entry[3])

    final = [tuple(lists[i:i + 3])for i in range(0, len(lists), 3)] #Creates the necessary number of tuples
    
    return final
    file.close()
    
#--------------------<>--------------------#
    
def generate_report(securities, sector):
    
    y = 0
    finish = ''
    
    for entry in securities:
        y += 1

        if y <= 9:  #Adds an extra space for single digits to make things look nicer
            fin = (str(y) + '.  ' + entry[0].ljust(7) + entry[1].ljust(50, '.') + entry[2]).format('.') + '\n'
            finish += fin
            
        else:
            fin = (str(y) + '. ' + entry[0].ljust(7) + entry[1].ljust(50, '.') + entry[2]).format('.') + '\n'
            finish += fin

    print(finish)
               
    choice = input('Save Report? ').lower()
     
    if choice[0] == 'y':    #Saves the file if y
        file = input("Enter file name: ")
        write = open(file, 'w')
        write.write(finish)
        write.close()
        print('Your file has been saved!')

    else:
        print('Your file has been discarded.')
   
#--------------------<>--------------------#


def main(file):
    sectors = list_sectors(file)
    sector = get_user_choices(sectors)
    securities = get_securities_in_sector(file, sector)
    generate_report(securities, sector)

main('sp500.csv')
