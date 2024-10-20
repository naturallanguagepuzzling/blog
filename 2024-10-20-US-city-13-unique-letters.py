#!/usr/bin/env python


## 2024/10/20. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/10/20 Sunday Puzzle:
## https://www.npr.org/2024/10/19/nx-s1-5156007/sunday-puzzle-a-paired-puzzle
## That puzzle:
"""
This week's challenge comes from listener David Dickerson, of Tucson, Arizona.
The city UTICA, NEW YORK, when spelled out, contains 12 letters, all of them
different. Think of a well-known U.S. city, that when its name is spelled out,
contains 13 letters, all of them different. Your answer doesn't have to match
mine.
"""

import re
from slugify import slugify


## I'm using a large tsv file containing only two columns: place name, US State;
## I've extracted it from the much larger file downloadable here:
## https://osmnames.org/download/
## See my blog entry for more details on deriving the file.
usa_places_file = '../annex/usa-places.tsv'
with open(usa_places_file, 'r') as placefile:
    usa_places = placefile.readlines()
usa_places = [p.strip() for p in usa_places]
usa_places = list(filter(None, usa_places))


def clean_string(ugly):
    ugly = ugly.strip()
    ugly = ugly.split(" ")
    ugly = [slugify(g) for g in ugly]
    ugly = [g.replace('-', '') for g in ugly]
    ugly = " ".join(ugly)
    return ugly

def get_x_letter_place_names(allplaces, x):
    candidate_places = []
    allplaces = [s for s in allplaces if not re.search(r'\d', s)]
    for place in allplaces:
        place = place.lower()
        ps = place.split('\t')
        if len(ps) != 2:
            pass
        else:
            ps = [p.strip() for p in ps]
            ps = list(filter(None, ps))
            ps = ' '.join(ps)
            ps = clean_string(ps)
            ps = ps.lower()
            if len(ps.replace(' ', '')) == x:
                candidate_places.append(ps)
            else: pass
    return candidate_places

def check_unique_letters(placestring):
    ps = placestring.replace(' ', '')
    ps = list(set(list(ps)))
    if len(ps) == len(placestring.replace(' ', '')):
        return True
    else:
        return False


def main():
    candidate_places = get_x_letter_place_names(usa_places, 13)
    for pl in candidate_places:
        if check_unique_letters(pl):
            print(pl)
        else: pass


if __name__ == '__main__':
    main()
