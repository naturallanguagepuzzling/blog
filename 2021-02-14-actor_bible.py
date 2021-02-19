#!/usr/bin/env python


## 2021/02/15. Levi King. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2021/02/14 Sunday Puzzle:
## https://www.npr.org/2021/02/14/967637320/sunday-puzzle-of-the-anagrams
## That puzzle:
"""
This week's challenge comes from listener Samuel Mace of Smyrna, Del.
Name a famous actor whose first name is a book of the Bible and whose last name
is an anagram of another book of the Bible. Who is it?
"""


## Using the KJV here; We could expand beyond but I suspect this will cover it.
bible_books = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy',
               'Joshua', 'Judges', 'Ruth', '1 Samuel', '2 Samuel', '1 Kings',
               '2 Kings', '1 Chronicles', '2 Chronicles', 'Ezra', 'Nehemiah',
               'Esther', 'Job', 'Psalms', 'Proverbs', 'Ecclesiastes',
               'Song of Solomon', 'Isaiah', 'Jeremiah', 'Lamentations',
               'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah',
               'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah',
               'Malachi', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans',
               '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians',
               'Philippians', 'Colossians', '1 Thessalonians',
               '2 Thessalonians', '1 Timothy', '2 Timothy', 'Titus', 'Philemon',
               'Hebrews', 'James', '1 Peter', '2 Peter', '1 John', '2 John',
               '3 John', 'Jude', 'Revelation']

## subset of above; removed numerals, e.g., "1 Peter" --> "Peter"
name_books = ['Joshua', 'Ruth', 'Samuel', 'Ezra', 'Nehemiah', 'Esther', 'Job',
              'Isaiah', 'Jeremiah', 'Ezekiel', 'Daniel', 'Hosea', 'Joel',
              'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk',
              'Zephaniah', 'Haggai', 'Zechariah', 'Malachi', 'Matthew', 'Mark',
              'Luke', 'John', 'Timothy',  'Titus', 'Philemon', 'James', 'Peter',
              'John', 'Jude']

