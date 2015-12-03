#!/usr/bin/python

import copy
import collections
from Node import Node

parent = dict()
rank = dict()

def runKruskals(trees):
	MSTs = list()
	for tree in trees:
		parent = dict()
		rank = dict()
		MSTs.append(runKruskallsOnTree(tree))
	return MSTs

def runKruskallsOnTree(tree):
	mstNodes = list()
	for n in tree:
		makeSet(n)
	edges = sortEdges(tree)
	for edge in edges:
		weight, nodes = (edge, edges[edge])
		n1, n2 = nodes[0], nodes[1]
		if find(n1) != find(n2):
			union(n1, n2)
			n1Copy = copy.copy(n1)
			n2Copy = copy.copy(n2)
			n1InMST, n2InMST = False, False
			for m in mstNodes:
				if n1Copy == m:
					n1Copy = m
					n1InMST = True
				if n2Copy == m:
					n2Copy = m
					n2InMST = True
			if not n1InMST:
				mstNodes.append(n1Copy)
				n1Copy.adjList = {}	
			n1Copy.adjList[n2Copy] = weight
			if not n2InMST:
				mstNodes.append(n2Copy)
				n2Copy.adjList = {}
			n2Copy.adjList[n1Copy] = weight
	return mstNodes

def makeSet(n):
	parent[n] = n
	rank[n] = 0

def find(n):
	if parent[n] != n:
		parent[n] = find(parent[n])
	return parent[n]

def union(n1, n2):
	root1 = find(n1)
	root2 = find(n2)
	if root1 != root2:
		if rank[root1] > rank[root2]:
			parent[root2] = root1
		else:
			parent[root1] = root2
			if rank[root1] == rank[root2]:
				rank[root2] += 1

def sortEdges(tree):
	edges = dict()
	for n in tree:
		for m in n.adjList:
			edges[n.adjList[m]] = list([n, m])
	return collections.OrderedDict(sorted(edges.items()))