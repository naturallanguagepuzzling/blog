#!/usr/bin/env python

## 2024/12/02. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/12/01 Sunday Puzzle:
## https://www.npr.org/2024/11/30/nx-s1-5204460/sunday-puzzle-cyber-monday-categories
## That puzzle:

"""
This week's challenge comes from the crossword constructor and editor Peter
Gordon. Think of a classic television actor -- first and last names. Add a
long-E sound at the end of each name and you'll get two things that are worn
while sleeping. What are they?
"""

## I'm using this g2p (grapheme to phoneme) python library:
## https://github.com/Kyubyong/g2p

from g2p_en import G2p
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


frame = 'I usually sleep in my pajamas or my __1__, but last night I slept in my __2__.'

def pron_mod(mypron):
    mypron = mypron.replace('0', '')
    mypron = mypron.replace('1', '')
    mypron = mypron.replace('2', '')
    return mypron

def create_cmu_p2g():
    cmu_file = '../annex/cmudict-master/modified-cmudict-dict.txt'
    # cmu_file = '../annex/cmudict-master/my-sample-dict.txt'
    p2g = {}
    with open(cmu_file, 'r') as cf:
        cmu_raw = cf.readlines()
        cmu_raw = [l.strip() for l in cmu_raw]
    for cr in cmu_raw:
        cr = cr.split(' ', 1)
        wd = cr[0]
        pron = cr[1]
        pron = pron_mod(pron).strip()
        if pron not in p2g:
            p2g[pron] = [wd]
        else:
            p2g[pron].append(wd)
    return p2g

def get_actors():
    actors_file = './resources/1200_actors_male_and_female.txt'
    with open(actors_file, 'r') as af:
        actorx = af.readlines()
    actorx = [p.strip() for p in actorx]
    actors = []
    for p in actorx:
        p = p.split(' ')
        actors.append(" ".join([p[0], p[-1]]))
    actors = list(filter(None, actors))
    return actors

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
    actors = get_actors()
    # actors = ['Hal Holbrook', 'Haley Osment', 'Nick Cage', 'Ted Knight', 'Bob Knight', 'Harrison Ford', 'Helena Carter', 'Henry Cavill']
    model, tokenizer = load_model('gpt2')
    g2p = G2p()
    p2g = create_cmu_p2g()
    # print("\n\nTED RESULTS")
    # print(p2g['T EH D'])
    ranked = []
    for actr in actors:
        # print("\n$\n\n"+actr)
        acr = actr.split(" ")
        first = acr[0]
        last = acr[1]
        firstpron = g2p(first)
        firstpron.append('IY')
        firstpron = ' '.join(firstpron)
        firstpron = pron_mod(firstpron)
        lastpron = g2p(last)
        lastpron.append('IY')
        lastpron = ' '.join(lastpron)
        lastpron = pron_mod(lastpron)
        if firstpron in p2g:
            firstcands = p2g[firstpron]
        else:
            firstcands = [None]
        if lastpron in p2g:
            lastcands = p2g[lastpron]
        else:
            lastcands = [None]
        if firstcands != [None] and lastcands != [None]:
            for f in firstcands:
                for l in lastcands:
                    sentence = frame.replace('__1__', f)
                    sentence = sentence.replace('__2__', l)
                    score = sent_scoring((model, tokenizer), sentence)
                    if score < 4.5:
                        ranked.append([score, actr, f, l, sentence])
        else:
            pass
    ranked.sort()
    for r in ranked:
        print('\t'.join([f"{r[0]:.3f}", r[1], r[2], r[3], r[4]]))

if __name__ == '__main__':
    main()
