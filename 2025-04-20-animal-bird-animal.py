#!/usr/bin/env python

## 2025/04/21. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2025/04/20 Sunday Puzzle:
## https://www.npr.org/2025/04/20/nx-s1-5362989/sunday-puzzle-earth-day-categories
## That puzzle:

"""
This week's challenge comes from Philip Goodman, of Binghamton, N.Y.
Name an animal in five letters. Add two letters and rearrange the result
to name a bird in seven letters. Then add two letters to that and rearrange
the result to name another animal in nine letters. What creatures are these?
"""

from collections import Counter

with open('./resources/birds.txt', 'r') as birdfile:
# with open('./resources/birds_test.txt', 'r') as birdfile:
    birds = birdfile.readlines()
birds = [b.strip() for b in birds]
birds = [b for b in birds if len(b) == 7]
with open('./resources/animals.txt', 'r') as animalfile:
# with open('./resources/animals_test.txt', 'r') as animalfile:
    animals = animalfile.readlines()
animals = [a.strip() for a in animals]
fives = [a for a in animals if len(a) == 5]
nines = [a for a in animals if len(a) == 9]
nines = [a for a in nines if ' ' not in a]


def get_sorted_letter_dict(mylist):
    sld = {}
    for m in mylist:
        mval = list(m)
        mval.sort()
        sld[m] = mval
    return sld

sbirds = get_sorted_letter_dict(birds)
sfives = get_sorted_letter_dict(fives)
snines = get_sorted_letter_dict(nines)

bird_animal_winners = []
for sb, sbval in sbirds.items():
    for sn, snval in snines.items():
        sbvalcopy = sbval[:]
        snvalcopy = snval[:]
        while sbvalcopy:
            bv = sbvalcopy.pop(0)
            if bv in snvalcopy:
                snvalcopy.remove(bv)
            # print(sbvalcopy, snvalcopy)
        # print(sb, sbvalcopy, sn, snvalcopy)
        if len(snvalcopy) == 2:
            bird_animal_winners.append((sb, sn))
            # print('POSSIBLE MATCH')
        # print('\n')

animal_bird_winners = []
for sb, sbval in sfives.items():
    for sn, snval in sbirds.items():
        sbvalcopy = sbval[:]
        snvalcopy = snval[:]
        while sbvalcopy:
            bv = sbvalcopy.pop(0)
            if bv in snvalcopy:
                snvalcopy.remove(bv)
            # print(sbvalcopy, snvalcopy)
        # print(sb, sbvalcopy, sn, snvalcopy)
        if len(snvalcopy) == 2:
            animal_bird_winners.append((sb, sn))
            # print('POSSIBLE MATCH')
        # print('\n')
print(bird_animal_winners,animal_bird_winners)

for ab in animal_bird_winners:
    for ba in bird_animal_winners:
        if ab[1] in ba:
            print(ab[0], ab[1], ba[1])
