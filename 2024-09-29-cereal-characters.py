#!/usr/bin/env python


## 2024/10/02. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/09/29 Sunday Puzzle:
## https://www.npr.org/2024/09/28/nx-s1-5130002/sunday-puzzle-drugstore-scramble
## That puzzle:
"""
This week's challenge comes from listener Curtis Guy, of Buffalo, N.Y. 
Name a certain breakfast cereal character. Remove the third, fifth,
and sixth letters and read the result backward. You'll get a word that
describes this breakfast cereal character. What is it?
"""

characters = [
    'Tony Tiger', 'Tony the Tiger', 'Toucan Sam', 'Capn Crunch',
    'Lucky the Leprechaun', 'Lucky Leprechaun', 'Count Chocula',
    'Snap', 'Crackle', 'Pop', 'Trix Rabbit', 'Sugar Bear', 'Fred Flintstone',
    'Sonny the Cuckoo Bird', 'Sonny Cuckoo', 'Cocoa Puffs Bird',
    'Dig Em Frog', 'Franken Berry', 'Boo Berry', 'Honey Nut Cheerios Bee',
    'BuzzBee', 'Raisin Bran Sun', 'Quaker Oats Man', 'Apple Jacks Kids',
    'CinnaMon', 'Bad Apple', 'Cookie Crisp Crook', 'Officer Crumb',
    'Golden Crisp Bear', 'Sugar Bear', 'Smacks Frog', 'Cornelius Rooster',
    'Honeycomb Crazy Craving', 'Crazy Craving', 'Cinnamon Toast Crunch Bakers',
    'Wendell', 'Chip the Wolf', 'Big Yella', 'King Vitaman',
    'Baron Von Redberry', 'Sir Grapefellow', 'Fruit Brute', 'Yummy Mummy',
    'Cheerios Kid', 'Crazy Squares'
    ]


frames = [
    'A favorite __2__ is __1__ from the popular breafast cereal.',
    'The character __1__ is very __2__.'
    ]


import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

## Note: this anagram function is adapted from this code by Raghav Gurung:
## https://gist.github.com/raghav330/9c20d66c8f07d438b6f7f28536063acc#file-anagram_solver-py

from collections import Counter

## You'll need to download and store the file as I did; I'm using this file:
## https://github.com/IlyaSemenov/wikipedia-word-frequency/blob/master/results/enwiki-2023-04-13.txt
lexfilename = "../annex/enwiki-2023-04-13.txt"
with open(lexfilename, 'r') as lexfile:
    lexicon = lexfile.readlines()
lexicon = filter(None, lexicon)
lexicon = [l.lower() for l in lexicon]
lexicon = [x.split()[0] for x in lexicon]


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

def transform_string(mystring):
    mystring = mystring.replace(' ', '')
    mystring = mystring[:2]+mystring[3]+mystring[6:]
    candidate = mystring[::-1]
    return candidate

def main():
    mycharacters = [h for h in characters if len(h) >= 6]
    candidates = []
    for c in mycharacters:
        tc = transform_string(c.lower())
        if tc in lexicon:
            candidates.append([c, tc])
            print(c, tc)
    model, tokenizer = load_model('gpt2')
    ranked = []
    for cand in candidates:
        for frame in frames:
            sentence = frame.replace("__1__", cand[0])
            sentence = sentence.replace("__2__", cand[1])
            score = sent_scoring((model, tokenizer), sentence)
            if score < 1000:
                ranked.append([score, sentence])
    ranked.sort(reverse=True)
    for rk in ranked:
        print(rk[0], "\t", rk[1])

if __name__ == '__main__':
    main()
