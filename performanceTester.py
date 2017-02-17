# This script runs increasingly difficult search tasks for the three algorithms, 
# logging performance in a text file.

import time
import random
import csv
from searchDefs import *

# Generate random list of crossing times
def makeState(num):
	persons = []
	for i in range(num):
		persons.append(str(random.randint(1,99)))
	persons.append('L')
	print(persons)
	return persons

def csvWrite(data, path):
	with open(path, "a", newline='') as csvFile:
		writer = csv.writer(csvFile, delimiter=',')
		#for line in data:
		writer.writerow(data)

# Setup the csv
csvWrite(['Persons', 'Depth-first','Depth-cross-time', 'Breadth-first', 'Breadth-cross-time', 'A*', 'A*-cross-time'], "perf.csv")
for i in range(2,7):
	# i represents number of persons in problem
	# Create the beginning state
	startState = makeState(i)

	# Calculate time for each search
	startTimeDepth = time.time()
	depthMoves = treeSearchDepth(startState)
	endTimeDepth = time.time()
	startTimeBreadth = time.time()
	breadthMoves = treeSearchBreadth(startState)
	endTimeBreadth = time.time()
	startTimeAStar = time.time()
	starMoves = treeSearchAStar(startState)
	endTimeAStar = time.time()
	depthTime = endTimeDepth - startTimeDepth
	breadthTime = endTimeBreadth - startTimeBreadth
	starTime = endTimeAStar - startTimeAStar

	# Build list of data
	timesList = []
	timesList.append(i)
	timesList.append(depthTime)
	timesList.append(depthMoves)
	timesList.append(breadthTime)
	timesList.append(breadthMoves)
	timesList.append(starTime)
	timesList.append(starMoves)

	# Record performance
	csvWrite(timesList, "perf.csv")