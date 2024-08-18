#!/usr/bin/env python

## 2024/08/18. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/08/18 Sunday Puzzle:
## https://www.npr.org/2024/08/17/nx-s1-5075189/sunday-puzzle-rhyming-destinations
# ## That puzzle:
"""
This week's challenge: This week's challenge comes from listener Peter
Collins, of Ann Arbor, Michigan. Think of a famous movie star -- first 
and last names, nine letters in all. The third, fourth, fifth, seventh,
and eighth letters, in order, name a profession. The star's last name
is something that this profession uses. Who is the movie star and what
is the profession?
"""

lexfilename = "resources/10k-lexicon.txt"
actorsfile = "resources/actors_1000_male_and_female.txt"

def get_lex(some_lexicon_filename):
    lexfile = open(some_lexicon_filename, "r")
    lex = lexfile.readlines()
    lexfile.close()
    return lex


def is_word(some_string, lex):
    if some_string in lex:
        word_val = True
    else:
        word_val = False
    return word_val

def main():
    raw_actors = get_lex(actorsfile)
    actors = [l.strip() for l in raw_actors if len(l.strip()) == 10]
    lex = get_lex(lexfilename)
    professionslex = [l.strip() for l in lex if len(l.strip()) == 5]
    for actor in actors:
        astring = "".join(actor.split(" "))
        pstring = astring[2]+astring[3]+astring[4]+astring[6]+astring[7]
        pstring = "".join(pstring).lower()
        if is_word(pstring, professionslex):
            print(actor, "\t", pstring)

if __name__ == '__main__':
    main()
