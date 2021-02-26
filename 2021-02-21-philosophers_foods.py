#!/usr/bin/env python

## 2021/02/22. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/02/21 Sunday Puzzle:
## https://www.npr.org/2021/02/21/969886068/sunday-puzzle-homophones
## That puzzle:
"""
This week's challenge comes from listener Andrew Chaikin, of San Francisco.
Think of a famous philosopher — first and last names. Change one letter in the
first name to get a popular dish. Drop two letters from the last name and
rearrange the result to get the kind of cuisine of this dish. What is it?
"""

from slugify import slugify
from itertools import combinations


## The full cuisine list is too long to include here, but it looks like this:
raw_cuisines = ['Albanian', 'Algerian', 'Cajun', 'Chinese', 'Ethiopian']
## "kind of cuisine" is a little ambiguous, so I include these too:
style_cuisines = ["Fusion", "Haute", "Nouvelle", "Vegan", "Vegetarian",
				  "Kosher", "Halal"]
## The full list of cuisines is read in from this file:
cuisinefile = open("resources/cuisines.txt", "r")
## overwrite the example list above:
raw_cuisines = cuisinefile.readlines()
cuisinefile.close()
raw_cuisines = raw_cuisines+style_cuisines
raw_cuisines = [cl.strip() for cl in raw_cuisines if cl]
raw_cuisines.sort()

## The real food list is too long to include here, but it looks like this:
raw_foods = ["alfalfa sprouts", "bagel and lox", "fried rice",
			 "waldorf pudding"]
## The full list of foods is read in from this file:
foodfile = open("resources/foods.txt", "r")
## overwrite the example list above:
raw_foods = foodfile.readlines()
foodfile.close()
raw_foods = [fl.strip() for fl in raw_foods if fl]
raw_foods.sort()

## The real philosopher list is too long to include here, but it looks like this:
raw_philos = ["john calvin", "martin heidegger","friedrich nietzsche",
			  "karl marx"]
## The full list of foods is read in from this file:
philosfile = open("resources/philosophers.txt", "r")
## overwrite the example list above:
raw_philos = philosfile.readlines()
raw_philos = [pl.strip() for pl in raw_philos if pl]
raw_philos.sort()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
			'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


## takes the list of foods and expands it by recombining words:
## "country fried steak"
## BECOMES -->
## "country"
## "fried"
## "steak"
## "country fried"
## "country steak"
## "fried steak"
## "country fried steak"
## it overgenerates and it's messy but we don't care!
def expand_foods(my_foods):
	r_foods = [fl.strip() for fl in my_foods if fl]
	expanded = []
	for rf in r_foods:
		rf = rf.split(" ")
		for i in range(1, len(rf)+1):
			for combo in combinations(rf, i):
				combo = " ".join(combo)
				if combo not in expanded:
					expanded.append(combo)
	expanded.sort()
	return expanded


## checks if string ends with "s"; if not, adds "s"; if yes, deletes "s";
## a dirty way to expand our list by approximating singulars/plurals
def get_dirty_plurals(cstr):
	alts = [cstr]
	if cstr.endswith("s"):
		alts.append(cstr[:-1])
	else:
		alts.append(cstr+"s")
	return alts


## lowercase, strip non-letters, convert special/accented letters to ASCII
## e.g., "homard à l'américaine" --> "homard a lamericaine"
def prep_foods(myfoods):
	holders = []
	for mf in myfoods:
		mf = mf.lower().split(" ")
		joint = []
		for m in mf:
			m = slugify(m)
			m = ''.join([i for i in m if i.isalpha()])
			joint.append(m)
			if m not in holders:
				holders.append(m)
		jt = ''.join(joint)
		if jt not in holders:
			holders.append(jt)
	holders.sort()
	keepers = []
	for h in holders:
		kk = get_dirty_plurals(h)
		for k in kk:
			if k not in keepers:
				keepers.append(k)
	return keepers


