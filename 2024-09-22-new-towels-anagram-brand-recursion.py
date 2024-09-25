#!/usr/bin/env python


## 2024/09/23. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/09/22 Sunday Puzzle:
## https://www.npr.org/2024/09/22/nx-s1-5122457/sunday-puzzle-gp-naming-spree
## That puzzle:
"""
Take the phrase NEW TOWELS. Rearrange its nine letters to get the brand name
of a product that you might buy at a supermarket.
"""
import itertools, os, sys, torch
from collections import Counter
from transformers import GPT2LMHeadModel, GPT2Tokenizer


## You'll need to download and store the lexicon file as I did; I'm using the first 
## 10,000 words (lines) from this file:
## https://github.com/first20hours/google-10000-english/blob/master/20k.txt
##
## Note: credit to Tony 'pyTony' Veijalainen; much of the anagram function is adapted from this:
## https://www.daniweb.com/programming/software-development/code/393153/multiword-anagrams-by-recursive-generator

def contains(bigger,smaller):
    """ 
    find the letters that are left from bigger
    when smaller's letters are taken from bigger; OR
    return None if smaller's letters are not contained in bigger
    """
    if len(bigger) >= len(smaller):
        while smaller:
            this, smaller = smaller[0:1] , smaller[1:]
            if this not in bigger:
                return None
            bigger = bigger.replace(this, '', 1)
        return bigger

takeout=" \t'-+\n\r"
ttable = str.maketrans("", "", takeout)
def trim_word(word, transtable=ttable):
    """ lowercase the word and return cleaned word """
    #word with letters not in takeout
    return word.lower().translate(transtable)
    # if you have clean directory and do not mind "we'd" missing use next line instead.
    # return word.lower().strip()

def find_words(candidate_words, letters, atleast):
    """ 
    candidate_words is iterable giving the words to choose from, like
    open file or list of words
    """
    valid_words = []
    for this in candidate_words:
        # we do not assume clean or ordered words, this is costly in execution time,
        # but more flexible
        this = trim_word(this)
        if contains(letters, this) is not None:
            if len(letters) >= len(this) >= atleast:
                valid_words.append(this)
    return sorted(valid_words, key=len, reverse=True)

def find_anagrams(word, words, atleast):
    """ 
    Find possibly multiple word anagrams from parameter 'word'
    with possibly repeating words of 'atleast' or more letters 
    from sequence parameter 'words' in order of the sequence
    (combinations with repeats, not permutations)
    """
    for word_index, current_word in enumerate(words):
        remaining_letters = contains(word, current_word)
        if remaining_letters=='':
            yield current_word
        elif remaining_letters is not None and len(remaining_letters) >= atleast:
            for x in find_anagrams(remaining_letters, words[word_index:], atleast):
                yield (' '.join((current_word, x)))

# Function to check if a string has two words or fewer
def max_number_of_words(target):
    return len(target) <= 3


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


def main():
    # original_string = 'NEWTOWELS'.lower()
    if len(sys.argv) > 3:
        print('Arguments: length of shortest allowed word; word or phrase to anagram (rest of line).')
        smallest, words = (int(sys.argv[1]), trim_word(''.join(sys.argv[2:])))
    else:
        words = trim_word(input('Give words: '))
        smallest = int(input('Minimum acceptable word length: '))
    language_file = os.path.expanduser('~/Desktop/naturallanguagepuzzling/blog/resources/10k-lexicon.txt')
    with open(language_file) as word_file:
        wordlist = find_words(word_file, words, smallest)
    print('%i words loaded.' % len(wordlist))
    my_solutions = list(find_anagrams(words, wordlist, smallest))
    my_solutions = list(set(my_solutions))
    new_solutions = set()
    for ms in my_solutions:
        ms = ms.split(" ")
        msps = list(itertools.permutations(ms))
        new_solutions.update([m for m in msps])
    new_solutions = list(new_solutions)
    new_solutions.sort()
    new_solutions = list(filter(None, new_solutions))
    results = list(filter(max_number_of_words, new_solutions))
    results = [" ".join(g) for g in results]
    # solcounter = Counter(new_solutions)
    solution_number = 0
    # for sn in new_solutions:
    #     print(" ".join(sn))
    #     solution_number += 1
    print('\n%i solutions found!' % len(results))
    model, tokenizer = load_model('gpt2')
    ranked = []
    frame = "I prefer to buy name brands like __1__ that can be found in supermarkets everywhere."
    for r in results:
        sentence = frame.replace("__1__", r)
        score = sent_scoring((model, tokenizer), sentence)
        if score < 6.3:
            ranked.append([score, sentence])
    ranked.sort(reverse=True)
    for rk in ranked:
        print(f'{rk[0]:.4f}', "\t", rk[1])

if __name__ == '__main__':
    main()
