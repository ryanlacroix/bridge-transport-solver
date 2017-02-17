# All code property of Ryan Lacroix
# February 2017

# This file contains all definitions necessary for
# search algorithms in searchDefs.py to run.

import copy

# BEGIN GENERAL HELPER DEFINITIONS

class Node:
	def __init__(self, state, parent, time):
		self.state = state # List representing problem state
		# eg ['12','66','42','L']
		self.time = time
		self.parent = parent
		# A* adds a .cost which is not necessary for other searches
		# A* adds a .successors which holds list of successors

# Determine if this node is a possible solution
def checkComplete(node):
	state = node.state
	# If first element is torch position, all people have crossed
	if state[0] == "L" or state[0] == "R":
		return True
	else:
		return False

# Returns index of element in list, -1 if not present
def getIndexOf(val, lis):
	for i in range(len(lis)):
		if val == lis[i]:
			return i
	return -1

# PRODUCTION SYSTEM
# Returns list of possible child states. 
# each element is a list, where:
#	index 0 = the new child state
#	index 1 = time taken for move
def getAllPossibleMoves(nodeState):
	if getIndexOf("L", nodeState) != -1:
		# Torch is on the left side
		# Only generate moves from left side to right
		state = nodeState[:getIndexOf("L", nodeState)]
		otherSide = nodeState[getIndexOf("L", nodeState):]
		side = "left"
	else:
		# Likewise, torch is on right
		state = nodeState[getIndexOf("R", nodeState)+1:]
		otherSide = nodeState[:getIndexOf("R", nodeState)+1]
		side = "right"

	candidates = []
	# Generate all possible pairs
	for i in range(len(state)):
		for j in range(i+1, len(state)):
			checkLis = []
			checkLis.append(str(state[i]))
			checkLis.append(str(state[j]))
			if checkLis not in candidates:	
				candidates.append(checkLis)
	# Generate all possible single moves
	for i in range(len(state)):
		tempLis = []
		tempLis.append(state[i])
		candidates.append(tempLis)

	childStates = []
	# Create the child states
	for i in range(len(candidates)):
		# Find slowest candidate in the move
		crossTime = max(list(candidates[i]))
		# Probably shouldn't touch the original node's state. Make a copy.
		tempState = copy.copy(state)
		# Manually remove each of the individuals from the original side
		# First dimension is list of pairs(also lists) to move
		# Second is the individuals constituting the pair
		for b in range(len(candidates[i])):
			tempState.remove(candidates[i][b])
		if side == "left":
			# Move torch to other side
			tempOtherSide = copy.copy(otherSide)
			tempOtherSide[getIndexOf("L", otherSide)] = "R"
			# Put together the new child state
			tempChild = list()
			tempChild.append(tempState + tempOtherSide + list(candidates[i]))
			tempChild.append(crossTime)
			childStates.append(tempChild)
		else:
			# Torch is currently on the right side
			tempOtherSide = copy.copy(otherSide)
			tempOtherSide[getIndexOf("R", otherSide)] = "L"
			tempChild = list()
			tempChild.append(list(candidates[i]) + tempOtherSide + tempState)
			tempChild.append(crossTime)
			childStates.append(tempChild)
	return childStates

# Expands list of child nodes into fringe
def expand(node, fringe):
	# This list contains all children to be put in the fringe
	children = []
	# Generate all possible child states
	childStates = getAllPossibleMoves(node.state)
	for i in range(len(childStates)):
		newNode = Node(childStates[i][0], node, childStates[i][1])
		children.append(newNode)
	#return children
	for i in range(len(children)):
		fringe.append(children[i])

# Prettily print the solution. Fixes hideous output from before
def printSolution(solStack):
	totalTime = 0
	solStack.reverse()
	for i in range(len(solStack)):
		print(i,"| ", end='')
		for o in range(len(solStack[i].state)):
			print(solStack[i].state[o], end=' ')
		print("") # go to next line
		totalTime += int(solStack[i].time)
	print("TOTAL TIME: ", totalTime)

# Check if a node has already been visited
def checkIfVisited(node, visitedNodes):
	for i in range(len(visitedNodes)):
		if node.state == visitedNodes[i].state:
			return True
		else:
			continue
	return False

def getSolutionList(node):
	# Must follow node's parents until root is found
	solutionList = []
	currNode = node
	while currNode.parent != "root":
		solutionList.append(currNode)
		currNode = currNode.parent
	# Add the root back in
	solutionList.append(currNode)
	return solutionList

# END GENERAL HELPER DEFINITIONS

# BEGIN HELPER DEFINITIONS FOR A* SEARCH

# Returns index of best node in a list based on move time
# (Slower is better in this case)
def getBestNode(nodeList):
	bestNode = nodeList[0]
	index = 0
	for i in range(len(nodeList)):
		if nodeList[i].time < bestNode.time:
			bestNode = nodeList[i]
			index = i
	return index

# Return the node whose state matches this one.
# Return false if node is not present
def getSameNode(node, nodeList):
	for i in range(len(nodeList)):
		if node.state == nodeList[i].state:
			return nodeList[i]
	return False

# Compute cost so far to reach current node
def getCostSoFar(node):
	currCost = 0
	while node.parent != "root":
		currCost += 1
		node = node.parent
	return currCost

# Regenerates successor list with new values
def regenSuccessors(node):
	try:
		successors = node.successors
		for i in range(len(successors)):
			successors[i].cost = getCostSoFar(successors[i]) + heuristic1(successors[i])
			regenSuccessors(successors[i])
	except:
		return True

# Heuristic function. Returns cost to goal
# Based on how many people are on starting side
def heuristic1(node):
	nodeState = node.state
	if getIndexOf("L", nodeState) != -1:
		# Torch is on the left side
		leftSide = nodeState[:getIndexOf("L", nodeState)]
	else:
		# Likewise, torch is on right
		leftSide = nodeState[:getIndexOf("R", nodeState)+1]
	return len(leftSide)

# Need one more heuristic, then DONE

# END HELPER DEFINITIONS FOR A* SEARCH