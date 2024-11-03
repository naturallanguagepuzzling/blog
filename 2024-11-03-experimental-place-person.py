#!/usr/bin/env python


## 2024/11/03. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/11/03 Sunday Puzzle:
## https://www.npr.org/2024/11/02/nx-s1-5166133/sunday-puzzle-can-you-guess-these-words-from-these-phonetic-clues
## That puzzle:
"""
This week's challenge comes from listener Mark Maxwell-Smith. Name a place 
where experiments are done (two words). Drop the last letter of each word. 
The remaining letters, reading from left to right, will name someone 
famously associated with experiments. Who is it?
"""

import itertools
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


p1 = ['laboratory', 'research', 'testing', 'experimental', 'experiment', 'science', 'control', 'test', 'clinical', 'physics', 'chemistry', 'biology', 'data', 'computer', 'computing']
p2 = ['room', 'lab', 'laboratory', 'facility', 'site', 'chamber', 'observatory', 'center']
frame = '__1__ was a famous scientist known for experiments.'


def get_places(pt1, pt2):
    places = list(itertools.product(pt1, pt2))
    places = [' '.join(p) for p in places]
    return places

def apply_puzzle_transformation(pstr):
    p1, p2 = pstr.split(' ')[0], pstr.split(' ')[1]
    p1 = p1[:-1]
    p2 = p2[:-1]
    f = ''.join([p1, p2])
    f = f.capitalize()
    return f

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
    sentence_prob = loss.item()
    return sentence_prob


def main():
    places = get_places(p1, p2)
    model, tokenizer = load_model('gpt2')
    ranked = []
    for plc in places:
        tf = apply_puzzle_transformation(plc)
        sentence = frame.replace('__1__', tf)
        score = sent_scoring((model, tokenizer), sentence)
        if score < 10:
            ranked.append([score, plc, tf])
    ranked.sort()
    for r in ranked:
        # print('\t'.join([str(r[0]), r[1], r[2]]))
        print('\t'.join([f"{r[0]:.2f}", r[1], r[2]]))


if __name__ == '__main__':
    main()
