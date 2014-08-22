import os
import sys

def charIsLoneWolf(filename):
    if not os.path.isfile(filename):
        print('Given wolfy character ' + filename + ' cannot be found!')
        sys.exit(1)
    return True

def parseEntry(entry):
    # returns char object

def getChar(name):
    # char object
    
    char_filename = name + '.lw'
    if charIsLoneWolf(char_filename):
        with open(char_filename, 'r') as char_file:
            char_history = char_file.read()
            char_file.close()
        char_entries = char_history.split('\n\n') # Entries are
                                                  # seperated by
                                                  # double newline.
        for entry in char_entries:
            parseEntry(entry) # char object equals
        print(char_entries)

        # etc.
