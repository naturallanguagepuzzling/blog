#!/usr/bin/env python


## 2024/03/18. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/03/17 Sunday Puzzle:
## https://www.npr.org/2024/03/17/1238827590/sunday-puzzle-beware-the-ides-of-march
## That puzzle:
"""
This week's challenge: Our challenge comes from Emma Meersman of Seattle, 
Washington: Take two three-letter tree names and combine them phonetically
to get a clue for a type of fabric, then change one letter in that word to
get something related to trees. Your answer should be the two tree names you
started with.
"""

import pandas as pd
from os import walk
from pytorch_pretrained_bert import BertTokenizer,BertForMaskedLM
import torch
import math
import os
import itertools
from random import shuffle
# from nltk.corpus import words


tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bertMaskedLM = BertForMaskedLM.from_pretrained('bert-base-uncased')
bertMaskedLM.eval()
script_dir = os.path.dirname(__file__)

trees = [
    # 'ash', 
    # 'elm', 
    # 'fig', 
    'fir', 
    # 'gum', 
    # 'oak', 
    # 'tea', 
    # 'wax', 
    'yew',
    # 'cot', #testcase
    # 'ton', #testcase
    ]

fabric_templates = [
    'What kind of fabric is ___ ?',
    'Is herringbone more ___ than twill?', 
    'We can describe textiles according to their weave or materials, like satin weave and ___ .',
    "I'm looking for a purse for my sister and she just loves ___ , so should I choose denim, leather, houndstooth or linen?",
]

## Call BERT (language model) to evaluate the probability of the sentence;
def get_score(sentence):
    tokenize_input = tokenizer.tokenize(sentence)
    tensor_input = torch.tensor([tokenizer.convert_tokens_to_ids(tokenize_input)])
    predictions=bertMaskedLM(tensor_input)
    loss_fct = torch.nn.CrossEntropyLoss()
    loss = loss_fct(predictions.squeeze(),tensor_input.squeeze()).data 
    return math.exp(loss)


## slot the relevant strings into the templates to form sentences;
## pass to BERT for score, average across templates is returned.
def score_candidate(cand):
    cscore = 0.0
    for ft in fabric_templates:
        candsent = ft.replace('___', cand)
        cscore += get_score(candsent)
    cavg = cscore/float(len(fabric_templates))
    return cavg


def main():
    tps = itertools.permutations(trees, 2)
    treepairs = []
    for tp in tps:
        treepairs.append(tp)
    # shuffle(treepairs)
    for p in treepairs:
        pt = " ".join(p)
        print(pt)
        ptavg = score_candidate(pt)
        print(ptavg)

    # for wd in words.words():
    #     for bp in bodyparts:
    #         if bp != wd:
    #             if len(wd) in range(len(bp)+2, len(bp)+3):
    #                 if bp in wd:
    #                     print(bp, wd)

    # candidate_pairs = get_pairs(bodyparts)
    # print(candidate_pairs)
    # candidate_triples = check_permutations(candidate_pairs)
    # # candidate_triples = check_permutations([('ear', 'ear')])
    # for ct in candidate_triples:
    #     print(ct)
        

    # candas = get_company_a_candidates(m_alts)  ## 5,5
    # candbs = get_company_b_candidates(m_alts)  ## 5,7,5
    # # for ca in candas: print(ca)
    # # for cb in candbs: print(cb)
    # cpairs = get_company_pairs(candas, candbs)
    # # print(len(cpairs))
    # scores = []
    # for pr in cpairs:
    #     scores.append([score_pair(pr), pr[0], pr[1]])
    # scores.sort()
    # for sc in scores:
    #     print(sc)


if __name__ == "__main__":
    main()
