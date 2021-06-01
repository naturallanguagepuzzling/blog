#!/usr/bin/env python


## 2021/05/09. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/05/09 Sunday Puzzle:
## https://www.npr.org/2021/05/09/995172987/sunday-puzzle-supermarket-scramble
## That puzzle:
"""
This week's challenge comes from listener Jim Dale, of Plano, Texas. Think of a
word with six syllables that's spelled with only 11 letters — and the four
middle syllables have the same vowel. What word is it?
"""

## You'll need to download the file as I did:
## https://github.com/dwyl/english-words/blob/master/words_alpha.txt
lexfilename = "../annex/words_alpha.txt"


## open & read lexicon file, return lexicon of only words of length n
def get_n_lex(some_lex_filename, my_n):
    lexfile = open(some_lex_filename, "r")
    full_lex = lexfile.readlines()
    print("Number of words in the full lexicon: "+str(len(full_lex)))
    n_lex = [l.strip().lower() for l in full_lex if len(l.strip())==my_n]
    print("Number of "+str(my_n)+"-letter words in lexicon: "+str(len(n_lex)))
    return n_lex


def n_of_a_kind_vowels(myn, some_lex):
	vowels = ['a', 'e', 'i', 'o', 'u', 'y']
	consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
	quads = []
	keep = []
	for lx in some_lex:
		midlex = lx[1:-1]
		for vw in vowels:
			if midlex.count(vw) >= myn:
				quads.append(lx)
	for qd in quads:
		qvs = 0
		for vw in vowels:
			qvs+=qd.count(vw)
		if qvs >= 6:
			keep.append(qd)
	print(len(keep))
	for kp in keep:
		print(kp)



def main():
	target_vowels = 4
	eleven_lex = get_n_lex(lexfilename, 11)
	n_of_a_kind_vowels(target_vowels, eleven_lex)


if __name__ == "__main__":
    main()
