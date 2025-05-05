#!/usr/bin/env python

## 2025/04/10. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2025/04/06 Sunday Puzzle:
## https://www.npr.org/2025/04/05/nx-s1-5344989/sunday-puzzle-whats-that-familiar-phrase
## That puzzle:

"""
This week's challenge comes from Andrew Tuite, of Chicago. There are four
countries whose names have one-syllable anagrams that rhyme with "Spain."
What are they?
"""

from itertools import permutations
from nltk.corpus import cmudict

prondict = cmudict.dict()

def filter_chars(wd):
    wd = wd.replace('-', '')
    wd = wd.replace(' ', '')
    wd = wd.replace("'", "")
    wd = wd.lower()
    return wd

with open('./resources/countries.txt', 'r') as cfile:
    countries = cfile.readlines()
countries = [c.strip() for c in countries]
countries = [filter_chars(c) for c in countries]
countries = [c for c in countries if len(c) <= 7]
countries = [c for c in countries if 'n' in c] ## vowels can vary but n is a must

def get_anagrams(word):
    perms = [''.join(p) for p in permutations(word)]
    perms = list(set(perms))
    perms = [p for p in perms if p != word] ## because must be an anagram
    perms = [p for p in perms if p in prondict]
    return perms


def main():
    # for c in countries:
    #     print(c)
    for c in countries:
        ccands = get_anagrams(c)
        for cc in ccands:
            ccpron = ' '.join(prondict[cc][0])
            ccpron = ccpron.replace('0', '')
            ccpron = ccpron.replace('1', '')
            ccpron = ccpron.replace('2', '')
            if ccpron.endswith('EY N'):
                print(f'  {c}')
                print(f'  {cc} {ccpron}')
                print('\n')

if __name__ == '__main__':
    main()

