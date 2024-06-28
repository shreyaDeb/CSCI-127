def average_char(filename):
    file = open(filename, "r")
    chars = 0
    lines = 0

    for line in file:
         lines += 1
         chars += len(line) - 1 # the -1 subtracts off the \n character

    average = chars/lines
    file.close

    return average

def main():
    result = average_char("AEHousman.txt")
    print("Average characters per line is:   ", round(result, 2))

main()
