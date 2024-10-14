#!/usr/bin/env python


## 2024/10/14. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/10/13 Sunday Puzzle:
## https://www.npr.org/2024/10/12/nx-s1-5148831/sunday-puzzle-the-pits-puzzle
## That puzzle:
"""
This week's challenge comes from listener Mike Selinker, of Renton, Wash.
Think of something to drink whose name is a compound word. Delete the first
letter of the first part and you'll get some athletes. Delete the first letter
of the second part and you'll get where these athletes compete. What words are
these?
"""

# import nltk
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from nltk.corpus import brown
from nltk.probability import FreqDist

bevs = [
    '7UP', 'Acai juice', 'Almond milk', 'Americano', 'Aperitivo',
    'Aperol Spritz', 'Apple juice', 'Aviation', "Bee's Knees", 'Black tea',
    'Blood and Sand', 'Bloody Mary', 'Boulevardier', 'Bourbon', 'Bramble',
    'Bubble tea', 'Caipirinha', 'Campari Soda', 'Cape Codder', 'Cappuccino',
    'Chai tea', 'Cherry soda', 'Coconut milk', 'Coconut water', 'Cola',
    'Cold brew', 'Cranberry juice', 'Daiquiri', "Dark 'n' Stormy",
    'Dr. Pepper', 'Earl Grey tea', 'El Diablo', 'Espresso',
    'Espresso Martini', 'Frappuccino', 'French 75', 'Fruit smoothies',
    'Gimlet', 'Gin Martini', 'Ginger ale', 'Grape soda', 'Grapefruit juice',
    'Green tea', 'Greyhound', 'Guava juice', 'Herbal tea', 'Hot chocolate',
    'Iced chocolate', 'Iced coffee', 'Iced tea', 'Irish coffee',
    'Jungle Bird', 'Kefir', 'Kombucha', 'Last Word', 'Latte',
    'Lemon-lime soda', 'Mai Tai', 'Mango juice', 'Manhattan', 'Margarita',
    'Martinez', 'Matcha latte', 'Mezcal Negroni', 'Milkshakes', 'Mint Julep',
    'Mocha', 'Mojito', 'Moscow Mule', 'Mountain Dew', 'Negroni',
    'Negroni Sbagliato', 'Oat milk', 'Old Fashioned', 'Old Timer',
    'Old-Fashioned', 'Oolong tea', 'Orange juice', 'Orange soda', 'Paloma',
    'Penicillin', 'Pina Colada', 'Pineapple juice', 'Pisco Sour',
    "Planter's Punch", 'Pomegranate juice', 'Ramos Gin Fizz',
    'Rhum Agricole Cocktail', 'Rice milk', 'Rob Roy', 'Root beer',
    'Rum Runner', 'Rye', 'Sazerac', 'Scotch', 'Screwdriver', 'Sea Breeze',
    'Sidecar', 'Singapore Sling', 'Soy milk', 'Sparkling water', 'Spritz',
    'Ti Punch', 'Tomato juice', "Tommy's Margarita", 'Vesper Martini',
    'Vienna coffee', 'Vodka Martini', 'Water', 'Whiskey Sour', 'White Lady',
    'White tea', 'Zombie'
    ]


corpus = brown.words()
fdist = FreqDist(corpus)
most_frequent_words = fdist.most_common()
wdlist = []
for wd, freq in most_frequent_words[:6000]:
    wdlist.append(wd)
frame = 'We went to the __1__ to watch the __0__ compete in the tournament.'


def tokenize_compound(someword):
    tokens = tokenizer.tokenize(someword)
    return tokens

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

def filter_bevs(somelist):
    somelist = [b.lower() for b in somelist]
    bl = [b for b in somelist if len(b.strip().split(" ")) == 1]
    bl = [b for b in bl if len(b) > 7]
    return bl

def split_string(string):
    result = []
    for i in range(3, len(string)-2):
        result.append([string[:i], string[i:]])
    return result


def main():
    mybevs = filter_bevs(bevs)
    allsplits = []
    for mb in mybevs:
        mbsplits = split_string(mb)
        for mbs in mbsplits:
            allsplits.append(mbs)
    model, tokenizer = load_model('gpt2')
    ranked = []
    for asp in allsplits:
        if asp[0] in wdlist and asp[1] in wdlist:
            sentence = frame.replace('__0__', asp[0][1:])
            sentence = sentence.replace('__1__', asp[1][1:])
            score = sent_scoring((model, tokenizer), sentence)
            if score < 10:
                ranked.append([score, sentence, asp])
    ranked.sort(reverse=True)
    for rk in ranked:
        print(f'{rk[0]:.4f}', '\t', rk[1], '\t', rk[2])


if __name__ == '__main__':
    main()
