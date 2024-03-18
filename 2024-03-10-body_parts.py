#!/usr/bin/env python


## 2024/03/11. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/03/10 Sunday Puzzle:
## https://www.npr.org/2024/03/17/1238827590/sunday-puzzle-beware-the-ides-of-march
## That puzzle:
"""
This week's challenge: Take a body part, add a letter at beginning and end to
get another body part, then add another letter at beginning and end to get
something designed to affect that body part.
"""


import pandas as pd
from pytorch_pretrained_bert import BertTokenizer,BertForMaskedLM
import torch
import math
import os
import itertools
from nltk.corpus import words


tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bertMaskedLM = BertForMaskedLM.from_pretrained('bert-base-uncased')
bertMaskedLM.eval()
script_dir = os.path.dirname(__file__)
letter_permutations = itertools.permutations('abcdefghijklmnopqrstuvwxyz', 2)


bodyparts = ['abdomen', 'adrenal', 'ankle', 'anus', 'aorta', 'appendix', 'arch', 'arm', 'artery', 'astragalus', 'atlas', 'axis', 'back', 'backbone', 'belly', 'bladder', 'blood', 'bone', 'brachial', 'brain', 'brainstem', 'breastbone', 'bronchus', 'buttock', 'calcaneus', 'calf', 'canine', 'capillary', 'carotid', 'carpal', 'cerebrum', 'cervical', 'cervix', 'cheek', 'chest', 'chin', 'clavicle', 'coccyx', 'collarbone', 'colon', 'cranium', 'cuboid', 'diaphragm', 'duodenum', 'ear', 'elbow', 'epididymis', 'esophagus', 'ethmoid', 'eye', 'eyebrow', 'eyelash', 'eyelid', 'face', 'fallopian', 'femoral', 'femur', 'fibula', 'finger', 'fist', 'foot', 'forearm', 'forehead', 'gallbladder', 'gland', 'groin', 'gum', 'hair', 'hamstring', 'hand', 'head', 'heart', 'heel', 'hip', 'humerus', 'ileum', 'ilium', 'incisor', 'intestine', 'iris', 'ischium', 'jaw', 'jejunum', 'joint', 'jugular', 'kidney', 'knee', 'kneecap', 'knuckle', 'larynx', 'leg', 'lip', 'liver', 'lumbar', 'lung', 'lymph', 'mandible', 'mastoid', 'maxilla', 'metacarpal', 'metatarsal', 'molar', 'mouth', 'muscle', 'nail', 'nasal', 'navel', 'navicular', 'neck', 'nerve', 'node', 'nose', 'nostril', 'occiput', 'ovary', 'palm', 'pancreas', 'parathyroid', 'patella', 'pelvis', 'penis', 'peroneal', 'phalange', 'pineal', 'pinky', 'pituitary', 'prostate', 'pubis', 'pupil', 'radial', 'radius', 'rectum', 'retina', 'rib', 'sacrum', 'scapula', 'sesamoid', 'shin', 'shoulder', 'sinus', 'skin', 'skull', 'sole', 'sphenoid', 'spine', 'spleen', 'sternum', 'stomach', 'subclavian', 'talus', 'tarsal', 'teeth', 'temples', 'tendon', 'testes', 'thigh', 'thoracic', 'throat', 'thumb', 'thymus', 'thyroid', 'tibia', 'toe', 'tongue', 'tooth', 'trachea', 'ulna', 'ulnar', 'urethra', 'uterus', 'vagina', 'vein', 'waist', 'wrist', 'xiphoid', 'zygomatic']


def get_pairs(mylist):
    mypairs = []
    for x in mylist:
        for y in mylist:
            if y != x:
                if x[1:-1] == y:
                    mypairs.append((y,x))
    return mypairs


## Call BERT (language model) to evaluate the probability of the sentence;
def get_score(sentence):
    tokenize_input = tokenizer.tokenize(sentence)
    tensor_input = torch.tensor([tokenizer.convert_tokens_to_ids(tokenize_input)])
    # predictions=bertMaskedLM(tensor_input)
    predictions=bertMaskedLM(tensor_input)
    loss_fct = torch.nn.CrossEntropyLoss()
    loss = loss_fct(predictions.squeeze(),tensor_input.squeeze()).data 
    return math.exp(loss)


## For each candidate pair, slot the relevant strings into the templates to form
## sentences; these sentences are passed to BERT for a score, and the average is
## returned for the pair
def score_pair(cpr):
    aa = cpr[0]
    awd = aa.split(" ")[0]
    bb = cpr[1]
    templates = [
        ["on tuesday,", bb, "announced plans to acquire", awd, "next quarter"],
        ["the", bb, "share price dipped due to a shortage of", awd],
        [bb, "has begun receiving regular shipments of", awd],
        ["due to the increased availability of", awd, "last year,", bb, "had its most productive quarter in three years"],
        [bb, "announced plans to purchase", awd, "from a new supplier"],
        [bb, "is looking for more", awd],
        ["companies like", bb, "can't get enough", awd]
        ]
    prscore = 0.0
    for tp in templates:
        tpcsent = " ".join(tp)
        prscore += get_score(tpcsent)
    pravg = prscore/float(len(templates))
    return pravg


def check_permutations(somecandidates):
    keepers = []
    for candpair in somecandidates:
        cand = candpair[1]
        print("\n\ncand: ", cand)
        for lp in letter_permutations:
            newcand = lp[0]+cand+lp[1]
            print(newcand)
            if newcand.lower() in words.words():
                keepers.append((candpair[0], candpair[1], newcand))
    return keepers


def main():
    for wd in words.words():
        for bp in bodyparts:
            if bp != wd:
                if len(wd) in range(len(bp)+2, len(bp)+3):
                    if bp in wd:
                        print(bp, wd)


if __name__ == "__main__":
    main()
