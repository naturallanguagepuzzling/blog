#!/usr/bin/env python


## 2021/06/21. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/05/30 Sunday Puzzle:
## https://www.npr.org/2021/06/20/1008352915/sunday-puzzle-hidden-cities
## That puzzle:
"""
This week's challenge comes from listener Iva Allen in Canada. Name a make of
car. Write it in all capital letters. Rotate one of the letters 90 degrees and
another letter 180 degrees to make a woman's name. What is it?
"""

import itertools
import string
from slugify import slugify


## mapping upright capital letters to 90degree rotated letters
upper_90d = {
    'C': ['U'],
    'E': ['M', 'W'],
    'H': ['I'],
    'I': ['H'],
    'M': ['E'],
    'N': ['Z'],
    'U': ['C'],
    'W': ['E'],
    'Z': ['N']
    }

## mapping upright capital letters to 180degree rotated letters
upper_180d = {
    'A': 'V',
    'M': 'W',
    'U': 'A',
    'V': 'A',
    'W': 'M',
    }

## You can use the text file lists of cars makers and girls names I've prepared;
## download them from GitHub and store it as I have:
car_makers_file = 'resources/car-makers.txt'
girls_names_file = 'resources/girls-names.txt'


## clean up each name to suit this puzzle: remove any whitespace,
## convert to upppercase, slugify (convert to ASCII), remove any non-letters
def clean_name(somename):
    s = somename.strip()
    s = slugify(s)
    s = "".join([l.upper() for l in s if l.isalpha()])
    return s


## takes in agenda (see get_car_variants); for each pair of indices in the
## agenda, does the rotations to produce variant(s)
def get_variants_by_agenda(car, agenda):
    car = "".join(car)
    variants = []
    for ag in agenda:
        agvars = []
        i90 = ag[0]
        i180 = ag[1]
        v90s = upper_90d[car[i90]]
        v180 = upper_180d[car[i180]]
        for v90 in v90s:
            carlist = list(car)
            carlist[i90] = v90
            carlist[i180] = v180
            agvars.append("".join(carlist))
        variants += agvars
    return variants


## takes a car maker (string), determines which positions in string can be
## rotated 90 or 180 degrees; produces a list (agenda) of pairs of positions
## to rotate in order to produce all variant strings; each pair is:
## (i90, i80), where i90 is index of letter to be rotated 90 degrees; i90 != i80
def get_car_variants(car, keys90, keys180):
    cvs = []
    car = list(car)
    i90s = []  ## index in car string for letters rotatable 90 degrees
    i180s = []  ## index in car string for letters rotatable 180 degrees
    for lx in car:
        if lx in keys90:
            i90s.append(car.index(lx))
        if lx in keys180:
            i180s.append(car.index(lx))
    if 0 not in [len(i90s), len(i180s)]:
        agenda = [ii for ii in itertools.product(i90s, i180s) if ii[0] != ii[1]]
        agenda = list(set(agenda))
        cvs += get_variants_by_agenda(car,agenda)
    else:
        pass
    return cvs


## iterate through car makers, expand each car maker to variants using rotated
## letters; compare variants against list of girl names; print solution
def cars_vs_girls(cars, girls, keys90, keys180):
    for car in cars:
        car_variants = get_car_variants(car, keys90, keys180)
        print(car)
        print(car_variants)
        for cv in car_variants:
            for g in girls:
                if cv.strip() == g.strip():
                    print(car, g)


## prepare lists of 90degree rotatable and 180degree rotatable letters
def solve_puzzle(cars, girls):
    keys90 = list(upper_90d.keys())
    keys180 = list(upper_180d.keys())
    cars_vs_girls(cars, girls, keys90, keys180)    


def main():
    girl_file = open(girls_names_file, "r")
    girl_list = girl_file.readlines()
    girl_file.close()
    girls = [clean_name(g) for g in girl_list]
    girls.sort()
    car_file = open(car_makers_file, "r")
    car_list = car_file.readlines()
    car_file.close()
    cars = [clean_name(c) for c in car_list]
    cars.sort()
    solve_puzzle(cars, girls)


if __name__ == "__main__":
    main()

"""
Solution:
MAZDA --> WANDA
"""
