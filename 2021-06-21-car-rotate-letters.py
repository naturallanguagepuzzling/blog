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

upper_180d = {
    'A': 'V',
    'M': 'W',
    'U': 'A',
    'V': 'A',
    'W': 'M',
    }

## You can use the text file list of athletes I've prepared; download it from
## GitHub and store it as I have:
car_makers_file = 'resources/car-makers.txt'
girls_names_file = 'resources/girls-names.txt'

## clean up each name to suit this puzzle: remove any whitespace,
## convert to upppercase, slugify (convert to ASCII), remove any non-letters
def clean_name(somename):
    s = somename.strip()
    s = slugify(s)
    s = "".join([l.upper() for l in s if l.isalpha()])
    return s


def get_candidate_cars(allcars, k90, k180):
    ccs = []
    for ac in allcars:
        ## first, we check for a letter in the k90 list, followed by a letter in
        ## the k180 list;
        acl = list(ac)
        while acl:
            l1 = acl.pop(0)
            print("STEP1: "+l1)
            while l1 not in k90:
                while acl:
                    l1 = acl.pop(0)
                    print("STEP2: "+l1)
                    while acl:
                        l2 = acl.pop(0)
                        print("STEP3: "+l2)
                        while l2 not in k180:
                            while acl:
                                l2 = acl.pop(0)
                                print("STEP4: "+l2)
                            break
                        ccs.append(ac)
                        break
                    break
                break
            break
        ## next, we check for a k180 letter, then k90 letter... this is a bit
        ## hacky, but should work just fine
        acl = list(ac)
        while acl:
            l1 = acl.pop(0)
            while l1 not in k180:
                while acl:
                    l1 = acl.pop(0)
                    while acl:
                        l2 = acl.pop(0)
                        while l2 not in k90:
                            while acl:
                                l2 = acl.pop(0)
                            break
                        ccs.append(ac)
                        break
                    break
                break
            break
    ccs = list(set(ccs))
    ccs.sort()
    return ccs


def get_variants_by_agenda(car, agenda):
    car = "".join(car)
    # print(agenda)
    variants = []
    for ag in agenda:
        # print(ag)
        agvars = []
        i90 = ag[0]
        i180 = ag[1]
        # print(i90)
        # print(car[i90])
        v90s = upper_90d[car[i90]]
        # print(i90, v90s)
        v180 = upper_180d[car[i180]]
        # print(i180, v180)
        for v90 in v90s:
            carlist = list(car)
            carlist[i90] = v90
            carlist[i180] = v180
            agvars.append("".join(carlist))
            # print(carlist)
        variants += agvars
    return variants


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
    # print(car)
    # print(i90s)
    # print(i180s)
    if 0 not in [len(i90s), len(i180s)]:
        agenda = [ii for ii in itertools.product(i90s, i180s) if ii[0] != ii[1]]
        agenda = list(set(agenda))
        cvs += get_variants_by_agenda(car,agenda)
    else:
        pass
    return cvs


def cars_vs_girls(cars, girls, keys90, keys180):
    for car in cars:
        car_variants = get_car_variants(car, keys90, keys180)
        # print(car)
        # print(car_variants)
        for cv in car_variants:
            # if cv in girls:
            for g in girls:
                # if g == "WANDA":
                   # print(cv, g)
                if cv.strip() == g.strip():
                    print(cv, g)


## iterate through women's names, expand each first name into candidates;
## iterate through candidate first names, combine with second name, then iterate
## through athlete names and check if candidate (first+second) name matches
def solve_puzzle(cars, girls):
    keys90 = list(upper_90d.keys())
    keys180 = list(upper_180d.keys())
    cars = ['MAZDA']
    ccars = get_candidate_cars(cars, keys90, keys180)
    print(ccars)
    cars_vs_girls(ccars, girls, keys90, keys180)    


def main():
    # myletters=list(string.ascii_lowercase)
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
"""
