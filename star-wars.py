# a python program to import the local nester module 
# and use it tp print out a nested data structure

# import just the function (risky if we have a local function with the same name)
# from nester import print_lol

# import the whole module - will require namespacing the function when used
import nester

# define a nested list
star_wars = ["Episode 4 - A New Hope", 1977,
    ["Tatooine", "Death Star", "Rebel Base", 
        ["Star Destroyer", "Millenium Falcon", "X-Wing Fighter"]
     ]
 ]

# invoke the print_lol method via the nester namespace prefix
nester.print_lol(star_wars, 0)

