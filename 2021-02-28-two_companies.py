#!/usr/bin/env python


## 2021/03/02. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/02/28 Sunday Puzzle:
# https://www.npr.org/2021/02/28/972103220/sunday-puzzle-you-got-an-a
## That puzzle:
"""
This week's challenge comes from Joseph Young of St. Cloud, Minn. I'm looking for
the names of two companies. One of them has a two-part name (5,5). The other has
a three-part name (5,7,5). The last five-letter part of the two names is the
same. And the first five-letter part of the first company's name is something
the second company wants. What is it?
"""


import pandas as pd
from os import walk


from pytorch_pretrained_bert import BertTokenizer,BertForMaskedLM
import torch
import math


tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bertMaskedLM = BertForMaskedLM.from_pretrained('bert-base-uncased')
bertMaskedLM.eval()



## For every name in our list, we want to try dropping these words before we
## check for a (5,5) or (5,7,5) match
optional_wds = [
    '&', 'a', 'a/s', 'ab', 'ag', 'bhd', 'branch', 'brand', 'brands', 'bv', 'cc',
    'co', 'coltd', 'companies', 'company', 'consolidated', 'corp',
    'corporation', 'cos', 'cv', 'dairies', 'dairy', 'dba', 'de', 'enterprise',
    'enterprises', 'foods', 'gk', 'gmbh', 'group', 'grp', 'holdings', 'inc',
    'incorporated', 'industries', 'international', 'intl', 'intl.', 'kg', 'kk',
    'limited', 'llc', 'ltd', 'manufacturing', 'mbh', 'mfg', 'ooo', 'partners',
    'partnership', 'pte', 'pty', 'rl', 's', 'sa', 'sarl', 'sas', 'sau', 'sdn',
    'service', 'services', 'spa', 'srl', 'sro', 'studio', 'studios', 'svcs',
    'too', 'tov', 'trust', 'works'
    ]


## read in the list of companies from the text file
def get_starting_companies(tfn):
    mcf = open(tfn, "r")
    mwd = {}
    mwl = []
    mcj = mcf.readlines()
    mcj = [m.strip() for m in mcj if m]
    return(mcj)


## clean up the company name: remove punctuation, etc.
def preprocess_company_name(cpn):
    cpn = cpn.replace("-", " ")
    cpn = cpn.replace(".", "")
    cpn = cpn.replace(",", "")
    cpn = cpn.replace('''"''', '''''')
    cpn = cpn.replace("""'""", """""")
    cpn = cpn.replace("(", "")
    cpn = cpn.replace(")", "")
    cpn = cpn.lower()
    if cpn.startswith("the "):
        cpn = cpn.replace("the ", "")
    return cpn


## from a company name, create a list of alternate versions by removing the
## optional words ("corp", "inc", etc)
def get_alts(mylist):
    alts = []
    alts.append(mylist)
    while mylist:
        mylist = mylist.split(" ")
        tail = mylist.pop()
        if tail in optional_wds:
            mylist = " ".join(mylist)
            if mylist:
                alts.append(mylist)
        else:
            break
    return alts


## search the expanded list of companies for Company A (5,5) candidates
def get_company_a_candidates(comps):
    cands = []
    for c in comps:
        cws = c.split(" ")
        cws = [x.strip() for x in cws]
        if len(cws) == 2:
            if len(cws[0]) == 5:
                if len(cws[1]) == 5:
                    cands.append(c.lower())
    return cands


## search the expanded list of companies for Company B (5,7,5) candidates
def get_company_b_candidates(comps):
    cands = []
    for c in comps:
        cws = c.split(" ")
        cws = [x.strip() for x in cws]
        if len(cws) == 3:
            if len(cws[0]) == 5:
                if len(cws[1]) == 7:
                    if len(cws[2]) == 5:
                        cands.append(c.lower())
    return cands
    

## search for Company A & Company B matches
def get_company_pairs(cas, cbs):
    cps = []
    for caa in cas:
        ca = caa.split(" ")
        for cbb in cbs:
            cb = cbb.split(" ")
            if ca[1] == cb[2]:
                cps.append([caa, cbb])
    return cps


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


def main():
    mcl = get_starting_companies("resources/companies.txt")
    m_alts = []
    for mcname in mcl:
        mcname = preprocess_company_name(mcname)
        mcalts = get_alts(mcname)
        m_alts += mcalts
    candas = get_company_a_candidates(m_alts)  ## 5,5
    candbs = get_company_b_candidates(m_alts)  ## 5,7,5
    # for ca in candas: print(ca)
    # for cb in candbs: print(cb)
    cpairs = get_company_pairs(candas, candbs)
    # print(len(cpairs))
    scores = []
    for pr in cpairs:
        scores.append([score_pair(pr), pr[0], pr[1]])
    scores.sort()
    for sc in scores:
        print(sc)


if __name__ == "__main__":
    main()

