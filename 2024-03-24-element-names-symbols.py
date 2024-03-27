#!/usr/bin/env python


## 2024/03/25. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/03/24 Sunday Puzzle:
## https://www.npr.org/2024/03/24/1240246714/sunday-puzzle-a-puzzle-for-the-puzzlemaster
## That puzzle:
"""
This week's challenge: This week's challenge comes to us from Mae McAllister,
from Bath, in the United Kingdom. As you may know, each chemical element can
be represented by a one or two-letter symbol. Hydrogen is H, helium is He, and
so on. McAllister points out that there are two commonly known elements whose
names each can be spelled using three other element symbols. Name either one.
"""

import itertools

elements_dict = {
    'hydrogen': 'H',
    'helium': 'He',
    'lithium': 'Li',
    'beryllium': 'Be',
    'boron': 'B',
    'carbon': 'C',
    'nitrogen': 'N',
    'oxygen': 'O',
    'fluorine': 'F',
    'neon': 'Ne',
    'sodium': 'Na',
    'magnesium': 'Mg',
    'aluminum': 'Al',
    'silicon': 'Si',
    'phosphorus': 'P',
    'sulfur': 'S',
    'chlorine': 'Cl',
    'argon': 'Ar',
    'potassium': 'K',
    'calcium': 'Ca',
    'scandium': 'Sc',
    'titanium': 'Ti',
    'vanadium': 'V',
    'chromium': 'Cr',
    'manganese': 'Mn',
    'iron': 'Fe',
    'cobalt': 'Co',
    'nickel': 'Ni',
    'copper': 'Cu',
    'zinc': 'Zn',
    'gallium': 'Ga',
    'germanium': 'Ge',
    'arsenic': 'As',
    'selenium': 'Se',
    'bromine': 'Br',
    'krypton': 'Kr',
    'rubidium': 'Rb',
    'strontium': 'Sr',
    'yttrium': 'Y',
    'zirconium': 'Zr',
    'niobium': 'Nb',
    'molybdenum': 'Mo',
    'technetium': 'Tc',
    'ruthenium': 'Ru',
    'rhodium': 'Rh',
    'palladium': 'Pd',
    'silver': 'Ag',
    'cadmium': 'Cd',
    'indium': 'In',
    'tin': 'Sn',
    'antimony': 'Sb',
    'tellurium': 'Te',
    'iodine': 'I',
    'xenon': 'Xe',
    'cesium': 'Cs',
    'barium': 'Ba',
    'lanthanum': 'La',
    'cerium': 'Ce',
    'praseodymium': 'Pr',
    'neodymium': 'Nd',
    'promethium': 'Pm',
    'samarium': 'Sm',
    'europium': 'Eu',
    'gadolinium': 'Gd',
    'terbium': 'Tb',
    'dysprosium': 'Dy',
    'holmium': 'Ho',
    'erbium': 'Er',
    'thulium': 'Tm',
    'ytterbium': 'Yb',
    'lutetium': 'Lu',
    'hafnium': 'Hf',
    'tantalum': 'Ta',
    'tungsten': 'W',
    'rhenium': 'Re',
    'osmium': 'Os',
    'iridium': 'Ir',
    'platinum': 'Pt',
    'gold': 'Au',
    'mercury': 'Hg',
    'thallium': 'Tl',
    'lead': 'Pb',
    'bismuth': 'Bi',
    'polonium': 'Po',
    'astatine': 'At',
    'radon': 'Rn',
    'francium': 'Fr',
    'radium': 'Ra',
    'actinium': 'Ac',
    'thorium': 'Th',
    'protactinium': 'Pa',
    'uranium': 'U',
    'neptunium': 'Np',
    'plutonium': 'Pu',
    'americium': 'Am',
    'curium': 'Cm',
    'berkelium': 'Bk',
    'californium': 'Cf',
    'einsteinium': 'Es',
    'fermium': 'Fm',
    'mendelevium': 'Md',
    'nobelium': 'No',
    'lawrencium': 'Lr',
    'rutherfordium': 'Rf',
    'dubnium': 'Db',
    'seaborgium': 'Sg',
    'bohrium': 'Bh',
    'hassium': 'Hs',
    'meitnerium': 'Mt',
    'darmstadtium': 'Ds',
    'roentgenium': 'Rg',
    'copernicium': 'Cn',
    'nihonium': 'Nh',
    'flerovium': 'Fl',
    'moscovium': 'Mc',
    'livermorium': 'Lv',
    'tennessine': 'Ts',
    'oganesson': 'Og',
}

element_symbols = list(elements_dict.values())
symbols = sorted(element_symbols, key=len, reverse=True)
symbols = [s.lower() for s in symbols]
element_names = list(elements_dict.keys())
names = sorted(element_names, key=len)
names = [n for n in names if len(n) <= 6] ## max length of 3 symbols is 6


def check_symbols(en):
    # print("element: ", en)
    solution = []
    vocab = [e for e in symbols if e in en] ## keep only symbols that are substrings of element name
    perms = itertools.permutations(vocab, 3) ## permutations of 3
    perms = [c for c in perms if len(''.join(c)) <= len(en)] ## total length of symbols must match name length
    for perm in perms:
        if elements_dict[en].lower() not in perm:
            myen = str(en)
            myperm = list(perm)
            while myperm:  ## iterate through each symbol in permutation
                mp = myperm.pop(0)
                if mp in myen:  ## if symbol is substring of name, replace in name with underscores
                    if len(mp) == 1:
                        myen = myen.replace(mp, '_', 1)
                    else:
                        myen = myen.replace(mp, '__', 1)
                else: ## if symbol is not substring of name, empty the permutation and move on
                    myperm = []
            if not myen.replace('_', ''): ## if all letters in name were replaced, keep name and permutation as solution
                solution = [en, perm]
    return solution


def main():
    for element_name in names:
        checked = check_symbols(element_name)
        if checked:
            print("\tSOLUTION:")
            print("\t", checked[0], checked[1])
            

if __name__ == "__main__":
    main()
