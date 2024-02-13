#!/usr/bin/env python


## 2024/02/12. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/02/11 Sunday Puzzle:
## https://www.npr.org/2024/02/11/1230606447/sunday-puzzle-youd-better-sit-down-for-this-one

"""
This week's challenge: Is from our puzzler friend A.J. Jacobs.
Start with the name of a blockbuster movie star. Remove the first letter of 
the first name and last two letters of the last name to get the types of 
movies he almost never stars in. Who is this?
"""

## retrieved and cleaned up this list:
## https://www.listchallenges.com/150-famous-male-actors
stars = ['Jet Li', 'Tim Roth', 'Jude Law', 'Ed Harris', 'Sean Penn', 
        'Tim Allen', 'Paul Rudd', 'Tom Hanks', 'Al Pacino', 'Eric Bana',
        'Brad Pitt', 'Tom Hardy', 'Joe Pesci', 'Paul Dano', 'Riz Ahmed',
        'Matt Damon', 'Jack Black', 'Vin Diesel', 'Will Smith', 'Idris Elba',
        'Guy Pearce', 'Jim Carrey', 'Mel Gibson', 'Tom Cruise', 'Hugh Grant',
        'John Ortiz', 'Toby Jones', 'Ben Foster', 'Jamie Foxx', 'Clive Owen',
        'Chris Pine', 'Oscar Isaac', 'Liam Neeson', 'John Hawkes',
        'Don Cheadle', 'David Morse', 'Andy Garcia', 'John Reilly',
        'Corey Stoll', 'Ben Affleck', 'Kevin Bacon', 'Gary Oldman',
        'Jack Huston', 'Johnny Depp', 'Colin Firth', 'Paul Walker',
        'Elijah Wood', 'Tom Selleck', 'Owen Wilson', 'Jackie Chan',
        'Ben Stiller', 'John Cusack', 'Chris Evans', 'Ethan Hawke',
        'Bill Murray', 'Keanu Reeves', 'Willem Dafoe', 'Steve Martin',
        'Adrien Brody', 'Rupert Grint', 'William Levy', 'Steve Carell',
        'Paul Bettany', 'Nicolas Cage', 'Bruce Willis', 'Heath Ledger',
        'Mark Ruffalo', 'David Wenham', 'Michael York', 'Ian McKellen',
        'Alec Baldwin', 'Alan Cumming', 'Alan Rickman', 'James McAvoy',
        'Ryan Gosling', 'Jason Isaacs', 'Jeremy Irons', 'Cuba Gooding',
        'Eddie Murphy', 'Kurt Russell', 'Richard Gere', 'John Goodman',
        'William Macy', 'Michael Cera', 'Gene Hackman', 'Sam Rockwell',
        'Hugh Jackman', 'Chuck Norris', 'Ben Kingsley', 'John Corbett',
        'Kevin Spacey', 'Sean Connery', 'James Franco', 'Danny Glover',
        'Michael Pitt', 'Stephen Root', 'Josh Duhamel', 'Daniel Craig',
        'Adam Sandler', 'Michael Ealy', 'Shia Labeouf', 'Russell Crowe',
        'Javier Bardem', 'Michael Caine', 'David Thewlis', 'Steve Buscemi',
        'Tom Wilkinson', 'Kevin Costner', 'Paul Giamatti', 'Edward Norton',
        'Mark Wahlberg', 'Michael Sheen', 'Kit Harington', 'Steven Seagal',
        'Colin Farrell', 'Jean VanDamme', 'Harrison Ford', 'Casey Affleck',
        'Jason Statham', 'Ewan McGregor', 'Robert Duvall', 'Danny De Vito',
        'Harvey Keitel', 'Ryan Reynolds', 'Matthew Goode', 'Michael Parks',
        'Orlando Bloom', 'Gerard Butler', 'John Turturro', 'James Marsden',
        'Stanley Tucci', 'Wesley Snipes', 'Rupert Friend', 'Adrian Lester',
        'David Oyelowo', 'Jeff Goldblum', 'John Travolta', 'Ralph Fiennes',
        'Jesse Plemons', 'Michael Pena', 'Robert Downey',
        'Rowan Atkinson', 'Patrick Swayze', 'Samuel Jackson',
        'John Krasinski', 'Liev Schreiber', 'Bradley Cooper',
        'Eugenio Derbez', 'Michael Rooker', 'Cillian Murphy',
        'Pierce Brosnan', 'Jack Nicholson', 'Philip Hoffman',
        'Walton Goggins', 'Gaspard Ulliel', 'Paul Schneider',
        'Michael Jordan', 'Dustin Hoffman', 'Robin Williams',
        'Morgan Freeman', 'George Clooney', 'Tom Hiddleston',
        'Brendan Fraser', 'Michael Murphy', 'Dwayne Johnson',
        'Ashton Kutcher', 'Robert Redford', 'Christian Bale',
        'Clint Eastwood', 'Robert De Niro', 'John Malkovich',
        'Peter Sarsgaard', 'Tommy Lee Jones', 'Joaquin Phoenix',
        'Chris Hemsworth', 'Forest Whitaker', 'Richard Jenkins',
        'Josh Hutcherson', 'Michael Shannon', 'Anthony Hopkins',
        'Patrick Dempsey', 'Michael Douglas', 'Garrett Hedlund',
        'Jake Gyllenhaal', 'Bruce Greenwood', 'Woody Harrelson',
        'Bobby Cannavale', 'Viggo Mortensen', 'David Strathairn',
        'Michael Williams', 'Domhnall Gleeson', 'Chiwetel Ejiofor',
        'Daniel Day Lewis', 'Michael Rapaport', 'Robert Pattinson',
        'Michael Angarano', 'Daniel Day-Lewis', 'Antonio Banderas',
        'Daniel Radcliffe', 'Donald Sutherland', 'Michael Stuhlbarg',
        'Benicio Del Torro', 'Matthew Broderick', 'Kiefer Sutherland',
        'Leonardo DiCaprio', 'Justin Timberlake', 'Denzel Washington',
        'Christopher Walken', 'Stellan Skarsgard', 'Sylvester Stallone',
        'Michael Fassbender', 'John Carroll Lynch', 'Matthew McConaughey',
        'Gael Garcida Bernal', 'Benedict Cumberbatch',
        'Arnold Schwarzenegger']

