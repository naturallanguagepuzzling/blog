#!/usr/bin/env python


## 2024/09/09. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/09/08 Sunday Puzzle:
## https://www.npr.org/2024/09/07/nx-s1-5103735/sunday-puzzle-antonyms-attract
## That puzzle:
"""
This week's challenge comes from listener Michael Schwartz, of Florence,
Oregon. Take the name of a watercraft that contains an odd number ofletters.
Remove the middle letter and rearrange the remaining ones to name a body of
water. What words are these?
"""

from itertools import permutations
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


## You'll need to download and store the file as I did; I'm using the first 
## 10,000 words (lines) from this file:
## https://github.com/first20hours/google-10000-english/blob/master/20k.txt
lexfilename = "./resources/10k-lexicon.txt"

frames = [
    "As the largest body of water in the area, the __1__ is a popular summer destination.",
    ]

watercraft = [
    # 'lakke','rarbulretoc'
    'airboat', 'angler', 'barge', 'battleship', 'brig', 'canoe', 'catamaran',
    'clipper', 'corvette', 'cruiser', 'cutter', 'daysailer', 'destroyer',
    'dhow', 'dinghy', 'downeast', 'ferry', 'flybridge', 'frigate', 'gondola',
    'houseboat', 'hovercraft', 'hydrofoil', 'icebreaker', 'inflatable', 'junk',
    'kayak', 'ketch', 'lifeboat', 'longship', 'minesweeper', 'motorboat',
    'motorsailer', 'steamer', 'paddleboard', 'paddleboat', 'patroler',
    'pilothouse', 'pontoon', 'racer', 'raft', 'riverboat', 'rowboat',
    'runabout', 'sailboat', 'sampan', 'schooner', 'skiff', 'sloop',
    'speedboat', 'submarine', 'surfboard', 'tanker', 'tender', 'towboat',
    'trawler', 'trimaran', 'tug', 'tugboat', 'walkaround', 'weekender',
    'whaleboat', 'windjammer', 'yacht', 'yawl'
    ]

def get_lex(some_lexicon_filename):
    lexfile = open(some_lexicon_filename, "r")
    full_lex = lexfile.readlines()
    lexfile.close()
    lex = [l.strip().lower() for l in full_lex]
    return lex


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


def get_valid_english_words(stringlist, lex):
    valid_words = []
    for string in stringlist:
        tokens = string.split()
        valid = 0
        for token in tokens:
            if token in lex:
                valid += 1
        if valid < len(tokens):
            pass
        else:
            valid_words.append(string)
    return valid_words


def get_valid_anagrams(mystring, lex):
    all_anagrams = []
    ## uncomment following to enable two-word solutions
    # mystring = mystring+" "
    anagrams_one_wd = [''.join(p) for p in permutations(mystring.lower())]
    anagrams_one_wd = [x.strip() for x in anagrams_one_wd]
    for anag in anagrams_one_wd:
        all_anagrams.append(anag)
    all_anagrams = list(set(all_anagrams))
    valid_anagrams = get_valid_english_words(all_anagrams, lex)
    valid_anagrams = list(set(valid_anagrams))
    return valid_anagrams


def main():
    lex = get_lex(lexfilename)
    model, tokenizer = load_model('gpt2')
    ranked = []
    for craft in watercraft:
        if len(craft) % 2 == 0:
            pass
        else:
            middle = len(craft) // 2
            crft = craft[:middle] + craft[(middle+1):]
            print(craft+" --> "+crft)
            canagrams = get_valid_anagrams(crft, lex)
            if canagrams:
                print(canagrams)
            for frame in frames:
                for can in canagrams:
                    sentence = frame.replace("__1__", can)
                    score = sent_scoring((model, tokenizer), sentence)
                    # if score < 7.65:
                    if score < 100:
                        ranked.append([score, sentence])
    ranked.sort(reverse=True)
    for rk in ranked:
        print(rk[0], "\t", rk[1])


if __name__ == '__main__':
    main()
