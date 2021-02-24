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

cooking = [
	'bain-marie', 'bake', 'baking', 'barbecue', 'barbecuing', 'blacken',
	'blackening', 'blanch', 'blanching', 'boil', 'boiling', 'braise',
	'braising', 'browning', 'charbroil', 'charbroiling', 'coddle', 'coddling',
	'convection', 'deep-fry', 'deep-frying', 'flambe', 'fricassee', 'fry',
	'frying', 'grill', 'grilling', 'microwaving', 'pan-fry', 'pan-frying',
	'parboil', 'parboiling', 'poach', 'poaching', 'pressure-cooking',
	'reduction', 'roast', 'roasting', 'rotisserie', 'saute', 'sauteing',
	'sear', 'searing', 'simmer', 'simmering', 'smoke', 'smoking', 'sous-vide',
	'steam', 'steaming', 'steep', 'steeping', 'stew', 'stewing', 'stir-fry',
	'stir-frying', 'toast', 'toasting'
	]

ethnic_cuisines = [
	'Ainu', 'Albanian', 'Algerian', 'American', 'Andhra', 'Anglo-Indian',
	'Arab', 'Argentine', 'Armenian', 'Assyrian', 'Awadhi', 'Azerbaijani',
	'Balochi', 'Bangladeshi', 'Bashkir', 'Belarusian', 'Belgians', 'Bengali',
	'Berber', 'Brazilian', 'British', 'Buddhist', 'Bulgarian', 'Cajun',
	'Canadian', 'Cantonese', 'Caribbean', 'Chechen', 'Chinese', 'Circassian',
	'Creole', 'Crimean', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Dutch',
	'Egyptian', 'English', 'Eritrean', 'Estonian', 'Ethiopian', 'Filipino',
	'French', 'Georgian', 'German', 'Goan', 'Greek', 'Gujarati', 'Haitian',
	'Hawaiian', 'Hyderabad', 'Indian', 'Indonesian', 'Inuit', 'Irish',
	'Italian', 'Jamaican', 'Japanese', 'Jewish', 'Karnataka', 'Kazakh',
	'Kenyan', 'Keralite', 'Korean', 'Kurdish', 'Laotian', 'Latvian',
	'Lebanese', 'Libyan', 'Lithuanian', 'Maharashtrian', 'Malay', 'Malaysian',
	'Mangalorean', 'Mediterranean', 'Mennonite', 'Mexican', 'Mordovian',
	'Mormon', 'Mughal', 'Native American', 'Nepalese', 'Nigerian', 'Odia',
	'Pakistani', 'Parsi', 'Pashtun', 'Peranakan', 'Persian', 'Peruvian',
	'Polish', 'Portuguese', 'Punjabi', 'Quebecois', 'Rajasthani', 'Romanian',
	'Russian', 'Salvadorian', 'Sami', 'Scottish', 'Serbian', 'Sindhi',
	'Singaporean', 'Slovak', 'Slovenian', 'Somali', 'Soviet', 'Spanish',
	'Sri Lankan', 'Swedish', 'Tahitian', 'Taiwanese', 'Tamil', 'Tatar', 'Texan',
	'Thai', 'Tibetan', 'Turkish', 'Udupi', 'Ukrainian', 'Vietnamese', 'Welsh',
	'Yamal', 'Zambian', 'Zanzibari'
	]

style_cuisines = [
	"Fusion", "Haute", "Nouvelle", "Vegan", "Vegetarian", "Kosher", "Halal"
	]

