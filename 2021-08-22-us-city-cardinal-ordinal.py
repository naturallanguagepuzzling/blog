#!/usr/bin/env python


## 2021/08/26. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/08/22 Sunday Puzzle:
## https://www.npr.org/2021/08/22/1029993143/sunday-puzzle-connect-the-words
## That puzzle:
"""
This week's challenge comes from listener Ben Austin, of Dobbs Ferry, N.Y. Take
the name of a major American city. Move one of its letters three spaces later in
the alphabet. Embedded in the resulting string of letters, reading left to
right, is a cardinal number. Remove that number, and the remaining letters,
reading left to right, spell an ordinal number. What city is it, and what are
the numbers?
"""

import pandas as pd
from slugify import slugify
import string

## I'm using a CSV of data on the 1000 largest US cities, which I found here:
## https://github.com/plotly/datasets/blob/master/us-cities-top-1k.csv
## You'll need to download that file to run this script.
cc_csv = "../annex/us-cities-top-1k-plotly.csv"

## contains "zero", "one", "two", thru "one hundred"; one per line; download it:
## 
cardinals_file = "resources/cardinals_100.txt"

## contains "first", "second", thru "one hundredth"; one per line: download it:
##
ordinals_file = "resources/ordinals_100.txt"


## return list of cities from csv file
def get_cities_list(my_cities_csv):
    cities_df = pd.read_csv(my_cities_csv)
    raw_cities = list(cities_df["City"])
    return raw_cities


## return city name: slugified, cleaned, lowercased, no spaces, hyphens, etc.
def clean_city(rc):
    rc = rc.split(" ")
    rc = [r.strip() for r in rc]
    rc = [slugify(r) for r in rc]
    rc = "".join([r.lower() for r in rc if r.isalpha()])
    return rc


## return list from text file: lowercased, no spaces, no hyphens, etc.
def txt_to_cleaned_list(fname):
    txt = open(fname, 'r').readlines()
    mylist = ["".join([c.lower() for c in cd if c.isalpha()]) for cd in txt]
    return mylist


## return string 'encoded' via caesar shift
def caesar_shift(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


def main():
    cardinals = txt_to_cleaned_list(cardinals_file)
    ordinals = txt_to_cleaned_list(ordinals_file)
    cities = get_cities_list(cc_csv)
    for rawcity in cities:
        c = clean_city(rawcity)
        cletters = list(c)
        for i in range(0,len(cletters)):
            shifted_letter = caesar_shift(cletters[i],3)
            shifted = cletters[:i]+[shifted_letter]+cletters[i+1:]
            shifted = "".join(shifted)
            # print(shifted)
            for card in cardinals:
                if card in shifted:
                    short = shifted.replace(card, "")
                    for ordl in ordinals:
                        if ordl in short:
                            print("SOLUTION: '"+rawcity+"' --> '"+shifted+"', which contains '"+card+"'; removing '"+card+"' yields '"+ordl+"'")


if __name__ == "__main__":
    main()


"""
SOLUTION: 'Fort Worth' --> 'foutworth', which contains 'two'; removing 'two' yields 'fourth'
"""
