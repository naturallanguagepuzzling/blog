#!/usr/bin/env python


## 2021/01/04. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/1/3 Sunday Puzzle:
## https://www.npr.org/2021/01/03/952835449/sunday-puzzle-new-names-in-2020


import re
import gensim.downloader as api
from gensim.models import KeyedVectors
from typing import Type


vec_models = {
    'a' : 'glove-wiki-gigaword-100',  ## no bar-b-que
    'b' : 'glove-wiki-gigaword-300',  ## no bar-b-que
    'c' : 'word2vec-google-news-300',  ## no bar-b-que
    'd' : 'glove-twitter-200',  ## yes, found bar-b-que !
    'e' : 'fasttext-wiki-news-subwords-300',  ## yes, found bar-b-que !
    'f' : 'conceptnet-numberbatch-17-06-300'  ## no bar-b-que
    }


## Finds top n most similar words for each seed word
def get_similar_words(word_vectors: Type[KeyedVectors],
                      seed_word: str, n_synonyms: int=1000) -> None:
    result_words = []
    try:
        results = word_vectors.most_similar(topn=1000, positive=[seed_word])
        for r in results[:n_synonyms]:
            result_words.append(r[0].lower())
            # print(f"{r[0]:<15}: {r[1]:.3f}")
    except:
        print("Word not in model vocabulary.\n")
    return result_words


def main():
    target_word = 'bar-b-que'
    model_choice = 'z'
    model_keys = ['a', 'b', 'c', 'd', 'e', 'f']
    while model_choice.lower() not in model_keys:
        model_choice = input(
            "Type 'a', 'b', etc. to load a model from the menu.\n"
            "a : glove-wiki-gigaword-100\n"
            "b : glove-wiki-gigaword-300\n"
            "c : word2vec-google-news-300\n"
            "d : glove-twitter-200\n"
            "e : fasttext-wiki-news-subwords-300\n"
            "f : conceptnet-numberbatch-17-06-300\n"
            )
    vmodel = api.load(vec_models[model_choice])
    while True:
        query = input('Type a word to get similar words from the model. Type '
                      'MODEL to select new model.\n')
        if query.lower() == 'model':
            model_choice = input(
            "Type 'a', 'b', etc. to load a model from the menu.\n"
            "a : glove-wiki-gigaword-100\n"
            "b : glove-wiki-gigaword-300\n"
            "c : word2vec-google-news-300\n"
            "d : glove-twitter-200\n"
            "e : fasttext-wiki-news-subwords-300\n"
            "f : conceptnet-numberbatch-17-06-300\n"
            ).lower().strip()
            if model_choice in model_keys:
                vmodel = api.load(vec_models[model_choice])
            else:
                continue
        else:
            results = get_similar_words(vmodel, query)
            # for r in results:
            #     print(r)
            if target_word in results:
                print('Target word "'+target_word+'" FOUND among results.\n')
            else:
                print('Target word "'+target_word+'" NOT found among results.\n')


if __name__ == "__main__":
    main()
