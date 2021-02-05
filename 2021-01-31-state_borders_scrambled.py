#!/usr/bin/env python


## 2021/02/02. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/1/31 Sunday Puzzle:
## https://www.npr.org/2021/01/31/962412357/sunday-puzzle-game-of-words
## That puzzle:
"""
This week's challenge comes from listener Derrick Niederman, of Charleston, S.C. Starting in Montana, you can drive into South Dakota and then into Iowa. Those three states have the postal abbreviations MT, SD, and IA — whose letters can be rearranged to spell AMIDST. The challenge is to do this with four connected states to make an eight-letter word. That is, start in a certain state, drive to another, then another, and then another. Take the postal abbreviations of the four states you visit, mix the letters up, and use them to spell a common eight-letter word. Derrick and I know of only one answer. Can you do this?
"""


states_po_list = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

## Adapted a dictionary from this site:
## https://thefactfile.org/u-s-states-and-their-border-states/
po_border_dict = {'AL': ['MS', 'TN', 'FL', 'GA'], 'AK': [], 'AZ': ['NV', 'NM', 'UT', 'CA', 'CO'], 'AR': ['OK', 'TN', 'TX', 'LA', 'MS', 'MO'], 'CA': ['OR', 'AZ', 'NV'], 'CO': ['NM', 'OK', 'UT', 'WY', 'AZ', 'KS', 'NE'], 'CT': ['NY', 'RI', 'MA'], 'DE': ['NJ', 'PA', 'MD'], 'FL': ['GA', 'AL'], 'GA': ['NC', 'SC', 'TN', 'AL', 'FL'], 'HI': [], 'ID': ['UT', 'WA', 'WY', 'MT', 'NV', 'OR'], 'IL': ['KY', 'MO', 'WI', 'IN', 'IA', 'MI'], 'IN': ['MI', 'OH', 'IL', 'KY'], 'IA': ['NE', 'SD', 'WI', 'IL', 'MN', 'MO'], 'KS': ['NE', 'OK', 'CO', 'MO'], 'KY': ['TN', 'VA', 'WV', 'IL', 'IN', 'MO', 'OH'], 'LA': ['TX', 'AR', 'MS'], 'ME': ['NH'], 'MD': ['VA', 'WV', 'DE', 'PA'], 'MA': ['NY', 'RI', 'VT', 'CT', 'NH'], 'MI': ['OH', 'WI', 'IL', 'IN', 'MN'], 'MN': ['ND', 'SD', 'WI', 'IA', 'MI'], 'MS': ['LA', 'TN', 'AL', 'AR'], 'MO': ['NE', 'OK', 'TN', 'AR', 'IL', 'IA', 'KS', 'KY'], 'MT': ['SD', 'WY', 'ID', 'ND'], 'NE': ['MO', 'SD', 'WY', 'CO', 'IA', 'KS'], 'NV': ['ID', 'OR', 'UT', 'AZ', 'CA'], 'NH': ['VT', 'ME', 'MA'], 'NJ': ['PA', 'DE', 'NY'], 'NM': ['OK', 'TX', 'UT', 'AZ', 'CO'], 'NY': ['PA', 'RI', 'VT', 'CT', 'MA', 'NJ'], 'NC': ['TN', 'VA', 'GA', 'SC'], 'ND': ['SD', 'MN', 'MT'], 'OH': ['MI', 'PA', 'WV', 'IN', 'KY'], 'OK': ['MO', 'NM', 'TX', 'AR', 'CO', 'KS'], 'OR': ['NV', 'WA', 'CA', 'ID'], 'PA': ['NY', 'OH', 'WV', 'DE', 'MD', 'NJ'], 'RI': ['MA', 'NY', 'CT'], 'SC': ['NC', 'GA'], 'SD': ['NE', 'ND', 'WY', 'IA', 'MN', 'MT'], 'TN': ['MS', 'MO', 'NC', 'VA', 'AL', 'AR', 'GA', 'KY'], 'TX': ['NM', 'OK', 'AR', 'LA'], 'UT': ['NV', 'NM', 'WY', 'AZ', 'CO', 'ID'], 'VT': ['NH', 'NY', 'MA'], 'VA': ['NC', 'TN', 'WV', 'KY', 'MD'], 'WA': ['OR', 'ID'], 'WV': ['PA', 'VA', 'KY', 'MD', 'OH'], 'WI': ['MI', 'MN', 'IL', 'IA'], 'WY': ['NE', 'SD', 'UT', 'CO', 'ID', 'MT']}


