#!/usr/bin/env python

## 2024/09/16. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/09/15 Sunday Puzzle:
## https://www.npr.org/2024/09/14/nx-s1-5110130/sunday-puzzle-two-letters-are-all-you-need
## That puzzle:

"""
This week's challenge comes from listener Rawson Scheinberg, of Northville,
Mich. Name a U.S. state capital. Then name a world capital. Say these names
one after the over and phonetically you'll get an expensive dinner entree.
What is it?
"""

## I'm using this g2p (grapheme to phoneme) python library:
## https://github.com/Kyubyong/g2p

from g2p_en import G2p

world_caps = [
    'Kabul', 'Tirana', 'Tirane', 'Algiers', 'Andorra la Vella', 'Luanda', 
    "Saint John's", 'Buenos Aires', 'Yerevan', 'Canberra', 'Vienna', 'Baku',
      'Nassau', 'Manama', 'Dhaka', 'Bridgetown', 'Minsk', 'Brussels', 
      'Belmopan', 'Porto Novo', 'Thimphu', 'La Paz', 'Sucre', 'Sarajevo', 
      'Gaborone', 'Brasilia', 'Bandar Seri Begawan', 'Sofia', 'Ouagadougou', 
      'Gitega', 'Phnom Penh', 'Yaounde', 'Ottawa', 'Praia', 'Bangui', 
      "N'Djamena", 'Santiago', 'Beijing', 'Bogota', 'Moroni', 'Kinshasa', 
      'Brazzaville', 'San Jose', 'Yamoussoukro', 'Zagreb', 'Havana', 
      'Nicosia', 'Prague', 'Copenhagen', 'Djibouti', 'Roseau', 'Santo Domingo',
      'Dili', 'Quito', 'Cairo', 'San Salvador', 'London', 'Malabo', 'Asmara',
      'Tallinn', 'Mbabane', 'Addis Ababa', 'Palikir', 'Suva', 'Helsinki',
      'Paris', 'Libreville', 'Banjul', 'Tbilisi', 'Berlin', 'Accra', 'Athens',
      "Saint George's", 'Guatemala City', 'Conakry', 'Bissau', 'Georgetown',
      'Port au Prince', 'Tegucigalpa', 'Budapest', 'Reykjavik', 'New Delhi',
      'Jakarta', 'Tehran', 'Baghdad', 'Dublin', 'Jerusalem', 'Rome',
      'Kingston', 'Tokyo', 'Amman', 'Astana', 'Nairobi', 'Tarawa Atoll',
      'Pristina', 'Kuwait City', 'Bishkek', 'Vientiane', 'Riga', 'Beirut',
      'Maseru', 'Monrovia', 'Tripoli', 'Vaduz', 'Vilnius', 'Luxembourg',
      'Antananarivo', 'Lilongwe', 'Kuala Lumpur', 'Male', 'Bamako',
      'Valletta', 'Majuro', 'Nouakchott', 'Port Louis', 'Mexico City',
      'Chisinau', 'Monaco', 'Ulaanbaatar', 'Podgorica', 'Rabat', 'Maputo',
      'Nay Pyi Taw', 'Nay Pyi Taw', 'Windhoek', 'Nauru', 'Kathmandu',
      'Amsterdam', 'Wellington', 'Managua', 'Niamey', 'Abuja', 'Pyongyang',
      'Skopje', 'Belfast', 'Oslo', 'Muscat', 'Islamabad', 'Melekeok',
      'Panama City', 'Port Moresby', 'Asuncion', 'Lima', 'Manila', 'Warsaw',
      'Lisbon', 'Doha', 'Bucharest', 'Moscow', 'Kigali', 'Basseterre',
      'Castries', 'Kingstown', 'Apia', 'San Marino', 'Sao Tome', 'Riyadh',
      'Edinburgh', 'Dakar', 'Belgrade', 'Victoria', 'Freetown', 'Singapore',
      'Bratislava', 'Ljubljana', 'Honiara', 'Mogadishu', 'Pretoria',
      'Bloemfontein', 'Cape Town', 'Seoul', 'Juba', 'Madrid',
      'Sri Jayawardenapura Kotte', 'Khartoum', 'Paramaribo', 'Stockholm',
      'Bern', 'Damascus', 'Taipei', 'Dushanbe', 'Dodoma', 'Bangkok', 'Lome',
      "Nuku'alofa", 'Port of Spain', 'Tunis', 'Ankara', 'Ashgabat',
      'Funafuti', 'Kampala', 'Kyiv', 'Kiev', 'Abu Dhabi', 'London',
      'Washington D.C.', 'Montevideo', 'Tashkent', 'Port Vila', 'Vatican City',
      'Caracas', 'Hanoi', 'Cardiff', "Sana'a", 'Lusaka', 'Harare'
    ]

