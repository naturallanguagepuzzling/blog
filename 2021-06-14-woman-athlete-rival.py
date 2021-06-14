#!/usr/bin/env python


## 2021/06/15. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/05/30 Sunday Puzzle:
## https://www.npr.org/2021/06/13/1005890820/sunday-puzzle-7-famous-letters
## That puzzle:
"""
This week's challenge comes from listener Sandy Weisz, of Chicago. Name a
famous woman in American history with a three-part name. Change one letter in
her first name to a double letter. The resulting first and second parts of her
name form the first and last names of a famous athlete. And the last part of
the woman's name is a major rival of that athlete. Who are these people?
"""

import string
from slugify import slugify

## A very non-comprehensive list of women from American history with 3 names
women_list = [
    'Lady Deborah Moody', 'Anne Marbury Hutchinson', 'Harriet Beecher Stowe',
    'Elizabeth Cady Stanton', 'Susan B. Anthony', 'Susan Brownell Anthony',
    'Mary Baker Eddy', 'Louisa May Alcott', 'Mary Harris Jones',
    'Frances Elizabeth Willard', 'Carry A. Nation', 'Carry Amelia Nation',
    'Pearl S. Buck', 'Pearl Sydenstricker Buck', 'Lady Bird Johnson',
    'Nancy Davis Reagan', 'Jacqueline Kennedy Onassis', 'Coretta Scott King',
    'Ruth Bader Ginsburg', 'Marian Wright Edelman'
    ]

## You can use the text file list of athletes I've prepared; download it from
## GitHub and store it as I have:
athletes_file = 'resources/athletes.txt'


## clean up each name to suit this puzzle: strip (leading/trailing whitespace),
## replace hyphens with spaces, slugify (convert to ASCII), remove any non-letters
def clean_name(somename):
    s = somename.strip()
    s = somename.replace(".", "")
    s = somename.replace("-", " ")
    snames = s.split(" ")
    cl = []
    for sn in snames:
        cn = slugify(sn)
        cn = "".join([l.lower() for l in cn if l.isalpha()])
        cl.append(cn)
    cleaned = " ".join(cl)
    return cleaned


## for a string (name), iterate through each position (letter), replace with all
## possible double letters: anna --> aanna, bbnna, ccnna, ... annaa, annbb, .. annzz
def expand_name(mls, onm):
    expanded = []
    for i in range(0, len(onm)):
        for letter in mls:
            expanded.append(onm[0:i]+letter+letter+onm[i+1:])
    return expanded
    

## iterate through women's names, expand each first name into candidates;
## iterate through candidate first names, combine with second name, then iterate
## through athlete names and check if candidate (first+second) name matches
def solve_puzzle(mls, wns, ans):
    for wn in wns:
        wnthree = wn.split(" ")
        wnfirst = wnthree[0]
        wnsecond = wnthree[1]
        wnthird = wnthree[2]
        wnfx = expand_name(mls, wnfirst)
        for x in wnfx:
            wx = x+" "+wnsecond
            for ax in ans:
                if wx in ax:
                    print("MATCH: ")
                    print(wn+" <---> "+ax)
                    print("Potential rivals: ")
                    for axx in ans:
                        if axx.endswith(wnthird):
                            print("\t"+axx)
                    print("\n\n\n")


def main():
    myletters=list(string.ascii_lowercase)
    women = [clean_name(wn) for wn in women_list]
    ath_file = open(athletes_file, "r")
    ath_list = ath_file.readlines()
    athletes = [clean_name(ath) for ath in ath_list]
    solve_puzzle(myletters, women, athletes)



if __name__ == "__main__":
    main()

"""
Solution:
Lady Bird Johnson --> Larry Bird, Johnson (i.e., Earvin 'Magic' Johnson)
"""
