#!/usr/bin/env python


## 2024/04/15. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/04/14 Sunday Puzzle:
## https://www.npr.org/2024/04/14/1244610377/sunday-puzzle-a-puzzle-for-the-guest-puzzlemaster-g-reg-p-liska
## That puzzle:
"""
This week's challenge: This week's challenge comes from Bruce DeViller, of
Brookfield, Ill. Think of a popular online service. Change the first letter
to a Y and rearrange the result to get what this service provides. What is it?
"""

from itertools import permutations
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


## You'll need to download and store the file as I did; I'm using the first 
## 10,000 words (lines) from this file:
## https://github.com/first20hours/google-10000-english/blob/master/20k.txt
lexfilename = "../annex/10k.txt"
companies = [
    'JD', 'QQ', 'VK', 'B2W', 'BMC', 'Box', 'CDK', 'Max', 'ANGI', 'ASOS',
    'Bing', 'Epic', 'Etsy', 'GoTo', 'Grab', 'Hulu', 'Kwai', 'Lyft', 'Meta',
    'Okta', 'Otto', 'Ozon', 'Sina', 'Snap', 'Trip', 'Uber', 'Wish', 'XNXX',
    'Zoom', 'eBay', 'Adobe', 'Asana', 'Baidu', 'Block', 'Chewy', 'Exela',
    'Globo', 'Hinge', 'Infor', 'Kakao', 'Match', 'Naver', 'Quora', 'Sabre',
    'Shein', 'Slack', 'Stars', 'Steam', 'Unity', 'Venmo', 'Vroom', 'Yahoo',
    'Zelle', 'Zynga', 'Airbnb', 'Akamai', 'Amazon', 'Bet365', 'Beyond',
    'Bumble', 'Copart', 'Docomo', 'Fandom', 'Google', 'Grindr', 'Kaplan',
    'Klarna', 'Newegg', 'OpenAI', 'PayPal', 'Reddit', 'Roblox', 'Shazam',
    'Splunk', 'Square', 'Stripe', 'Suning', 'TikTok', 'Tinder', 'Twilio',
    'Twitch', 'Yandex', 'Zappos', 'Zillow', 'iTunes', 'wework', 'Alibaba',
    # 'Booking', 'Carsome', 'Carvana', 'Compass', 'Coupang', 'Discord',
    # 'Dropbox', 'Expedia', 'GoDaddy', 'Groupon', 'Grubhub', 'HubSpot',
    # 'LogMeIn', 'Meituan', 'MongoDB', 'NetEase', 'Netflix', 'Outlook',
    # 'Pornhub', 'Rakuten', 'Samsung', 'Shopify', 'Spotify', 'Tencent',
    # 'Twitter', 'Wayfair', 'Weather', 'Workday', 'XVideos', 'YouTube',
    # 'Zalando', 'ZenNews', 'Zendesk', 'Alphabet', 'Bilibili', 'Coolblue',
    # 'DocuSign', 'DocuWare', 'DoorDash', 'Facebook', 'Fanatics', 'Farfetch',
    # 'Flexport', 'J2Global', 'LinkedIn', 'Opendoor', 'PetSmart', 'Telegram',
    # 'Verisign', 'WhatsApp', 'xHamster', 'Atlassian', 'Bloomberg', 'ByteDance',
    # 'Endurance', 'EpicGames', 'Instacart', 'Instagram', 'Microsoft',
    # 'PagerDuty', 'Pinduoduo', 'Pinterest', 'Qualtrics', 'Rackspace',
    # 'SalesLoft', 'StitchFix', 'Stripchat', 'Wikipedia', 'ZoomVideo',
    # 'AngiesList', 'BlueYonder', 'Craigslist', 'DuckDuckGo', 'Salesforce',
    # 'SeaLimited', 'ServiceNow', 'SharePoint', 'Shutterfly', 'Travelport',
    # 'TurboPages', 'CrowdStrike', 'EPAMSystems', 'RingCentral', 'Wildberries',
    # 'SurveyMonkey',
]

frames = [
    # "The online service __1__ is popular for providing __2__ to customers around the country.",
    # "__1__, which offers __2__, is a popular online service.",
    "__1__ is known for __2__ services online.",
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
    valid_anagrams = get_valid_english_words(all_anagrams, lex)
    valid_anagrams = list(set(valid_anagrams))
    return valid_anagrams


def main():
    lex = get_lex(lexfilename)
    model, tokenizer = load_model('gpt2')
    ranked = []
    for company in companies:
        yompany = "Y"+company[1:]
        print(company)
        yanagrams = get_valid_anagrams(yompany, lex)
        for frame in frames:
            frame = frame.replace("__1__", company)
            for yan in yanagrams:
                sentence = frame.replace("__2__", yan)
                score = sent_scoring((model, tokenizer), sentence)
                if score < 7.65:
                    ranked.append([score, sentence])
    ranked.sort(reverse=True)
    for rk in ranked:
        print(rk[0], "\t", rk[1])


if __name__ == '__main__':
    main()
