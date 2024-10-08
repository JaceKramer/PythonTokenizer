
# List of symbols
symbols = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '=',
           '+', '-', '*', '/', '&', '|', '~', '<', '>']
# List of reserved words
reserved = ['class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', 'var',
            'static', 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false',
            'null', 'this']
# List of numbers
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-']

# prompts for file name
filename = input('What .jack file do you want to analyze? (CASE SENSITIVE ) (DO NOT INCLUDE .jack)\n')

# opens file
file = open(filename + ".jack")

# copies file text into grab variable
grab = file.read()

# Makes with each item being a line
chop = grab.splitlines()
# print(chop)

# Initialize empty list
chain = []

# Used for looping through chop list
i = 0

for x in chop:
    # Splits current line by spaces
    cut = chop[i].split()
    # checks to see if cut is empty and progresses to next line if true
    if not cut:
        i = i + 1
    # checks the first character of the first item in the cut list to see
    # if the full line is a comment and progresses to next line if true
    elif bool(cut[0][0] == "/" or cut[0][0] == "*"):
        i = i + 1
    # if the current line is not empty or a full line comment then add the
    # line to a new list that will contain only the lines we care about
    else:
        chain += [chop[i]]
        i = i + 1

print(chain)

# Used for looping through chain list
j = 0
# Used for looping through characters in cut list
k = 0
# Used for looping though items in cut list
g = 0
# Collecting strings for output
pantry = "<tokens>\n"
# Collecting strings for string constant
quote = ""
# holds and combines characters in order to output and test
pot = ""
# hold numbers
pan = ""
# used for string constants
stringy = False

# loop to go through entire file
for x in chain:
    # Splits the current line
    cut = chain[j].split()
    print(cut)
    # resets g to 0 to go back to first object in list
    g = 0
    # resets break flag to false
    break_flag = False
    # loop to go through current line/list
    for y in cut:
        # resets k to 0 to reset at the first character in the current string
        k = 0
        # checks to make sure pot is not empty
        if not bool(pot == ""):
            # checks if the string is a keyword
            if pot in reserved:
                pantry = pantry + "    <keyword> " + pot + " </keyword>\n"
                pot = ""
            # if it is not a keyword then it is an identifier
            else:
                pantry = pantry + "    <identifier> " + pot + " </identifier>\n"
                pot = ""
        # loop to go through current string
        for z in cut[g]:
            # prints current character being observed
            print(cut[g][k])
            # if middle of line comment is found, break_flag goes to true which will send to the next line in the file
            if bool(cut[g] == "//"):
                break_flag = True
                break
            else:
                # checks if current character is a symbol
                if cut[g][k] in symbols:
                    # for formatting we need to display the pot before the symbol so
                    # this checks to make sure pot is not empty
                    if not bool(pot == ""):
                        # checks if pot is a keyword
                        if pot in reserved:
                            pantry = pantry + "    <keyword> " + pot + " </keyword>\n"
                            pot = ""
                        # it is an identifier if it is not a keyword
                        else:
                            pantry = pantry + "    <identifier> " + pot + " </identifier>\n"
                            pot = ""

                    pantry = pantry + "    <symbol> " + cut[g][k] + " </symbol>\n"
                    k = k + 1
                    # visual used when running program to make sure it was seeing every symbol
                    print("symbol")
                # if pot is a reserved word and the current character being observed is not a symbol
                elif pot in reserved:
                    pantry = pantry + "    <keyword> " + pot + " </keyword>\n"
                    pot = ""
                # checks if first character of the string is a number
                elif cut[g][0] in numbers:
                    pan = cut[g]
                    # removes all symbols that may get stuck to the end of the number Ex: 1;
                    for d in symbols:
                        pan = pan.replace(d, '')
                    pantry = pantry + "    <integerConstant> " + pan + " </integerConstant>\n"
                    pan = ""
                    k = k + 1
                # checks if the current character is a quotation mark
                elif bool(cut[g][k] == '"'):
                    # stringy gets changed from false to true and the character gets added to the quote variable
                    # essentially gets turned on for first quotation mark found
                    if not stringy:
                        stringy = True
                        quote = quote + cut[g][k]
                        print(quote)
                        k = k + 1
                    # stringy gets changed from true to false and the character gets added to the quote variable
                    # essentially gets turned off for second quotation mark found
                    else:
                        stringy = False
                        quote = quote + cut[g][k]
                        print(quote)
                        k = k + 1
                        pantry = pantry + "    <stringConstant> " + quote + " </stringConstant>\n"
                        quote = ""
                else:
                    # if it is not a string constant, characters get put into normal variable
                    if not stringy:
                        pot = pot + cut[g][k]
                        print(pot)
                        k = k + 1
                    # if it is a string constant, characters get put into special variable
                    else:
                        quote = quote + cut[g][k]
                        print(quote)
                        k = k + 1
        # breaks out of loop if break_flag is true
        if break_flag:
            break
        # iterates loop to move to the next string in current line
        g = g + 1
    # iterates loop to move to the next line
    j = j + 1

pantry = pantry + "</tokens>"

# test output
print(pantry)

with open(filename + "T.xml", 'w') as the_file:
    the_file.write(pantry)
