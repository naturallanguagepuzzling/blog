#!/usr/bin/env python


## 2024/02/26. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/02/25 Sunday Puzzle:
## https://www.npr.org/2024/02/25/1233435347/sunday-puzzle-hidden-figures-in-two-word-phrases

"""
This week's challenge: This week's challenge comes to us from listener 
Eric Berlin of Milford, Connecticut. Take the word SETS. You can add a 
three-letter word to this twice to get a common phrase: SPARE PARTS. Can 
you now do this with the word GENIE, add a three-letter word to it twice 
to get a common phrase. Again, start with GENIE, insert a three-letter 
word twice, get a common phrase.
"""

from datetime import datetime
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import itertools
import string
import torch

print(datetime.now())

# Initialize the model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

mystring = "genie"
## get a list of tuples containing all usable pairs of indices in the string
combinations = list(itertools.combinations([x for x in range(0,len(mystring)+1)], 2))

## These are the top 50 most frequent 3-letter words found in the English Wikipedia.
## Derived from: https://github.com/IlyaSemenov/wikipedia-word-frequency/blob/master/results/enwiki-2023-04-13.txt
mywords = [
           'the', 'and', 'was', 'for', 'his', 'are', 'had', 'has', 'its', 
           'she', 'new', 'one', 'her', 'who', 'but', 'not', 'two', 'all', 
           'may', 'him', 'out', 'can', 'war', 'won', 'end', 'use', 'due', 
           'now', 'day', 'age', 'did', 'any', 'set', 'own', 'law', 'led', 
           'art', 'cup', 'son', 'top', 'old', 'air', 'off', 'six', 'way', 
           'act', 'you', 'few', 'win', 'men'
           ]
testphrases = ['okie dokie', 'bacon grease', 'never mind', 'penny farthing', 'hggwh yzqepm', 'bdtjkll kkqqkn']

def insert_string(original, new, index):
    # Create a new string with the  substring inserted at the specified index
    modified = original[:index] + new + original[index:]
    return modified

def getPerplexity(phrase):
    sentenceframe = ["I asked my cousin about the phrase, '", "', and she told me to ask you."]
    sentence = sentenceframe[0]+phrase+sentenceframe[1]
    inputs = tokenizer(sentence, return_tensors='pt')
    outputs = model(**inputs, labels=inputs['input_ids'])
    loss = outputs.loss
    perplexity = torch.exp(loss)
    return perplexity

## our perplexity threshold; any phrase that scores below the threshold will 
## be saved for the user to review
threshold = 53
possible_solutions = []

wn = 0
for wd in mywords:
    wn += 1
    print(wn, wd)
    for cb in combinations:
        newstring = insert_string(mystring, wd, cb[1])
        newstring = insert_string(newstring, wd,cb[0])
        for i in range(1, len(newstring)):
            phrase = insert_string(newstring, " ", i)
            iperp = getPerplexity(phrase)
            if iperp < threshold:
                possible_solutions.append((iperp.item(), wd, phrase))

## add the testcases-- this will help us find the appropriate threshold
for tp in testphrases:
    tperp = getPerplexity(tp)
    possible_solutions.append((tperp.item(), "###", tp))

## sort the possible solutions from lowest to highest perplexity.
## lower perplexity means "more probable".
possible_solutions.sort()
## print the sorted possibilities for the user to review.
for ps in possible_solutions:
    print(ps[1], '\t', ps[2], '\t', ps[0])

print(datetime.now())
