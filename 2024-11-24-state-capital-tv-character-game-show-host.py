#!/usr/bin/env python


## 2024/11/24. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/11/24 Sunday Puzzle:
## https://www.npr.org/2024/11/23/nx-s1-5198595/sunday-puzzle-double-take-famous-names-with-repeated-letters
## That puzzle:
"""
This week's challenge comes from listener Greg VanMechelen, of Berkeley, Calif.
Name a state capital. Inside it in consecutive letters is the first name of a
popular TV character of the past. Remove that name, and the remaining letters
in order will spell the first name of a popular TV game show host of the past.
What is the capital and what are the names?
"""

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


statecaps = [
    'Montgomery', 'Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver',
    'Hartford', 'Dover', 'Tallahassee', 'Atlanta', 'Honolulu', 'Boise',
    'Springfield', 'Indianapolis', 'Des Moines', 'Topeka', 'Frankfort',
    'Baton Rouge', 'Augusta', 'Annapolis', 'Boston', 'Lansing', 'St. Paul',
    'Saint Paul', 'Jackson', 'Jefferson City', 'Helena', 'Lincoln', 
    'Carson City', 'Concord', 'Trenton', 'Santa Fe', 'Albany', 'Raleigh',
    'Bismarck', 'Columbus', 'Oklahoma City', 'Salem', 'Harrisburg',
    'Providence', 'Columbia', 'Pierre', 'Nashville', 'Austin',
    'Salt Lake City', 'Montpelier', 'Richmond', 'Olympia', 'Charleston',
    'Madison', 'Cheyenne'
    ]
frame = '__1__ is a TV character and __2__ is a TV game show host.'


def get_substrings(s):
    substrings = []
    s = s.lower()
    s = s.replace(' ', '')
    for i in range(len(s)):
        for j in range(i + 1, i + 6):
            try:
                newsub = s[i:j]
                leftover = s[:i]+s[j:]
                substrings.append((s, newsub, leftover))
            except:
                pass
    return substrings

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
    model, tokenizer = load_model('gpt2')
    ranked = []
    allcands = []
    for sc in statecaps:
        sccands = get_substrings(sc)
        allcands += [c for c in sccands]
    allcands = list(set(allcands))
    allcands.sort()
    oldheader = ''
    for sub in allcands:
        # print(sub[0])
        newheader = sub[0]
        if newheader != oldheader:
            print(newheader)
        sentence = frame.replace('__1__', sub[1].capitalize())
        sentence = sentence.replace('__2__', sub[2].capitalize())
        score = sent_scoring((model, tokenizer), sentence)
        if score < 8:
            ranked.append([score, sub[0].capitalize(), sub[1].capitalize(), sub[2].capitalize(), sentence])
        oldheader = newheader
    ranked.sort()
    for r in ranked:
        print('\t'.join([f"{r[0]:.2f}", r[1], r[2], r[3], r[4]]))


if __name__ == '__main__':
    main()