## I asked ChatGPT for a long list of types of movies and cleaned it up
types = ['action', 'adventure', 'animated', 'animation', 'biographical', 
         'biography', 'biopic', 'buddy cop', 'comedy', 'coming-of-age', 
         'courtroom drama', 'crime', 'cyberpunk', 
         'disaster', 'documentary', 'drama', 
         'educational', 'epic', 'epic adventure', 'experimental', 'family', 
         'family adventure', 'fantasy', 'film noir', 'film-noir', 
         'found footage', 'gangster', 'heist', 'historical', 
         'historical biopic', 'historical epic', 'horror', 'independent',
         'indie', 'mockumentary', 'music', 'musical', 'musical comedy',
         'musical', 'mystery', 'political drama', 'post-apocalyptic',
         'psychological thriller', 'road trip', 'romance', 
         'romantic comedy', 'satirical comedy', 'science fiction',
         'short', 'short film', 'silent', 'silent horror', 'space opera',
         'sport', 'sports drama', 'spy', 'spy thriller', 'steampunk',
         'superhero', 'surreal', 'swashbuckler', 'thriller', 
         'time travel', 'war', 'war epic', 'western', 'zombie']

## per the puzzle, function to apply the transformation
def transform_name(mystar):
    mystar = mystar.lower()
    mystar = mystar[1:-2]
    mystar = "".join(mystar.split(" "))
    return mystar

## to be thorough, we'll try removing spaces and hyphens too
def expand_types(mytypes):
    expanded_types = []
    for ty in mytypes:
        tyx = ty.replace(" ", "")
        tyx = tyx.replace("-", "")
        expanded_types.append(ty)
        expanded_types.append(tyx)
    return expanded_types

def main():
    solutions_a = []
    solutions_b = []
    solutions_c =[]
    solutions_d = []
    x_types = list(set(expand_types(types)))
    for star in stars:
        starx = transform_name(star)
        for xt in x_types:
            ## look for exact matches
            if starx == xt:
                solutions_a.append([star, starx, "(exact)", xt])
            ## Here and below, allowing for a fuzzy match at the end of string
            ## to account for "comedy" vs "comedies", etc.
            ## We also ensure that the length of the matching star and type
            ## strings are at least within margin of 2. This prevents e.g.,
            ## "Jet Li" --> "et" --> "e" matching with "adventure".
            elif abs(len(starx[:-1]) - len(xt)) <= 2 and starx[:-1] in xt:
                solutions_b.append("'"+star+"' becomes '"+starx+"' becomes '"+starx[:-1]+"', which matches '"+xt+"'")
            elif abs(len(starx[:-2]) - len(xt)) <= 2 and starx[:-2] in xt:
                solutions_c.append("'"+star+"' becomes '"+starx+"' becomes '"+starx[:-2]+"', which matches '"+xt+"'")
            elif abs(len(starx[:-3]) - len(xt)) <= 2 and starx[:-3] in xt:
                solutions_d.append("'"+star+"' becomes '"+starx+"' becomes '"+starx[:-3]+"', which matches '"+xt+"'")
            else:
                pass

    print("SOLUTIONS:\n Perfect match:")
    if not solutions_a:
        print("(None)")
    else:
        for sa in solutions_a:
            print(sa)
    print("Final letter not matched:")
    for sb in solutions_b:
        print(sb)
    print("Final 2 letters not matched:")
    for sc in solutions_c:
        print(sc)
    print("Final 3 letters not matched:")
    for sd in solutions_d:
        print(sd)
                           
if __name__ == "__main__":
    main()
