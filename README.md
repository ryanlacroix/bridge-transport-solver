Bridge Transport Problem Solving Agent
======================================
*COMP4106 Artificial Intelligence Assignment*

A Python implementation of breadth-first, depth-first and A* search algorithms for solving a bridge transport problem. 

Problem
-------
Some number of people are standing on one side of a canyon, and the goal is to get everyone to the other side (preferably in a timely manner). It is dark out and the bridge is narrow, so a torch (of which there is only one) must be carried across any time someone crosses the bridge. No more than two people can be on the bridge at any given time. Each person is carrying a different amount of gear, and thus each individual crosses the bridge at their own speed. Because the torch must be shared, two people crossing the bridge must cross at the speed of the pace of the slower person. The goal of this problem is to find the quickest way to get everyone across the bridge.

Search Algorithms
-----------------
This program gives the user the option to pick which of the three search algorithms to use in order to solve the problem. A timer keeps track of how long the given algorithm takes to solve the problem.

Usage
-----
Run `UI.py` using python 3. Further instructions are provided in the program. Note: A good solution for more than six people can take a *very* long time on a normal system (even using A*).