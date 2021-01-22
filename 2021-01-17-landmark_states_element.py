#!/usr/bin/env python


## 2021/01/19. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/1/17 Sunday Puzzle:
## https://www.npr.org/2021/01/17/957639050/sunday-puzzle-switch-the-vowel
## That puzzle:
"""
This challenge comes from listener Gerry Reynolds of Chicago.
Name a national landmark (6,3). Add the name of a chemical element.
Rearrange all the letters to name two states. What are they?
"""
## For the text files used here, I cut and pasted the text from the links here 
## and cleaned it up a bit manually:
## https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext&titles=2011
## https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext&titles=2021


states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
          'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
          'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
          'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
          'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
          'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
          'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
          'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
          'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
          'West Virginia', 'Wisconsin', 'Wyoming']

elements = ['Actinium', 'Aluminum', 'Americium', 'Antimony', 'Argon',
            'Arsenic', 'Astatine', 'Barium', 'Berkelium', 'Beryllium',
            'Bismuth', 'Bohrium', 'Boron', 'Bromine', 'Cadmium', 'Calcium',
            'Californium', 'Carbon', 'Cerium', 'Cesium', 'Chlorine',
            'Chromium', 'Cobalt', 'Copernicium', 'Copper', 'Curium',
            'Darmstadtium', 'Dubnium', 'Dysprosium', 'Einsteinium', 'Erbium',
            'Europium', 'Fermium', 'Flerovium', 'Fluorine', 'Francium',
            'Gadolinium', 'Gallium', 'Germanium', 'Gold', 'Hafnium', 'Hassium',
            'Helium', 'Holmium', 'Hydrogen', 'Indium', 'Iodine', 'Iridium',
            'Iron', 'Krypton', 'Lanthanum', 'Lawrencium', 'Lead', 'Lithium',
            'Livermorium', 'Lutetium', 'Magnesium', 'Manganese', 'Meitnerium',
            'Mendelevium', 'Mercury', 'Molybdenum', 'Moscovium', 'Neodymium',
            'Neon', 'Neptunium', 'Nickel', 'Nihonium', 'Niobium', 'Nitrogen',
            'Nobelium', 'Oganesson', 'Osmium', 'Oxygen', 'Palladium',
            'Phosphorus', 'Platinum', 'Plutonium', 'Polonium', 'Potassium',
            'Praseodymium', 'Promethium', 'Protactinium', 'Radium', 'Radon',
            'Rhenium', 'Rhodium', 'Roentgenium', 'Rubidium', 'Ruthenium',
            'Rutherfordium', 'Samarium', 'Scandium', 'Seaborgium', 'Selenium',
            'Silicon', 'Silver', 'Sodium', 'Strontium', 'Sulfur', 'Tantalum',
            'Technetium', 'Tellurium', 'Tennessine', 'Terbium', 'Thallium',
            'Thorium', 'Thulium', 'Tin', 'Titanium', 'Tungsten', 'Uranium',
            'Vanadium', 'Xenon', 'Ytterbium', 'Yttrium', 'Zinc', 'Zirconium']

