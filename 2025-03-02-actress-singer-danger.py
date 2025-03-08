#!/usr/bin/env python

## 2025/03/02. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2025/03/02 Sunday Puzzle:
## https://www.npr.org/2025/03/02/nx-s1-5311999/sunday-puzzle-consonant-countries
## That puzzle:

"""
This week's challenge comes from listener Dennis Burnside, of Lincoln, Neb.
Think of a famous singer and actress, first and last names, two syllables each.
The second syllable of the last name followed by the first syllable of the
first name spell something that can be dangerous to run into. What is it?
"""

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import spacy
import spacy_syllables
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

frame = 'Stay alert because running into a __1__ can be very dangerous.'
mystars = [
    'Beyoncé Knowles-Carter', 'Jennifer Lopez', 'Lady Gaga', 'Madonna', 'Cher',
    'Barbra Streisand', 'Dolly Parton', 'Whitney Houston', 'Aretha Franklin',
    'Diana Ross', 'Tina Turner', 'Celine Dion', 'Mariah Carey', 'Taylor Swift',
    'Rihanna', 'Miley Cyrus', 'Ariana Grande', 'Demi Lovato', 'Selena Gomez',
    'Jennifer Hudson', 'Alicia Keys', 'Kelly Clarkson', 'Christina Aguilera',
    'Pink (Alecia Moore)', 'Adele', 'Norah Jones', 'Shakira', 'Gloria Estefan',
    'Debbie Harry', 'Stevie Nicks', 'Pat Benatar', 'Alanis Morissette',
    'Sheryl Crow', 'Jewel', 'Lauryn Hill', 'Mary J. Blige', 'Janet Jackson',
    'Paula Abdul', 'Vanessa Williams', 'Queen Latifah', 'Bette Midler',
    'Rita Moreno', 'Julie Andrews', 'Liza Minnelli', 'Judy Garland',
    'Marlene Dietrich', 'Lena Horne', 'Eartha Kitt', 'Olivia Newton-John',
    'Kylie Minogue', 'Björk', 'Kate Bush', 'Tori Amos', "Sinead O'Connor",
    'Annie Lennox', 'Cyndi Lauper', 'Carole King', 'Joni Mitchell',
    'Linda Ronstadt', 'Emmylou Harris', 'Bonnie Raitt', 'Chaka Khan',
    'Roberta Flack', 'Gladys Knight', 'Dionne Warwick', 'Nancy Sinatra',
    'Connie Francis', 'Brenda Lee', 'Lesley Gore', 'Dusty Springfield',
    'Shirley Bassey', 'Ella Fitzgerald', 'Billie Holiday', 'Sarah Vaughan',
    'Nina Simone', 'Peggy Lee', 'Rosemary Clooney', 'Dinah Washington'
]

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("syllables", after="tagger")

def get_syllables(myname):
    try:
        tokendoc = nlp(myname)
        sylls = [token._.syllables for token in tokendoc][0]
        return sylls
    except Exception as e:
        logging.error(f"Error getting syllables for {myname}: {e}")
        return []

def first_last_stars(starlist):
    return [[x.split(' ')[0], x.split(' ')[-1]] for x in starlist if len(x.split(' ')) >= 2]

def get_two_syllable_stars(twonameslist):
    candidates = []
    for tn in twonameslist:
        first_syllables = get_syllables(tn[0])
        last_syllables = get_syllables(tn[1])
        if len(first_syllables) == 2 and len(last_syllables) == 2:
            candidates.append(tn)
    return candidates

def load_model(model_string):
    try:
        tokenizer = GPT2Tokenizer.from_pretrained(model_string)
        model = GPT2LMHeadModel.from_pretrained(model_string)
        model.eval()
        return model, tokenizer
    except Exception as e:
        logging.error(f"Error loading model {model_string}: {e}")
        return None, None

def sent_scoring(model_tokenizer, text):
    model, tokenizer = model_tokenizer
    if model is None or tokenizer is None:
        return float('inf')  # Return a high score on error.
    try:
        input_ids = torch.tensor(tokenizer.encode(text)).unsqueeze(0)
        with torch.no_grad():
            outputs = model(input_ids, labels=input_ids)
        loss = outputs[0].item()
        return loss
    except Exception as e:
        logging.error(f"Error scoring sentence: {e}")
        return float('inf') # return high score on error.

def main():
    stars = first_last_stars(mystars)
    candidates = get_two_syllable_stars(stars)
    model_tokenizer = load_model('gpt2')
    if model_tokenizer[0] is None:
        return

    ranked = []
    for c in candidates:
        first_syllables = get_syllables(c[0])
        last_syllables = get_syllables(c[1])
        if not first_syllables or not last_syllables: #skip if syllable extraction failed.
          continue
        danger = last_syllables[-1] + first_syllables[0]
        sentence = frame.replace('__1__', danger)
        score = sent_scoring(model_tokenizer, sentence)
        ranked.append([score, c, sentence])
    cheat = frame.replace('__1__', 'sandbar')
    cheatscore = sent_scoring(model_tokenizer, cheat)
    ranked.append([cheatscore, ['Barbra', 'Streisand'], cheat])
    ranked.sort()
    for r in ranked:
        print('\t'.join([f"{r[0]:.3f}", ' '.join(r[1]), r[2]]))

if __name__ == '__main__':
    main()