## 1000 actors, adapted from: https://www.imdb.com/list/ls058011111/
actors = ['Robert DeNiro', 'Jack Nicholson', 'Marlon Brando',
          'Denzel Washington', 'Katharine Hepburn', 'Humphrey Bogart',
          'Meryl Streep', 'Daniel Day-Lewis', 'Sidney Poitier', 'Clark Gable',
          'Ingrid Bergman', 'Tom Hanks', 'Elizabeth Taylor', 'Bette Davis',
          'Gregory Peck', 'Leonardo DiCaprio', 'Cate Blanchett',
          'Audrey Hepburn', 'Spencer Tracy', 'Kate Winslet', 'Shah Khan',
          'Viola Davis', 'Sophia Loren', 'Cary Grant', 'Vivien Leigh',
          'Marilyn Monroe', 'Laurence Olivier', 'James Stewart',
          'Steve McQueen', 'Halle Berry', 'Julia Roberts', 'Bruce Lee',
          'Jodie Foster', 'Judy Garland', 'Henry Fonda', 'Morgan Freeman',
          'Catherine Deneuve', 'Grace Kelly', 'Helen Mirren', 'James Cagney',
          'Angela Bassett', 'Johnny Depp', 'Greta Garbo', 'Olivia deHavilland',
          'Charles Chaplin', 'Setsuko Hara', 'Julie Andrews',
          'Montgomery Clift', 'Isabelle Huppert', 'Al Pacino', 'Kirk Douglas',
          'Marcello Mastroianni', 'Gene Kelly', 'James Dean', 'Will Smith',
          'Toshiru Mifune', 'John Wayne', 'Mohanlal', 'Harrison Ford',
          'Gary Cooper', 'GÈrard Depardieu', 'Forest Whitaker',
          'Dustin Hoffman', 'Charlton Heston', 'Tom Cruise', 'Paul Newman',
          'Samuel Jackson', "Peter O'Toole", 'Robin Williams', 'Don Cheadle',
          'Antonio Banderas', 'Eddie Murphy', 'Anthony Hopkins', 'Omar Sharif',
          'Heath Ledger', 'Diane Keaton', 'Rita Hayworth', 'Natalie Wood',
          'Joan Crawford', 'Susan Sarandon', 'Glenn Close', 'Joan Fontaine',
          'Julianne Moore', 'Regina King', 'Angelina Jolie', 'Jane Fonda',
          'Liv Ullmann', 'Natalie Portman', 'Sandra Bullock', 'Deborah Kerr',
          'Emma Thompson', 'Michelle Pfeiffer', 'Faye Dunaway', 'Penelope Cruz',
          'Nicole Kidman', 'Salma Hayek', 'Sigourney Weaver', 'Kathy Bates',
          'Lucy Liu', 'Amy Adams', 'Jeff Bridges', 'Ben Kingsley',
          'Tommy Lee Jones', 'Robert Redford', 'Jack Lemmon',
          'Christopher Plummer', 'George Scott', 'Joaquin Phoenix',
          'Christopher Walken', 'Philip Seymour Hoffman', 'George Clooney',
          'Gene Hackman', 'Bruce Willis', 'Sean Connery', 'Ian McKellen',
          'Russell Crowe', 'Bill Murray', 'Nicolas Cage', 'Joe Pesci',
          'Brad Pitt', 'Kevin Costner', 'Donald Sutherland', 'Clint Eastwood',
          'Michael Douglas', 'Robert Downey', 'Ava Gardner', 'Sally Field',
          'Doris Day', 'Shirley MacLaine', 'Holly Hunter', 'Hilary Swank',
          'Claudette Colbert', 'Diane Lane', 'Jessica Lange', 'Gloria Swanson',
          'Lauren Bacall', 'Frances McDormand', 'Norma Shearer', 'Bette Midler',
          'Mary Moore', 'Anna Magnani', 'Judi Dench', 'Sharon Stone',
          'Kim Basinger', 'Glenda Jackson', 'Donna Reed', 'Demi Moore',
          'Anne Hathaway', 'Liza Minnelli', 'Geena Davis', 'Peter Sellers',
          'Woody Allen', 'Mel Gibson', 'Jim Carrey', 'Mark Wahlberg',
          'Steve Martin', 'Javier Bardem', 'Christoph Waltz', 'Tim Robbins',
          'Arnold Schwarzenegger', 'Sylvester Stallone', 'Viggo Mortensen',
          'Christopher Lee', 'Geoffrey Rush', 'Alec Guinness', 'Richard Burton',
          'Alec Baldwin', 'James Caan', 'Chiwetel Ejiofor', 'Mads Mikkelsen',
          'Ben Stiller', 'Willem Dafoe', 'Ed Harris', 'Harvey Keitel',
          'Jon Voight', 'Drew Barrymore', 'Winona Ryder', 'Kathleen Turner',
          'Uma Thurman', 'Rene Russo', 'Whoopi Goldberg', 'Annette Bening',
          'Maggie Smith', 'Barbra Streisand', 'Jennifer Lawrence',
          'Joanne Woodward', 'Mercedes McCambridge', 'Anjelica Huston',
          'Dianne Wiest', 'Goldie Hawn', 'Claudia Cardinale', 'Gwyneth Paltrow',
          'Charlize Theron', 'Debra Winger', 'Marion Cotillard',
          'Christina Ricci', 'Juliette Binoche', 'Daryl Hannah',
          'Shirley Booth', 'Reese Witherspoon', 'Benicio DelToro',
          'Kevin Bacon', 'Patrick Swayze', 'Michael Caine', 'Robert Duvall',
          'Burt Lancaster', 'Robert Mitchum', 'Colin Farrell', 'William Holden',
          'Edward Robinson', 'William Powell', 'Jared Leto', 'Errol Flynn',
          'Groucho Marx', 'James Mason', 'Buster Keaton', 'Orson Welles',
          'Fred Astaire', 'Bradley Cooper', 'Gary Oldman', 'Jude Law',
          'Paul Giamatti', 'Liam Neeson', 'Matt Damon', 'Michael Fassbender',
          'Carol Burnett', 'Jessica Tandy', 'Helen Hunt', 'Patricia Arquette',
          'Carmen Miranda', 'Kate Hudson', 'Catherine Zeta-Jones',
          'Cameron Diaz', 'Debbie Reynolds', 'Ellen Burstyn', "Maureen O'Hara",
          'Myrna Loy', 'Lena Headey', 'Toni Collette', 'Laura Linney',
          'Marlene Dietrich', 'Carole Lombard', 'Jean Arthur', 'Jean Harlow',
          'Ginger Rogers', 'Mary Pickford', 'Mae West', 'Gillian Anderson',
          'Emma Watson', 'Meg Ryan', 'Alan Arkin', 'Kurt Russell',
          'Jake Gyllenhaal', 'Ryan Gosling', 'Colin Firth', 'Jamie Foxx',
          'Adrien Brody', 'Roberto Benigni', 'Jeremy Irons', 'F. Abraham',
          'Richard Dreyfuss', 'Peter Finch', 'Art Carney', 'Cliff Robertson',
          'Lee Marvin', 'Rex Harrison', 'Anthony Quinn', 'Maximilian Schell',
          'Tom Hardy', 'David Niven', 'William Hurt', 'Yul Brynner',
          'Ernest Borgnine', 'Benedict Cumberbatch', 'Rod Steiger',
          'Chloe Grace Moretz', 'Anna Kendrick', 'Emily Watson',
          'Helena Bonham Carter', 'Keira Knightley', 'Alexis Thorpe',
          'Marion Davies', 'Scarlett Johansson', 'Dakota Fanning',
          'Jennifer Aniston', 'Jennifer Connelly', 'Rachel McAdams',
          'Carey Mulligan', 'Mila Kunis', 'Amanda Seyfried', 'Jennifer Lopez',
          'Neve Campbell', 'Fairuza Balk', 'Jessica Alba', 'Kristen Stewart',
          'Julie Walters', 'Rooney Mara', 'Jamie Curtis', 'Emma Stone',
          'Kirsten Dunst', 'Jose Ferrer', 'Broderick Crawford', 'Ronald Colman',
          'Fredric March', 'Ray Milland', 'Bing Crosby', 'Paul Lukas',
          'Robert Donat', 'Paul Muni', 'Victor McLaglen', 'Charles Laughton',
          'Wallace Beery', 'Lionel Barrymore', 'Jeff Goldblum',
          'Chris Hemsworth', 'Warner Baxter', 'Emil Jannings', 'Chris Cooper',
          'Jim Broadbent', 'James Coburn', 'Cuba Gooding', 'Martin Landau',
          'Jack Palance', 'Kevin Kline', 'Don Ameche', 'Kate Beckinsale',
          'Zooey Deschanel', 'Michelle Williams', 'Milla Jovovich',
          'Selena Gomez', 'Rachel Weisz', 'Kristen Bell', 'Katherine Heigl',
          'Liv Tyler', 'Jessica Chastain', 'Megan Fox', 'Betty White',
          'Geraldine Page', 'Eliza Dushku', 'Robin Wright', 'Leighton Meester',
          'Jennifer Jones', 'Shirley Temple', 'Julia Louis-Dreyfus',
          'Olivia Thirlby', 'Cher', 'Sissy Spacek', 'Louise Fletcher',
          'Julie Christie', 'Patricia Neal', 'Haing Ngor', 'Louis Gossett',
          'John Gielgud', 'Timothy Hutton', 'Melvyn Douglas', 'Jason Robards',
          'George Burns', 'Christian Bale', 'Ethan Hawke', 'Ben Johnson',
          'John Mills', 'Jack Albertson', 'Sean Penn', 'George Kennedy',
          'Walter Matthau', 'Martin Balsam', 'Peter Ustinov', 'Ed Begley',
          'George Chakiris', 'Hugh Griffith', 'Burl Ives', 'Red Buttons',
          "Edmond O'Brien", 'Chris Pratt', 'Frank Sinatra', 'Anne Bancroft',
          'Kim Novak', 'Simone Signoret', 'Elliot Page', 'Angela Lansbury',
          'Judy Holliday', 'Loretta Young', 'Shirley Jones', 'Vera Farmiga',
          'Helen Hayes', 'Marie Dressler', 'Janet Gaynor', "Lupita Nyong'o",
          'Octavia Spencer', 'Melissa Leo', "Mo'Nique", 'Marlee Matlin',
          'Tilda Swinton', 'Jennifer Hudson', 'RenÈe Zellweger',
          'Marcia Gay Harden', 'Anna Paquin', 'Marisa Tomei', 'Mercedes Ruehl',
          'Brenda Fricker', 'Jean Reno', 'George Sanders', 'Dean Jagger',
          'Walter Huston', 'Edmund Gwenn', 'Harold Russell', 'Hugh Grant',
          'Barry Fitzgerald', 'Charles Coburn', 'Van Heflin', 'Donald Crisp',
          'Thomas Mitchell', 'Walter Brennan', 'Joseph Schildkraut',
          'Keanu Reeves', 'Channing Tatum', 'Hugh Jackman', 'Dwayne Johnson',
          'Adam Sandler', 'Daniel Radcliffe', 'Daniel Craig', 'Henry Cavill',
          'Vin Diesel', 'Ben Affleck', 'Chris Pine', 'Olympia Dukakis',
          'Peggy Ashcroft', 'Linda Hunt', 'Maureen Stapleton',
          'Mary Steenburgen', 'Beatrice Straight', 'Vanessa Redgrave',
          'Lee Grant', 'Eileen Heckart', 'Cloris Leachman', 'Ruth Gordon',
          'Estelle Parsons', 'Sandy Dennis', 'Shelley Winters',
          'Maggie Gyllenhaal', 'Katie Holmes', 'Patty Duke', 'Rita Moreno',
          'Wendy Hiller', 'Miyoshi Umeki', 'Dorothy Malone', 'Jo Van Fleet',
          'Eva Marie Saint', 'Gloria Grahame', 'Kim Hunter', 'Lee Cobb',
          'Andrew Garfield', 'John Cazale', 'Jeremy Renner', 'Steve Carell',
          'Jean Dujardin', 'Chris Evans', 'James Franco', 'Zach Galifianakis',
          'Will Ferrell', 'Shia LaBeouf', 'Seth Rogen', 'Joseph Gordon-Levitt',
          'Ryan Reynolds', 'Paul Rudd', 'Jason Segel', 'Jason Statham',
          'Dick Van Dyke', 'Jesse Eisenberg', 'Owen Wilson', 'Jason Bateman',
          'Tyler Perry', 'Liam Hemsworth', 'William Shatner', 'Gene Wilder',
          'Thora Birch', 'Claire Trevor', 'Celeste Holm', 'Anne Baxter',
          'Queen Latifah', 'Ethel Barrymore', 'Rosario Dawson', 'Teresa Wright',
          'Mary Astor', 'Jane Darwell', 'Alicia Vikander', 'Mia Wasikowska',
          'Abigail Breslin', 'Gale Sondergaard', 'Melissa McCarthy', 'Tina Fey',
          'Zoe Saldana', 'Elisabeth Moss', 'Adrianne Palicki',
          'Jennifer Garner', 'Kristen Wiig', 'June Squibb', 'Sally Hawkins',
          'Kaley Cuoco', 'Naomi Watts', 'Robert Pattinson', 'Charlie Hunnam',
          'Nicholas Hoult', 'Aaron Taylor-Johnson', 'Bryan Cranston',
          'Gerard Butler', 'Paul Walker', 'Karl Urban', 'Logan Lerman',
          'Dave Franco', 'Tom Hiddleston', 'Peter Dinklage', 'Taylor Kitsch',
          'Edward Norton', 'Guy Pearce', 'Mark Ruffalo', 'Mickey Rourke',
          'Frank Langella', 'Eddie Redmayne', 'David Strathairn',
          'Terrence Howard', 'Ralph Fiennes', 'Tom Wilkinson',
          'Richard Farnsworth', 'Nick Nolte', 'AnnaSophia Robb',
          'Gemma Arterton', 'Olivia Wilde', 'Isla Fisher', 'Shailene Woodley',
          'Rebel Wilson', 'Emma Roberts', 'Amber Heard', 'Teresa Palmer',
          'Saoirse Ronan', 'Elizabeth Banks', 'Ida Lupino', 'Natalie Dormer',
          'Brittany Snow', 'Kate Mara', 'Julianne Hough', 'Lily Collins',
          'Cobie Smulders', 'Alice Eve', 'Jamie Chung', 'Noomi Rapace',
          'Blake Lively', 'Maggie Grace', 'Jessica Biel', 'Eva Green',
          'Peter Fonda', 'Woody Harrelson', 'Billy Bob Thornton', 'Idris Elba',
          'Nigel Hawthorne', 'Laurence Fishburne', 'Stephen Rea',
          'Warren Beatty', 'Richard Harris', 'John Cusack', 'Kenneth Branagh',
          'Edward James Olmos', 'Max von Sydow', 'Bruce Dern', 'Bob Hoskins',
          'James Woods', 'John Hawkes', 'James Garner', 'Sam Waterston',
          'Tom Hulce', 'Albert Finney', 'Tom Conti', 'Tom Courtenay',
          'Dudley Moore', 'John Hurt', 'Kat Dennings', 'Priyanka Chopra',
          'Emmanuelle Riva', 'Greta Gerwig', 'Brie Larson', 'Jessica Lucas',
          'Maria Falconetti', 'Greer Garson', 'Rosalind Russell',
          'Raquel Welch', 'Linda Fiorentino', 'Gabourey Sidibe', 'Judy Davis',
          'Mia Farrow', 'Audrey Tautou', 'Jeanne Moreau', 'Jane Wyman',
          'Gena Rowlands', 'Lesley Manville', 'Elizabeth Olsen',
          'Nastassja Kinski', 'MÈlanie Laurent', 'Whitney Houston',
          'Felicity Huffman', 'Imelda Staunton', 'Oscar Isaac', 'Jon Heder',
          'Miles Teller', 'Daniel Bruhl', 'James Gandolfini', 'Michael Jordan',
          'Anthony Perkins', 'David Thewlis', 'Klaus Kinski',
          'Malcolm McDowell', 'Ray Winstone', 'Jean-Paul Belmondo',
          'Andy Serkis', 'Matthew Broderick', 'Dennis Hopper', 'Michael Rooker',
          'Vincent Gallo', 'Kevin Spacey', 'Vincent Cassel', 'J.K. Simmons',
          'Boris Karloff', 'Peter Lorre', 'Matthew McConaughey',
          'Paddy Considine', 'Ryan Phillippe', 'Kerry Washington',
          'Carrie-Anne Moss', 'Janet Leigh', 'Catalina Moreno',
          'Samantha Morton', 'Keisha Castle-Hughes', 'Barbara Stanwyck',
          'Joan Allen', 'Janet McTeer', 'Fernanda Montenegro', 'Kristin Thomas',
          'Brenda Blethyn', 'Elisabeth Shue', 'Miranda Richardson',
          'Stockard Channing', 'Luise Rainer', 'Mary McDonnell', 'Lucille Ball',
          'Laura Dern', 'Pauline Collins', 'Isabelle Adjani',
          'Melanie Griffith', 'Sally Kirkland', 'Jane Alexander',
          'Marsha Mason', 'Freddie Highmore', 'Michael Fox', 'John Travolta',
          'Yun-Fat Chow', 'Seth MacFarlane', 'Jet Li', 'John Houseman',
          'Chuck Norris', 'Jean-Claude VanDamme', 'Sam Rockwell', 'Takashi Shimura',
          'Richard Grant', 'Leslie Nielsen', 'Simon Pegg', 'John Malkovich',
          'Michael Shannon', 'Martin Sheen', 'Christopher Guest',
          'Alan Rickman', 'Jackie Haley', 'Gig Young', 'James Spader',
          'Eric Bana', 'Romain Duris', 'Robert Shaw', 'Jacki Weaver',
          'BÈrÈnice Bejo', 'Hailee Steinfeld', 'Jennifer Jason Leigh',
          'Kathleen Quinlan', 'Taraji P. Henson', 'Amy Ryan', 'Ruby Dee',
          'Jill Clayburgh', 'Adriana Barraza', 'Rinko Kikuchi',
          'Catherine Keener', 'Charlotte Rampling', 'Sophie Okonedo',
          'Patricia Clarkson', 'Shohreh Aghdashloo', 'Lindsay Lohan',
          'Michelle Trachtenberg', 'ChloÎ Sevigny', 'Lynn Redgrave',
          'Rachel Griffiths', 'Margot Robbie', 'Lili Taylor', 'Robin Weigert',
          'Lake Bell', 'Claude Rains', 'Steve Buscemi', 'John Rhys-Davies',
          'Jean-Louis Trintignant', 'Joseph Cotten', 'Barry Pepper',
          'Erich von Stroheim', 'Patrick Wilson', 'Christopher Lloyd',
          'Ben Foster', 'Joel McCrea', 'Choi Min-sik', 'Ewan McGregor',
          'Gael GarcÌa Bernal', 'Bruno Ganz', 'Sean Astin', 'Irrfan Khan',
          'Michael C. Hall', 'Roy Scheider', 'Casey Affleck', 'Gary Busey',
          'Norman Reedus', 'Jeff Daniels', 'Stanley Tucci', 'Kiefer Sutherland',
          'Michelle Yeoh', 'LÈa Seydoux', 'Dakota Johnson', 'Julie Delpy',
          'Linda Hamilton', 'Carrie Fisher', 'Pam Grier', 'Bjork',
          'Emily Browning', 'Juliette Lewis', 'Sarah Jessica Parker',
          'Piper Laurie', 'Miley Cyrus', 'Lily Tomlin', 'Jane Seymour',
          'Gloria Stuart', 'Talia Shire', 'Gal Gadot', 'Sue Lyon',
          'Olivia Newton-John', 'Minnie Driver', 'Teri Garr', 'Keri Russell',
          'Jean Seberg', 'Sarah Polley', 'Josh Brolin', 'Hal Holbrook',
          'Djimon Hounsou', 'Matt Dillon', 'Alan Alda', 'Thomas Haden Church',
          'Clive Owen', 'Ken Watanabe', 'Suraj Sharma', 'John C. Reilly',
          'Michael Clarke Duncan', 'Haley Joel Osment', 'Greg Kinnear',
          'Burt Reynolds', 'Robert Forster', 'Jason Schwartzman',
          'William H. Macy', 'Armin Mueller-Stahl', 'Tim Roth',
          'James Cromwell', 'Chazz Palminteri', 'Gary Sinise', 'Paul Scofield',
          'Pete Postlethwaite', 'Hugo Weaving', 'Jada Pinkett Smith',
          "Tatum O'Neal", 'Anna Faris', 'Hattie McDaniel', 'Famke Janssen',
          'Rosamund Pike', 'Bonnie Hunt', 'Leslie Mann', 'Mindy Kaling',
          'Thandie Newton', 'Amy Poehler', 'Amanda Peet', 'Julia Stiles',
          'Maria Bello', 'Eva Mendes', 'Emily Blunt', 'Rose Byrne',
          'Ashley Judd', 'Emilia Clarke', 'Christina Applegate', 'Nia Long',
          'Felicity Jones', 'TÈa Leoni', 'Alexandra Daddario', 'Jena Malone',
          'Richard Gere', 'Nick Frost', 'Ray Liotta', 'Chris Rock', 'Jon Hamm',
          'Neil Patrick Harris', 'Charlie Sheen', 'Mark Rylance', 'Andy Garcia',
          'Michael Lerner', 'Graham Greene', 'Bruce Davison', 'Dan Aykroyd',
          'Danny Aiello', 'River Phoenix', 'Dean Stockwell', 'Billy Crystal',
          'John Goodman', 'Orlando Bloom', 'Stellan Skarsgard',
          'Alexander Skarsgard', 'Mike Myers', 'Tyrese Gibson', 'Elijah Wood',
          'Danny DeVito', 'Susan Hayward', 'Michelle Rodriguez',
          'Sarah Michelle Gellar', 'Sandra Oh', 'Margot Kidder', 'Beyonce',
          'Rebecca Hall', 'Piper Perabo', 'Courteney Cox', 'Parker Posey',
          'Paula Patton', 'Michelle Monaghan', 'Claire Danes', 'Allison Janney',
          'Kate Bosworth', 'Evan Rachel Wood', 'Mira Sorvino', 'Ziyi Zhang',
          'Amanda Bynes', 'Lisa Kudrow', 'Brit Marling', 'Cynthia Erivo',
          'Sofia Vergara', 'Mandy Moore', 'Virginia Madsen', 'James Marsden',
          'Tim Allen', 'Giovanni Ribisi', 'Rutger Hauer', 'Vince Vaughn',
          'Brian Cox', 'Dennis Quaid', 'John Leguizamo', 'Michael Keaton',
          'Billy Burke', 'Brendan Gleeson', 'Charles Bronson', 'Jonathan Pryce',
          'Tobey Maguire', 'Michael Sheen', 'Justin Long', 'Jack Black',
          'Mel Brooks', 'Pierce Brosnan', 'Sean Bean', 'Mahershala Ali',
          'Josh Duhamel', 'Chadwick Boseman', 'Jon Favreau', 'Danny Glover',
          'Freida Pinto', 'Hilary Duff', 'Mary Elizabeth Winstead',
          'Jennifer Coolidge', 'Andrea Riseborough', 'Molly Ringwald',
          'January Jones', 'Maya Rudolph', 'Sophie Marceau', 'Franka Potente',
          'Claire Foy', 'Rashida Jones', 'Alicia Silverstone', 'Lillian Gish',
          'Evangeline Lilly', 'Olivia Colman', 'Mireille Enos',
          'Jennifer Love Hewitt', 'Emmy Rossum', 'Joey King',
          'Ginnifer Goodwin', 'Christine Taylor', 'Vanessa Hudgens',
          'Abbie Cornish', 'Florence Pugh', 'Ian Holm', 'Nathan Lane',
          'Cary Elwes', 'Martin Lawrence', 'Steve Coogan', 'Sacha Baron Cohen',
          'Jeffrey Wright', 'Jackie Chan', 'Aaron Eckhart', 'Sam Worthington',
          'Jack Davenport', 'Alfred Molina', 'Tim Curry', 'Mark Hamill',
          'Brendan Fraser', 'Ice Cube', 'Liev Schreiber', 'Ed Helms',
          'Val Kilmer', 'Russell Brand', 'Craig T. Nelson', 'Bernie Mac',
          'Patrick Stewart', 'Seth Green', 'Ashton Kutcher', 'Randy Quaid',
          'Wesley Snipes', 'David Oyelowo', 'Mark Strong', 'Rob Schneider',
          'Jay Baruchel', 'Hayden Christensen', 'Ray Stevenson', 'Paul Bettany',
          'Hugh Laurie', 'Chris Tucker', 'John Candy', 'Richard Attenborough',
          "Chris O'Donnell", 'Benjamin Bratt', 'Common', 'Marlon Wayans',
          'Albert Brooks', 'Aaron Paul', 'Macaulay Culkin', 'Sam Elliott',
          'Taron Egerton', 'Jim Caviezel', 'Elvis Presley', 'Jonah Hill',
          'Sung Kang', 'Jason Sudeikis', 'Josh Hartnett', 'Cillian Murphy',
          'Billy Crudup', 'Anthony Mackie', 'John Barrymore',
          'Timothy Olyphant', 'Josh Gad', 'Billy Zane', 'Luke Wilson',
          'Peter Sarsgaard', 'Rhys Ifans', 'Topher Grace', 'Kevin Hart',
          'Paul Dano', 'Bill Hader', 'Rob Lowe', 'Mel Blanc', 'David Spade',
          'Rob Riggle', 'Lance Henriksen', 'Richard Jenkins', 'Emilio Estevez',
          'Michael Ealy', 'Jamie Bell', 'Troy Baker', 'Danny McBride',
          'Jonathan Rhys Meyers', 'Michael Cera', 'Bill Paxton',
          'Ioan Gruffudd', 'Andrew Lincoln', 'Ezra Miller', 'Bill Pullman',
          'Craig Robinson', 'Charlie Day', 'Andy Samberg', 'Garrett Hedlund',
          'Cam Gigandet', 'John Krasinski', 'Kevin James', 'Christopher Reeve',
          'James McAvoy', 'Rufus Sewell', 'Adam Driver', 'Ned Beatty',
          'John Cleese', 'John Turturro', 'Jerry Lewis']


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
def prep_bible_book(some_book):
    b = some_book.lower()
    b = ''.join([i for i in b if i.isalpha()])
    return b

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


def main():
    ## lowercase all names in name_books; e.g., "Ezra" --> "ezra"
    nbs = [j.lower() for j in name_books]
    ## lowercase and remove numerals from all bible books; e.g., "1 Kings" --> "kings"
    bbs = [prep_bible_book(g) for g in bible_books]
    ## remove duplicates (because, e.g., "1 Kings" & "2 Kings" both --> "kings")
    bbs = list(set(bbs))
    ## iterate through actors list
    for ac in actors:
        ## get first and last name of actor
        acf, acl = prep_personal_name(ac)
        ## check if first name is in list of bible books that are personal names
        if acf in nbs:
            ## if so, iterate through full list of bible books
            for bb in bbs:
                ## check if last name and bible book are anagrams
                if is_anagram(acl, bb):
                    ## print any solutions
                    print(ac+" : "+acf+" "+bb)
                else:
                    pass
        else:
            pass
        
    
if __name__ == "__main__":
    main()
