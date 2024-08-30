#!/usr/bin/env python

## 2024/08/27. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/08/25 Sunday Puzzle:
## https://www.npr.org/2024/08/24/nx-s1-5086401/sunday-puzzle-two-of-the-same
## That puzzle:

"""
This week's challenge: This week's challenge comes from listener Lillian
Range, of New Orleans. The word NONUNION has four N's and no other consonant.
What famous American of the past -- first and last names, 8 letters in all --
has four instances of the same consonant and no other consonant?
"""

famous_people_file = "resources/10k-famous-people.txt"

def get_lex(some_lexicon_filename):
    lexfile = open(some_lexicon_filename, "r")
    lexlines = lexfile.readlines()
    lex = [l.strip() for l in lexlines]
    lexfile.close()
    return lex

def is_consonant(char):
    vowels = "aeiouyAEIOUY"
    return char.isalpha() and char not in vowels

def get_consonants(string):
    consonants = [char for char in string if is_consonant(char)]
    return consonants

def main():
    famous = get_lex(famous_people_file)
    famous_eights = [f for f in famous if len(f.replace(" ", ""))==8]
    for fe in famous_eights:
        fe_cons = get_consonants(fe)
        if len(fe_cons) == 4 and len(set(fe_cons)) == 1:
            print(fe)

if __name__ == '__main__':
    main()
