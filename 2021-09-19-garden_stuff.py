#!/usr/bin/env python


## 2021/09/20. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/09/19 Sunday Puzzle:
## https://www.npr.org/2021/09/19/1038562762/sunday-puzzle-rare-letter-swap
"""
This week's challenge comes from listener Rachel Cole of Oakland, Calif. Name
something grown in a garden. Change the second letter, and double the third
letter, to get an adjective that describes this thing. What is it?
"""

## The "predict_masked_sent" function below was copied and adapted from:
## https://gist.githubusercontent.com/yuchenlin/
## a2f42d3c4378ed7b83de65c7a2222eb2/raw/
## c83fbf49f19f06034633a8508804a16eb399172e/masked_word_prediction_bert.py

from slugify import slugify
import string, torch
from transformers import BertTokenizer, BertModel, BertForMaskedLM
import logging
logging.basicConfig(level=logging.INFO)# OPTIONAL


tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
model.eval()
# model.to('cuda')  # if you have gpu

## We use this list to query our BERT model.
## We expect the words in the solution to appear in contexts like "[MASK]" here.
raw_queries = [
    ["I grew the most [MASK] and sweet ", "xyz", " in my garden this year."],
    # ["Sunlight is the key to growing such [MASK] ", "xyz", " in most gardens."],
    # ["The ", "xyz", " from their garden tastes [MASK]."],
    # ["My neighbor grows the most [MASK] and colorful ", "xyz", " in his garden."],
    # ["How do you get your ", "xyz", " to grow so [MASK] each year?"],
    # ["It's best to harvest your ", "xyz", " when it is nice and [MASK]."],
    # ["It's best to harvest your ", "xyz", " when it is [MASK]."],
    # ["The ", "xyz", " and other fruits they grow always look so [MASK]."],
    # ["The ", "xyz", " and other vegetables they grow always look so [MASK]."],
    # ["The ", "xyz", " and other flowers they grow always look so [MASK]."],
    # ["The ", "xyz", " and other herbs they grow always look so [MASK]."],
    # ["The ", "xyz", " and other plants they grow always look so [MASK]."],
    # ["The ", "xyz", " and other fruits they grow always taste so [MASK]."],
    # ["The ", "xyz", " and other vegetables they grow always taste so [MASK]."],
    # ["The ", "xyz", " and other flowers they grow always taste so [MASK]."],
    # ["The ", "xyz", " and other herbs they grow always taste so [MASK]."],
    # ["The ", "xyz", " and other plants they grow always taste so [MASK]."],
    # ["The ", "xyz", " and other fruits they grow always smell so [MASK]."],
    # ["The ", "xyz", " and other vegetables they grow always smell so [MASK]."],
    # ["The ", "xyz", " and other flowers they grow always smell so [MASK]."],
    # ["The ", "xyz", " and other herbs they grow always smell so [MASK]."],
    # ["The ", "xyz", " and other plants they grow always smell so [MASK]."],
    ]
mygarden = [m.strip() for m in open("./resources/garden_things.txt", 'r').readlines() if m]
alphabet = list(string.ascii_lowercase)


def iterate_for_sbert(some_queries):
    mytexts = []
    for mv in mygarden:
        for template in some_queries:
            template = [x.replace("xyz", mv) for x in template]
            mytext = "".join(template)
            mytexts.append(mytext)
    return mytexts


## This function will take in a masked sentence and return a list of predictions
def predict_masked_sent(text, top_k):
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
        pt = slugify(predicted_token)
        if pt.strip():
            my_words.append(pt)
    return my_words


## Runs all queries, generating k candidates for each;
## returns a list of unique candidate words
def get_all_words(my_queries, k):
    all_words = []
    for mm in my_queries:
        all_words += predict_masked_sent(mm, k)
        all_words = list(set(all_words))
        all_words.sort()
    return(all_words)    


def expand_candidate(mycan):
    newcans = []
    ## double the third letter:
    mycan = mycan[:3]+mycan[2]+mycan[3:]
    ## replace 2nd letter with all possibilities
    for lett in alphabet:
        newcan = mycan[:1]+lett+mycan[2:]
        newcans.append(newcan)
    return newcans




def main():
    solutions = []
    my_queries = iterate_for_sbert(raw_queries)
    my_top_k = 100  ## the number of predictions per query
    all_words = get_all_words(my_queries, my_top_k)
    # print(all_words)
    for myplant in mygarden:
        print(myplant)
        plurals = [myplant]
        if myplant[-1] == "s":
            plurals.append(myplant[:-1])
        else:
            plurals.append(myplant+"s")
        for plur in plurals:
            for myadj in all_words:
                print("\t"+myadj)
                if len(myadj) == len(plur)+1:
                    expanded = expand_candidate(plur)
                    for exp in expanded: print("\t\t"+exp)
                    if myadj in expanded:
                        solutions.append([plur, myadj])
                        print("SOLUTION: ", plur+" --> "+myadj)
    print("SOLUTIONS: \n\n")
    for solution in solutions:
        print(solution)
                
                    


if __name__ == "__main__":
    main()
