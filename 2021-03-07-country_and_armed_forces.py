#!/usr/bin/env python


## 2021/03/07. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/03/07 Sunday Puzzle:
## https://www.npr.org/2021/03/07/974377830/sunday-puzzle-pb-and-j-time
## That puzzle:
"""
This week's challenge comes from listener Mark Scott, of Seattle. Think of a
country with a one-word name. You can rearrange its letters to identify a member
of one of our country's armed forces. Who is that, and what's the country?
"""


from slugify import slugify


members = ['soldier', 'marine', 'sailor', 'airman', 'infantry', 'frogman', 'seal',
		   'ranger', 'paratrooper', 'troop', 'trooper', 'leatherneck', 'jarhead']


countries = [
'Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa',
'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda',
'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan',
'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize',
'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bonaire', 'Bosnia and Herzegovina',
'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory',
'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde',
'Cambodia', 'Cameroon', 'Canada', 'Cayman Islands', 'Central African Republic',
'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos', 'Colombia', 'Comoros',
'Congo', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba', 'Curaçao', 'Cyprus',
'Czechia', "Côte d'Ivoire", 'Denmark', 'Djibouti', 'Dominica',
'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Falkland Islands',
'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia',
'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany',
'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe',
'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
'Heard Island and McDonald Islands', 'Holy See', 'Honduras', 'Hong Kong',
'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland',
'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan',
'Kazakhstan', 'Kenya', 'Kiribati', 'Korea', 'Korea', 'Kuwait', 'Kyrgyzstan',
"Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia',
'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao',
'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte',
'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro',
'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia',
'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua',
'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'North Macedonia',
'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau',
'Palestine', 'Panama',
'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland',
'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda',
'Réunion', 'Saint Barthélemy', 'Saint Helena', 'Saint Kitts and Nevis',
'Saint Lucia', 'Saint Martin', 'Saint Pierre and Miquelon',
'Saint Vincent and the Grenadines', 'Samoa', 'San Marino',
'Sao Tome and Principe', 'Saudi Arabia',
'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten',
'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa',
'South Georgia and the South Sandwich Islands', 'South Sudan', 'Spain',
'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard and Jan Mayen', 'Sweden',
'Switzerland', 'Syrian Arab Republic', 'Taiwan', 'Tajikistan', 'Tanzania',
'Thailand', 'Timor-Leste',
'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine',
'United Arab Emirates', 'United Kingdom of Great Britain and Northern Ireland',
'United States Minor Outlying Islands', 'United States of America', 'Uruguay',
'Uzbekistan', 'Vanuatu', 'Venezuela', 'Viet Nam', 'Virgin Islands',
'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe'
]

cfile = open('resources/countries-one_word.txt', 'r')
countries = cfile.readlines()
cfile.close()
countries = [h.strip() for h in countries]

mfile = open('resources/military-personnel.txt', 'r')
members = mfile.readlines()
mfile.close()
members = [j.strip() for j in members]


def clean_countries(cc):
	cl = []
	for rc in cc:
		rc = rc.strip()
		rc = rc.replace("  ", " ")
		rc = rc.replace("  ", " ")
		rc = rc.split(" ")
		cx = slugify(rc[0])
		cl.append(cx.lower())
	return cl

	
## sort each string's letters, then compare
def is_anagram(x, y):
	x = x.lower()
	x = list(x)
	x = [e for e in x if e.isalpha()]
	x.sort()
	x = "".join(x)
	y = y.lower()
	y = list(y)
	y = [u for u in y if u.isalpha()]
	y.sort()
	y = "".join(y)
	if x == y:
		return True
	else:
		return False


def main():
	ccs = clean_countries(countries)
	for m in members:
		for cy in ccs:
			# print(m, cy)
			if is_anagram(m, cy):
				print("ANAGRAM: ", cy, m)
			elif  is_anagram("a"+m, cy):
				print("ANAGRAM: ", cy, "(a) "+m)


if __name__ == "__main__":
    main()
