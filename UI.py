# All code property of Ryan Lacroix
# February 2017

# This file contains user interface definitions and is
# the intended entry point when running the program.

import time
from searchDefs import *

# BEGIN UI DEFINITONS

def getUserStart():
	print("This is the bridge transport problem. Please enter individual times one by one, ending with an empty input")
	personList = []
	currVal = 0
	while currVal != "":
		currVal = input(">")
		if currVal != "":
			personList.append(currVal)
		else:
			personList.append("L")
	#print(personList)
	return personList


# Start here. Takes in input and asks for type of search
def mainMenu():
	startState = getUserStart()
	searchType = input("Great! What kind of search are we using? \n Options: depth breadth a*\n>")
	startTime = time.time()
	if searchType == "depth":
		treeSearchDepth(startState)
	elif searchType == "breadth":
		treeSearchBreadth(startState)
	elif searchType == ("a*"):
		treeSearchAStar(startState)
	else:
		print("Search type not recognized. Exiting..")
		return 0
	endTime = time.time()
	totalTime = endTime - startTime
	print("Search took ", totalTime, " seconds.")

# END UI DEFINITIONS

# Launch the main menu
mainMenu()