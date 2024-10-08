#!/usr/bin/env python


## 2024/10/07. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/10/06 Sunday Puzzle:
## https://www.npr.org/2024/10/05/nx-s1-5137981/sunday-puzzle-phonetic-fun
## That puzzle:
"""
This week's challenge comes from listener Joe Krozel, of Creve Coeur, MO.
Think of a place in America. Two words, 10 letters altogether. The first
five letters read the same forward and backward. The last five letters spell
something found in the body. What place is this?
"""

import torch
from slugify import slugify
from transformers import GPT2LMHeadModel, GPT2Tokenizer


## I'm using a large tsv file containing only two columns: place name, US State;
## I've extracted it from the much larger file downloadable here:
## https://osmnames.org/download/
## See my blog entry for more details on deriving the file.
usa_places_file = '../annex/usa-places.tsv'
with open(usa_places_file, 'r') as placefile:
    usa_places = placefile.readlines()
usa_places = [p.strip() for p in usa_places]
usa_places = list(filter(None, usa_places))
frames = [
    'In anatomy class, students learn about all the things inside the body, like bones and __1__.',
    'Each anatomy lesson focuses on a new part of the body, like a bone or a __1__.'
    ]


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

def clean_string(ugly):
    # print("0: ", ugly)
    ugly = ugly.strip()
    ugly = ugly.split(" ")
    # print("1: ", ugly)
    ugly = [slugify(g) for g in ugly]
    # print("2: ", ugly)
    ugly = [g.replace('-', '') for g in ugly]
    # print("3: ", ugly)
    ugly = " ".join(ugly)
    # ugly = "".join([l for l in ugly if l.isalpha()])
    # print("4: ", ugly)
    return ugly

def check_first_five(mystring):
    mystring = mystring.replace(' ', '').lower()
    myfive = mystring[:5]
    return myfive == myfive[::-1]

def get_10_letter_place_names(allplaces):
    candidate_places = []
    for place in allplaces:
        place = place.lower()
        ps = place.split('\t')
        ps = [p.strip() for p in ps]
        ps = list(filter(None, ps))
        if len(ps) == 2:
            p1 = clean_string(ps[0])
            p1s = p1.split(' ')
            p1s = list(filter(None, p1s))
            if len(p1s) == 2:
                p1j = ''.join(p1s)
                if len(p1j) == 10:
                    candidate_places.append(p1j)
                else: pass
            elif len(p1s) == 1:
                p1j = p1s[0]
                if len(p1j) <= 6: ## total string is 2 words, 10 letters; shortest state names are 4 letters (ohio, iowa), so if we are combining the place name with the state name, the first part can be at most 6 letters. 
                    p2 = ps[1].replace(' ', '').lower()
                    if len(p1j) + len(p2) == 10:
                        candidate_places.append(p1j+p2)
            else: pass
        else: pass
    return candidate_places


def main():
    candidate_places = get_10_letter_place_names(usa_places)
    candidate_places = list(set(candidate_places))
    palindromes = []
    for cand in candidate_places:
        # print(cand)
        if check_first_five(cand) == True:
            palindromes.append(cand)
            # print(cand+" :  "+cand[5:])
    model, tokenizer = load_model('gpt2')
    ranked = []
    for pal in palindromes:
        for frame in frames:
            sentence = frame.replace('__1__', pal[5:])
            score = sent_scoring((model, tokenizer), sentence)
            if score < 10:
                ranked.append([score, sentence, pal])
    ranked.sort(reverse=True)
    for rk in ranked:
        print(f'{rk[0]:.4f}', '\t', rk[1], '\t', rk[2])

if __name__ == '__main__':
    main()
