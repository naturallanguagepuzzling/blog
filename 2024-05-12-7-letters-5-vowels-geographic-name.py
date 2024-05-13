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

## You'll need to download the lexicon file as I did:
## https://github.com/dwyl/english-words/blob/master/words_alpha.txt
lexfilename = "../annex/words_alpha.txt"

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

orthovowels = ['a', 'e', 'i', 'o', 'u', 'y']


## read in the lexicon file
def get_lex(some_lexicon_filename):
    lexfile = open(some_lexicon_filename, "r")
    lex = lexfile.readlines()
    lexfile.close()
    return lex


## return all 7-letter words with 5 (orthographic) vowels
def get_7_letters_5_vowels(lex):
    keepers = []
    for wd in lex:
        wd = wd.strip().lower()
        if len(wd) != 7:
            pass
        else:
            vcount = 0
            for i in range(0,len(wd)-1):
                if wd[i] in orthovowels:
                    vcount += 1
            if vcount == 5:
                keepers.append(wd)
    return keepers


## reads in the cmu pronunciation dictionary; keeps only those entries on our
## list of candidates, returns dictionary
def get_pron_dict_for_cands(mycands):
    pd = {}
    cmupf = open(prondictfile, 'r')
    cmul = cmupf.readlines()
    cmupf.close()
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


def main():
    lex = get_lex(lexfilename)
    candidates = get_7_letters_5_vowels(lex)
    print(len(candidates))
    mypd = get_pron_dict_for_cands(candidates)
    for k, v in mypd.items():
        print(k, v)


if __name__ == '__main__':
    main()
