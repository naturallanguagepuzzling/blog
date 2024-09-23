#!/usr/bin/env python


## 2024/09/23. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/09/22 Sunday Puzzle:
## https://www.npr.org/2024/09/22/nx-s1-5122457/sunday-puzzle-gp-naming-spree
## That puzzle:
"""
Take the phrase NEW TOWELS. Rearrange its nine letters to get the brand name
of a product that you might buy at a supermarket."""

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

## Note: this anagram function is adapted from this code by Raghav Gurung:
## https://gist.github.com/raghav330/9c20d66c8f07d438b6f7f28536063acc#file-anagram_solver-py

from collections import Counter

## You'll need to download and store the file as I did; I'm using the first 
## 10,000 words (lines) from this file:
## https://github.com/first20hours/google-10000-english/blob/master/20k.txt
lexfilename = "./resources/10k-lexicon.txt"
with open(lexfilename, 'r') as lexfile:
    lexicon = lexfile.read()
lexicon = [l.lower() for l in lexicon.split('\n')]

def return_anagrams(letters: str) -> list:
    global dictionary
    assert isinstance(letters,
                      str), 'Scrambled letters should only be of type string.'
    letters = letters.lower()
    letters_count = Counter(letters)
    anagrams = set()
    for word in lexicon:
        # Check if all the unique letters (TYPES) in word are in the
        # scrambled letters
        if not set(word) - set(letters):
            check_word = set()
            # Check if the count of each letter is less than or equal
            # to the count of that letter in scrambled letter input
            for k, v in Counter(word).items():
                if v <= letters_count[k]:
                    check_word.add(k)
            # Check if check_words is exactly equal to the unique letters
            # in the word of dictionary
            if check_word == set(word):
                anagrams.add(word)
    anagrams.remove('')
    return sorted(list(anagrams), key=lambda x: len(x))

def reanagram(original_string, single_anagrams):
    doubles = []
    for n in single_anagrams:
        l = n.replace(" ", "")
        ogletters = list(original_string)
        sgletters = list(l)
        while sgletters:
            s = sgletters.pop(0)
            if s in ogletters:
                ogletters.remove(s)
        remainders = return_anagrams(''.join(ogletters))
        for r in remainders:
            if r+' '+n not in doubles:
                doubles.append(r+' '+n)
            if n+' '+r not in doubles:
                doubles.append(n+' '+r)
    return doubles

def load_model(model_string):
    tokenizer = GPT2Tokenizer.from_pretrained(model_string)
    model = GPT2LMHeadModel.from_pretrained(model_string)
    model.eval()
    return model, tokenizer

def sent_scoring(model_tokenizer, text):
    model = model_tokenizer[0]
    tokenizer = model_tokenizer[1]
    input_ids = torch.tensor(tokenizer.encode(text)).unsqueeze(0)  # Batch size 1
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
    loss = outputs[0]
    # logits = outputs [1]
    sentence_prob = loss.item()
    return sentence_prob


def main():
    model, tokenizer = load_model('gpt2')
    original_string = 'NEWTOWELS'.lower()
    singles = return_anagrams(original_string)
    doubles = reanagram(original_string, singles)
    triples = reanagram(original_string, doubles)
    singles = [s for s in singles if len(s.replace(" ", ""))==9]
    doubles = [d for d in doubles if len(d.replace(" ", ""))==9]
    triples = [t for t in triples if len(t.replace(" ", ""))==9]
    results = singles+doubles+triples
    results = list(set(results))
    ranked = []
    frame = "I prefer to buy name brands like __1__ that can be found in supermarkets everywhere."
    for r in results:
        sentence = frame.replace("__1__", r)
        score = sent_scoring((model, tokenizer), sentence)
        if score < 1000:
            ranked.append([score, sentence])
    ranked.sort(reverse=True)
    for rk in ranked:
        print(rk[0], "\t", rk[1])

if __name__ == '__main__':
    main()