## Found this list via web search at:
## https://www.listchallenges.com/print-list/77462
all_landmarks = ['Acadia National Park', 'Alamo', 'Alcatraz',
             'American Museum of Natural History', 'Animal Kingdom',
             'Arches National Park', 'Area 51', 'Arlington National Cemetery',
             'AT&T Stadium', 'Atlanta Aquarium', 'Atlantic City',
             'Atlantic City Boardwalk', 'Audubon Aquarium of the Americas',
             'Badlands National Park', 'Balboa Park', 'Bellagio',
             'Belmont Park', 'Big Bend National Park', 'Biltmore',
             'Black Mountain', 'Bonaventure Cemetery', 'Bourbon Street',
             'Broadway', 'Brooklyn Bridge', 'Bryce Canyon National Park',
             'Buffalo National River', 'Busch Gardens Tampa Bay', 'Cape Cod',
             'Casa Grande Ruins National Monument',
             'Castillo De San Marcos National Monument', 'Catalina Island',
             'Cedar Point', 'Central Park',
             'Chaco Culture National Historical Park',
             'Chimney Rock National Historic Site', 'Chrysler Building',
             'Crater Lake', 'Craters of the Moon National Monument & Preserve',
             'Daytona Beach', 'Death Valley', 'Declaration of Independence',
             'Devils Tower National Monument', 'Diamond Head',
             'Discovery Cove', 'Disney World', 'Disneyland', 'Ellis Island',
             'Empire State Building', 'Epcot', 'Everglades National Park',
             'Falling Water', 'Faneuil Hall Marketplace',
             'Finger Lakes National Forest', "Fisherman's Wharf",
             "Ford's Theater",
             'Fort McHenry National Monument and Historic Shrine',
             'Fort Sumter National Monument', 'Freedom Trail in Boston',
             'French Quarter', 'Frenchmen Street', 'Gateway Arch',
             'George Washington Birthplace National Monument',
             'Gettysburg National Military Park', 'Glacier Bay National Park',
             'Glacier National Park', 'Golden Gate Bridge', 'Graceland',
             'Grand Canyon', 'Grand Central Terminal',
             'Grand Teton National Park', 'Great Smoky Mountains National Park',
             'Griffith Observatory', 'Harvard University',
             'Historic Charleston', 'Hollywood Sign', 'Hollywood Studios',
             'Homestead National Monument of America', 'Hoover Dam',
             'Hot Springs National Park', 'Indianapolis Speedway',
             'Iwo Jima Statue', 'Jackson Square', 'Kennedy Space Center',
             'Key West', 'Kilauea Caldera', 'Lake Michigan', 'Lake Powell',
             'Lake Tahoe', 'Las Vegas Strip', 'Liberty Bell',
             'Library of Congress', 'Lincoln Memorial',
             'Little Bighorn Battlefield National Monument', 'Lombard Street',
             'Mackinac Bridge', 'Madison Square Garden', 'Magic Kingdom',
             'Mall of America', 'Mammoth Cave National Park',
             'Mark Twain House & Museum', "Martha's Vineyard",
             'Mercedes-Benz Superdome', 'Mesa Verde National Park',
             'Meteor Crater', 'Metropolitan Museum of Art', 'Miami Beach',
             'Military Working Dog Teams National Monument', 'Millennium Park',
             'Mississippi River', 'Mojave Desert', 'Mono Lake',
             'Montezuma Castle National Monument', 'Monticello', 'Montpellier',
             'Monument Valley', 'Moody Gardens', 'Mount McKinley (Denali)',
             'Mount Rushmore', 'Mount St', 'Mount Washington', 'Myrtle Beach',
             'Napa Valley', 'National Cowboy and Western Heritage Museum',
             'National Mall', 'National September 11 Memorial & Museum',
             'The National WWII Museum', 'National Zoological Park',
             'Nauvoo Historic District', 'Navy Pier', 'Newport Mansions',
             'Niagra Falls', 'North Cascades National Park',
             'Oak Alley Plantation', 'Old Faithful Geyser',
             'Olympic National Park', 'Padre Island National Seashore',
             'The Painted Canyon', 'Paul Bunyan', 'The Paul Revere House',
             'Pentagon', 'Pier 39', 'Pike Place Market', 'Plymouth Rock',
             "Punalu'u Beach", 'Rainbow Bridge National Monument',
             'Red Rocks Amphitheatre', 'Redwood National Park',
             'Rio Grande National Forest', 'Rock and Roll Hall of Fame',
             'Rockefeller Center', 'Rocky Mountain National Park',
             'Rodeo Drive', 'Route 66', 'Royal Gorge Bridge',
             'San Andreas Fault', 'San Antonio River Walk',
             'Schlitterbahn Waterpark New Braunfels', 'Sears Tower Skydeck',
             'Sedona', 'Sequoia National Park', 'Sea World', 'Six Flags',
             'Smithsonian National Museum of Natural History',
             "Smithsonian's National Air and Space Museum",
             'South Street Seaport', 'Space Center Houston',
             'Space Needle', 'Statue of Liberty', 'Table Rock State Park',
             'Temple Square', 'Texas Hill Country Trail',
             'Thomas Jefferson Memorial', 'Times Square', 'Tobasco Tour',
             'Tomb of the Unknown Soldier',
             'Torrey Pines State Natural Reserve',
             'Trail of Tears National Historic Trail',
             'U.S. Space & Rocket Center', 'Union Station', 'Universal Studios',
             'US Botanic Garden', 'USS Arizona Memorial', 'USS Constitution',
             'USS Midway', 'Venice Beach', 'Vicksburg National Military Park',
             'Vietnam Veterans Memorial', 'Waikiki Beach', 'Waimea Canyon',
             'Walk of Fame', 'Wall Street', 'Washington Monument',
             'Washington National Cathedral', 'White House',
             'World of Coca-Cola', 'Wright Brothers National Memorial',
             'Wrigley Field', 'Yellowstone National Park',
             'Yosemite National Park', 'Zion National Park']


## returns all 1225 possible state pairs
def get_state_pairs(my_states):
    state_pairs = []
    for st in my_states:
        for ts in my_states:
            if ts == st:
                pass
            elif [ts, st] in state_pairs or [st, ts] in state_pairs:
                pass
            else:
                state_pairs.append([st,ts])
    return state_pairs


## filters landmarks, keeping only those matching: 6 letter word + 3 letter word
def filter_landmarks(some_landmarks):
    keepers = []
    for ldm in some_landmarks:
        if sum(c.isalpha() for c in ldm) == 9:
            z = ldm.split(" ")
            if len(z[0]) == 6:
                if len(z[1]) == 3:
                    keepers.append(ldm)
    return keepers


## returns all landmark + element pairs
def get_landmark_element_pairs(some_landmarks, some_elements):
    landmark_element_pairs = []
    for lm in some_landmarks:
        for el in some_elements:
            landmark_element_pairs.append([lm, el])
    return landmark_element_pairs


## returns one string of sorted, lowercase letters (ONLY letters) from list;
## e.g., ["North Dakota", "Ohio"] --> "aadhhiknoooortt"
def get_comparison_string(some_list):
    cs = "".join(some_list)
    cs = [d.lower() for d in cs if d.isalpha()]
    cs.sort()
    cs = "".join(cs)
    return cs


## iterates through state pairs and landmark-element pairs to find a pair of
## pairs that use exactly the same letters
def find_solutions(some_state_pairs, some_ld_el_pairs):
    solutions = []
    for sp in some_state_pairs:
        sp_str = get_comparison_string(sp)
        for lp in some_ld_el_pairs:
            lp_str = get_comparison_string(lp)
            if sp_str == lp_str:
                solutions.append([sp, lp])
            else:
                pass
    return solutions


def main():
    st_pairs = get_state_pairs(states)
    print(len(st_pairs))
    landmarks = filter_landmarks(all_landmarks)
    print(landmarks)
    ld_el_pairs = get_landmark_element_pairs(landmarks, elements)
    print(len(ld_el_pairs))
    solved = find_solutions(st_pairs, ld_el_pairs)
    print(solved)


if __name__ == "__main__":
    main()
