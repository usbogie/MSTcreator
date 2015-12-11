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
	treeToMst = dict()
	mstToTree = dict()
	for n in tree:
		m = copy.copy(n)
		m.adjList = {}
		treeToMst[n] = m
		mstToTree[m] = n
	first = treeToMst[tree.keys()[0]]
	mstNodes.append(first)
	done = False
	while (not done):
		if len(mstNodes) == len(tree):
			done = True
		else:
			mstNodes.append(getNextNode(mstNodes, tree, treeToMst, mstToTree))
	return mstNodes

def getNextNode(mstNodes, tree, treeToMst, mstToTree):
	lowestNode = Node(0, 0, 0, {})
	lowestWeight = -1
	parent = Node(0, 0, 0, {})
	treeChild = Node(0, 0, 0, {})
	for n in mstNodes:
		treeNode = mstToTree[n]
		for p in treeNode.adjList:
			if (treeNode.adjList[p] < lowestWeight or lowestWeight == -1) and not treeToMst[p] in mstNodes:
				lowestWeight = treeNode.adjList[p]
				lowestNode = treeToMst[p]
				treeChild = p
				parent = n
	treeParent = mstToTree[parent]
	del treeParent.adjList[treeChild]
	del treeChild.adjList[treeParent]
	parent.adjList[lowestNode] = lowestWeight
	lowestNode.adjList[parent] = lowestWeight
	return lowestNode