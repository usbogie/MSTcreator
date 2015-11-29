#!/usr/bin/python

import copy
from Node import Node

def runSollins(trees):
	MSTs = list()
	for tree in trees:
		MSTs.append(runSollinsOnTree(tree))
	return MSTs

def runSollinsOnTree(tree):
	subtrees = list()
	for n in tree:
		t = list()
		newN = copy.copy(n)
		newN.adjList = {}
		t.append(newN)
		subtrees.append(t)
	while len(subtrees) != 1:
		subtrees = runPhase(subtrees, tree)
	return subtrees.pop(0)

def runPhase(subtrees, tree):
	for subtree in subtrees:
		lowestNode = Node(0, 0, 0, {})
		lowestWeight = -1
		parent = Node(0, 0, 0, {})
		for n in subtree:
			treeNode = Node(0, 0, 0, {})
			for m in tree:
				if n == m:
					treeNode = m
			for p in treeNode.adjList:
				inComponent = False
				for q in subtree:
					if p == q:
						inComponent = True
				if not inComponent and (treeNode.adjList[p] < lowestWeight or lowestWeight == -1):
					lowestWeight = treeNode.adjList[p]
					lowestNode = p
					parent = n
		subtrees = combineComponents(subtrees, subtree, parent, lowestNode, lowestWeight)
	return subtrees

def combineComponents(subtrees, subtree, parent, child, lowestWeight):
	childSubtree = list()
	actChild = Node(0, 0, 0, {})
	for sub in subtrees:
		for x in sub:
			if x == child:
				childSubtree = sub
				actChild = x
	parent.adjList[actChild] = lowestWeight
	actChild.adjList[parent] = lowestWeight
	for y in subtree:
		childSubtree.append(copy.copy(y)) 
	subtrees.remove(subtree)
	return subtrees