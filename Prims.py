#!/usr/bin/python

import copy
from Node import Node

def runPrims(trees):
	MSTs = list()
	for tree in trees:
		MSTs.append(runPrimsOnTree(tree))
	return MSTs

def runPrimsOnTree(tree):
	mstNodes = list()
	temp = tree.keys()[0] # Get the first node in the tree
	first = Node(temp.xloc,temp.yloc,temp.kval,dict())
	mstNodes.append(first)
	done = False
	while (not done):
		if len(mstNodes) == len(tree):
			done = True
		else:
			mstNodes.append(getNextNode(mstNodes, tree))
	return mstNodes

def getNextNode(mstNodes, tree):
	lowestNode = Node(0, 0, 0, {})
	lowestWeight = -1
	parent = Node(0, 0, 0, {})
	for n in mstNodes:
		treeNode = Node(0, 0, 0, {})
		for m in tree:
			if n == m:
				treeNode = m
		for p in treeNode.adjList:
			inMst = False
			for q in mstNodes:
				if p == q:
					inMst = True
			if (treeNode.adjList[p] < lowestWeight or lowestWeight == -1) and not inMst:
				lowestWeight = treeNode.adjList[p]
				lowestNode = p
				parent = n
	child = copy.copy(lowestNode)
	parent.adjList[child] = lowestWeight
	child.adjList = {}
	child.adjList[parent] = lowestWeight
	return child