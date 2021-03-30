#!/usr/bin/env python

## 2021/03/30. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/03/28 Sunday Puzzle:
## https://www.npr.org/2021/03/28/981915586/sunday-puzzle-here-the-homophone
## That puzzle:
"""
This week's challenge comes from listener Greg VanMechelen, of Berkeley, Calif.
Name something birds do. Put the last sound of this word at the start and the
first sound at the end, and phonetically you'll name something else birds do.
What are these things?
"""

## To use this script, you'll need:
## stanza: https://stanfordnlp.github.io/stanza/
## Gensim word2vec: https://radimrehurek.com/gensim/
## CMU pronunciation dict: https://github.com/cmusphinx/cmudict; store the dict
## file as I have below (see variable called "cmup")

import re, stanza
import gensim.downloader as api
from gensim.models import KeyedVectors
from typing import Type


nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma')
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
sample_size = 100
vec_models = [
    'glove-wiki-gigaword-100',
    # 'glove-wiki-gigaword-300',
    # 'word2vec-google-news-300',
    'glove-twitter-200',
    # 'fasttext-wiki-news-subwords-300',
    # 'conceptnet-numberbatch-17-06-300'
    ]


## a few words that are quite particular to birds; i'm using progressive forms
## here in hopes of getting back verb forms; we'll lemmatize the results anyway
my_seeds = [
    "flying",
    "flapping",
    "nesting",
    "brooding",
    "pecking",
    "roosting",
    "tweeting",
    "cawing",
    "crowing",
    ]


## using stanza, lemmatize each word in the list we got from word2vec
def lemmatize_list(dirty):
    lemm = []
    for dw in dirty:
        # print(dw+" ########################")
        d = nlp(dw)
        dwlem = [word.lemma for sent in d.sentences for word in sent.words][0]
        lemm.append(dwlem)
    return lemm


## Finds top n (sample_size) most similar words for each seed word
def get_similar_words(word_vectors: Type[KeyedVectors],
                      seed_word: str, n_synonyms: int=sample_size) -> None:
    result_words = []
    results = word_vectors.most_similar(topn=sample_size, positive=[seed_word])
    for r in results[:n_synonyms]:
        result_words.append(r[0].lower())
        # print(f"{r[0]:<15}: {r[1]:.3f}")
    return result_words


## Runs every seed word in list, combines all results into flat list of types
def run_seed_list(my_model, my_seeds):
    all_results = []
    for ms in my_seeds:
        print(ms)
        try:
            ms_results = get_similar_words(my_model, ms)
        except:
            ms_results = []
        for mr in ms_results:
            if mr not in all_results:
                all_results.append(mr)
            else:
                pass
    all_results = remove_nonwords(all_results)
    return all_results


## keep only words containing letters only (remove strings containing digits)
def remove_nonwords(aw):
    aw = [zw for zw in aw if zw.isalpha()]
    return aw


## keep words of min_length or greater
def filter_for_length(some_words, min_length):
    # print(some_words)
    flw = [x for x in some_words if len(x) > min_length]
    return(flw)


## reads in the cmu pronunciation dictionary; keeps only those entries on our
## list of candidates, returns dictionary
def get_pron_dict_for_cands(mycands):
    pd = {}
    cmupf = open(cmup, 'r')
    cmul = cmupf.readlines()
    cmupf.close()
    for mc in mycands:
        pd[mc] = []
        # pron = 'null'
        for l in cmul:
            if l.startswith(mc+" ") or l.startswith(mc+"(2)"):
                l = l.split(" # ")[0]
                pron = l.split(" ", 1)[1].strip()
                pd[mc].append(pron)
            else:
                pass
    return pd


## removes left hand phonemes until it finds vowel, then splits off the onset;
## removes right hand phonemes until it finds vowel, then splits off coda;
## swaps initial onset and final coda; returns all such swaps (multiple are
## possible where a spelling has multiple pronunciations)
def swap_phones(werd, pd):
    swapped = []
    wps = pd[werd]
    for wp in wps:
        onset = ''
        coda = ''
        wp = wp.split(" ")
        while True:
            x = wp.pop(0)
            ## collect left hand phonemes until we hit a numeral (0,1,2 are
            ## stress markers and occur on every nucleus)
            if x.isalpha():
                onset = onset+" "+x
            else:
                wp.insert(0, x)
                break
        while True:
            y = wp.pop()
            ## collect coda phonemes until we hit a numeral (stress marker on nucleus)
            if y.isalpha():
                coda = y+" "+coda
            else:
                wp.append(y)
                break
        swp = " ".join(wp)
        ## swap head and tail (onset & coda) and rejoin the three pieces:
        swp = coda.strip()+" "+swp+" "+onset.strip()
        swp = swp.replace("  ", " ")
        swapped.append(swp)
    return swapped
    

## Run the main routine using above functions:
def main():
    ## min word length is 3 letters because we need onset and coda to swap;
    min_length = 3
    ## add seeds to the list of candidates (to be expanded later);
    cands = list(my_seeds)
    ## try multiple word2vec models to generate a wide variety of candidates;
    for vec_model_name in vec_models:  ## use each model to generate candidates
        print("\n#####################################################\n")
        print("Loading model "+vec_model_name+"...\n")
        vmodel = api.load(vec_model_name)
        print("Generating candidate words from these seed words:\n")
        cands+=run_seed_list(vmodel, my_seeds)
    ## strip any duplicate strings;
    cands = list(set(cands))
    ## filter out any candidates of 2 letters or fewer;
    cands = filter_for_length(cands, min_length)
    ## lemmatize candidates: "fluttered" --> "flutter", "nesting" --> "nest";
    cands = lemmatize_list(cands)
    cands.sort()
    print("\n#####################################################\n")
    print("Number of words in candidate list: "+str(len(cands)))
    solutions = []
    ## load cmu file, return dictionary: {spelling: [pronunciations]} for candidates
    prondict = get_pron_dict_for_cands(cands)
    ## iterate through candidates;
    for cd in cands:
        ## get the onset-coda swapped strings for candidate;
        cswaps = swap_phones(cd, prondict)
        ## iterate through the swapped strings;
        for csw in cswaps:
            ## iterate through all the *other* candidates in the list
            for cd2 in cands:
                if cd2 == cd:
                    pass
                else:
                    ## if a swapped pronunciation appears in another candidate's
                    ## list of pronunciations, add the two words to solutions
                    if csw in prondict[cd2]:
                        solutions.append(cd+" "+cd2)
                        solutions = list(set(solutions))
    ## print out the possible solutions
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
