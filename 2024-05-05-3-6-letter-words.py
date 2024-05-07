#!/usr/bin/env python

## 2024/05/06. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/05/05 Sunday Puzzle:
## https://www.npr.org/2024/05/05/1248990211/sunday-puzzle-april-showers-bring-may-flowers
## That puzzle:
"""
This week's challenge: This week's challenge comes from listener Jim Bricker,
of Wayland, Mass. Think of three common six-letter words that have vowels in
the second and fifth positions. The last five letters of the words are the
same. Only the first letters differ. And none of the words rhyme with either
of the others. What words are they?
"""

## You'll need to download and store the lexicon as I did; I'm using this 
## file of 20,000 words:
## https://github.com/first20hours/google-10000-english/blob/master/20k.txt
lexfilename = "../annex/20k.txt"

## I'm relying on the cmu pronuciation dictionary, available here:
## https://github.com/cmusphinx/cmudict
prondictfile = "../annex/cmudict-master/cmudict-dict.txt"
## it looks like:
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


## Vowels in the CMU pron dictionary (without stress markers) are:
vowels = [
    'AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY',
    'OW', 'OY', 'UH', 'UW'
    ]


## read in the lexicon file
def get_lex(some_lexicon_filename):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    lexfile = open(some_lexicon_filename, "r")
    full_lex = lexfile.readlines()
    lexfile.close()
    lex = [l.strip().lower() for l in full_lex]
    lex = [s for s in lex if len(s) == 6]
    lex = [s for s in lex if s[1] in vowels and s[4] in vowels]
    return lex


## return cases of 3 or more 6-letter words that share the same final 5 letters
def find_matching_endings(lex):
    wdict = {}
    for wd in lex:
        ending = wd[1:]
        if ending in wdict:
            wdict[ending].append(wd)
        else:
            wdict[ending] = [wd]
    keepers = []
    for value in wdict.values():
        if len(value) > 2:
            keepers.append(value)
    return keepers


## reads in the cmu pronunciation dictionary; keeps only those entries on our
## list of candidates, returns dictionary
def get_pron_dict_for_cands(mycands):
    pd = {}
    cmupf = open(prondictfile, 'r')
    cmul = cmupf.readlines()
    cmupf.close()
    # flatten mycands, which is currently 2-D
    mycands = [item for sublist in mycands for item in sublist]
    for mc in mycands:
        pd[mc] = []
        for l in cmul:
            if l.startswith(mc+" ") or l.startswith(mc+"(2)"):
                l = l.split(" # ")[0]
                pron = l.split(" ", 1)[1].strip()
                pd[mc].append(pron)
            else:
                pass
    return pd


def check_for_rhymes(candidate, prondict):
    rhymedict = {}
    for cand in candidate:
        candprons = prondict[cand]
        for candpron in candprons:
            candrhyme = candpron.split(" ")
            candrhyme = [o for o in candrhyme if o[:2] in vowels]
            candrhyme = "".join(candrhyme)
            if candrhyme in rhymedict:
                rhymedict[candrhyme].append((cand, candpron))
            else:
                rhymedict[candrhyme] = [(cand, candpron)]
    return rhymedict


def main():
    lex = get_lex(lexfilename)
    candidates = find_matching_endings(lex)
    prondict = get_pron_dict_for_cands(candidates)
    for candidate in candidates:
        rhymedict = check_for_rhymes(candidate, prondict)
        if len(rhymedict) > 2:
            print("SOLUTION FOUND")
            for k, v in rhymedict.items():
                print(v)
            print("\n")
    else:
        pass


if __name__ == '__main__':
    main()
