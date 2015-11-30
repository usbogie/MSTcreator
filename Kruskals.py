#!/usr/bin/python

import copy
import collections
from Node import Node

def runKruskals(trees):
	MSTs = list()
	for tree in trees:
		MSTs.append(runKruskallsOnTree(tree))
	return MSTs

def runKruskallsOnTree(tree):
	mstNodes = list()
	edges = sortEdges(tree)
	for edge in edges:
		weight, nodes = (edge, edges[edge])
		x, y = nodes[0], nodes[1]
		end1, end2 = False, False
		for n in mstNodes:
			if x == n:
				end1 = True
				x = n
			elif y == n:
				end2 = True
				y = n
		if not (end1 and end2):
			if x not in mstNodes:
				mstNodes.append(x)
			if y not in mstNodes:
				mstNodes.append(y)
			x.adjList[y] = weight
			y.adjList[x] = weight
	return mstNodes

def sortEdges(tree):
	edges = dict()
	for n in tree:
		for m in n.adjList:
			n1 = copy.copy(n)
			m1 = copy.copy(m)
			n1.adjList = {}
			m1.adjList = {}
			edges[n.adjList[m]] = list([n1, m1])
	return collections.OrderedDict(sorted(edges.items()))