## You'll need to download the file as I did:
## https://github.com/dwyl/english-words/blob/master/words_alpha.txt
lexfilename = "../annex/words_alpha.txt"


## just lowercasing the dictionary above
def prep_lower_dict(some_dict):
    lower_dict = {}
    for k in some_dict:
        lower_dict[k.lower()] = [v.lower() for v in some_dict[k]]
    return lower_dict


## open & read lexicon file, return lexicon of only words of length n
def get_n_lex(some_lex_filename, my_n):
    lexfile = open(some_lex_filename, "r")
    full_lex = lexfile.readlines()
    print("Number of words in the full lexicon: "+str(len(full_lex)))
    n_lex = [l.strip().lower() for l in full_lex if len(l.strip())==my_n]
    print("Number of "+str(my_n)+"-letter words in lexicon: "+str(len(n_lex)))
    return n_lex


## convert string (word) to string of sorted letters, e.g., 'yard' --> 'adry'
def string_to_sorted_string(some_string):
    some_string = list(some_string)
    some_string.sort()
    some_string = "".join(some_string)
    return some_string


## convert list to sorted string, e.g. ['ne', 'mo', 'ar', 'tn'] --> 'aemnnort'
def list_to_sorted_string(some_list):
    some_string = "".join(some_list)
    some_string = string_to_sorted_string(some_string)
    return some_string


