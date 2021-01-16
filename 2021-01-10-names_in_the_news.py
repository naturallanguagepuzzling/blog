#!/usr/bin/env python


## 2021/01/11. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/1/10 Sunday Puzzle:
## https://www.npr.org/2021/01/10/955279867/sunday-puzzle-categories-first

## For the text files used here, I cut and pasted the text from the links here 
## and cleaned it up a bit manually:
## https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext&titles=2011
## https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext&titles=2021

import stanza
import unidecode

## load tokenizer and named entity recognizer pipeline
nlp = stanza.Pipeline(lang='en', processors='tokenize,ner')


## find named entities in the text, keep only PERSON names; among those, look
## for combos to get target length of letters (full name, last name only, etc.)
def get_persons(f_name, letter_count):
    infile = open(f_name, "r")
    mytext = infile.read()
    doc = nlp(mytext)
    my_persons = []
    initial_person = []
    my_ents = doc.entities
    for me in my_ents:
        if me.type == "PERSON":
            mt = me.text.strip()
            mt = mt.replace(".", "")
            mt = unidecode.unidecode(mt)  ## drop accents, etc. --> ascii
            mt = mt.lower()
            my_persons.append(mt)
    my_persons.sort()
    target_letters = []
    for mp in my_persons:
        # print(mp)
        if sum(c.isalpha() for c in mp) == letter_count:  ## full name
            target_letters.append(mp)
        else:
            mp = mp.split(" ")
            if len(mp) == 1:
                pass
            else:
                first = mp[0]  ## first name only
                last = mp[-1]  ## last name only
                first_last = " ".join([first, last])  ## first and last names
                combos = [first, last, first_last]
                if len(mp) > 2:
                    last_two = " ".join([mp[-2], last])  ## last two names; e.g., 'van halen'
                    combos.append(last_two)
                for cb in combos:
                    if sum(c.isalpha() for c in cb) == letter_count:
                        target_letters.append(cb)
    target_letters = list(set(target_letters))  ## list --> set --> list : trick to remove duplicates
    target_letters.sort()
    return(target_letters)


def transform_names(j11, k21):
    mt = []
    for j in j11:
        jx = "".join([c for c in j if c.isalpha()])
        jz = "".join([jx[0], jx[1], jx[5], jx[6], jx[7]])
        for k in k21:
            print(k+" <--> "+jz+" <-- "+j)
            if k == jz:
                mt.append(k+" <--> "+jz+" <-- "+j)
    return mt


def main():
    f2011 = "2021-01-10-Wikipedia_2011.txt"
    f2021 = "2021-01-10-Wikipedia_2021.txt"
    names2011 = get_persons(f2011, 8)
    names2021 = get_persons(f2021, 5)
    matches = transform_names(names2011, names2021)
    print("\n##################################\n\nFound these matches:")
    for m in matches:
        print(m)


if __name__ == "__main__":
    main()