foods = ['fried rice', 'abalone', 'ahi', 'aioli', 'albacore', 'alfalfa', 'alfredo', 'almond', 'almonds', 'ambrosia', 'antelope', 'apple', 'apples', 'applesauce', 'arepa', 'arepas', 'artichoke', 'arugala', 'asparagus', 'aubergine', 'avacado', 'avocado', 'babaganoosh', 'bacon', 'bagel', 'bagels', 'baguette', 'bahn', 'bahnmi', 'baklava', 'bamboo', 'banana', 'bananas', 'bangers', 'bar-b-cue', 'bar-b-que', 'barbecue', 'barbeque', 'barley', 'barramundi', 'basmati', 'bbq', 'bean', 'beans', 'beef', 'bento', 'berliner', 'bialy', 'bibimbap', 'biryani', 'biscuit', 'biscuits', 'bison', 'bisque', 'bistecca', 'blintzes', 'blueberries', 'blueberry', 'bluefish', 'boeuf', 'bonbon', 'bonbons', 'borscht', 'bouffe', 'bouillabaisse', 'bourbon', 'bourgogne', 'bourguignon', 'bourguignonne', 'bread', 'breads', 'breadsticks', 'breakfast', 'brie', 'briocha', 'brioche', 'broccoli', 'broth', 'brownies', 'bruscetta', 'bufala', 'buffalo', 'bulgogi', 'bulgur', 'bun', 'buns', 'burger', 'buritto', 'burrata', 'burritos', 'burta', 'butterscotch', 'cabbage', 'caesar', 'cake', 'cakes', 'calzone', 'camembert', 'cannoli', 'cantalope', 'capers', 'caprese', 'caramel', 'cardamom', 'carne', 'carp', 'carrot', 'carrots', 'cashew', 'casserole', 'catfish', 'caviar', 'celery', 'celery-leaf', 'cereal', 'ceviche', 'challah', 'chanterelles', 'charcuterie', 'cheddar', 'cheese', 'cheeseburger', 'cheesecake', 'cheetos', 'cherry', 'cherries', 'chestnut', 'chestnuts', 'chicken', 'chickpeas', 'chimichanga', 'chimichurri', 'chip', 'chips', 'chocolat', 'chocolate', 'chowder', 'churro', 'churros', 'clam', 'clams', 'cobb', 'cobbler', 'coconut', 'codfish', 'compote', 'conch', 'congee', 'cookie', 'cookies', 'corn', 'cornbread', 'couscous', 'crab', 'crabcakes', 'crabs', 'crackers', 'cranberry', 'crawfish', 'crepe', 'crepes', 'croissant', 'croque', 'croquette', 'croquettes', 'crostini', 'cupcakes', 'currants', 'curry', 'cuttlefish', 'dal', 'date', 'dates', 'dolma', 'dolmas', 'doner', 'donuts', 'doritos', 'duck', 'dulce', 'dumplings', 'eclairs', 'edamame', 'edimame', 'eel', 'eels', 'egg', 'eggplant', 'eggrolls', 'eggs', 'empanada', 'empanadas', 'enchilada', 'enchiladas', 'endive', 'escargots', 'etoufee', 'fajita', 'fajitas', 'falafel', 'fenugreek', 'fez', 'fig', 'figs', 'fish', 'flambee', 'flank', 'foie', 'foiegras', 'fondu', 'fontina', 'frankfurter', 'franks', 'fricassee', 'frijoles', 'frisee', 'frita', 'frites', 'frito', 'fritters', 'frog', 'frontera', 'fruit', 'fruitcake', 'frybread', 'fudge', 'garlic', 'gazpacho', 'gefilte', 'gefiltefish', 'gelatin', 'gelato', 'gelee', 'geoduck', 'ganoush', 'ghanoush', 'babaghanoush', 'babaganoush', 'ginger', 'gizzard', 'gnocchi', 'goat', 'gochujang', 'goose', 'gooseberry', 'gorgonzola', 'goulash', 'graham', 'grahamcracker', 'granola', 'grape', 'grapefruit', 'grapes', 'gratin', 'gravy', 'grits', 'grouse', 'guacamole', 'guava', 'gumbo', 'gyro', 'haggis', 'halibut', 'ham', 'hamburger', 'hash', 'hassleback', 'hazelnuts', 'herring', 'honey', 'honeydew', 'horseradish', 'huckleberries', 'huevos', 'hummus', 'jalapeno', 'jalebi', 'jam', 'jambalaya', 'jambon', 'jamon', 'japchae', 'jelly', 'jellyfish', 'jerk', 'jerky', 'juice', 'kabob', 'kabobs', 'kale', 'kebab', 'kebabs', 'shishkabob', 'shishkabobs', 'shishkebab', 'shishkebabs', 'shishkebob', 'shishkebobs', 'ketchup', 'kielbasa', 'kimchi', 'kingfish', 'kishkes', 'kiwi', 'knishes', 'knodel', 'kohlrabi', 'kombu', 'lamb', 'lambs', 'lammestek', 'lasagna', 'lasagne', 'lassi', 'latkes', 'leche', 'lemon', 'lemons', 'lentil', 'lentils', 'licorice', 'lime', 'lingonberries', 'linguine', 'liver', 'liverwurst', 'lobster', 'loin', 'loquat', 'lorraine', 'lotus', 'lox', 'lychee', 'mac', 'macadamia', 'macaroni', 'macaron', 'macarons', 'macaroon', 'macaroons', 'manchego', 'mango', 'marinara', 'marmalade', 'marrow', 'marshmallow', 'marzipan', 'masala', 'mascarpone', 'mash', 'meat', 'meatballs', 'meatloaf', 'melba', 'melon', 'melons', 'meringue', 'migas', 'milkshake', 'mince', 'minestrone', 'mint', 'miso', 'mousse', 'mozzarella', 'muffaletta', 'muffin', 'muffins', 'mulligatawny', 'mushroom', 'mushrooms', 'mussels', 'mussles', 'mustard', 'naan', 'nachos', 'nicoise', 'noodle', 'noodles', 'nopales', 'nuggets', 'nutmeg', 'nuts', 'olive', 'olives', 'omelet', 'omelette', 'omlet', 'onigiri', 'onion', 'onions', 'orange', 'oreo', 'orzo', 'ostrich', 'ovos', 'oyster', 'oysters', 'padthai', 'paella', 'pan', 'pancake', 'pancakes', 'papa', 'papaya', 'parmesan', 'parmigiano', 'pasta', 'pastel', 'pastrami', 'pastry', 'pasty', 'pate', 'patty', 'peach', 'peaches', 'peanut', 'peanuts', 'pear', 'peas', 'pecan', 'pecorino', 'peppercorns', 'pepperoni', 'peppers', 'persimmon', 'pesce', 'pesto', 'pheasant', 'pho', 'pickles', 'pie', 'pierogi', 'pierogies', 'pies', 'pigeon', 'pigs', 'pike', 'pilaf', 'pineapple', 'pistachios', 'pizza', 'po-boy', 'poke', 'pokey', 'polenta', 'pollo', 'pomegranate', 'pommes', 'popcorn', 'pork', 'porridge', 'potato', 'potatoes', 'poutine', 'prawn', 'prawns', 'pretzel', 'prosciutto', 'pudding', 'puff', 'pumpernickel', 'pumpkin', 'quesadilla', 'quiche', 'quinoa', 'rabe', 'raclette', 'radishes', 'rambutan', 'ramen', 'raspberries', 'ratatouille', 'ravioli', 'relish', 'reuben', 'ribs', 'rice', 'ricotta', 'rijsttafel', 'risotto', 'roast', 'roll', 'rolls', 's-mores', 'saag', 'sablefish', 'saffron', 'salad', 'salami', 'salmon', 'salsa', 'saltfish', 'saltwater', 'sambal', 'sandwich', 'sandwiches', 'saratoga', 'satay', 'sauerkraut', 'saurkraut', 'sausage', 'sausages', 'savoy', 'scallion', 'scallions', 'scampi', 'schnitzel', 'scotch', 'scottish', 'seafood', 'seed', 'seeds', 'semsemiyeh', 'sesame', 'shabu-shabu', 'shellfish', 'shitake', 'shoots', 'shortbread', 'shrimp', 'shrimps', 'snaps', 'soba', 'sofra', 'sole', 'sopa', 'sopaipilla', 'sorrel', 'sorrell', 'sorrento', 'souffle', 'soufflees', 'soup', 'sourdough', 'soy', 'spaghetti', 'spanakopita', 'spinach', 'springbok', 'squash', 'squid', 'squirrel', 'steak', 'stew', 'stilton', 'strawberries', 'strawberry', 'stroganoff', 'stuffing', 'submarine', 'sugarplums', 'sulze', 'sundae', 'sushi', 'sweetbreads', 'tabbouleh', 'taco', 'tacos', 'taffy', 'tagine', 'tahini', 'tamal', 'tamale', 'tamales', 'tamarind', 'tandoori', 'tangerine', 'tapas', 'tart', 'tarte', 'tater', 'tatertot', 'tempura', 'tenders', 'teriyaki', 'tiramisu', 'toast', 'toffee', 'tofu', 'tomato', 'tomatoes', 'tongue', 'torta', 'torte', 'tortilla', 'tortillas', 'tostones', 'tots', 'tourte', 'tourtiere', 'treacle', 'truffle', 'truffles', 'tuna', 'turkey', 'twinkies', 'vanilla', 'veal', 'vegemite', 'venison', 'vidalia', 'vindaloo', 'wafer', 'waffles', 'wagyu', 'wakame', 'walnut', 'walnuts', 'wasabi', 'watercress', 'watermelon', 'whitefish', 'wiener', 'wings', 'wurst', 'xiaolongbau', 'xiaolongbao', 'yogurt', 'yuzu', 'ziti', 'zucchini', 'panini', 'panino']


