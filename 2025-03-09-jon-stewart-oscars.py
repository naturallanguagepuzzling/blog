#!/usr/bin/env python

## 2025/03/09. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2025/03/09 Sunday Puzzle:
## https://www.npr.
## That puzzle:

"""
This week's challenge comes from listener Al Gori, of Cozy Lake, N.J.
Take the name JON STEWART, as in the comedian and TV host. Rearrange the
letters to spell the titles of three classic movies. One of the titles is
its familiar shortened form.
"""

import re
import logging
import itertools

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

oscarsfile = open('resources/oscars_titles.txt', 'r')
oscars = oscarsfile.readlines()
oscars = [x.strip() for x in oscars if not x.startswith('#')]
target = ['a', 'e', 'j', 'n', 'o', 'r', 's', 't', 't', 'w'] # 'jon stewart'


def get_letter_list(mystring):
    ms = re.sub(r'[^a-zA-Z]', '', mystring)
    ms = ms.lower()
    ms = list(ms)
    ms.sort()
    return ms

def get_candidate_titles(movielist):
    shorttitles = []
    for m in movielist:
        if 1 <= len(re.sub(r'[^a-zA-Z]', '', m)) <= 6: ## 10 letters total for 3 movies, so each title should be 2-6 letters
            shorttitles.append(m)
    return shorttitles

def get_combos(movielist):
    allcombos = itertools.combinations(movielist, 3)
    return allcombos

def main():
    shortlist = get_candidate_titles(oscars)
    mycombos = get_combos(shortlist)
    for mc in mycombos:
        cstring = ''.join(mc)
        cstring = get_letter_list(cstring)
        if cstring == target:
            print(mc)

if __name__ == '__main__':
    main()

