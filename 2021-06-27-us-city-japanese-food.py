#!/usr/bin/env python


## 2021/06/27. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/06/27 Sunday Puzzle:
## https://www.npr.org/2021/06/27/1010586683/sunday-puzzle-words-within-words
## That puzzle:
"""
This week's challenge comes from listener Julia Lewis, of Fort Collins, Colo.
Take the name of a major American city. Hidden inside it in consecutive letters
is the name of a Japanese food. Remove that. The remaining letters can be
rearranged to to spell some Mexican foods. Name the city and the foods.
"""

import pandas as pd
from slugify import slugify

## I'm using a CSV of data on the 1000 largest US cities, which I found here:
## https://github.com/plotly/datasets/blob/master/us-cities-top-1k.csv
## You'll need to download that file to run this script.
cc_csv = "../annex/us-cities-top-1k-plotly.csv"
# bp_csv = "resources/best-pictures.csv"
## I'm using *very* short lists of Japanese and Mexican foods, but given the
## the nature of this puzzle, I'm pretty confident we don't need more
jfoods = ["sushi", "tofu", "ramen", "udon", "soba"]
mfoods = ["taco", "nacho", "tamal", "burrito", "enchilada", "tostada", "salsa"]


## open cities data file; return dictionary; key is slugified and cleaned
## and lowercased concatenated string of city name (no spaces); value is
## original string of city and state; e.g.:
## {"sanfrancisco": "San Francisco, California",
##  "haitiportauprince": "Haiti, Port-au-Prince"}
def get_cities_dict(my_cities_csv):
    cities_df = pd.read_csv(my_cities_csv)
    raw_states = list(cities_df["State"])
    raw_cities = list(cities_df["City"])
    cities_dict = {}
    while raw_states:
        rstate = raw_states.pop(0)
        rcity = raw_cities.pop(0)
        dval = rcity+", "+rstate
        dkey = rcity.split(" ")
        dkey = [slugify(c) for c in dkey]
        dkey = "".join([l.lower() for l in dkey if l.isalpha()])
        cities_dict[dkey] = dval
    return cities_dict
 

def check_mfood_vs_city(mx,ct):
    match = "none"
    m1letters = list(mx)
    m2letters = list(mx+"s")
    m3letters = list(mx+"es")
    m1letters.sort()
    m2letters.sort()
    m3letters.sort()
    m1 = "".join(m1letters)
    m2 = "".join(m2letters)
    m3 = "".join(m3letters)
    if ct == m1:
        match = mx
    elif ct == m2:
        match = mx+"s"
    elif ct == m3:
        match = mx+"es"
    else:
        pass
    return match


def main():
    all_cities = get_cities_dict(cc_csv)
    for c in all_cities:
        for j in jfoods:
            if j in c:
                cl = c.replace(j, "")
                cl = list(cl)
                cl.sort()
                cl = "".join(cl)
                for m in mfoods:
                    match = check_mfood_vs_city(m, cl)
                    if match == "none":
                        pass
                    else:
                        print("SOLUTION:\n"+c+", "+j+", "+match)


if __name__ == "__main__":
    main()



"""
SOLUTION:
sacramento, ramen, tacos
"""
