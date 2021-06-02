#!/usr/bin/env python


## 2021/06/01. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/05/30 Sunday Puzzle:
## https://www.npr.org/2021/05/30/1001564473/sunday-puzzle-double-double
## That puzzle:
"""
This week's challenge comes from listener Al Gori, of Oak Ridge, N.J. Name a
famous city in 10 letters that contains an "S." Drop the "S." Then assign the
remaining nine letters their standard value in the alphabet — A = 1, B= 2,
C = 3, etc. The total value of the nine letters is only 25. What city is it?
"""

import pandas as pd

## You'll need to download this CSV file of cities data as I did:
## https://worldpopulationreview.com/world-cities
# cities_csv = "../annex/world_cities.csv"
cities_csv = "../annex/words_alpha.txt"

letter_values = {
                'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
                'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
                'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
                'w': 23, 'x': 24, 'y': 25, 'z': 26
                }


## open cities file, return list of only cities of 10 letters; do not count
## spaces, hyphens, etc; keep only cities with exactly one 's'
# def get_ten_letter_cities(my_cities_csv):
#     cities_df = pd.read_csv(cities_csv, index_col=0)
#     all_cities = list(cities_df["Name"])
#     my_cities = []
#     for ac in all_cities:
#         aclist = [l.lower() for l in ac if l.isalpha()]
#         if aclist.count('s') == 1:
#             acjoined = "".join(aclist)
#             my_cities.append(acjoined)
#         else:
#             pass
#     my_cities = [mc for mc in my_cities if len(mc)==10]

def get_ten_letter_cities(my_cities_csv):
    cities_file = open(my_cities_csv, 'r')
    cities_df = cities_file.readlines()
    all_cities = [ct.strip() for ct in cities_df]
    my_cities = []
    for ac in all_cities:
        aclist = [l.lower() for l in ac if l.isalpha()]
        if aclist.count('s') == 1:
            acjoined = "".join(aclist)
            my_cities.append(acjoined)
        else:
            pass
    my_cities = [mc for mc in my_cities if len(mc)==6]


## pull each letter's alphabetical value ('a' = 1, 'b' = 2);
## if total value is 25, print as solution
def get_letter_values(my_cities):
    for mc in my_cities:
        mclist = [u for u in mc]
        mcval = 0
        for m in mclist:
            if m == 's':
                pass
            else:
                mv = letter_values[m]
                mcval += mv
                print(m, mv, mcval)
        if mcval == 108:
            print('SOLUTION: '+mc)


def main():
    ten_letter_cities = get_ten_letter_cities(cities_csv)
    get_letter_values(ten_letter_cities)
    

if __name__ == "__main__":
    main()



"""
Solution:
Addis Ababa
"""