alphabet = [
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
	'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
	]


def prep_foods(myfoods):
	keepers = []
	for mf in myfoods:
		mf = mf.lower().split(" ")
		joint = []
		for m in mf:
			m = slugify(m)
			joint.append(m)
			if m not in keepers:
				keepers.append(m)
		jt = ''.join(joint)
		if jt not in keepers:
			keepers.append(jt)
	return keepers


def prep_philosopher(my_philo):
	mp = my_philo.lower().split(" ")
	fname = mp[0]
	fname = slugify(fname)
	fname = ''.join([i for i in fname if i.isalpha()])
	if len(mp) == 1:
		lname = "NONE"
	else:
		lname = mp[-1]
		lname = slugify(lname)
		lname = ''.join([i for i in lname if i.isalpha()])
	return fname, lname



## lowercase all letters, remove punctuation, return first and last name
def prep_personal_name(some_name):
    s = some_name.lower()
    s = s.split(" ")
    f = s[0]
    l = s[-1]
    f = ''.join([i for i in f if i.isalpha()])
    l = ''.join([i for i in l if i.isalpha()])
    return f, l


## lowercase all letters; remove numerals.
def prep_cuisine(mc):
	pc = mc.lower()
	pc = ''.join([i for i in pc if i.isalpha()])
	pc = slugify(pc)
	return pc


