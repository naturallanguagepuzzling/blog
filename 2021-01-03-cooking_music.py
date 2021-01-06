#!/usr/bin/env python


## 2021/01/04. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/1/3 Sunday Puzzle:
## https://www.npr.org/2021/01/03/952835449/sunday-puzzle-new-names-in-2020


import re
import gensim.downloader as api
from gensim.models import KeyedVectors
from typing import Type


vec_models = ['glove-wiki-gigaword-100', 'glove-wiki-gigaword-300',
              'word2vec-google-news-300', 'glove-twitter-200',
              'fasttext-wiki-news-subwords-300',
              'conceptnet-numberbatch-17-06-300']

cooking_seeds = ['arabic', 'atkins', 'bain-marie', 'bake', 'baked', 'baking',
                 'barbecue', 'barbecuing', 'blacken', 'blackening', 'blanch',
                 'blanching', 'boil', 'boiling', 'braise', 'braising',
                 'brazilian', 'broil', 'brown', 'browning', 'cajun', 'candied',
                 'casserole', 'cave-man', 'caveman', 'charbroil',
                 'charbroiling', 'chicken-fried', 'chinese', 'clambake',
                 'coddle', 'coddling', 'convection', 'cookoff', 'cook-off',
                 'cookout', 'cook-out', 'country-fried', 'country-style',
                 'creaming', 'cure', 'curing', 'dairy-free', 'decoction',
                 'deep-fried', 'deep-fry', 'dehydrate', 'detox', 'dry-roast',
                 'dry-roasting', 'dutch', 'ethiopian', 'ethnic', 'european',
                 'fat-free', 'ferment', 'fermenting', 'flambe', 'flame-broil',
                 'flat-top', 'french', 'fricassee', 'fruitarianism', 'fry',
                 'frying', 'german', 'gluten-free', 'greek', 'griddle', 'grill',
                 'grilled', 'grilling', 'halal', 'high-fat', 'home-style',
                 'hotpot', 'indian', 'infusion', 'italian', 'japanese',
                 'jewish', 'korean', 'kosher', 'low-carb', 'low-glycemic',
                 'low-heat', 'low-salt', 'macrobiotic', 'marinate', 'meal-kit',
                 'mediterranean', 'microwave', 'microwaving', 'middle-eastern',
                 'oaxacan', 'open-fire', 'open-pit', 'paleo', 'parboil',
                 'parboiling', 'pescetarian', 'pickle', 'pickled', 'pickling',
                 'plant-based', 'poach', 'poaching', 'pot-luck', 'raw-food',
                 'reduce', 'reduction', 'regional', 'roast', 'roasted',
                 'roasting', 'rotisserie', 'saute', 'sauteing', 'sear',
                 'searing', 'simmer', 'simmering', 'skewered', 'slow-carb',
                 'smoke', 'smoking', 'soul-food', 'sous-vide', 'steam',
                 'steaming', 'steep', 'steeping', 'stew', 'stewed', 'stewing',
                 'stir-fry', 'sun-dried', 'superfood', 'tex-mex', 'thai',
                 'toast', 'toasting', 'turkish', 'vegan', 'vegetarian',
                 'vietnamese']

music_seeds = ['a-capella', 'acapella', 'acoustic', 'adagio', 'allegro',
               'anthem', 'anthemic', 'aria', 'ballad', 'barbershop', 'bassy',
               'be-bop', 'beat-box', 'beatbox', 'bluegrass', 'blues', 'bluesy',
               'brassy', 'choir', 'choral', 'chromatic', 'country', 'crooner',
               'cumbia', 'decrescendo', 'discordant', 'doo-wop', 'doowop',
               'falsetto', 'flamenco', 'folk', 'fortissimo', 'funk', 'funky',
               'harmonic', 'harmonious', 'harmony', 'hip-hop', 'instrumental',
               'jazz', 'jazzy', 'karaoke', 'klezmer', 'libretto', 'march',
               'mariachi', 'melody', 'melodious', 'metal', 'opera', 'operatic',
               'operetta', 'orchestral', 'pentatonic', 'percussive',
               'pianissimo', 'polyphonic', 'punk', 'ragtime', 'rap', 'rapping',
               'reedy', 'reggae', 'rhythmic', 'rondo', 'salsa', 'scherzo',
               'shanty', 'sonata', 'sonata', 'symphonic', 'tonal', 'up-beat',
               'upbeat', 'vibrato', 'vocal', 'waltz', 'yodeling']


