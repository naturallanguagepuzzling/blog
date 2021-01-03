#!/usr/bin/env python


## 2021/01/02. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2020/12/20 Sunday Puzzle:
## https://www.npr.org/2020/12/20/948348016/sunday-puzzle-christmas-capitals

## The "predict_masked_sent" function below was copied and adapted from:
## https://gist.githubusercontent.com/yuchenlin/
## a2f42d3c4378ed7b83de65c7a2222eb2/raw/
## c83fbf49f19f06034633a8508804a16eb399172e/masked_word_prediction_bert.py

import torch
from transformers import BertTokenizer, BertModel, BertForMaskedLM
import logging
logging.basicConfig(level=logging.INFO)# OPTIONAL


tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
model.eval()
# model.to('cuda')  # if you have gpu

## We use this list to query our BERT model.
## We expect the words in the solution to appear in contexts like "[MASK]" here.
my_queries = ["All I want for Christmas is [MASK]",
            "All I want for Christmas is a [MASK]",
            "[MASK] are selling out this Christmas",
            "sold out of [MASK] this Christmas",
            "I'm wishing for [MASK] this Christmas",
            "I'm wishing for a [MASK] this Christmas",
            "I got [MASK] for Christmas",
            "I got a [MASK] for Christmas",
            "Classic Christmas gifts like [MASK] and ",
            "[MASK] is the hottest Christmas gift",
            "I wish for [MASK] this Christmas",
            "asked Santa Claus for [MASK]",
            "asked Santa for [MASK]",
            "asked Santa Claus for a [MASK]",
            "asked Santa for a [MASK]",
            "best Christmas gift was [MASK]",
            "Christmas gift was a [MASK]",
            "gave me a [MASK] for Christmas",
            "gave me [MASK] for Christmas",
            "the gift of [MASK] this Christmas"
            ]


## This function will take in a masked sentence and return a list of predictions
def predict_masked_sent(text, top_k=100):
    # Tokenize input
    my_words = []
    text = "[CLS] %s [SEP]"%text
    tokenized_text = tokenizer.tokenize(text)
    masked_index = tokenized_text.index("[MASK]")
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    tokens_tensor = torch.tensor([indexed_tokens])
    # tokens_tensor = tokens_tensor.to('cuda')    # if you have gpu
    # Predict all tokens
    with torch.no_grad():
        outputs = model(tokens_tensor)
        predictions = outputs[0]
    probs = torch.nn.functional.softmax(predictions[0, masked_index], dim=-1)
    top_k_weights, top_k_indices = torch.topk(probs, top_k, sorted=True)
    for i, pred_idx in enumerate(top_k_indices):
        predicted_token = tokenizer.convert_ids_to_tokens([pred_idx])[0]
        token_weight = top_k_weights[i]
        # print("[MASK]: '%s'"%predicted_token, " | weights:", float(token_weight))
        # print(predicted_token)
        my_words.append(predicted_token)
    return my_words
   
     
## Runs all queries, generating 2000 candidates for each;
## returns a list of unique candidate words
def get_all_words(my_queries):
    all_words = []
    for mm in my_queries:
        all_words += predict_masked_sent(mm, top_k=100)
        all_words = list(set(all_words))
    return(all_words)    


## Removes any candidate words outside our target length of 3-7 letters
def filter_for_length(some_words):    
    flw = [x for x in some_words if 2 < len(x) < 8]
    return(flw)


## Removes any word that cannot be spelled from our list of letters
def filter_for_characters(some_words):
    my_chars = ["b", "u", "e", "n", "o", "s", "a", "i", "r", "e", "s"]
    fcw = []
    for sw in some_words:
        keep = "yes"
        current_chars = list(my_chars)
        sw_chars = list(sw)
        for swc in sw_chars:
            if swc not in current_chars:
                keep = "no"
                break
            else:
                current_chars.remove(swc)
        if keep == "yes":
            fcw.append(sw)
    fcw.sort()
    return(fcw)

 
 ## Finds pairs of words where the length sums to 10
def find_pairs_sum_ten(good_words):
    sum_ten = []
    while good_words:
        gwa = good_words.pop(0)
        for gwb in good_words:
            if len(gwa)+len(gwb) == 10:
                sum_ten.append([gwa, gwb])
            else:
                pass
    return(sum_ten)
 

def filter_buenos_aires_pairs(some_pairs):
    ba_pairs = []
    my_chars = ["b", "u", "e", "n", "o", "s", "a", "i", "r", "e", "s"]
    for sp in some_pairs:
        keep = "yes"
        spp = sp[0]+sp[1]
        current_chars = list(my_chars)
        spp_chars = list(spp)
        for sppc in spp_chars:
            if sppc not in current_chars:
                keep = "no"
                break
            else:
                current_chars.remove(sppc)
        if keep == "yes":
            ba_pairs.append(sp)
    return(ba_pairs)
 

def main():
    all_words = get_all_words(my_queries)
    fl_words = filter_for_length(all_words)
    fc_words = filter_for_characters(fl_words)
    ten_sums = find_pairs_sum_ten(fc_words)
    buenos_pairs = filter_buenos_aires_pairs(ten_sums)
    print(len(buenos_pairs))
    for bp in buenos_pairs:
        print(bp)


if __name__ == "__main__":
    main()
