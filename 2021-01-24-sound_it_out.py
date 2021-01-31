#!/usr/bin/env python


## 2021/01/26. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/1/24 Sunday Puzzle:
## https://www.npr.org/2021/01/24/959931057/sunday-puzzle-sound-it-out
## That puzzle:
"""
This week's challenge is a spinoff of my on-air puzzle, and it's a little
tricky. Think of a hyphenated word you might use to describe a young child that
sounds like three letters spoken one after the other.
"""


import re
import gensim.downloader as api
from gensim.models import KeyedVectors
from typing import Type


## We'll try each of these word2vec models
vec_models = [
    # 'glove-wiki-gigaword-100',
    'glove-wiki-gigaword-300',
    # 'word2vec-google-news-300',
    'glove-twitter-200',
    'fasttext-wiki-news-subwords-300',
    'conceptnet-numberbatch-17-06-300'
    ]


## We'll query word2vec for similar words to these; we're casting a wide net
## here, but these seed words might be used to describe a young child
seed_words = [
    'active', 'adorable', 'adventurous', 'angel', 'angry', 'animated',
    'annoying', 'anxious', 'athletic', 'beauty', 'blessing', 'blond', 'blonde',
    'brave', 'bright', 'bundle', 'cautious', 'champ', 'champion', 'character',
    'charmer', 'charming', 'cheerful', 'childish', 'clever', 'clown', 'clumsy',
    'comedian', 'competitive', 'confident', 'creative', 'curious', 'darling',
    'delicate', 'delight', 'delightful', 'demanding', 'dependent', 'dreamer',
    'dynamo', 'eager', 'emotional', 'energetic', 'expressive', 'fearless',
    'fierce', 'fragile', 'frail', 'friendly', 'funny', 'gentleman', 'gifted',
    'growing', 'handful', 'helpless', 'imaginative', 'immature', 'independent',
    'infant', 'innocent', 'intelligent', 'joker', 'little', 'lively', 'lovely',
    'loving', 'miracle', 'mischievous', 'monkey', 'naive', 'naughty', 'nervous',
    'noisy', 'optimistic', 'outgoing', 'peculiar', 'performer', 'petite',
    'playful', 'plump', 'precious', 'prince', 'princess', 'prodigy', 'quick',
    'radiant', 'rebel', 'rebellious', 'reserved', 'restless', 'saint', 'savage',
    'scared', 'scholar', 'selfish', 'sensitive', 'sharp', 'short', 'silly',
    'singer', 'skinny', 'slender', 'spirited', 'spitfire', 'spoiled',
    'stubborn', 'student', 'sunny', 'superhero', 'superstar', 'sweet',
    'sweetheart', 'sweetie', 'talented', 'tender', 'terror', 'thoughtful',
    'tiger', 'treat', 'trusting', 'tyrant', 'vulnerable', 'woman', 'wonderful',
    'youthful'
    ]


## We'll only keep candidates that start with these sequences. I commented out
## those which are redundant; e.g., N could start with "en" or "in", but we need
## to keep all words starting with "e*" anyway to accommodate words like "evil"
## or "emergency", and "i*" for words like "identical"
start_letters = [
    "a", #A; "ei"
    "be", "bi", #B
    "ce", "ci", "se", "si", #C
    "de", "di", "dy", #D
    "e", "i", #E; "ee"
    #F; "ef", "eph"
    "gee", "gi", "jee", "ji", #G
    #H; "ai", "ay", "ei", "ey"
    "i", #I; "ai", "ay"
    "ja", "jei", "dza", "zh", "dj", #J
    "ca", "que", "ka", "ke", #K
    #L; "el"
     #M; "em"
    #N; "en", "in"
    "o", #O
    "pe", "pi", #P
    "cu", "ku", #Q
    #R; "ar"
    #S; "es"
    "te", "ti", #T
    "u", "yu", "you", #U; "ew"
    "ve", "vi" #V
    #X; "ex", "ecks", "ecc"
    "why", "wy", #Y
    "ze", "zi" #X
    ]


## Finds top n most similar words for each seed word
def get_similar_words(word_vectors: Type[KeyedVectors],
                      seed_word: str, n_synonyms: int=300) -> None:
    result_words = []
    results = word_vectors.most_similar(topn=300, positive=[seed_word])
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
    return all_results


## This applies the puzzle rules, at least roughly. We only keep candidates that
## start with an allowed sequence of letters (start_letters); We only keep
## those with a hyphen; We only keep those candidates that are between 7 and 11
## letters---this is my guess at a range that would accommodate the rule:
## "sounds like three letters spoken one after the other"
def my_rule_filters(some_list, starters):
    keepers = []
    some_list = [w for w in some_list if w[:2] in starters]
    for wd in some_list:
        if "-" in wd:
            if not re.search("\d", wd):
                if 6 < sum(c.isalpha() for c in wd) < 12:
                    keepers.append(wd)
    return keepers


def main():
    all_candidates=[]
    for vec_model_name in vec_models:  ## use each model to generate candidates
        print("\n#####################################################\n")
        print("Loading model "+vec_model_name+"...\n")
        vmodel = api.load(vec_model_name)
        print("Generating candidate words from these seed words:\n")
        all_candidates+=run_seed_list(vmodel, seed_words)
    filtered_candidates = my_rule_filters(all_candidates, start_letters)
    print("\n#####################################################\n",
          "These are the candidates most likely to be the solution:\n")
    filtered_candidates = list(set(filtered_candidates))
    filtered_candidates.sort()
    print(len(filtered_candidates))
    for fc in filtered_candidates:
        print(fc)


if __name__ == "__main__":
    main()
