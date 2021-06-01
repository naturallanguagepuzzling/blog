#!/usr/bin/env python


## 2021/05/26. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/05/23 Sunday Puzzle:
## https://www.npr.org/2021/05/23/999454616/sunday-puzzle-name-that-city
## That puzzle:
"""
This week's challenge: This week's challenge comes from listener Roger Barkan of
Savage, Md. Think of an eight-letter word in which the third and sixth letters
are "A." Remove the A's. The remaining six letters start a common series. What
is it? And what comes next in that series?
"""

## You'll need to download the file as I did:
## https://github.com/dwyl/english-words/blob/master/words_alpha.txt
lexfilename = "../annex/words_alpha.txt"

my_eights = "resources/2021-05-23-candidate-words.txt"

elementstring  = 'hhelibebcnofnenamgalsipsclarkcasctivcrmnfeconicuzngageassebrkrrbsryzrnbmotcrurhpdagcdinsnsbteixecsbalaceprndpmsmeugdtbdyhoertmybluhftawreosirptauhgtlpbbipoatrnfrraacthpaunppuamcmbkcfesfmmdnolrrfdbsgbhhsmtdsrgcnnhflmclvtsog'

## open & read lexicon file, return lexicon of only words of length n
def get_n_lex(some_lex_filename, my_n):
    lexfile = open(some_lex_filename, "r")
    full_lex = lexfile.readlines()
    print("Number of words in the full lexicon: "+str(len(full_lex)))
    n_lex = [l.strip().lower() for l in full_lex if len(l.strip())==my_n]
    print("Number of "+str(my_n)+"-letter words in lexicon: "+str(len(n_lex)))
    return n_lex

def get_aa_lex(tlex):
    al = []
    c = 0
    for tl in tlex:
        if tl[2] == 'a' and tl[5] == 'a':
            c+=1
            al.append(tl)
            print(str(c)+"\t"+tl[0:2]+" "+tl[3:5]+" "+tl[6:8]+"\t"+tl+'\n\n\n\n\n')
            # print(tl[0:2]+tl[3:5]+tl[6:8]+"\t"+tl)
    print("Number of words matching pattern '__a__a__' : "+str(len(al)))
    return al

def try_sequences(my_alx):
    for alx in my_alx:
        ax = alx[0:2]+alx[3:5]+alx[6:8]
        if ax in elementstring:
            print("SOLUTION: "+ax)


def main():
    # target_length_lex = get_n_lex(lexfilename, 8)
    target_length_lex = get_n_lex(my_eights, 8)
    aa_lex = get_aa_lex(target_length_lex)
    aa_lex.append('gaalsaip')
    try_sequences(aa_lex)
    # for aa in aa_lex:
    #     print(aa)

if __name__ == "__main__":
    main()