## lowercase, strip non-letters, convert special/accented letters to ASCII;
## also return name as [firstname, lastname]
## e.g., "Stanisław Ignacy Witkiewicz" --> ["Stanislaw", "Witkiewicz"]
## e.g., "Socrates" --> ["Socrates", "NONE"]
## Note that the list I'm using is somewhat pre-processed already
def prep_philosopher(my_philo):
	mp = my_philo.split("#")[0].strip()
	mp = mp.split(" ")
	fname = mp[0]
	fname = slugify(fname)
	fname = ''.join([i for i in fname if i.isalpha()])
	fname = fname.lower()
	if len(mp) == 1:
		lname = "NONE"
	else:
		lname = mp[-1]
		lname = slugify(lname)
		lname = ''.join([i for i in lname if i.isalpha()])
		lname = lname.lower()
	return fname, lname


## lowercase letters; remove numerals, convert accented chars to plain ASCII:
def prep_cuisine(mc):
	pc = mc.lower()
	pc = ''.join([i for i in pc if i.isalpha()])
	pc = slugify(pc)
	return pc


## recursive function, takes a string, returns all the possible new strings
## where n (integer) positions in the original string have been replaced with
## another letter; calls one_swap function for each cycle until reaching n;
def swap_letters(n, some_string):
	some_string = [[some_string]]
	while n > 0:
		some_string = one_swap(some_string)
		n -= 1
	return [c[1] for c in some_string]


## takes a string, plus a list of indices; the indices indicate any positions
## in the string that have already been swapped; function leaves the changed
## positions alone and returns all the possible strings with one new position
## swapped to a new letter
def one_swap(sstring):
	swaps = []
	for ixs_stg in sstring:
		if len(sstring) == 1:
			ixs = []
			stg = sstring[0][0]
		else:
			ixs = ixs_stg[0]  ## list
			stg = ixs_stg[1]  ## string
		for i in range(0, len(stg)):
			if i in ixs:
				pass
			else:
				for l in alphabet:
					if l == stg[i]:
						pass
					else:
						new_stg = list(stg)
						new_stg[i] = l
						new_stg = "".join(new_stg)
						new_ixs = ixs+[i]
						new_ixs.sort()
						new_swap = [new_ixs, new_stg]
						if new_swap not in swaps:
							swaps.append(new_swap)
	return swaps


## takes an integer n and a string, returns all the possible new strings after
## deleting n letters;
## e.g., drop_letters(2, "pear") --> ["pe", "pa", "pr", "ea", "er", "ar"]
def drop_letters(n, some_string):
	new_strings = []
	substrings = [list(c) for c in combinations(
		some_string, len(some_string)-n)]
	new_strings = ["".join(ss) for ss in substrings]
	return new_strings
	

## lowercase, sort each string's letters, then compare;
## e.g., is_anagram("dog", "God") -->
## "dog" --> "dgo"
## "God" --> "god" --> "dgo"
## "dgo" == "dgo" --> "True"
def is_anagram(x, y):
    x = x.lower()
    x = list(x)
    x.sort()
    x = "".join(x)
    y = y.lower()
    y = list(y)
    y.sort()
    y = "".join(y)
    if x == y:
        return True
    else:
        return False



def main():
	## next lines simply clean and expand lists to forms needed for comparison
	cuisines = [prep_cuisine(cu) for cu in raw_cuisines]
	foods = expand_foods(raw_foods)
	foods = prep_foods(foods)
	philosophers = [prep_philosopher(p) for p in raw_philos]
	## iterate through list of philosophers
	for philo in philosophers:
		fphil, lphil = philo[0], philo[1]
		## reject any without a last name ("socrates", "plato", etc.)
		if lphil == "NONE":
			pass
		else:
			## get all possible respellings of first name when we swap 1 letter
			fcandidates = swap_letters(1, fphil)
			## get all possible strings from last name when we drop 2 letters
			lcandidates = drop_letters(2, lphil)
			## iterate through first name respellings
			for fc in fcandidates:
				## continue only if first name respelling is found in food list
				if fc in foods:
					## iterate through last name string candidates
					for lc in lcandidates:
						## iterate through cuisines
						for cu in cuisines:
							## check if last name candidate matches the cuisine
							if is_anagram(lc, cu):
								print("SOLUTION: "+fphil+" "+lphil, fc, cu)


					
if __name__ == "__main__":
	main()
