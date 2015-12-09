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
	treeToMst = dict()
	mstToTree = dict()
	for n in tree:
		t = list()
		m = copy.copy(n)
		m.adjList = {}
		t.append(m)
		subtrees.append(t)
		treeToMst[n] = m
		mstToTree[m] = n
	while len(subtrees) != 1:
		subtrees = runPhase(subtrees, tree, treeToMst, mstToTree)
	return subtrees.pop(0)

def runPhase(subtrees, tree, treeToMst, mstToTree):
	for subtree in subtrees:
		lowestNode = Node(0, 0, 0, {})
		lowestWeight = -1
		parent = Node(0, 0, 0, {})
		for n in subtree:
			treeNode = mstToTree[n]
			for p in treeNode.adjList:
				temp = treeToMst[p]
				if temp not in subtree and (treeNode.adjList[p] < lowestWeight or lowestWeight == -1):
					lowestWeight = treeNode.adjList[p]
					lowestNode = temp
					parent = n
		subtrees = combineComponents(subtrees, subtree, parent, lowestNode, lowestWeight)
	return subtrees

def combineComponents(subtrees, subtree, parent, child, lowestWeight):
	childSubtree = list()
	for sub in subtrees:
		if child in sub:
			childSubtree = sub
	parent.adjList[child] = lowestWeight
	child.adjList[parent] = lowestWeight
	for y in subtree:
		childSubtree.append(y) 
	subtrees.remove(subtree)
	return subtrees