## Finds top 1000 most similar words for each seed word
def get_similar_words(word_vectors: Type[KeyedVectors],
                      seed_word: str, n_synonyms: int=2000) -> None:
    result_words = []
    results = word_vectors.most_similar(topn=2000, positive=[seed_word])
    for r in results[:n_synonyms]:
        result_words.append(r[0].lower())
        # print(f"{r[0]:<15}: {r[1]:.3f}")
    return result_words


## Runs every seed word in a list, combines all results into a flat list of types
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


## some predicted "words" are numerals or contain numerals; this removes them
def remove_numerals(some_words):
    non_numerals = []
    for sw in some_words:
        if re.search('\d', sw):  ## remove numerals
            pass
        elif '--' in sw:  ## remove strings with unwanted characters/sequences
            pass
        elif '/' in sw:
            pass
        elif '#' in sw:
            pass
        else:
            non_numerals.append(sw)
    return non_numerals


## for the cooking words, we only want to keep those with a hyphen
def hyphenated_only(some_words):
    some_words = [j for j in some_words if "-" in j]
    return some_words


## keep words of given length; 8 for cooking (7 letters + hyphen); 7 for music
def filter_for_length(some_words, target_length):
    # print(some_words)
    flw = [x for x in some_words if len(x.strip())==target_length]
    return(flw)


def find_matches(cooking, music):
    matches = []
    for cw in cooking:
        cz = cw.replace("-", "")
        for mw in music:
            if cz[:3]==mw[:3]:
                if cz[3]!=mw[3]:
                    if cz[4:]==mw[4:]:
                        print("Found a cooking word and music word that match "
                              "the pattern:")
                        print(cw, mw)
                        matches.append([cw, mw])
    return matches
## Uncomment to run in interactive mode (comment out main() below)
# while True:
#     seed = input("Enter a seed word: ")
#     rw = get_similar_words(word_vectors, seed_word=seed)
#     for h in rw:
#         print(h)


def main():
    # print("\nCollecting similar words for these cooking seed words:")
    all_cooking_results = list(cooking_seeds)  ## add seeds to candidate list
    all_music_results = list(music_seeds)
    for vec_model_name in vec_models:  ## use each model to generate candidates
        print("\n#####################################################\n")
        print("Running model "+vec_model_name+
              " to generate candidate words from seed words...\n")
        vmodel = api.load(vec_model_name)
        all_cooking_results+=run_seed_list(vmodel, cooking_seeds)
        all_music_results+=run_seed_list(vmodel, music_seeds)
    all_cooking_results = list(set(all_cooking_results))
    all_cooking_results.sort()
    all_music_results = list(set(all_music_results))
    all_music_results.sort()
    hyphenated_cooking_words = hyphenated_only(all_cooking_results)
    clean_cooking_words = remove_numerals(hyphenated_cooking_words)
    keep_cooking_words = filter_for_length(clean_cooking_words, 8)
    print("\n#####################################################\n")
    print("Keeping these 7-letter hyphenated cooking words: ("
          +str(len(keep_cooking_words))+" total)")
    print(keep_cooking_words)
    # for kc in keep_cooking_words:
    #     print(kc)
    clean_music_words = remove_numerals(all_music_results)
    keep_music_words = filter_for_length(clean_music_words,7)
    print("\n#####################################################\n")
    print("Keeping these 7-letter music words: ("
          +str(len(keep_music_words))+" total)")
    print(keep_music_words)
    # print("Looking for a music word that matches the pattern for these cooking "
    #       "words:")
    solutions = find_matches(keep_cooking_words, keep_music_words)
    print(solutions)


if __name__ == "__main__":
    main()
