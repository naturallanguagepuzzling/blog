#!/usr/bin/env python


## 2024/04/10. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/04/07 Sunday Puzzle:
## https://www.npr.org/2024/04/07/1243253871/sunday-puzzle-idioms-for-the-eclipse
## That puzzle:
"""
This week's challenge: This week's challenge comes from listener Steve Baggish
of Arlington, Massachusetts. Think of a nine-letter word naming a kind of tool
that is mentioned in the Bible. Remove the second and sixth letters and the
remaining letters can be rearranged to spell two new words that are included
in a well known biblical passage and are related to the area in which the tool
is used. What are the three words?
"""

import pythonbible as bible
import time

# bcv_dict = {} ## bcv for book, chapter, verse
print(time.ctime())
allverseids = []
# for verse_id in range(1001001, 1050026):  # Range covers all verses in Genesis
for book in range(1, 67): ## Revelation is book 66
    print(book)
    for chapter in range(1, 151): ## Psalms has 150 chapters
        print("\t", chapter)
        for verse in range(1, 177): ## Psalm 119 is longest chapter with 176 verses
            verse_id = int(str(book)+str(chapter).zfill(3)+str(verse).zfill(3))
            if bible.is_valid_verse_id(verse_id):
                allverseids.append(verse_id)
                print(verse_id)

# Open the file in write mode ('w')
with open('bible_verse_ids.txt', 'w') as file:
    for num in allverseids:
        file.write(str(num) + '\n')

print(time.ctime())
