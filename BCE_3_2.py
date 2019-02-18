# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 18:06:11 2019

CGU IST 303.W SP2019 1
Module 3: BCE 3.2: Team Exercise

"""

#Task 1 Answer
#Create tuples
george, john, paul, ringo = ("George", "guitar"), ("John", "guitar"), ("Paul", "bass"), ("Ringo", "drums")
#Add tuples to list, including the list name, "beatles"
beatles = ["beatles", george, john, paul, ringo]
#Print to verify output
print("Task 1: Beatles list\n", beatles, "\n")
#Output: ['beatles', ('George', 'guitar'), ('John', 'guitar'), ('Paul', 'bass'), ('Ringo', 'drums')]

#Task 1 Alternative Answers
#Create tuple of tuples
band = (("George", "guitar"), ("John", "guitar"), ("Paul", "bass"), ("Ringo", "drums"))
#Add tuples to list, including the list name, "beatles"
beatles2 = ["beatles"]
for musician in band:
    beatles2.append(musician)
#Print to verify output
print("Task 1 alternative 1: Beatles2 list\n", beatles2, "\n")
#Can also create list is a single line:
beatles3 = ["beatles", ("George", "guitar"), ("John", "guitar"), ("Paul", "bass"), ("Ringo", "drums")]
print("Task 1 alternative 2: Beatles3 list\n", beatles3, "\n")

#Task 2 Answer
#Create dictionary
beatles_dict = {}
#Populate dictionary by iterating over beatles list, starting with the second element
for musician in beatles[1:]:
    beatles_dict[musician[0]] = musician[1]
#Print to verify output
print("Task 2: Beatles dictionary\n", beatles_dict, "\n")
#Output: {'George': 'guitar', 'John': 'guitar', 'Paul': 'bass', 'Ringo': 'drums'}

#Task 3 Answer
#create tuples
mick, keith, charlie, ronnie = ("Mick", "piano"), ("Keith", "guitar"), ("Charlie", "drums"), ("Ronnie", "guitar")
#Add tuples to list, including the list name, "stones"
stones = ["stones", mick, keith, charlie, ronnie]
#Print to verify output
print("Task 3: Stones list\n", stones, "\n")
#Output: ['stones', ('Mick', 'piano'), ('Keith', 'guitar'), ('Charlie', 'drums'), ('Ronnie', 'guitar')]

#Task 4 Answer
#Create dictionary
stones_dict = {}
#Populate dictionary by iterating over stones list, starting with the second element
for musician in stones[1:]:
    stones_dict[musician[0]] = musician[1]
#Print to verify output
print("Task 4: Stones dictionary\n", stones_dict, "\n")
#Output: {'Mick': 'piano', 'Keith': 'guitar', 'Charlie': 'drums', 'Ronnie': 'guitar'}

#Task 5 Answer
#Create dictionary
bands_dict = {"Beatles": beatles_dict, "Stones": stones_dict}
#Print to verify output
print("Task 5: Bands dictionary\n", bands_dict, "\n")
#Output: {'Beatles': {'George': 'guitar', 'John': 'guitar', 'Paul': 'bass', 'Ringo': 'drums'}, 'Stones': {'Mick': 'piano', 'Keith': 'guitar', 'Charlie': 'drums', 'Ronnie': 'guitar'}}

#Task 6 Answer
#bands_dict["Beatles"] returns the value of "Beatles", i.e. the beatles_dict dictionary
#bands_dict["Beatles"]["Ringo"] returns "drums", the value of "Ringo" in the beatles_dict dictionary
print("Task 6:\nThe Value associated with 'Ringo' in the beatles_dict sub-dictionary is '"+bands_dict["Beatles"]["Ringo"]+"'")
#Output: The Value associated with 'Ringo' in the beatles_dict sub-dictionary is 'drums'










