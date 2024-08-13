#!/usr/bin/env python

## 2024/08/12. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/05/05 Sunday Puzzle:
## https://www.npr.org/2024/08/10/nx-s1-5068349/sunday-puzzle-this-puzzle-is-as-easy-as-1-2-3
# ## That puzzle:
"""
This week's challenge: This week's challenge comes from listener Greg 
VanMechelen, of Berkeley, Calif. Think of a popular food item in six letters.
Change the last two letters to a K to make a common five-letter word in which
none of the letters are pronounced the same as in the six-letter food. What
food is this?
"""

lexfilename = "resources/10k-lexicon.txt"
foodlexfilename = "resources/foods.txt"

def get_lex(some_lexicon_filename):
    lexfile = open(some_lexicon_filename, "r")
    lex = lexfile.readlines()
    lexfile.close()
    return lex

def change_letters(sixer):
    fiver = sixer[:4]+'k'
    return fiver

def is_word(some_string, lex):
    if some_string in lex:
        word_val = True
    else:
        word_val = False
    return word_val

def main():
    foodlex = get_lex(foodlexfilename)
    foodlex = [l.strip() for l in foodlex if len(l.strip()) == 6]
    lex = get_lex(lexfilename)
    lex = [l.strip() for l in lex if len(l.strip()) == 5]
    for food in foodlex:
        transformed = change_letters(food)
        if is_word(transformed, lex):
            print(food, "\t", transformed)

if __name__ == '__main__':
    main()
