#!/usr/bin/env python

## 2025/04/10. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2025/04/06 Sunday Puzzle:
## https://www.npr.org/2025/04/05/nx-s1-5344989/sunday-puzzle-whats-that-familiar-phrase
## That puzzle:

"""
This week's challenge comes from listener Andrew Chaikin, of San Francisco.
Think of an 11-letter word thay might describe milk. Change one letter in
it to an A, and say the result out loud. You'll get a hyphenated word that
might describe beef. What is it?
"""

milkwords = [
    'alternative', 'animal', 'base', 'basic', 'beneficial', 'beverage',
    'binder', 'bottled', 'breakfast staple', 'cartoned', 'childhood favorite',
    'cleanser', 'cloudy', 'cold', 'common', 'component', 'condensed', 'cool',
    'cooling', 'creamy', 'cultured', 'dairy', 'delicious', 'dietary',
    'dietary staple', 'drink', 'elemental', 'emulsifier', 'enriched',
    'essential', 'evaporated', 'everyday', 'farm-fresh', 'fermented',
    'flavored', 'fluid', 'fortified', 'fresh', 'fundamental', 'fundamental',
    'grade a', 'healthy', 'heavy', 'homely', 'homogenized', 'hydrating',
    'imported', 'ingredient', 'integral', 'light', 'liquid', 'local',
    'low-fat', 'milky', 'moisturizer', 'natural', 'nourishing',
    'nursery staple', 'nutritious', 'opaque', 'organic', 'pasteurized',
    'pitched', 'plant-based', 'powdered', 'primary', 'product', 'pure', 'raw',
    'refreshing', 'refrigerated', 'rich', 'satisfying', 'shelf-stable',
    'simple', 'skim', 'smooth', 'soothing', 'source', 'standard', 'supplement',
    'sweet', 'tetra-packed', 'thick', 'thin', 'traditional',
    'ultra-pasteurized', 'unprocessed', 'versatile', 'white', 'whole',
    'wholesome'
    ]

def filter_chars(mylist):
    keepers = []
    for wd in mylist:
        v1 = wd.replace('-', '')
        v2 = wd.replace(' ', '')
        v3 = v1.replace(' ', '')
        for v in [v1, v2, v3, wd]:
            if len(v) == 11 and v not in keepers:
                keepers.append(v)
    return keepers

def main():
    print('11-letter words that can describe milk:')
    candidates = filter_chars(milkwords)
    for c in candidates:
        print(c)

if __name__ == '__main__':
    main()