def swap_letters(n, some_string):
	some_string = [[some_string]]
	while n > 0:
		some_string = one_swap(some_string)
		n -= 1
	return [c[1] for c in some_string]


def one_swap(sstring):
	swaps = []
	# alphabet = ['a', 'b', 'c']
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



def drop_letters(n, some_string):
	new_strings = []
	substrings = [list(c) for c in combinations(
		some_string, len(some_string)-n)]
	new_strings = ["".join(ss) for ss in substrings]
	return new_strings
	

## sort each string's letters, then compare
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


def get_dirty_plurals(cstr):
	alts = [cstr]
	if cstr.endswith("s"):
		alts.append(cstr[:-1])
	else:
		alts.append(cstr+"s")
	return alts


def main():
	# cuisines = cooking+ethnic_cuisines+style_cuisines
	cuisines = cooking+ethnic_cuisines+style_cuisines+foods
	cuisines = [prep_cuisine(cu) for cu in cuisines]
	# foods = foods1+foods2
	foodlist = cuisines+foods
	foodlist = prep_foods(foodlist)
	foodlist = list(set(foodlist))
	foodlist.sort()
	print(len(foodlist))
	print(len(cuisines))
	# for f in foodlist:
	# 	print(f)
	# philofile = open('../working/clean_philosophers.txt', 'r')
	philofile = open('resources/philosophers.txt', 'r')
	philosophers = philofile.readlines()
	philosophers = [x.strip() for x in philosophers]
	for philo in philosophers:
		fphil, lphil = prep_philosopher(philo)
		# print(fphil, lphil)
		if lphil == "NONE":
			pass
		else:
			fcandidates = swap_letters(1, fphil)
			for fc in fcandidates:
				# print(fphil, fc)
				if fc in foodlist:
					# print("FOOD: "+philo+" "+fc)
					lcandidates = drop_letters(2, lphil)
					for lc in lcandidates:
						for cu in cuisines:
							# ccandidates = drop_letters(2, cu)
							# for cc in ccandidates:
							ccalts = get_dirty_plurals(cu)
							# print(ccalts)
							for ca in ccalts:
								if is_anagram(lc, ca):
									print("SOLUTION: ")
									print(philo, fc, ca, cu)

					
if __name__ == "__main__":
	main()


### friedrich nietzsche <--> friedrice, chinese