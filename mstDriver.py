#!/usr/bin/python

import GenGraph
import Sollins
import Prims
import Kruskals
from Node import Node

def driver():
	print "Hello! This is a program which randomly generates nodes and edges to connect those nodes.",
	print "After the graph is generated, you can then choose from finding an MST of each tree created",
	print "by using either Prim's, Kruskal's, or Sollin's algorithm. Addtionally, there are two methods",
	print "of generating edges. The first method is to randomly assign a weight between 1 and the user-defined",
	print "maximum edge weight, the second is to assign the weight based on the actual distance between",
	print "the two nodes. Finally, the amount of nodes in the graph, the size of the graph, and the k-value,",
	print "which determines the likelihood any two nodes will have an edge between them."

	print "Which method of edge generation would you like to use?"
	print "1: Weight based on actual distance between nodes"
	print "2: Weight based on user-defined maximum edge weight"
	edgeMethod = int(raw_input('> '))

	print "How many nodes are in the graph (any number greater than 0)?"
	totalNodes = int(raw_input('> '))
	print "How big is the graph (any number greater than 0)?"
	graphSize = int(raw_input('> '))
	print "What is the k-value that should be used (any number greater than 0)?"
	kval = int(raw_input('> '))
	maxWeight = 0
	if edgeMethod == 2:
		print "What is the maximum weight of an edge (any number greater than 0)?"
		maxWeight = int(raw_input('> '))
	trees = GenGraph.GenerateGraph(totalNodes, graphSize, maxWeight, kval, edgeMethod)
	print "Here are the adjacency lists of the trees randomly generated using your inputs (format = ((x,y,) weight)):"
	print "Trees:"
	for t in trees:
		print "Tree:{"
		for x in t:
			print printNode(x)+": {",
			for y in x.adjList:
				print "("+printNode(y)+", "+str(x.adjList[y])+")",
			print "}"
		print "}"
	print "Now, to find the MST of each of the generated trees, please select an algorithm to use."
	print "1: Prim's algorithm"
	print "2: Kruskal's algorithm"
	print "3: Sollin's algorithm"
	mstMethod = int(raw_input('> '))
	MSTs = list()
	if mstMethod == 1:
		MSTs = Prims.runPrims(trees)
	elif mstMethod == 2:
		MSTs = Kruskals.runKruskals(trees)
	elif mstMethod == 3:
		MSTs = Sollins.runSollins(trees)
	print "Here are the MSTs for each of the generated trees."
	print "MSTS:"
	for t in MSTs:
		print "MST:{"
		for x in t:
			print printNode(x)+": {",
			for y in x.adjList:
				print "("+printNode(y)+", "+str(x.adjList[y])+")",
			print "}"
		print "}"

def printNode(n):
	return "("+str(n.xloc)+","+str(n.yloc)+")"

driver()