## count the vowels in a string
def count_vowels(some_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    char_list = list(some_string)
    some_v = [c for c in char_list if c in vowels]
    return len(some_v)


## find and return dict of all possible paths through 4 states; key is sorted
## string; value is original path as string; e.g.:
## {'aemnnort': 'ne-mo-ar-tn', ...}
## Note -- only returns those with at least 2 vowels
def get_four_state_paths(slist, bdict):
    alpha_spath_dict = {}
    for st_po1 in slist:
        for st_po2 in bdict[st_po1]:
            for st_po3 in bdict[st_po2]:
                for st_po4 in bdict[st_po3]:
                    spath = [st_po1, st_po2, st_po3, st_po4]
                    spath = [y.lower() for y in spath]
                    alpha_quad = list(spath)
                    alpha_quad = list(set(alpha_quad))
                    if len(alpha_quad) != 4:
                        pass
                    else:
                        alpha_string = list_to_sorted_string(alpha_quad)
                        if alpha_string in alpha_spath_dict:
                            pass
                        else:
                            # print(alpha_string, spath)
                            alpha_spath_dict[alpha_string] = "-".join(spath)
    ## More accurately, this is the number of unique 8-letter combinations
    ## resulting from the abbreviations of 4 states along a path, in the
    ## unlikely case where different combos of state abbreviations contain
    ## the same 8 letters.
    print("Number of unique 4-state combos along a contiguous path: "
          +str(len(alpha_spath_dict)))
    candidates = {k:v for (k,v) in alpha_spath_dict.items() if count_vowels(k) > 1}
    print("Number of those combos containing 2 or more vowels: "
          +str(len(candidates)))
    return candidates


## iterate through dictionary keys; compare letters in state abbreviation combos
## with letters in lexicon words and return matches
def compare_for_solutions(lex, cdict):
    solutions = []
    for c in cdict:
        for l in lex:
            ls = string_to_sorted_string(l)
            if c == ls:
                solutions.append(l+" "+cdict[c])
    solutions.sort()
    return(solutions)


def main():
    # prepare (lowercase) the dictionary of states and their bordering states:
    lower_dict = prep_lower_dict(po_border_dict)
    # open, read lexicon file, return list of 8 letter words:
    eight_lex = get_n_lex(lexfilename, 8)
    # get list of all possible paths through 4 states:
    alpha_path_dict = get_four_state_paths(states_po_list, po_border_dict)
    # iterate state combos, compare letters w/ words in lex, return matches
    solutions = compare_for_solutions(eight_lex, alpha_path_dict)
    print("Number of solutions found: "+str(len(solutions))+"\n")
    for sol in solutions:
        print(sol)
    print("\n\n\n")
    for sol in solutions:
        print(sol.split(" ")[0])
        

if __name__ == "__main__":
    main()


## The current output:
"""
Number of words in the full lexicon: 370103
Number of 8-letter words in lexicon: 51627
Number of unique 4-state combos along a contiguous path: 967
Number of those combos containing 2 or more vowels: 901
Number of solutions found: 67

alamonti al-tn-mo-ia
alismoid il-mo-ia-sd
amarillo il-mo-ar-la
amidmost mo-ia-sd-mt
animator ar-tn-mo-ia
antinome ia-ne-mo-tn
cameroon ar-mo-ne-co
codeinas co-ne-sd-ia
coenamor ar-mo-ne-co
condemns co-ne-sd-mn
contused sd-ne-co-ut
ctenodus sd-ne-co-ut
daimones ia-sd-ne-mo
diamonds mo-ia-sd-nd
diaphone de-pa-oh-in
diocesan co-ne-sd-ia
dioramas ar-mo-ia-sd
disilane il-ia-ne-sd
donatism sd-ia-mo-tn
eduction id-ut-co-ne
encommon mo-ne-co-nm
eromania ar-mo-ne-ia
flagrant ar-tn-ga-fl
galavant al-ga-tn-va
kymation ia-mo-tn-ky
limation ia-il-mo-tn
limnoria ar-mo-il-in
mactroid ca-or-id-mt
madrones ar-mo-ne-sd
magneton ga-tn-mo-ne
makimono ia-mo-ok-nm
martagon ar-mo-tn-ga
matronal al-tn-mo-ar
mediants ia-ne-sd-mt
miltonia ia-il-mo-tn
moleskin il-mo-ne-ks
monactin ia-mo-tn-nc
monadism mn-sd-ia-mo
monamine mn-ia-ne-mo
monecian co-ne-ia-mn
monoecia co-ne-mo-ia
monomark ar-mo-ok-nm
montagne ga-tn-mo-ne
montanic ia-mo-tn-nc
montilla al-tn-mo-il
moralism il-mo-ar-ms
nocument ne-co-nm-ut
nomadise ia-sd-ne-mo
nomadism mn-sd-ia-mo
nominate ia-ne-mo-tn
nonmetal al-tn-mo-ne
oomiacks co-ks-mo-ia
ornament ar-tn-mo-ne
ransomed ar-mo-ne-sd
saintdom sd-ia-mo-tn
samaroid ar-mo-ia-sd
sandmite ia-ne-sd-mt
stallman al-tn-ms-la
takingly ga-tn-ky-il
tamanoir ar-tn-mo-ia
tangrams ar-ms-tn-ga
tankroom ar-ok-mo-tn
tidesman ia-ne-sd-mt
torminal ar-tn-mo-il
trangams ar-ms-tn-ga
turkoman ar-ok-nm-ut
unsocket ks-ne-co-ut
"""







"""
Of the above, keepers by frequency:
diamonds, mo-ia-sd-nd;
ornament, ar-tn-mo-ne;
nominate, ia-ne-mo-tn;
animator, ar-tn-mo-ia;
condemns, co-ne-sd-mn;
flagrant, ar-tn-ga-fl;
dioramas, ar-mo-ia-sd;
moleskin, il-mo-ne-ks;
eduction, id-ut-co-ne;
nonmetal, al-tn-mo-ne;
ransomed, ar-mo-ne-sd;
tangrams, ar-ms-tn-ga;
moralism, il-mo-ar-ms;
magneton, ga-tn-mo-ne;
nomadism, mn-sd-ia-mo;

Plus a few proper nouns:
cameroon, ar-mo-ne-co;
amarillo, il-mo-ar-la;

"""
