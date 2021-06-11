#!/usr/bin/env python


## 2021/06/07. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/06/06 Sunday Puzzle:
## https://www.npr.org/2021/06/06/1003633804/sunday-puzzle-television-scramble
## That puzzle:
"""
This week's challenge comes from listener Matthew Leal of San Francisco. Write
down the name of a country plus its capital, one after the other. Hidden in
consecutive letters inside this is the name of a film that won an Academy Award
for Best Picture. Name the country, capital, and film.
"""

import pandas as pd
from slugify import slugify

## I've prepared the countries and capitals in a CSV, and best picture winners
## in another CSV. You'll need to download these and save them in a folder
## called "resources"; folder must be in same location as this script
cc_csv = "resources/countries-capitals.csv"
bp_csv = "resources/best-pictures.csv"


## open countries-capitals file; return dictionary; key is slugified and cleaned
## and lowercased concatenated string of country and city (no spaces); value is
## original string of country and city; e.g.:
## {"faroeislandstorshavn": "Faroe Islands, Tórshavn",
##  "haitiportauprince": "Haiti, Port-au-Prince"}
## spaces, hyphens, etc; keep only cities with exactly one 's'
def get_capitals_dict(my_caps_csv):
    caps_df = pd.read_csv(my_caps_csv)
    raw_countries = list(caps_df["Country"])
    raw_caps = list(caps_df["Capital"])
    caps_dict = {}
    while raw_countries:
        rcountry = raw_countries.pop(0)
        rcap = raw_caps.pop(0)
        dval = rcountry+", "+rcap
        dkey = rcountry+rcap
        dkey = slugify(dkey)
        dkey = "".join([l.lower() for l in dkey if l.isalpha()])
        caps_dict[dkey] = dval
    return caps_dict


## read best picture CSV and return a similar dictionary, e.g.:
## {"benhur": "Ben-Hur", "thekingsspeech": "The King's Speech"}
def get_best_pic_dict(my_movies_csv):
    movies_df = pd.read_csv(my_movies_csv)
    raw_movies = list(movies_df["Movie"])
    movies_dict = {}
    while raw_movies:
        rmovie = raw_movies.pop(0)
        mkey = slugify(rmovie)
        mkey = "".join([l.lower() for l in mkey if l.isalpha()])
        movies_dict[mkey] = rmovie
    return movies_dict
        

def main():
    all_caps = get_capitals_dict(cc_csv)
    all_movies = get_best_pic_dict(bp_csv)
    for ck in all_caps:
        for mk in all_movies:
            if mk in ck:
                print("SOLUTION:")
                print(all_caps[ck], "&", all_movies[mk])


if __name__ == "__main__":
    main()



"""
SOLUTION:
Bahrain, Manama & Rain Man
"""
