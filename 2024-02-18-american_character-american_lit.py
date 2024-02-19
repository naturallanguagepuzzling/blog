#!/usr/bin/env python


## 2024/02/19. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/02/18 Sunday Puzzle:
## https://www.npr.org/2024/02/18/1232027200/sunday-puzzle-p-is-for-president

"""
This week's challenge: It comes to us from listener Andrew Chaikin of San 
Francisco, also known as the singer Kid Beyond. Think of a famous character
in American literature. Change each letter in that character's name to its
position in the alphabet — A=1, B=2, etc. — to get a famous year in American
history. Who is this person and what is the year?
"""

import string

## Asked ChatGPT to give me a list of famous characters from American literature
## Obviously some of these aren't even American (Don Quixote, Sherlock Holmes)
lit_chars = ['Atticus Finch', 'Captain Ahab', 'Celie', 'Daisy Buchanan',
    'Don Quixote', 'Elizabeth Bennet', 'Hester Prynne', 'Holden Caulfield', 
    'Huckleberry Finn', 'Ishmael', 'James Bond', 'Jane Eyre', 'Jay Gatsby', 
    'Jo March', 'Lisbeth Salander', 'Nick Carraway', 'Randle McMurphy', 
    'Roland Deschain', 'Scarlett OHara', 'Scout Finch', 
    'Sherlock Holmes', 'Tom Sawyer', 'Willy Loman']

## function to transform a string into digits
def letter_to_number(text):
    alphabet = string.ascii_lowercase
    # generate a list of digits for each letter
    # all lowercase, use ord function to get ASCII value
    # subtract 96 (because 'a' is ASCII 97)
    positions = [str(ord(char) - 96) if char in alphabet else char for char in text.lower()]
    return ''.join(positions)

def main():
    for lc in lit_chars:
        lc_tokens = lc.split()
        for lct in lc_tokens:
            if len(lct) not in range(2,5):
                pass
            else:
                numstring = letter_to_number(lct)
                if len(numstring) != 4:
                    pass
                else:
                    if int(numstring) not in range(1492,2024):
                        pass
                    else:
                        print(lc, "/", lct, "/", numstring)
                           
if __name__ == "__main__":
    main()
