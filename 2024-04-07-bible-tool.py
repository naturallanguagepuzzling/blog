#!/usr/bin/env python


## 2024/04/10. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/04/07 Sunday Puzzle:
## https://www.npr.org/2024/04/07/1243253871/sunday-puzzle-idioms-for-the-eclipse
## That puzzle:
"""
This week's challenge: This week's challenge comes from listener Steve Baggish
of Arlington, Massachusetts. Think of a nine-letter word naming a kind of tool
that is mentioned in the Bible. Remove the second and sixth letters and the
remaining letters can be rearranged to spell two new words that are included
in a well known biblical passage and are related to the area in which the tool
is used. What are the three words?
"""

import math
from nltk import pos_tag
from nltk.tokenize import word_tokenize
import os
import pythonbible as bible
from pytorch_pretrained_bert import BertTokenizer,BertForMaskedLM
import time
import torch


tool_templates = [
    'Who invented tools like the ___ ?',
    'The ___ was an improvement over more primitive tools.',
    'The ___ is a tool described in the Bible. ',
    'Do you know how to use a ___ ?'
    ]

## Load BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bertMaskedLM = BertForMaskedLM.from_pretrained('bert-base-uncased')
bertMaskedLM.eval()
script_dir = os.path.dirname(__file__)


def get_candidate_words():
    candidates = []
    file_path = 'bible_verse_ids.txt'
    with open(file_path, 'r') as file:
        for line in file:
            try:
                verse_id = int(line.strip())
                vtext = bible.get_verse_text(verse_id, version=bible.Version.KING_JAMES)
                vtext = vtext.lower()
                verse = word_tokenize(vtext)
                for wd in verse:
                    if len(wd) == 9:
                        candidates.append(wd)
            except ValueError:
                pass
                # print(f"Skipping non-integer line: {line.strip()}")
    candidates = list(set(candidates))
    candidates.sort()
    print('a,', len(candidates))
    # for c in candidates:
    #     print(pos_tag([c])[0][1])
    candidates = [c for c in candidates if pos_tag([c])[0][1] in ['NN', 'NNS']]
    print('b,', len(candidates))
    candidates += ['plowshare', 'millstone', 'slingshot', 'snickerdoodle', 'toilet', 'marathon', 'orbit', 'hilarious']
    return candidates


def get_score(sentence):
    tokenize_input = tokenizer.tokenize(sentence)
    tensor_input = torch.tensor([tokenizer.convert_tokens_to_ids(tokenize_input)])
    predictions=bertMaskedLM(tensor_input)
    loss_fct = torch.nn.CrossEntropyLoss()
    loss = loss_fct(predictions.squeeze(),tensor_input.squeeze()).data 
    return math.exp(loss)


def score_candidate(cand):
    cscore = 0.0
    for tt in tool_templates:
        candsent = tt.replace('___', cand)
        cscore += get_score(candsent)
        # cscore = get_score(candsent)
        # print(candsent, cscore)
    cavg = cscore/float(len(tool_templates))
    return cavg


def main():
    candscores = []
    print(time.ctime())
    candidates = get_candidate_words()
    print(len(candidates))
    for cand in candidates:
        score_candidate(cand)
        candavg = score_candidate(cand)
        candscores.append((candavg, cand))
    candscores.sort()
    for cs in candscores:
        print(cs)


if __name__ == "__main__":
    main()