state_caps = [
    'Albany', 'Annapolis', 'Atlanta', 'Augusta', 'Austin', 'Baton Rouge',
    'Bismarck', 'Boise', 'Boston', 'Carson City', 'Charleston', 'Cheyenne',
    'Columbia', 'Columbus', 'Concord', 'Denver', 'Des Moines', 'Dover',
    'Frankfort', 'Harrisburg', 'Hartford', 'Helena', 'Honolulu',
    'Indianapolis', 'Jackson', 'Jefferson City', 'Juneau', 'Lansing',
    'Lincoln', 'Little Rock', 'Madison', 'Montgomery', 'Montpelier',
    'Nashville', 'Oklahoma City', 'Olympia', 'Phoenix', 'Pierre',
    'Providence', 'Raleigh', 'Richmond', 'Sacramento', 'Saint Paul', 'Salem',
    'Salt Lake City', 'Santa Fe', 'Springfield', 'Tallahassee', 'Topeka',
    'Trenton'
    ]

entrees = [
    'Abalone', 'Alaskan King Crab', 'Arctic Char', 'Baked Alaska',
    'Barramundi', 'Beef Wellington', 'Beluga Caviar', 'Black Cod Miso',
    'Black Truffle Pizza', 'Bluefin Tuna', 'Bouillabaisse', 'Branzino',
    'Carabineros', 'Caviar', 'Chanterelle Mushrooms', 'Chateaubriand',
    'Chilean Sea Bass', 'Coq au Vin', 'Dover Sole', 'Eel', 'Filet Mignon',
    'Foie Gras', 'Frog Legs', 'Gnocchi with Truffle', 'Grouper',
    'Guinea Fowl','Hake', 'Halibut', 'Hanger Steak', 'Iberico Ham',
    'John Dory', 'King Prawns', 'Kobe Beef', 'Langoustine Risotto',
    'Langoustines', 'Lobster Bisque', 'Lobster Ravioli', 'Lobster Thermidor',
    'Mahi Mahi', 'Marlin', 'Monkfish', 'Morel Mushrooms', 'Moreton Bay Bugs',
    'Octopus', 'Orange Roughy', 'Oysters Rockefeller', 'Partridge',
    'Patagonian Toothfish', 'Peking Duck', 'Pheasant', 'Pompano', 'Porchetta',
    'Porcini Mushrooms', 'Quail', 'Rack of Lamb', 'Red Mullet', 'Red Snapper',
    'Roasted Goose', 'Rock Lobster', 'Sablefish', 'Saffron Paella',
    'Sardines', 'Scallops', 'Sea Bream', 'Sea Urchin', 'Skate Wing',
    'Smoked Salmon', 'Snapper', 'Snow Crab', 'Soft Shell Crab',
    'Sole Véronique', 'Spiny Lobster', 'Squab', 'Squid Ink Pasta',
    'Stone Crab', 'Stuffed Quail', 'Sturgeon', 'Suckling Pig',
    'Surf and Turf', 'Sweetbreads', 'Swordfish', 'Tilefish',
    'Truffle Pasta', 'Truffle Risotto', 'Turbot', 'Turbot Fillet',
    'Turbotin', 'Veal Ossobuco', 'Venison', 'Wagyu Beef', 'Wahoo',
    'White Truffle Pasta', 'Whitebait', 'Wild Boar', 'Wild Salmon',
    'Yellowfin Tuna', 'Yellowtail', 'Zander', 'Zucchini Blossoms'
    ]

def pron_strip(mypron):
    # mypron = mypron.replace("0", "")
    # mypron = mypron.replace("1", "")
    # mypron = mypron.replace("2", "")
    # for v in ['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']:
    #     mypron = mypron.replace(v, "")
    while "  " in mypron:
        mypron = mypron.replace("  ", " ")
    return mypron


def main():
    g2p = G2p()
    state_caps.sort(key=len)
    # limiting string lengths to something reasonably likely to succeed:
    scs = [sc for sc in state_caps if len(sc) < 9]
    world_caps.sort(key=len)
    wcs = [wc for wc in world_caps if len(wc) < 9]
    entrees.sort(key=len)
    ees = [ee for ee in entrees if 8 < len(ee) < 16]
    matches = []
    for sc in scs:
        print("\n"+sc)
        for wc in wcs:
            sw = g2p(sc)+g2p(wc)
            sw = " ".join(sw)
            candidate = pron_strip(sw)
            print("\t"+wc+" : "+sw)
            for ee in ees:
                ex = g2p(ee)
                ex = " ".join(ex)
                reference = pron_strip(ex)
                # print("\t"+ee+" : "+reference)
                if candidate == reference:
                    matches.append([sc, wc, ee, candidate])
    print("\n\nMatches: ")
    for m in matches:
        print(m)

if __name__ == '__main__':
    main()
