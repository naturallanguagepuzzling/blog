#!/usr/bin/env python

## 2025/06/22. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2025/05/04 Sunday Puzzle:
## https://www.npr.org/2025/06/22/g-s1-73310/sunday-puzzle
## That puzzle:

"""
This week's challenge comes from listener Bob Weisz. Take the name of a major
film director. Drop the last six letters of his name, and rearrange what
remains. You'll get the name of a major film award -- for which this director
has been nominated six times. Who is he and what is the award?
"""

# from itertools import permutations
from slugify import slugify


directors = [
             'Steven Spielberg',
             'Martin Scorsese',
             'Akira Kurosawa',
             'Stanley Kubrick',
             'Alfred Hitchcock',
             'Quentin Tarantino',
             'Ridley Scott',
             'Francis Ford Coppola',
             'Clint Eastwood',
             'Woody Allen',
             'Ingmar Bergman',
             'Federico Fellini',
             'Billy Wilder',
             'Christopher Nolan',
             'Pedro Almodóvar',
             'Wes Anderson',
             'Paul Thomas Anderson',
             'David Fincher',
             'Joel Coen',
             'Ethan Coen',
             'Ang Lee',
             'Jean-Luc Godard',
             'Robert Altman',
             'John Ford',
             'George Lucas',
             'Frank Capra',
             'Roman Polanski',
             'Michael Haneke',
             'Ken Loach',
             'Spike Lee'
             ]

awards = [
            'Academy Award',
            'Oscar',
            'BAFTA',
            'Golden Globe',
            'Cannes Film Festival Award',
            'Palme d Or',
            'Directors Guild of America Award',
            'Screen Actors Guild Award',
            'Critics Choice Movie Award',
            'Independent Spirit Award'
        ]
        

def filter_chars(wd):
    wd = wd.replace('-', '')
    wd = wd.replace(' ', '')
    wd = wd.replace("'", "")
    wd = wd.lower()
    wd = slugify(wd)
    return wd



def main():
    dstrings = [filter_chars(d) for d in directors]
    astrings = [filter_chars(a) for a in awards]
    for d in dstrings: 
        if len(d) < 6:
            continue
        dshort = d[:-6]
        for a in astrings:
            if len(a) != len(dshort):
                continue
            if sorted(a) == sorted(dshort):
                print(f"Director: {d}, Award: {a}")
                break


if __name__ == '__main__':
    main()

