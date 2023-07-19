#--------------------<>--------------------#
#Since it is a csv (COMMA seperated values) file, each entry is seperated 
#by a comma, meaning it would interpret that line as having three parts instead of two
#--------------------<>--------------------#

def create_dictionary(file): 
    y = open(file, 'r') #opens file
    book = y.readlines()
    
    mydict = {} #Starting parameters
    terms = []
    values = []
    x = len(book)-1


    for entry in range(x):
        value = book[entry][0:8]    #Seperates binary code
        term = book[entry][9:-1]    #Seperates character
        
    
        if term == 'space': #Changes words to characters
            term = ' '

        elif term == 'comma':
            term = ','

        elif term == 'quote':
            term = '"'
            
        terms.append(term)  #Adds variables to empty lists
        values.append(value)

        
    for n in terms: #Puts lists into a dictionary
        for x in values:
            mydict[n] = x
            values.remove(x)
            break

    
    y.close()
    
    return mydict

#--------------------<>--------------------#
    
def translate(sent, mydict, file): 
    char = [*sent]    #Seperates sentence into list of characters
    x = len(char) - 1
    output = ''
    
         
    for letter in sent:
        
        if letter in mydict:    #Adds corresponding code to string if present in mydict
            output += mydict[letter]
            
        else:
            output += '\nUNDEFINED\n'
            

    write = open(file, 'w')     #Writes translation in a file
    write.write(output)
    write.close()
    

#--------------------<>--------------------#
    
def main():
    dictionary = create_dictionary("ascii-codes.csv")
    sentence = "A long time ago in a galaxy far, far away..."
    translate(sentence, dictionary, "output-1.txt")
    sentence = "Montana State University (406) 994-0211"
    translate(sentence, dictionary, "output-2.txt")
    sentence = "“True friends stab you in the front.” —Wilde"
    translate(sentence, dictionary, "output-3.txt")

#--------------------<>--------------------#

main()
