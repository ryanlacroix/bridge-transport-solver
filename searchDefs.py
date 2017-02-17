# All code property of Ryan Lacroix
# February 2017

# This file contains the definitions for
# depth-first, breadth-first, and A* search algorithms.

# Algorithms are specific to the transport problem
# outlined in README.md

import copy
from helperDefs import *

# BEGIN SEARCH DEFINITIONS

# Depth-first
# Takes in initial start state list
def treeSearchDepth(startState):
	fringe = [] # Contains nodes to be visited
	currStack = [] # Current nodes in path.
	visitedNodes = [] # Nodes already seen.
	# Add root node to the fringe
	fringe.append(Node(startState, "root", 0))
	while len(fringe) > 0:
		currNode = fringe.pop() # Depth-first
		if checkComplete(currNode):
			# This is a solution
			print("FOUND A SOLUTION.")
			currStack = getSolutionList(currNode)
			printSolution(currStack)
			return True
			# return will go somewhere in here
		else:
			# Put children of node into fringe
			if checkIfVisited(currNode, visitedNodes) == True:
				continue
			else:
				visitedNodes.append(currNode)
				expand(currNode, fringe)

# Breadth-first
# Takes in initial start state list
def treeSearchBreadth(startState):
	fringe = [] # Contains nodes to be visited
	currStack = [] # Current nodes in path.
	visitedNodes = [] # Nodes already seen.
	# Add root node to the fringe
	fringe.append(Node(startState, "root", 0))
	while len(fringe) > 0:
		currNode = fringe.pop(0) # Breadth-first
		if checkComplete(currNode):
			# This is a solution
			print("FOUND A SOLUTION.")
			currStack = getSolutionList(currNode)
			printSolution(currStack)
			return True
		else:
			# Put children of node into fringe
			if checkIfVisited(currNode, visitedNodes) == True:
				continue
			else:
				visitedNodes.append(currNode)
				expand(currNode, fringe)

# A* search
# Takes in initial start state list
def treeSearchAStar(startState):
	openNodes = [] # Contains nodes currently open to visiting
	closedNodes = [] # Contains nodes which have already been visited
	currStack = [] # Current nodes in path.

	# Add root node to the openNodes
	startNode = Node(startState, "root", 0)
	startNode.cost = 0
	openNodes.append(startNode)
	currParent = ""
	while len(openNodes) > 0:
		# Retrieve best node
		#currNode = openNodes.pop(getBestNode(openNodes))
		currNode = openNodes.pop(getBestNode(openNodes))

		if checkComplete(currNode) == True:
			printSolution(getSolutionList(currNode))
			return True
		# Generate successors
		successors = []
		expand(currNode, successors)
		# Throw successors into node
		currNode.successors = successors
		# Place the node in closed
		closedNodes.append(currNode)

		# Iterate through node's successors
		for i in range(len(successors)):
			# Node not in open or closed
			if checkIfVisited(successors[i], openNodes) == False and checkIfVisited(successors[i], closedNodes) == False:
				# Evaluate the successors
				successors[i].cost = getCostSoFar(successors[i]) + heuristic1(successors[i])
				openNodes.append(successors[i])
				# Set this as parent for next iteration
				currParent = successors[i]
			# Node is contained in open
			elif checkIfVisited(successors[i], openNodes) == True:
				thisCost = getCostSoFar(successors[i]) + heuristic1(successors[i])
				tempNode = getSameNode(successors[i], openNodes)
				# Does node need updating?
				if tempNode.cost > thisCost:
					# Update the node's parent
					tempNode.parent = currNode
					# Update the node's cost
					tempNode.cost = getCostSoFar(tempNode) + heuristic1(tempNode)
					# Renerate node's successors with new cost values
					regenSuccessors(tempNode)
			# Node is contained in closed
			elif checkIfVisited(successors[i], closedNodes) == True:
				thisCost = getCostSoFar(successors[i]) + heuristic1(successors[i])
				tempNode = getSameNode(successors[i], closedNodes)
				# Does node need updating?
				if tempNode.cost > thisCost:
					# Update the node's parent
					tempNode.parent = currNode
					# Update the node's cost
					tempNode.cost = getCostSoFar(tempNode) + heuristic1(tempNode)
					# Renerate node's successors with new cost values
					regenSuccessors(tempNode)

# END SEARCH DEFINITIONS