#!/usr/bin/env python

## 2024/09/04. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/09/01 Sunday Puzzle:
## https://www.npr.org/2024/09/01/nx-s1-5094886/sunday-puzzle-three-of-a-kind
## That puzzle:

"""
This week's challenge comes from listener Ethan Kane (ph) of Albuquerque, N.M.
Name a famous TV personality of the past. Drop the second letter of this
person's last name, and phonetically, the first and last names together will
sound like a creature of the past. What celebrity is this?
"""

## To use this script, you'll need:
## Gensim word2vec: https://radimrehurek.com/gensim/
## CMU pronunciation dict: https://github.com/cmusphinx/cmudict; store the dict
## file as I have below (see variable called "cmup")

## I'm relying on the cmu pronuciation dictionary, available here:
## https://github.com/cmusphinx/cmudict
cmup = "../annex/cmudict-master/cmudict-dict.txt"
##looks like:
"""
missourians M AH0 Z UH1 R IY0 AH0 N Z
misspeak M IH0 S S P IY1 K
misspeak(2) M IH0 S P IY1 K
misspell M IH0 S S P EH1 L
misspell(2) M IH0 S P EH1 L
misspelled M IH0 S S P EH1 L D
misspelled(2) M IH0 S P EH1 L D
misspelling M IH0 S S P EH1 L IH0 NG
"""

from slugify import slugify

tv_persons_file = "resources/past-tv-personalities.txt"


def get_lex(some_lexicon_filename):
    lexfile = open(some_lexicon_filename, "r")
    lexlines = lexfile.readlines()
    lex = [l.strip() for l in lexlines]
    lexfile.close()
    return lex

## reads in the cmu pronunciation dictionary; keeps only those entries on our
## list of candidates, returns dictionary
def get_pron_dict_for_cands(mycands):
    pd = {}
    cmupf = open(cmup, 'r')
    cmul = cmupf.readlines()
    cmupf.close()
    for mc in mycands:
        mcs = mc.split(" ")
        for mcx in mcs:
            pd[mcx] = []
            for l in cmul:
                if l.startswith(mcx+" ") or l.startswith(mcx+"(2)"):
                    l = l.split(" # ")[0]
                    pron = l.split(" ", 1)[1].strip()
                    pd[mcx].append(pron)
                else:
                    pass
    return pd

def filter_empty_lists(dictionary):
  filtered_dict = {}
  for key, value in dictionary.items():
    if value and not isinstance(value, list) or (isinstance(value, list) and value):
      filtered_dict[key] = value
  return filtered_dict

def get_personx(person):
    person = person.split(" ")
    surname = person.pop()
    surname = surname[0]+surname[2:]
    person = " ".join(person)
    personx = (person+" "+surname)
    return personx

def pron_strip(mypron):
    mypron = mypron.replace("0", "")
    mypron = mypron.replace("1", "")
    mypron = mypron.replace("2", "")
    mypron = mypron.replace(" ", "")
    return mypron

creatures = [
    'Ammonite', 'Andrewsarchus', 'Arthropleura', 'Brachiosaurus', 
    'Deinotherium', 'Dimetrodon', 'Dinosaur', 'Dodo',
    'Dunkleosteus', 'Glyptodon', 'Gorgonops', 'Ichthyosaurus',
    'Mammoth', 'Mastodon', 'Megalodon', 'Megatherium', 'Mosasaurus',
    'Plesiosaurus', 'Pterodactyl', 'Smilodon', 'Stegosaurus',
    'Titanoboa', 'Triceratops', 'Trilobite', 'Uintatherium',
    'Velociraptor',
    'Cave lion', 'Dire wolf', 'Giant ground sloth', 'Tasmanian tiger',
    'Tyrannosaurus Rex', 'Saber-toothed tiger'
            ]

def main():
    ## prep creatures data objects
    crs = []
    for c in creatures:
        crs.append(slugify(c))
    crs = [c.replace("-", " ") for c in crs]
    creature_prons = get_pron_dict_for_cands(crs)
    creature_prons = filter_empty_lists(creature_prons)
    ## prep TV personalities data objects
    tvp = get_lex(tv_persons_file)
    tvpslug = []
    for t in tvp:
        tvpslug.append(slugify(t))
    persons = [t.replace("-", " ") for t in tvpslug]
    psx = [get_personx(p) for p in persons]
    person_prons = get_pron_dict_for_cands(psx)
    person_prons = filter_empty_lists(person_prons)
    ## iterate through persons, then creatures to match pronunciations
    for pr in persons:
        personx = get_personx(pr)
        ppron = ''
        for pname in personx.split(" "):
            if pname not in person_prons:
                break
            else:
                ppron += person_prons[pname][0]
        for cr in creature_prons:
            if pron_strip(creature_prons[cr][0]) == pron_strip(ppron):
                print("MATCH: "+pr+" | "+cr+" | "+creature_prons[cr][0])
            else:
                pass


if __name__ == '__main__':
    main()
